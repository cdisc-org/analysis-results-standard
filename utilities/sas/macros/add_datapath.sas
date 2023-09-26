%macro add_datapath(maplib=,inlib=,slotdefs=);

/***********************************************************************************\
*                                                                                   *
* Name: add_datapath.sas                                                            *
*                                                                                   *
* Description: Creates a WORK dataset as a copy of each mapped dataset, in which    *
*              all ordinal variables (that are assigned by the JSON libname engine  *
*              mapping) are replaced with 2 variables:                              *
*              - TABLEPATH: contains the SAS-defined path for source dataset mapped *
*                           in the JSON file.                                       *
*              - DATAPATH: contains a value (specified using JSON Pointer notation) *
*                          indicating the location of the corresponding data in the *
*                          input JSON reporting event file.                         *
*              - SORTPATH: contains a string value that combines slot names with    *
*                          corresponding ordinal variable values for each           *
*                          observation in a format that can be used to re-sort      *
*                          combined data. Note that data is re-sorted by            *
*                          alphabetic slot name and numeric ordinal value (not by   *
*                          the original order of the slots in the original JSON     *
*                          file).                                                   *
*                                                                                   *
* Input parameters:                                                                 *
*                                                                                   *
* MAPLIB: The libref for the temporary JSON mapping.                                *
*                                                                                   *
* INLIB: The libref for the JSON reporting event file.                              *
*                                                                                   *
* SLOTDEFS: The name of the WORK dataset containing class/slot definitions read in  *
*           from the JSON schema file.                                              *
*                                                                                   *
* Outputs: This macro creates:                                                      *
*          - A WORK dataset corresponding with each mapped dataset, as described    *
*            above.                                                                 *
*          - Three additional WORK datasets:                                        *
*            > PATHMAP: Contains the association between mapped data path values    *
*                       (which are combinations of slot names and ordinal values    *
*                       assigned by the JSON libname engine) and the corresponding  *
*                       JSON Pointer value. (Retained for reference only)           *
*            > KEYTALLY: Contains a running tally of the array index value used for *
*                        each repeating element in the data path. This allows the   *
*                        index to be incremented across repeating elements found    *
*                        in different parts of the JSON file. (Retained for         *
*                        reference only)                                            *
*            > DATASET_VARIABLES: Contains combined information for mapped datasets *
*                                 and variables, with a variable order assigned.    *
*                                                                                   *
\***********************************************************************************/


  /* Initialize the PATHMAP and KEYTALLY datasets */

  data pathmap;
  length mapdpath jsonpath $200;
  call missing(mapdpath,jsonpath);
  stop;
  run;

  data keytally;
  length pathkey $200 idx 8;
  call missing(pathkey,idx);
  stop;
  run;

  /* Create the DATASET_VARIABLES dataset */

  data dataset_variables;
  merge &maplib..datasets &maplib..datasets_variables;
  by ordinal_datasets;
  if first.ordinal_datasets then varord = 0;
  varord + 1;
  run;

  /* Create lists of mapped dataset names and corresponding table paths */

  proc sql noprint;

    select dsname,tablepath
    into : dsnames separated by '|',
         : tbpaths separated by '|'
    from &maplib..datasets
    order by tablepath;

    %let nds = &sqlobs;

  quit;

  /* Loop through the datasets */

  %do i =  1 %to &nds;
    %let ds = %scan(&dsnames,&i,%str(|));
    %let tpth = %scan(&tbpaths,&i,%str(|));

    /* Create a list of ordinal variables for the mapped dataset being processed */

    proc sql noprint;

      select name
      into : ordvars separated by ' '
      from dataset_variables
      where dsname = "&ds"
      and name like "ordinal\_%" escape "\";

      %let nords = &sqlobs;

    quit;

    /* Create a copy of the mapped dataset in the WORK library */

    data &ds;
    length tablepath $ &tpthlen mapdpath mdpathel pathkey jpathel pathkey datapath sortpath $ 200 slot $ 100 reid1 is_array idx 8;
    retain reid1;
    set &inlib..&ds end = lastone;
    if _n_ eq 1 then
      do;
        /* Hash table to check if a slot is multivalued (i.e., defined as an array) */
        declare hash class_slots(dataset: "work.&slotdefs");
        class_slots.definekey("slot");
        class_slots.definedata("is_array");
        class_slots.definedone();
        call missing(is_array);
        /* Hash table for the checking and updating the PATHMAP dataset */
        declare hash pm(dataset: "work.pathmap (rename = (mapdpath = mdpathel jsonpath = jpathel))", ordered: "y");
        pm.definekey("mdpathel");
        pm.definedata("mdpathel","jpathel");
        pm.definedone();
        /* Hash table for the checking and updating the KEYTALLY dataset */
        declare hash kt(dataset: "work.keytally", ordered: "y");
        kt.definekey("pathkey");
        kt.definedata("pathkey","idx");
        kt.definedone();
        /* Regular expression to identify repeating elements in the mapped data path (slot name(s) followed by an ordinal value) */
        reid1 = prxparse("/(\/[a-zA-Z]+)+\/[0-9]+/");
      end;
    array ordvars{&nords} &ordvars;
    tablepath = "&tpth";
    /* Create a mapped data path value by looping through the slot names in the table path (starting at 2 because we don't
       want to include "root") and ... */
    do _i_ = 2 to &nords;
      /* Check if the slot is multivalued (is an array) */
      slot = scan(tablepath,_i_,'/');
      class_slots.find();
      /* Add the slot name to the mapped data path */
      mapdpath = cats(mapdpath,"/",scan(tablepath,_i_,'/'));
      /* If the slot is multivalue, also add the corresponding ordinal value */
      if is_array then
        mapdpath = cats(mapdpath,"/",ordvars{_i_});
      /* Add slot name and corresponding ordinal value to the sort path for all slots */
      sortpath = catx(".",sortpath,cats(scan(tablepath,_i_,'/'),put(ordvars{_i_},z6.)));
    end;
    /* Loop through each of the repeating elements in the generated mapped data path and ... */
    start = 1;
    stop = length(mapdpath);
    call prxnext(reid1, start, stop, mapdpath, position, length);
      do while (position > 0);
        found = substr(mapdpath, position, length);
        mdpathel = cats(mdpathel,found);
        /* Retrieve the corresponding JSON path value from the path map table if it's there */
        if pm.check() eq 0 then pm.find();
        /* Otherwise ... */
        else
          do;
            /* Create a look-up key based on the JSON path for a previous repeating element in the table path combined
               with the slot names (without the last ordinal value) for the current repeating element */
            pathkey = cats(jpathel,substr(found,1,findc(found,'/','b')-1));
            /* Try to retrieve the array index value for the path key from the key tally table */
            if kt.find() eq 0 then
              do;
                /* If it's retrieved, increment it and update the key tally table */
                idx = idx+1;
                kt.replace();
              end;
            else
              do;
                /* If it's not retrieved, initialize it as 0 and add it to the key tally table */
                idx = 0;
                kt.add();
              end;
            /* Append the repeating element's slot name(s) and the incremented/new array index value to the JSON path */ 
            jpathel = catx('/',pathkey,idx);
            /* Add the mapped data path and corresponding JSON path to the path map table */
            pm.add();
          end;
        call prxnext(reid1, start, stop, mapdpath, position, length);
      end;
    /* After processing any/all repeating elements in the mapped data path, assign the data path either as the
       corresponding JSON path with trailing non-repeating slot name(s) appended (if the mapped data path contained
       repeating elements), or a copy of the mapped data path */
    if jpathel ne '' then datapath = cats(jpathel,substr(mapdpath,length(mdpathel)+1));
    else datapath = mapdpath;
    /* If this is the last record, write the updated path map and key tally tables back to the PATHMAP and KEYTALLY
       datasets (respectively) so that they can be referenced when processing the next mapped dataset */ 
    if lastone then
      do;
        pm.output(dataset: "work.pathmap (rename = (mdpathel = mapdpath jpathel = jsonpath))");
        kt.output(dataset: "work.keytally");
      end;
    drop ordinal_: _i_ start stop position length found mapdpath mdpathel pathkey jpathel pathkey slot reid1 is_array idx ;
    run;
   
  %end;

%mend;
