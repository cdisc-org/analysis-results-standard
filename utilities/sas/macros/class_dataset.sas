%macro class_dataset(maplib=,inlib=,classlst=,classnm=,slotdefs=,outlib=);

/***********************************************************************************\
*                                                                                   *
* Name: class_dataset.sas                                                           *
*                                                                                   *
* Description: Creates a new library for class-based datasets. Loops through the    *
*              classes identified for mapped datasets and runs to CLASS_DATASET     *
*              macro to create a class-based dataset for each class. Deletes the    *
*              WORK datasets created by the ADD_DATAPATH macro.                     *
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
* OUTLIB: The libref to be used for the library that will contain the created class *
*         datasets.                                                                 *
*                                                                                   *
* Dependencies: This macro references the WORK.SLOT_DATASETS dataset created by the *
*               MAP_JSON_RE macro and WORK.DATASET_VARIABLES dataset created by the *
*               ADD_DATAPATH macro.                                                 *
*                                                                                   *
\***********************************************************************************/

  /* 
     Initialize macro variables:
     - VARLENS is a list of variable length specifications
     - KEEPVARS is a list of class-specific variables to keep
  */

  %let varlens = %str();
  %let keepvars = %str();

  proc sql noprint;

    /*
       Create lists of dataset names and table paths for mapped datasets associated
       with the specified class(es)
    */

    select b.dsname,
           a.tablepath
    into : dsnames separated by ' ',
         : tpaths separated by '|'
    from slot_datasets as a
    inner join &maplib..datasets as b
    on a.tablepath = b.tablepath
    where a.range = "&classlst";

    %let nds = &sqlobs;

    /*
       Create a list of maximum variable length specifications for non-ordinal variables in 
       mapped datasets associated with the specified class(es)
    */

    select catx(' ',name,
           case type
           when 'CHARACTER' then catx(' ','$',maxlen)
         else '8'
         end)
    into : varlens separated by ' '
    from (select c.name, c.type, max(c.current_length) as maxlen, min(c.varord) as minord
          from (select b.name, b.type, b.current_length, b.varord
                from slot_datasets (where = (range = "&classlst")) as a
                inner join dataset_variables as b
                on a.tablepath = b.tablepath
                and b.name not like "ordinal\_%" escape "\") as c
          group by c.name, c.type)
    order by minord;

    /* If there is more than one potential class ... */
    %if %sysfunc(countw(&classlst,%str(|))) gt 1 %then
      %do;

        /*
           Create lists for variables for the specific single class being processed:
           - KEEPVARS: variables corresponding with a slot in the specified class
           - DROPVARS: variables that do not correspond with a slot in the specified class
           - VARREQD:  flags indicating whether the corresponding variable is required (1)
                       or not (0) in the specified class
        */

        select distinct 
               case
                 when c.slot is not missing then b.name
                 else ""
               end as keepvars,
               case 
                 when c.slot is missing then b.name
                 else ""
               end as dropvars,
               c.is_reqd
        into : keepvars separated by ' ',
             : dropvars separated by ' ',
             : varreqd separated by ','
        from slot_datasets (where = (range = "&classlst")) as a
        left join dataset_variables (where = (name not like 'ordinal\_%' escape '\')) as b
        on a.tablepath = b.tablepath
        left join &slotdefs (where = (parent_class = "&classnm")) as c
        on ((c.is_array <> 1 and b.name = c.slot)
            or (c.is_array = 1 and b.name like trim(c.slot)||'_%'));
      %end;

  quit;

  /*
     If there is only a single potential class or there is at least one variable corresponding
     with the single class being processed from a list of potential classes ... 
  */

  %if %sysfunc(countw(&classlst,%str(|))) eq 1 or %length(&keepvars) gt 0 %then 
    %do;

      /*
         Create the class-based dataset by combining (SETting) all mapped datasets associated 
         with the class
      */

      data &outlib..&classnm;
      length tablepath $ &tpthlen datapath $ 200 &varlens;
      set &dsnames;
      /* If there is more than one potential class ... */
      %if %sysfunc(countw(&classlst,%str(|))) gt 1 %then
        %do;
          /* Only keep observations when the number of empty class-specific variables is
             not greater than the number of non-required variables for the class */ 
          if cmiss(of &keepvars) le %sysfunc(countw(&keepvars)) - sum(&varreqd);
          /* If there are any variables in the dataset(s) that are not associated with the class ... */
          %if %length(&dropvars) gt 0 %then
            /* Remove observations where any of them is not missing */
            if cmiss(of &dropvars) ne %sysfunc(countw(&dropvars)) then delete;;
          keep tablepath datapath sortpath &keepvars;
        %end;
      run;

      /* If the resultant class-specific dataset has any observations ... */
      %if &sysnobs gt 0 %then
        %do;
          /* Sort it by the SORTPATH variable (and then drop the SORTPATH variable) */
          proc sort data = &outlib..&classnm out = &outlib..&classnm (drop = sortpath);
          by sortpath;
          run;
        %end;
      /* Otherwise ... */
      %else
        %do;
          /* Delete it */
          proc datasets lib=&outlib nolist;
            delete &classnm;
          quit;
        %end;

    %end;

%mend;
