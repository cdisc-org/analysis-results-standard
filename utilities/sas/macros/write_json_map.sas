%macro write_json_map(fref=,dsds=,vards=);

/***********************************************************************************\
*                                                                                   *
* Name: write_json_map.sas                                                          *
*                                                                                   *
* Description: Reads the mapped dataset and variable definitions from the specified *
*              input datasets and writes a JSON libname engine mapping to the       *
*              specified file reference.                                            *
*                                                                                   *
* Input parameters:                                                                 *
*                                                                                   *
* FREF: The fileref for the JSON mapping.                                           *
*                                                                                   *
* DSDS: The name of the dataset containing mapped dataset definitions.              *
*                                                                                   *
* VARDS: The name of the dataset containing mapped dataset variable definitions.    *
*                                                                                   *
\***********************************************************************************/

  %local tdsid vdsid rc vrc;

  proc json out=&fref pretty nosastags;
    /* Initialize the mapping */
    write open object;
      write values "DATASETS";
      /* Open the specified mapped dataset definition dataset */
      write open array;
        %let tdsid = %sysfunc(open(&dsds,i));
        %syscall set(tdsid);
        /* Loop through each of the mapped dataset definitions and ... */
        %let rc=%sysfunc(fetch(&tdsid));
        %do %while(&rc eq 0);
          /* Add the dataset definition details to the mapping */
          write open object;
            write values "DSNAME" "&DSNAME";
            write values "TABLEPATH" "&TABLEPATH";
            write values "VARIABLES";
            /* Open the mapped dataset variables dataset for the mapped dataset being processed and ... */
            write open array;
              %let vdsid = %sysfunc(open(&vards (where = (ordinal_datasets eq &ordinal_datasets)),i));
              %syscall set(vdsid);
              /* Loop through each of the mapped dataset variable definitions and ... */
              %let vrc=%sysfunc(fetch(&vdsid));
              %do %while(&vrc eq 0);
                /* Add the variable definition details to the mapping */
                write open object;
                  write values "NAME" "&NAME";
                  write values "TYPE" "&TYPE";
                  write values "PATH" "&PATH";
                  %if &CURRENT_LENGTH ne . %then 
                    write values "CURRENT_LENGTH" &CURRENT_LENGTH;;
                write close;
                %let vrc=%sysfunc(fetch(&vdsid));
              %end;
              %let vrc = %sysfunc(close(&vdsid));
            write close;
          write close;
          %let rc=%sysfunc(fetch(&tdsid));
        %end;
        %let rc = %sysfunc(close(&tdsid));
      write close;
    write close;
  run;

%mend;
