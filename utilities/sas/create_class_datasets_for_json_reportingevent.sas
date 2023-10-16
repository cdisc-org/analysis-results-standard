
/***********************************************************************************\
*                                                                                   *
* Name: create_class_datasets_for_json_reportingevent.sas                           *
*                                                                                   *
* Description: Reads in a JSON ReportEvent to create a separate dataset for each    *
*              ARS class referenced in the reporting event. In the created class    *
*              datasets:                                                            *
*              - There is one observation for each instance of the class.           *
*              - On each observation:                                               *
*                > The TABLEPATH variable contains the SAS-defined path for source  *
*                  dataset mapped in the JSON file.                                 *
*                > The DATAPATH variable contains a value (specified using JSON     *
*                  Pointer notation) indicating the location of the corresponding   *
*                  data in the input JSON reporting event file.                     *
*              - Multiple atomic values (e.g., multiple strings or multiple         *
*                numeric values) for a single attribute/slot are transposed into    *
*                separate variables (e.g., value1, value2, etc. for multiple values *
*                of the value attribute/slot).                                      *
*                                                                                   *
* Purpose: To create a generic, model-based representation of data contained in a   *
*          JSON reporting event file.                                               *
*                                                                                   *
* Dependencies: This program uses the following autocall macro files, which can be  *
*               downloaded from the utilities/sas/macros folder of the ARS GitHub   *
*               Repository:                                                         *
*               - add_datapath.sas                                                  *
*               - class_dataset.sas                                                 *
*               - get_class_slots.sas                                               *
*               - make_class_datasets.sas                                           *
*               - map_json_re.sas                                                   *
*               - write_json_map.sas                                                *
*                                                                                   *
* Notes: DATAPATH values are '/' delimited lists of attribute/slot names and, for   *
*        repeating objects, zero-indexed ordinal values. For example, a DATAPATH    *
*        value of "/methods/1/operations/0" indicates the first item (ordinal = 0)  *
*        in the list of items specified for the "operations" attibute of the second *
*        item (ordinal = 1) in the list of items specified for the "methods"        *
*        attribute of the reporting event - i.e. the first operation of the         *
*        reporting event's second method.                                           *
*                                                                                   *
*        The DATAPATH variable may be used to reassemble information that is split  *
*        across multiple class datasets. For example, OperationResult records can   *
*        be combined with corresponding ResultGroup records using PROC SQL:         *
*                                                                                   *
*        PROC SQL;                                                                  *
*          CREATE TABLE combined_results AS                                         *
*          SELECT *                                                                 *
*          FROM classds.OperationResult as a                                        *
*          LEFT JOIN classds.ResultGroup as b                                       *
*          ON SUBSTR(b.datapath,1,LENGTH(a.datapath)) = a.datapath;                 *
*        QUIT;                                                                      *
*                                                                                   *
*        This works because the first part of a child object's DATAPATH value       *
*        matches the DATAPATH value of its parent.                                  *
*                                                                                   *
*        The ARS example JSON content is UTF-8 encoded. Ideally, this program       *
*        should be run in a SAS session with UTF-8 encoding so that non-ASCII       *
*        example values such as "≥ 65 years" are represented correctly.             *
*                                                                                   *
\***********************************************************************************/

/***********************************************************************************\
* Configuration                                                                     *
*                                                                                   *
* Assign a value for each of the following 8 macro variables:                       *
*                                                                                   *
* MACDIR: The path to the local directory/folder containing the autocall macro      *    
*         files specified in Dependencies in the header above.                      *
*                                                                                   *
\*.................................................................................*/
%let macdir = %str(C:\CDISC\ars\analysis-results-standard\utilities\sas\macros);
/*.................................................................................*\
*                                                                                   *
* JSCHMAFL: The path to the local copy of the JSON-Schema definition file for the   *
*           ARS model, ars_ldm.json, which has been downloaded from the model       *
*           folder for the ARS GitHub repository.                                   *
*                                                                                   *
\*.................................................................................*/
%let jschmafl = %str(C:\CDISC\ars\analysis-results-standard\model\ars_ldm.json);
/*.................................................................................*\
*                                                                                   *
* REJSONFL: The path to the JSON file containing the reporting event information to *
*           be converted to SAS datasets.                                           *
*                                                                                   *
\*.................................................................................*/
%let rejsonfl = %str(C:\CDISC\ars\analysis-results-standard\workfiles\examples\ARS v1\Common Safety Displays.json);
/*.................................................................................*\
*                                                                                   *
* MAPLIB: The fileref to be used for the temporary JSON mapping that is generated   *
*         and then rewritten. This fileref is also used as the libref of the        *
*         corresponding library that is created to access mapped dataset and        *
*         variable definitions. The default value ("map") does not need to be       *
*         changed.                                                                  *
*                                                                                   *
\*.................................................................................*/
%let maplib = %str(map);
/*.................................................................................*\
*                                                                                   *
* INLIB: The fileref to be used for the JSON reporting event file specified in the  *
*        REJSONFL macro variable. This fileref is also used as the libref of the    *
*        corresponding library that is created to access the mapped datasets. The   *
*        default value ("in") does not need to be changed.                          *
*                                                                                   *
\*.................................................................................*/
%let inlib = %str(in);
/*.................................................................................*\
*                                                                                   *
* SLOTDEFS: The name to be assigned to the dataset containing class/slot            *
*           definitions read in from the JSON schema file. The default value        *
*           ("class_slots") does not need to be changed. Note that this should be a *
*           single-level name for a dataset to be created in the WORK library.      *
*                                                                                   *
\*.................................................................................*/
%let slotdefs = %str(class_slots);
/*.................................................................................*\
*                                                                                   *
* OUTLIB: The libref to be used for the library that will contain the created class *
*         datasets. The default value ("classds") does not need to be changed, but  *
*         it may be replaced with a value that is specific to the reporting event   *
*         being read in (e.g., "csd" for the Common Safety Displays example         *
*         reporting event or "fdastf" from the FDA STF example reporting event).    *
*                                                                                   *
\*.................................................................................*/
%let outlib = %str(classds);
/*.................................................................................*\
*                                                                                   *
* OUTDIR: The path to the directory/folder that will contain the class-specific     *
*         datasets created from the JSON reporting event file.                      *
*                                                                                   *
\*.................................................................................*/
%let outdir = %str(C:\CDISC\ars\classds);
/*.................................................................................*\
*                                                                                   *
* [End of configuration]                                                            *
*                                                                                   *
\***********************************************************************************/

/* Clear the WORK library */

proc datasets lib=work nolist kill;
quit;

/* 
   Add the directory/folder containing autocall macro files - specified in the
   MACDIR macro variable - to the SASAUTOS option.
*/

%macro add_sasautos(macdir=);
  options mautosource mrecall;
  %let sasautos=%sysfunc(getoption(sasautos));
  %if %index(&sasautos,"%trim(&macdir)") eq 0 %then
    %do;
      options append=(sasautos=("%trim(&macdir)"));
    %end;
%mend;

%add_sasautos(macdir=&macdir);

/* 
   Create a WORK dataset containing class/slot definitions from the specified
   JSON-Schema file.
*/

%get_class_slots(jschmafl=&jschmafl,outds=&slotdefs);

/*
   Create and modify a JSON mapping file for the specified JSON reporting event
   file.
*/

%map_json_re(rejsonfl=&rejsonfl,maplib=&maplib,inlib=&inlib,slotdefs=&slotdefs);

/*
   For each of the mapped reporting event datasets, create a WORK dataset in which
   ordinal variables are replaced with the TABLEPATH and DATAPATH variables.
*/

%add_datapath(maplib=&maplib,inlib=&inlib,slotdefs=&slotdefs);

/* Collate the mapped reporting event datasets into class-specific datasets */

%make_class_datasets(maplib=&maplib,inlib=&inlib,slotdefs=&slotdefs,outlib=&outlib,outdir=&outdir);


