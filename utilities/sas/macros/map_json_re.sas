%macro map_json_re(rejsonfl=,maplib=,inlib=,slotdefs=);

/***********************************************************************************\
*                                                                                   *
* Name: map_json_re.sas                                                             *
*                                                                                   *
* Description: Creates a default mapping for the specified JSON reporting event     *
*              file, then updates the mapping to:                                   *
*              - Append repeated atomic values to the parent mapped dataset.        *
*              - Create mappings for class instances that do not contain any        *
*                attribute data values (i.e., they only contain child objects).     *
*                                                                                   *
* Input parameters:                                                                 *
*                                                                                   *
* REJSONFL: The path to the JSON file containing the reporting event information to *
*           be converted to SAS datasets.                                           *
*                                                                                   *
* MAPLIB: The fileref to be used for the temporary JSON mapping that generated is   *
*         and then rewritten. This fileref is also used as the libref of the        *
*         corresponding library that is created to access mapped dataset and       *
*         variable definitions.                                                     *
*                                                                                   *
* INLIB: The fileref to be used for the JSON reporting event file specified in the  *
*        REJSONFL macro variable. This fileref is also used as the libref of the    *
*        corresponding library that is created to access the mapped datasets.       *
*                                                                                   *
* SLOTDEFS: The name of the WORK dataset containing class/slot definitions read in  *
*           from the JSON schema file.                                              *
*                                                                                   *
* Dependencies: This macro calls the WRITE_JSON_MAP macro.                          *
*                                                                                   *
* Outputs: This macro creates:                                                      *
*          - Two libraries definitions:                                             *
*            > One named according to the INLIB input paramater which contains      *
*              mapped reporting event datasets.                                     *
*            > One named according to the MAPLIB input paramater which contains     *
*              datasets of the dataset and variable definitions for the mapped      *
*              reporting event datasets.                                            *
*          - The global TPTHLEN macro variable which holds the maximum length of    *
*            the TABLEPATH variable. This is used in the CLASS_DATASET macro.       *
*          - Five WORK datasets:                                                    *
*            > OBJTBL: Contains new definitions for mapped datasets that do not     *
*                      contain data values. (Retained for reference only)           *
*            > OBJVAR: Contains new definitions for variables in mapped datasets    *
*                      that do not contain data values. (Retained for reference     *
*                      only)                                                        *
*            > MAP_DATASETS: Contains modified mapped dataset definitions.          *
*                            (Retained for reference only)                          *
*            > MAP_DATASETS_VARIABLES: Contains modified mapped variable            *
*                                      definitions. (Retained for reference only)   *
*            > SLOT_DATASETS: Contains information about the slots corresponding    *
*                             with each mapped dataset.                             *
*                                                                                   *
\***********************************************************************************/

  %global tpthlen;

  /* Create the default JSON mapping for the specified reporting event file */

  filename &inlib "&rejsonfl";
  filename &maplib temp;
  libname &inlib json map=&maplib automap=replace ordinalcount=ALL;
  libname &maplib json;

  /*
     The JSON libname engine automapper creates a dataset mapping for each branch
     of the JSON file that contains data values. To create a dataset for each ARS
     class referenced in the reporting event, we need a dataset for every slot
     referenced in the JSON file, even if the slot does not (directly) contain
     any data values. A mapped dataset that does not directly contain any data
     values will only have ordinal variables (identifying the location of the slot
     instance within the JSON file).

     The following datastep identifies slots that do not already have a
     corresponding mapped dataset and creates mapping specifications for
     a new dataset containing only ordinal variables.
  */

  data _null_;
  set &maplib..datasets end = lastone;
  length newods ordinal_VARIABLES 8 dsname1 dsname2 NAME $ 32 TYPE $ 9 PATH $ 200;
  retain reid;
  if _n_ eq 1 then
    do;
      /* Hash table for existing mapped dataset paths */
      declare hash idx(dataset: "&maplib..datasets (rename = (tablepath = pathpart))");
      idx.definekey("pathpart");
      idx.definedone();
      /* Hash table to keep track of assigned mapped dataset names */
      declare hash dsn(dataset: "&maplib..datasets (keep = dsname)");
      dsn.definekey("dsname");
      dsn.definedata("dsname");
      dsn.definedone();
      /* Hash table of ordinal variables */
      declare hash ordvars(dataset: "&maplib..datasets_variables (where = (name like 'ordinal\_%' escape '\'))",multidata: "y", ordered:"y");
      ordvars.definekey("ordinal_datasets");
      ordvars.definedata("ordinal_VARIABLES","NAME","TYPE","PATH");
      ordvars.definedone();
      /* Hash table for newly defined data-less mapped datasets */
      declare hash objtbl(ordered:"y");
      objtbl.definekey("pathpart");
      objtbl.definedata("ordinal_root","newods","dsname","pathpart");
      objtbl.definedone();
      /* Hash table for variables in newly defined data-less mapped datasets */
      declare hash objvar(ordered:"y");
      objvar.definekey("ordinal_VARIABLES");
      objvar.definedata("newods","ordinal_VARIABLES","NAME","TYPE","PATH");
      objvar.definedone();
      /* Regular expression to find each slot name referenced in a table path */
      reid = prxparse("/(\/[a-zA-Z]+)/");
      /* Copy the ordinal_DATASETS variable to create a variable for the newly assigned ordinal datasets values */
      newods = ordinal_datasets;
      /* Copy the TABLEPATH variable to create a variable for the new path values */
      pathpart = tablepath;
      call missing(newods,pathpart,ordinal_VARIABLES,NAME,TYPE,PATH);
    end;
    start = 1;
    stop = length(tablepath);
    /* Loop through each of the slots referenced in the table path */
    call prxnext(reid, start, stop, tablepath, position, length);
      do while (position > 0);
        found = substr(tablepath, position, length);
        pathpart = cats(pathpart,found);
        /* If there isn't already a table defined for the slot... */
        if idx.check() ne 0 then
          do;
            /* Assign a new ordinal_DATASETS value */
            newods = ordinal_datasets - 0.5;
            /* If we haven't already created a new dataset definition... */
            if objtbl.check() ne 0 then
              do;
                /* Assign a new dataset name based on the slot and parent slot names */
                dsname1 = scan(pathpart,countw(pathpart,'/')-1,'/');
                dsname2 = scan(pathpart,countw(pathpart,'/'),'/');
                if dsname1 eq 'root' then dsname = dsname2;
                else dsname = catx('_',substr(dsname1,1,length(dsname1)><(32-(length(dsname2)+1))),dsname2);
                /* Check if the dataset name has already been used */
                rc = dsn.check();
                /* If it has... */
                if rc eq 0 then
                  do;
                    /* Add a number to the end and increment it until an unused dataset name is obtained */
                    dsnidx = 1;
                    do until(rc ne 0);
                      dsnidx = dsnidx + 1; /* (Intentionally starting with 2) */
                      dsname2 = cats(scan(pathpart,countw(pathpart,'/'),'/'),dsnidx);
                      dsname = catx('_',substr(dsname1,1,length(dsname1)><(32-(length(dsname2)+1))),dsname2);
                      rc = dsn.check();
                    end;
                  end;
                /* Add the new dataset name to the list of used names */
                rc = dsn.add();
                /* Record the newly mapped dataset definition */
                objtbl.add();
              end;
            /* Loop through the ordinal variables for the current mapped dataset and record each
               for the newly mapped dataset */
            ordvars.reset_dup();
            do while(ordvars.do_over(key:ordinal_datasets) eq 0);
              rc = ordvars.has_next(result:more);
              if more then objvar.ref(); /* Only add to objvar if this is not the last ordinal variable found */
            end;
          end;
        call prxnext(reid, start, stop, tablepath, position, length);
      end;
    /* If this is the last record, output the data-less dataset/variable definitions out to datasets */
    if lastone then
      do;
        objtbl.output(dataset:"work.objtbl (rename = (newods = ordinal_DATASETS pathpart = TABLEPATH))");
        objvar.output(dataset:"work.objvar (rename = (newods = ordinal_DATASETS))");
      end;
  run;

  /* Create a combined list of mapped dataset definitions, including the new definitions */

  data map_datasets;
  set &maplib..datasets objtbl;
  by ordinal_datasets;
  run;

  /*
    Each mapped dataset contains information relating to the attribute/slot whose name is the final
    element in the TABLEPATH value. To create class-based datasets, we need to identify the parent class
    for the named slot. In cases where a slot is only used in a single class, it's possible to identify the
    parent class by using the slot name alone. However, if a slot may is used in multiple classes, it
    is necessary traverse the data tree to identify the appropriate parent class. For example, the
    information in a mapped dataset with "groups" as the last element in TABLEPATH may relate to either
    the "AnalysisGroup" class or the "DataGroup" class and it's only possible to determine the correct class
    by identifying the class associated with the previous slot named in the TABLEPATH (e.g., if
    TABLEPATH is "/root/analysisGroupings/groups", the previous named slot is "analysisGroupings", which
    is associated with the "AnalysisGrouping" class, in which the "groups" slot uses the "AnalysisGroup"
    class). There are also situations where it is not possible to identify the parent class by traversing
    the data tree.

    The following datastep traverses the data tree specified in each TABLEPATH value to try and identify
    the range (i.e., class) for each slot. If a unique class cannot be identified, a pipe (|) delimited
    list of possible ranges/classes is created. The unique class is then identified through subsequent
    processing based on slot variable population (see the CLASS_DATASET macro).
  */

  data slot_datasets;
  set map_datasets end = lastone;
  by ordinal_datasets;
  length parent_slot parent_range slot rangelist check_range range $ 100 depth 8;
  if _n_ eq 1 then
    do;
    /* Hash table of class/slot definitions */
    declare hash class_slots(dataset: "work.&slotdefs (rename = (parent_class = parent_range))", multidata:"y");
    class_slots.definekey("parent_range","slot");
    class_slots.definedata("range");
    class_slots.definedone();
    call missing(range);
  end;
  rangelist = '';
  /* Loop through the slots named in the TABLEPATH value */
  do _i_ = 2 to countw(tablepath,'/','m');
    parent_slot = slot;
    parent_range = range;
    slot = scan(tablepath,_i_,'/','m');
    /* If range hasn't been found yet, this must be the "root" element so just look up its range */
    if range eq '' then rc = class_slots.find(key:range,key:slot);
    /* Otherwise, loop through each of the previously found range/class values to see which one contains this slot */
    else 
      do _j_ = 1 to countw(range,'|');
        check_range = scan(range,_j_,'|');
        rc = class_slots.find(key:check_range,key:slot);
        if rc eq 0 then
          do;
            /* If the parent range was a list, replace it with the single range/class that contains this slot */
            parent_range = check_range;
            goto found;
          end;
      end;
    found:
    /* If there are additional classes that contain this slot, add them to the list */
    class_slots.has_next(result:more);
    if more then
      do;
      rangelist = range;
        do while(more);
          rc = class_slots.find_next(key:parent_range,slot); 
          rangelist = catx('|',rangelist,range);
        class_slots.has_next(result:more);
        end;
      range = rangelist;
      end;
  end;
  depth = countw(tablepath,'/');
  /* Assign the TPTHLEN macro variable as the length of the TABLEPATH variable */
  if lastone then call symput('tpthlen',put(vlength(tablepath),best.-l));
  drop rangelist check_range rc _i_ _j_ more;
  run;

  /*
     The JSON libname engine automapper creates a separate dataset for each repeating element in an
     array, even if the repeating elements are single values. In the ARS model, repeating single values
     are not separate instances of a class; they are separate values for an attribute/slot within a class.
     To create class-based datasets, these repeating values need to be moved into the parent dataset.

     The following datastep identifies mapped variables in mapped datasets that are based on repeating
     string or integer values, changes each identified variable mapping to include it in the parent
     mapped dataset (by assigning a new value for ordinal_DATASETS and TABLEPATH), and removes the
     redundant dataset and ordinal variable mappings.
  */ 

  data map_datasets_variables ( keep = chgods ordinal_VARIABLES name type path current_length rename = (chgods = ordinal_DATASETS));
  length chgods 8 range $ 100 dsname $ 32 tablepath $ 200;
  set objvar &maplib..datasets_variables end = lastone;
  by ordinal_datasets;
  retain chgods;
  if _n_ eq 1 then
    do;
      /* Hash table to look up TABLEPATH and range by ordinal_datasets value */
      declare hash h(dataset: "work.slot_datasets");
      h.definekey("ordinal_datasets");
      h.definedata("tablepath","range");
      h.definedone();
      /* Hash table of mapped datasets */
      declare hash mapds(dataset: "work.map_datasets (rename = (ordinal_datasets = chgods))", ordered:"y");
      mapds.definekey("tablepath");
      mapds.definedata("chgods","dsname","tablepath");
      mapds.definedone();
      call missing(range,dsname,tablepath);
    end;
    /* All variables in a mapped dataset will be modified in the same way, so only need to process the first */
    if first.ordinal_datasets then
      do;
        chgods = .;
        /* Find the range for the slot defining the mapped dataset */
        rc = h.find();
        /* If the dataset has been created for repeating string or integer values... */
        if range in ('string','integer') then
          do;
            /* Remove the dataset mapping */
            mapds.remove();
            /* Create a new tablepath by removing the last element of the original tablepath */
            lstslsh = findc(tablepath,'/','b');
            ntpth = substr(tablepath,1,lstslsh-1);
            /* Retrieve the ordinal_datasets and dsname values corresponding with the new tablepath */
            rc = mapds.find(key:ntpth);
            /* If there's no existing dataset with the new tablepath, keep removing the last tablepath
               element until a matching dataset is found */
            do while(rc ne 0);
              lstslsh = findc(ntpth,'/','b');
              ntpth = substr(tablepath,1,lstslsh-1);
              rc = mapds.find(key:ntpth);
            end;
          end;
        /* If the dataset is not for repeating string/integer, leave the ordinal_datasets value unchanged */
        else chgods = ordinal_datasets;
      end;
  /* Save the modified list of mapped datasets */
  if lastone then mapds.output(dataset: "work.map_datasets (rename = (chgods = ordinal_datasets))");
  /* Remove ordinal variables that were defined for the original repeating string/integer dataset */
  if chgods ne ordinal_datasets and substr(name,1,8) eq 'ordinal_' then delete;
  run;

  /* Create a new JSON mapping definition based on the modified mapped datasets and variables */
  filename &maplib temp;
  %write_json_map(fref=&maplib,dsds=work.map_datasets,vards=work.map_datasets_variables);

  /* Reassign the libraries for mapped data and mapped dataset/variable definitions based on the new mapping */
  libname &inlib json map=&maplib;
  libname &maplib json;

%mend;
