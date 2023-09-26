%macro make_class_datasets(maplib=,inlib=,slotdefs=,outlib=,outdir=);

/***********************************************************************************\
*                                                                                   *
* Name: make_class_datasets.sas                                                     *
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
* OUTDIR: The path to the directory/folder that will contain the class-specific     *
*         datasets created from the JSON reporting event file.                      *
*                                                                                   *
* Dependencies: This macro calls the CLASS_DATASET macro. It also references the    *
*               WORK.SLOT_DATASETS dataset created by the MAP_JSON_RE macro and     *
*               the SASHELP.VTABLE view, and it expects there to be a WORK dataset  *
*               corresponding with each mapped dataset (as created by the           *
*               ADD_DATAPATH macro).                                                *
*                                                                                   *
\***********************************************************************************/

  /* Create the specified library for the specified path */

  libname &outlib "&outdir";

  /* Remove any previously created datasets from the new library */

  proc datasets lib=&outlib nolist kill;
  quit;

  /* Create a list of classes referenced by mapped datasets */

  proc sql noprint;
    select distinct range into : ranges separated by ' '
    from slot_datasets
    where range not in ('string','integer');
  quit;

  %let nrds = &sqlobs;

  /* Loop through the classes and ...*/

  %do i = 1 %to &nrds;
    %let rnglst = %scan(&ranges,&i,%str( ));
    /* More than one class may be referenced for each mapped dataset, so loop through each referenced class and ... */
    %do j = 1 %to %sysfunc(countw(&rnglst,%str(|)));
      /* Run the CLASS_DATASET macro for each */ 
      %class_dataset(maplib=&maplib,inlib=&inlib,classlst=&rnglst,classnm=%scan(&rnglst,&j,%str(|)),slotdefs=&slotdefs,outlib=&outlib);
    %end;
  %end;

  /* Create a list of WORK datasets corresponding with mapped datasets */

  proc sql noprint;

    select dsname
    into : dsnames separated by ' '
    from &maplib..datasets as a
    inner join sashelp.vtable as b
    on upcase(a.dsname) = b.memname
    where b.libname = 'WORK';

    %let nds = &sqlobs;

  quit;

  /* Delete the identified WORK datasets */

  proc datasets lib=work nolist;
    delete &dsnames;
  quit;

%mend;
