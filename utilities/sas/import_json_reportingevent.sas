/***********************************************************************************\
*                                                                                   *
* Name: import_json_reportingevent.sas                                              *
*                                                                                   *
* Description: Reads in a JSON ReportEvent to create datasets corresponding with    *
*              the sheets in the ARS Template.xlsx file.                            *
*                                                                                   *
* Purpose: To demonstrate various methods of reading JSON content to create         *
*          datasets. The ARS Template.xlsx file is just an example of how ARS       *
*          information may be represented in a tabular structure - it is not        *
*          the "standard" tabular representation of ARS data. This program just     *
*          uses the template's structure to demostrate conversion methods. Other    *
*          tabular representations may be created using similar methods to          *
*          facilitate other types of implementation.                                *
*                                                                                   *
* Notes: The ARS example JSON content is UTF-8 encoded. Ideally, this program       *
*        should be run in a SAS session with UTF-8 encoding so that non-ASCII       *
*        example values such as "≥ 65 years" are represented correctly.             *
*                                                                                   *
*        The datasets are written to the WORK library. The WORK library is cleared  *
*        at the beginning of execution and temporary interim datasets are removed   *
*        at the end. Comment out or remove the relevant PROC DATASETS call if you   *
*        don't want clearing/removal to happen.                                     *
*                                                                                   *
\***********************************************************************************/

/***********************************************************************************\
*  JSON content may be read using the JSON libname engine either from a file        *
*  or directly from an API call.  In either case, this program expects the JSON     *
*  content to represent a full, single reporting event.                             *
*  Examples:                                                                        *
*                                                                                   *
filename in "C:\CDISC\analysis-results-standard-api\workfiles\examples\Hackathon\Common Safety Displays.json" encoding="utf-8";
filename in url "http://127.0.0.1:8000/mdr/ars/reportingevents/0/" encoding="utf-8" debug;
*                                                                                   *
\***********************************************************************************/

filename in "[CHANGE TO: Path to .json file]" encoding="utf-8";
/**OR**/
filename in url "[CHANGE TO: API reporting event request address]" encoding="utf-8" debug;

/***********************************************************************************\
*  The JSON libname engine can use a configurable MAP file to locate dataset and    *
*  variable information within the JSON content.                                    *
*  Example:                                                                         *
*                                                                                   *
filename map 'C:\CDISC\ars\analysis-results-standard\utilities\sas\reportingevent.map';
*                                                                                   *
*  Note that variable lengths are assigned automatically according to the data      *
*  in the JSON content that was used initially to generate the MAP file. If the     *
*  same MAP file is reused for different content, it may be necessary to adjust     *
*  the variable lengths assigned in the MAP file to avoid truncation of longer data *
*  values.                                                                          *
\***********************************************************************************/

filename map '[CHANGE TO: Path to MAP file for reporting event JSON content]';

libname in json map=map automap=reuse;

/* Clear the WORK library */

proc datasets library = work nolist kill;
quit;

/***********************************************************************************\
* Datasets/sheets: ReportingEvent, ReferenceDocuments, GlobalDisplaySections,       *
*                  TerminologyExtensions                                            *
*                                                                                   *
* These simple datasets do not require much processing so their structure has been  *
* defined by updating the reportingevent.map file and they can then just be copied. *
\***********************************************************************************/

proc copy in=in out=work;
select ReportingEvent
	   ReferenceDocuments
       GlobalDisplaySections
       TerminologyExtensions;
run;

/***********************************************************************************\
* Dataset/sheet: Categorizations                                                    *
*                                                                                   *
* The JSON libname engine creates a separate dataset for each level within the      *
* hierarchical JSON structure and automatically assigns ordinal variables that      *
* indicate the order of the represented elements. These ordinal variables can be    *
* used to join data back together using PROC SQL.                                   *
*                                                                                   *
* Note that this query would need to be adjusted if there were additional levels    *
* of categorization (i.e., subcategorizations within subcategorizations).           *
\***********************************************************************************/

proc sql noprint;
	create table Categorizations (drop = tabord ordinal_subcategorizations) as
	select 2 as tabord,a.ordinal_subcategorizations,a.id, a.label,
           b.id as parent_category_id, c.id as category_id, c.label as category_label
	from in.categories_subcategorizations as a
	inner join in.Analysiscategorizat_categories as b
	on a.ordinal_categories = b.ordinal_categories
	inner join in.subcategorizations_categories as c
	on a.ordinal_subcategorizations = c.ordinal_subcategorizations
	union all
	select 1,a.ordinal_analysisCategorizations,a.id, a.label, ' ' , b.id, b.label
	from in.Analysiscategorizations as a
	inner join in.Analysiscategorizat_categories as b
	on a.ordinal_analysisCategorizations = b.ordinal_analysisCategorizations
	order by 1,2;
quit;

/***********************************************************************************\
* Datasets/sheets: ListOfPlannedAnalyses, ListOfPlannedOutputs                      *
*                                                                                   *
* Both these datasets/sheets have the same structure as they're based on the        *
* NestedList class. This class allows any number of levels (sublists within         *
* sublists within sublists...).  The JSON libname engine also creates an ALLDATA    *
* dataset that represents the hierarchical JSON content in a standardized tabular   *
* structure. This structure has enough Pn variables to accommodate the maximum      *
* number of JSON levels and all values are represented in a single variable. The    *
* P variable indicates the number of levels represented on each row (and can        *
* therefore be used to select the Pn variable containing the name of the attribute  *
* whose value is represented on the record).                                        *
\***********************************************************************************/

/* Store a list of the Pn variables in a macro variable for later use.
   Also create a corresponding list of OPn variables that will be used to store
   hierarchical ordering values */

proc sql noprint;
	select name,  'O' || name into : pvars separated by ' ',: ordvars separated by ' '
	from sashelp.vcolumn
	where libname = 'IN'
	and memname = 'ALLDATA'
	and trim(name) like 'P_%';
quit;

/* The GET_NLIST macro flattens and transposes the ALLDATA information. */

%macro get_nlist(list);	

	data _tmp_&list ;
	set in.alldata (where = (p1 eq "&list"));
	length _name_ $ 10;
	array pvars {*} &pvars;
	array ordvars {*} &ordvars;
	do _i_ = p+1 to dim(ordvars);
		ordvars{_i_} = .;
	end;
	select (pvars{p});
		when("&list")
			/* Create a set of dummy records to prespecify the transposed variable order */
			do _name_ = 'level', 'name', 'order', 'outputId', 'analysisId';
				output;
			end;
		when("sublist");
		when("listItems") ordvars{p}+1; /* Increment hierarchical order for each new set */ 
		otherwise                       /* of list items                                 */
			do;
				_name_ = pvars{p};
				output;
			end;
	end;
	run;

	proc sort data = _tmp_&list;
	by &ordvars;
	run;

	proc transpose data = _tmp_&list
                   out = %sysfunc(propcase(&list.))
                        (where = (level is not missing) /* Remove the dummy records */
                         drop = &ordvars _name_);
	by &ordvars;
	id _name_;
	var Value;
	run;

%mend get_nlist;

%get_nlist(listOfPlannedAnalyses)
%get_nlist(listOfPlannedOutputs)

/***********************************************************************************\
* Dataset/sheet: Outputs                                                            *
*                                                                                   *
* This dataset/sheet contains one row per output, with:                             *
*  - Multiple category ids represented as a ' | ' delimited list in the categoryIds *
*    variable.                                                                      *
*  - The id of each display in the output shown in a separate variable named        *
*    "display[display order]_id" (e.g., display1_id, display2_id).                  *
*  - The file name and location for multiple file specifications each shown as a    *
*    single value in a single variable - the Excel template expects the same file   *
*    name (without file type extension) and location to be used for all file        *
*    specifications for a single output (note that this is not a requirement of the *
*    model). Multiple file type extensions are shown are represented as a ' | '     *
*    delimited list in a single variable.                                           *
*                                                                                   *
\***********************************************************************************/

/* Create a concatenated list of referenced category ids */

%macro get_catid(objstype /* Objects type: should be outputs or analyses */);

	data _tmp_&objstype._categoryids;
	set in.&objstype._categoryids;
	array catids{*} categoryIds:;
	categoryIds = catx(' | ',of catids{*});
	keep ordinal_&objstype categoryIds;
	run;

%mend get_catid;

%get_catid(outputs)

/* Transpose referenced displays to create one variable for each display id per output. 
   Note that ordinal variable values are assigned incrementally by the JSON libname  
   engine, so it's usually not necessary to sort before merging by ordinal variables */

data _tmp_display_ids;
merge in.outputs_displays
      in.displays_display (keep = ordinal_displays id);
by ordinal_displays;
_name_ = cats('display',order,'_id');
run;

proc transpose data=_tmp_display_ids out=_tmp_output_display_ids (drop = _name_);
by ordinal_outputs;
var id;
id _name_;
run;

/* Combine file type controlled terms and sponsor term ids into a single variable */

data _tmp_output_filespecifications1;
merge in.outputs_filespecifications
      in.filespecifications_filetype;
by ordinal_fileSpecifications;
array ftype{2} $ controlledTerm sponsorTermId;
fileType = coalescec(of ftype{*});
drop controlledTerm sponsorTermId;
run;

/* Create a single file specification record per output. This is not a requirement
   of the model - it's just how the Excel template is currently designed */

data _tmp_output_filespecifications2;
set _tmp_output_filespecifications1;
by ordinal_outputs;
attrib fileSpecification_file_name length = $ 200
       fileSpecification_file_location length = $ 200
	   fileSpecification_file_fileTypes length = $ 200
                                        label = 'fileSpecification_file_fileType(s)';
retain fileSpecification_file_:;
if first.ordinal_outputs then
	do;
		fileSpecification_file_name = name;
		fileSpecification_file_location = location;
		fileSpecification_file_fileTypes = fileType;
	end;
else
	do;
		/* Although not a requirement of the logical data model, the Excel
	       template expects the same file name and location for all files
	       of different formats for the same output */
		if fileSpecification_file_name ne name then
			put 'WARN' 'ING: Inconsistent file name found for ordinal_output: ' ordinal_outputs;
		if fileSpecification_file_location ne location then
			put 'WARN' 'ING: Inconsistent file location found for ordinal_output: ' ordinal_outputs;
		fileSpecification_file_fileTypes = catx(' | ',fileSpecification_file_fileTypes,fileType);
	end;
if last.ordinal_outputs then output;
drop ordinal_fileSpecifications ordinal_fileType name location fileType;
run;

/* Join all output information to create a single dataset */

proc sql noprint;
	create table Outputs (drop = ordinal_outputs) as
	select a.id, a.version, a.name, b.categoryIds,
	       c.*, /* Using '*' as the max number of displays per output is unknown. */
           d.fileSpecification_file_name,
           d.fileSpecification_file_location,
           d.fileSpecification_file_fileTypes
	from in.outputs as a
	left join
	_tmp_outputs_categoryids as b
	on a.ordinal_outputs = b.ordinal_outputs
	left join
	_tmp_output_display_ids as c
	on a.ordinal_outputs = c.ordinal_outputs
	left join
	_tmp_output_filespecifications2 as d
	on a.ordinal_outputs = d.ordinal_outputs;
quit;

/***********************************************************************************\
* Dataset/sheet: Displays                                                           *
*                                                                                   *
* This dataset/sheet contains one row for each value specified for each section     *
* of the display.  If there are multiple sections (Title, Footnote, etc.) or        *
* multiple entries for a given section, display-level information (e.g., id, name)  *
* is shown on every row for the display. Sub-section text can be specified either   *
* with an assigned id and piece of text or as a reference to a GlobalDisplaySection.*
* In this dataset/sheet, the individually specified ids and referenced global       *
* display section ids are shown in the same variable (displaySection_subSection_id) *
\***********************************************************************************/

proc sql noprint;
	create table Displays as
	select a.id, a.name, a.version, a.displayTitle,
	       b.sectionType as displaySection_sectionType,
	       c.order as displaySection_ordSubSect_order label = 'displaySection_orderedSubSection_order',
	       coalescec(c.subSectionId,d.id) as displaySection_subSection_id,
	       d.text as displaySection_subSection_text
	from in.displays_display as a
	left join in.display_displaySections as b
	on a.ordinal_display = b.ordinal_display
	left join in.displaySections_orderedSubsect as c
	on b.ordinal_displaySections = c.ordinal_displaySections
	left join in.orderedSubSections_subSection as d
	on c.ordinal_orderedSubSections = d.ordinal_orderedSubSections;
quit;

/***********************************************************************************\
* Datasets/sheets: OutputProgrammingCode, AnalysisProgrammingCode,                  *
*                  AnalysisMethodCodeTemplate                                       *
*                                                                                   *
* Programming code (including template code associated with analysis methods) may   *
* be specified either as textual code statements stored in the 'code' attribute or  *
* as a reference to a document (e.g., a program file). The model currently expects  *
* there to be only one code specification per output/analysis/method and, in these  *
* datasets/sheets, the type of specification is indicated by the 'specifiedAs'      *
* variable ('Code' or 'DocumentRef'). The value is calculated here as "if there is  *
* a programmingCode/codeTemplate document reference for the output/analysis/method  *
* then 'DocumentRef'; otherwise 'Code'".                                            *
*                                                                                   *
* Note that the JSON libname engine automatically assigns dataset names with an     *
* incrementing numeric suffix when the same JSON sub-element is found in different  *
* places in the input JSON structure (e.g. "programmingCode_documentRef" for        *
* analysis programming code document refs and "programmingCode_documentRef1" for    *
* output programming code document refs). Some of these automatically assigned      *
* dataset names were changed in the reportingevent.map file to make them more       *
* meaningful and consistent so that they can be processed in the same way by a      *
* macro, e.g.:                                                                      *
* - programmingCode_documentRef  -> analyses_programmingCode_docRef                 *
* - programmingCode_documentRef1 -> outputs_programmingCode_docRef                  *
* - codeTemplate_documentRef     -> methods_codeTemplate_docRef                     *
\***********************************************************************************/

%macro get_progcode(objtype /* Object type: should be output, analysis or method */);

	%if &objtype eq %str(analysis) %then %let objstype = analyses;
	%else %let objstype = &objtype.s;

	%if &objtype eq %str(method) %then 
		%do;
			%let dsname = AnalysisMethodCodeTemplate;
			%let codetype = codeTemplate;
		%end;
	%else 
		%do;
			%let dsname = %sysfunc(propcase(&objtype))ProgrammingCode;
			%let codetype = programmingCode;
		%end;

	proc sql noprint;
		create table &dsname as
		select a.id as &objtype._id,
		       b.context,
			   case c.ordinal_&codetype
			   	when . then 'Code'
				else 'DocumentRef'
		       end as specifiedAs,
			   b.code
		from in.&objstype as a
		inner join in.&objstype._&codetype as b
		on a.ordinal_&objstype = b.ordinal_&objstype
		left join in.&objstype._&codetype._docRef as c
		on b.ordinal_&codetype = c.ordinal_&codetype;
	quit;

%mend get_progcode;

%get_progcode(output)
%get_progcode(analysis)
%get_progcode(method)

/***********************************************************************************\
* Datasets/sheets: OutputCodeParameters, AnalysisCodeParameters,                    *
*                  AnalysisMethodCodeParameters                                     *
*                                                                                   *
* These datasets/sheets contain one row per parameter per output/analysis/method.   *
* Programming code parameters for outputs/analyses/methods all have a name and      *
* description.  For outputs/analyses, each parameter has a single value (i.e., the  *
* value of the parameter that is/was used when the programming code is/was run to   *
* produce the results for the output/analysis). For methods, each parameter may     *
* have one of the following:                                                        *
*  - A valueSource indicating the analysis metadata attribute that holds the value  *
*    to be used for the parameter (either when analysis-specific code is generated  *
*    or at run time), or                                                            *
*  - A single value representing the parameter value to be used with the            *
*    programming code for all analyses that use the method (in which case the value *
*    does not need to be re-specified as a parameter value for each analysis).      *
*  - A list of two or more values representing the parameter values available to    *
*    be used when the template code is used in a specific analysis. In this case,   *
*    the single parameter value selected from the list should be specified as the   *
*    analysis programming code parameter value.                                     *
\***********************************************************************************/

%macro get_codeparm(objtype /* Object type: should be output, analysis or method */);

	%if &objtype eq %str(analysis) %then %let objstype = analyses;
	%else %let objstype = &objtype.s;

	%if &objtype eq %str(method) %then 
		%do;
			%let dsname = AnalysisMethodCodeParameters;
			%let codetype = codeTemplate;
		%end;
	%else 
		%do;
			%let dsname = %sysfunc(propcase(&objtype))CodeParameters;
			%let codetype = programmingCode;
		%end;

	/* Create a concatenated list of parameter values. There should only be multiple
	   values for method code template parameters */

	data _tmp_&objstype._parameters_value (rename = (vlist = value));
	set in.&objstype._parameters_value;
	array vals{*} value:;
	vlist = catx(' | ',of vals{*});
	keep ordinal_parameters vlist;
	run;

	/* Combine parameter information to create a single dataset */

	proc sql noprint;
		create table &dsname as
		select a.id as &objtype._id,
		       c.name as parameter_name,
			   c.description as parameter_description,
			   %if &objtype eq method %then c.valueSource as parameter_valueSource,;
			   d.value as parameter_value
		from in.&objstype as a
		inner join in.&objstype._&codetype as b
		on a.ordinal_&objstype = b.ordinal_&objstype
		inner join in.&objstype._&codetype._params as c
		on b.ordinal_&codetype = c.ordinal_&codetype
		left join _tmp_&objstype._parameters_value as d
		on c.ordinal_parameters = d.ordinal_parameters;
	quit;

%mend get_codeparm;

%get_codeparm(output)
%get_codeparm(analysis)
%get_codeparm(method)

/***********************************************************************************\
* Datasets/sheets: OutputDocumentRefs, AnalysisDocumentRefs,                        *
*                  AnalysisMethodDocumentRefs                                       *
*                                                                                   *
* Two types of document reference may be made for any output/analysis/method:       *
* - 'Documentation' document references that are used for information purposes such *
*   as documentation of the output/analysis/method specification. There can be more *
*   than one document referenced as documentation for each output/analysis/method   *
*   and, for each document, there may be more than one page reference, where a page *
*   reference is one of the following:                                              *
*   > One or more page numbers specified as pageNumbers                             *
*   > One or more named destinations in the document (e.g., bookmarks) specified as *
*     pageNames                                                                     *
*   > A range of page numbers specified as firstPage to lastPage                    *
* - A 'ProgrammingCode' document reference for a file containing programming code   *
*   for outputs/analyses or template programming code for methods. Currently, the   *
*   model only allows one ProgrammingCode document reference for each output/       *
*   analysis/method. Page references (as described above) are optional and are      *
*   usually not provided as there is usually a single program per file.             *
*                                                                                   *
* These datasets/sheets contain one row for each page reference for each document   *
* reference (of either type) for each output/analysis/method. All types of page     *
* reference are represented in a single variable (pageRef_pages), with multiple     *
* page numbers/names shown as pipe-delimited lists and page ranges shown as         *
* [firstPage-lastPage] (e.g., 6-19). The referenceType variable is populated with   *
* either 'Documentation' or 'ProgrammingCode' to indicate the type of document      *
* reference.                                                                        *
*                                                                                   *
* Note that this program currently does not extract page references for             *
* ProgrammingCode document references.                                              *
\***********************************************************************************/

/* The GET_REFLIST macro creates pipe-delimited list of page numbers or names */

%macro get_reflist(objstype /* Objects type: should be outputs, analyses or methods */,
                   reftype /* Reference type: should be pageNumbers or pageNames */);

	/* Page numbers are numeric so (if necessary) change the MISSING option to ''
	   to prevent other indicators of missing (e.g., '.') being included in the
	   concatenated list */

	%let misset = 0;
	%let missopt = %sysfunc(getoption(missing,keyword));

	%if &reftype eq pageNumbers and &missopt ne %str( ) %then
		%do;
			%let missset = 1;
			options missing = '';
		%end;

	/* Create the concatenated list */

	data _tmp_&objstype._&reftype (rename = (reflist = &reftype));
	set in.&objstype._pagerefs_&reftype;
	array refs {*} &reftype:;
	reflist = catx('|',of refs{*});
	drop &reftype:;
	run;

	/* Reset the MISSING option if it was changed */
	%if &misset %then
		%do;
			options missing = "&missopt";
		%end;

%mend get_reflist;

/* The GET_DOCREFS macro combines all document and page reference information into a single dataset */

%macro get_docrefs(objtype /* Object type: should be output, analysis or method */);

	%if &objtype eq %str(analysis) %then %let objstype = analyses;
	%else %let objstype = &objtype.s;

	%if &objtype eq %str(method) %then 
		%do;
			%let dsname = AnalysisMethodDocumentRefs;
			%let codetype = codeTemplate;
		%end;
	%else 
		%do;
			%let dsname = %sysfunc(propcase(&objtype))DocumentRefs;
			%let codetype = programmingCode;
		%end;

	%get_reflist(&objstype,pageNumbers)
	%get_reflist(&objstype,pageNames)

	proc sql noprint;
		create table &dsname as
		select a.id as &objtype._id,
		       b.referenceType,
			   b.referenceDocumentId as refDocumentId,
			   c.refType as pageRef_refType,
			   c.label as pageRef_label,
			   case
			     when c.firstPage is not null and c.lastPage is not null then catx('-',c.firstPage,c.lastPage)
			     else d.reflist
			   end as pageRef_pages
		from in.&objstype as a
		inner join 
			(select ordinal_&objstype, ordinal_documentRefs, 'Documentation  ' as referenceType, referenceDocumentId
			 from in.&objstype._documentRefs
			 union all
			 select ba.ordinal_&objstype, bc.ordinal_documentRef, 'ProgrammingCode', bc.referenceDocumentId
			 from in.&objstype as ba
			 inner join in.&objstype._&codetype as bb
			 on ba.ordinal_&objstype = bb.ordinal_&objstype
			 inner join in.&objstype._&codetype._docRef as bc
			 on bb.ordinal_&codetype = bc.ordinal_&codetype) as b
		on a.ordinal_&objstype = b.ordinal_&objstype
		left join (select 'Documentation  ' as referenceType, *
	               from in.&objstype._documentRefs_PageRefs) as c
		on b.referenceType = c.referenceType
	    and b.ordinal_documentRefs = c.ordinal_documentRefs
		left join
			(select 'Documentation  ' as referenceType, ordinal_pageRefs, pageNumbers as reflist
			 from _tmp_&objstype._pageNumbers
			 union all
			 select 'Documentation  ', ordinal_pageRefs, pageNames
			 from _tmp_&objstype._pageNames) as d
		on c.referenceType = d.referenceType
	    and c.ordinal_pageRefs = d.ordinal_pageRefs
		order by a.id, b.referenceType;
	quit;

%mend get_docrefs;

%get_docrefs(output)
%get_docrefs(analysis)
%get_docrefs(method)

/***********************************************************************************\
* Datasets/sheets: DataSubsets, AnalysisSets                                        *
*                                                                                   *
* The structure of both these datasets/sheets is the same because data subsets and  *
* analysis sets are both based on the WhereClause class. Both datasets/sheets       *
* contain one row for each compenent of the each where clause (simple dataset       *
* variable comparator value(s) or the logical operator for a compound expression.   *
* The id and label for the data subset or analysis set is shown on all the relevant *
* rows.                                                                             *
\***********************************************************************************/

/* The GET_WC macro flattens and transposes where clause information from the ALLDATA
   dataset and then copies id and label to all rows for the data subset or analysis
   set */

%macro get_wc(wctype /* Where clause type: should be dataSubsets or analysisSets */);

	data _tmp_&wctype.1 ;
	set in.alldata (where = (p1 eq "&wctype"));
	length _name_ $ 20;
	retain dummydone 0;
	array pvars {*} &pvars;
	array ordvars {*} &ordvars;
	do _i_ = p+1 to dim(ordvars);
		ordvars{_i_} = .;
	end;
	select (pvars{p});
		when("&wctype")
			/* Create a set of dummy records to prespecify the transposed variable order */
			do;
				if not dummydone then
					do;
						dummydone+1;
						do _name_ = 'id', 'label', 'level', 'order', 'logicalOperator', 'dataset',
                                    'variable', 'comparator', 'value1', 'value2', 'value3';
							output;
						end;
					end;
				ordvars{p}+1;
			end;
		when("condition", "compoundExpression", "value");
		when("whereClauses") ordvars{p}+1;
		otherwise
			do;
				_name_ = pvars{p};
				output;
			end;
	end;
	run;

	proc sort data = _tmp_&wctype.1;
	by &ordvars;
	run;

	proc transpose data = _tmp_&wctype.1
                   out = _tmp_&wctype.2 (where = (level is not missing)
                                         drop = &ordvars _name_);
	by &ordvars;
	id _name_;
	var Value;
	run;

	/* Add id and label to all records for the same WhereClause and create a concatenated list of values */

	data &wctype (rename = (logicalOperator = compndExpression_logicalOperator
                            dataset = condition_dataset
                            variable = condition_variable
							comparator = condition_comparator
                            vlist = condition_value));
	set _tmp_&wctype.2;
	retain ret_id ret_lbl;
	array vals {*} value:;
	vlist = catx(" | ",of vals{*});
	if id ne '' then
		do;
			ret_id = id;
			ret_lbl = label;
		end;
	else
		do;
			id = ret_id;
			label = ret_lbl;
		end;
	drop value: ret_:;
	run;

%mend get_wc;

%get_wc(dataSubsets)
%get_wc(analysisSets)

/***********************************************************************************\
* Dataset/sheet: AnalysisGroupings                                                  *
*                                                                                   *
* Despite its name, this dataset/sheet contains information for both subject-based  *
* analysisGroupings and records-based dataGroupings, with records differentiated by *
* the "grouping_type" variable:                                                     *
* - Subject = analysisGroupings                                                     *
* - Data    = dataGroupings                                                         *
*                                                                                   *
* The dataDrive flag for subject and data groupings indicates whether the grouping  *
* is data-driven (the group are not prespecified and are derived from the set of    *
* values in the analysis dataset) or not. Groupings that are not data-driven each   *
* have a set of prespecified groups and each group is defined as a where clause.    *
*                                                                                   *
* This dataset/sheet contains one row per where clause expression (simple condition *
* or the logical operator for a compound expression) per group per grouping. Data-  *
* driven groupings are represented on a single row which has no group-level         *
* information. When group where clause information is included, group-level         *
* information is copied onto every row for the group and grouping-level information *
* is copied onto every row for the grouping.                                        *
\***********************************************************************************/

/* The GET_WC macro flattens and transposes grouping, group and where clause
   information from the ALLDATA dataset and then copies id, label, groupingVariable
   and dataDriven to all rows for the grouping, and group_id and group_label to all
   rows for the group */

%macro get_grouping(grptype /* Groupings type: should be analysisGroupings or dataGroupings */);

	data _tmp_&grptype.1 ;
	set in.alldata (where = (p1 eq "&grptype"));
	length _name_ $ 20;
	retain dummydone 0;
	array pvars {*} &pvars;
	array ordvars {*} &ordvars;
	do _i_ = p+1 to dim(ordvars);
		ordvars{_i_} = .;
	end;
	select (pvars{p});
		when("&grptype")
			/* Create a set of dummy records to prespecify the transposed variable order */
			do;
				if not dummydone then
					do;
						dummydone = 1;
						do _name_ = 'id', 'label', 'level', 'order', 'logicalOperator', 'dataset',
                                    'variable', 'comparator', 'value1', 'value2', 'value3';
							output;
						end;
					end;
				ordvars{p}+1;
			end;
		when("condition", "compoundExpression", "value");
		when("groups", "whereClauses") ordvars{p}+1;
		otherwise
			do;
				_name_ = pvars{p};
				output;
			end;
	end;
	run;

	proc sort data = _tmp_&grptype.1;
	by &ordvars;
	run;

	proc transpose data = _tmp_&grptype.1
                   out = _tmp_&grptype.2 (where = (n(%sysfunc(translate(&ordvars,%str(,),%str( )))) gt 0)
                                         drop = _name_);
	by &ordvars;
	id _name_;
	var Value;
	run;

	/* Add id, label, groupingVariable and dataDriven to all records for the same grouping,
	   add group_id and group_label to all reacords for the same group and create a concatenated
	   list of values */

	data _tmp_&grptype.3 (rename = (vlist = condition_value));
	retain id label groupingVariable dataDriven ret_id ret_lbl;
	set _tmp_&grptype.2 (rename = (groupingVariable = gv
                                  dataDriven = dd
                                  id = group_id
                                  label = group_label
                                  level = group_level
                                  logicalOperator = group_logicalOperator
                                  dataset = group_condition_dataset
                                  variable = group_condition_variable
                                  comparator = group_condition_comparator));
	by &ordvars;
	array vals {*} value:;
	vlist = catx(" | ",of vals{*});
	if first.op1 then
		do;
			id = group_id;
			label = group_label;
			groupingVariable = gv;
			dataDriven = upcase(dd);
			if not last.op1 then delete; /* Delete the grouping record unless it's the only */
		end;                             /* record for the grouping (data-driven groupings  */
	else                                 /* have no prespecified groups)                    */
		do;
			if id ne '' then
				do;
					ret_id = id;
					ret_lbl = label;
				end;
			else
				do;
					id = ret_id;
					label = ret_lbl;
				end;
		end;
	drop &ordvars value: ret_: gv dd;
	run;

%mend get_grouping;

%get_grouping(analysisGroupings)
%get_grouping(dataGroupings)

/* Combine subject-based analysisGroupings and records-based dataGroupings to create
   a single dataset and assign grouping_type */

data AnalysisGroupings;
length grouping_type $ 7;
set _tmp_analysisGroupings3 (in = ina)
	_tmp_dataGroupings3;
if ina then grouping_type = 'Subject';
else grouping_type = 'Data';
run;

/***********************************************************************************\
* Dataset/sheet: Analyses                                                           *
*                                                                                   *
* This dataset/sheet contains one row per analysis, with:                           *
*  - Multiple category ids represented as a ' | ' delimited list in the categoryIds *
*    variable.                                                                      *
*  - The id and resultsByGroup flag for each grouping in the analysis are           *
*    represented in seperate groupingIdn and resultsByGroupn variables (e.g.,       *
*    groupingId1, resultsByGroup1, groupingId2 and resultsByGroup2 for an analysis  *
*    with two groupings.                                                            *
*  - The referencedOperationRelationshipId and analysisId for each                  *
*    referencedAnalysisOperation are represented in separate                        *
*    refAnOp_refOperationRelIdn and refAnOp_analysisIdn variables (e.g.,            *
*    refAnOp_refOperationRelId1, refAnOp_analysisId1, refAnOp_refOperationRelId2    *
*    and refAnOp_analysisId2 for an analysis whose method contains an operation or  *
*    operations that reference the results from two other analysis operations).     *
*    Note that these variable names do not exactly match the column names in the    *
*    Excel template, which are too long for SAS variable names.                     *
\***********************************************************************************/

/* Create a concatenated list of referenced category ids */

%get_catid(analyses)

/* Add referenced operation order to faciliate transposition */

data _tmp_referencedAnalysisOperation;
set in.analyses_referencedAnalysisOpe;
by ordinal_analyses;
if first.ordinal_analyses then order = 1;
else order + 1;
run;

/* The GET_ANALYSES macro combines all the pieces of analysis information to create
   a single dataset. A macro is used because neither the maximum number of groupings
   per analysis nor the maximum number of referenced operations per analysis are
   known. Both maximum values are calculated and then sets of relevant variables
   and the necessary table joins are added to the query dynamically */

%macro get_analyses;

	proc sql noprint;

		select max(order) into : maxgrp
		from in.analyses_orderedGroupings;

		select max(order) into : maxref
		from _tmp_referencedAnalysisOperation;

		create table Analyses as
		select a.id, a.version, a.name, b.categoryIds,
	           coalescec(c.controlledTerm,c.sponsorTermId) as reason,
	           coalescec(d.controlledTerm,d.sponsorTermId) as purpose,
			   a.analysisSetId,
			   %do i = 1 %to &maxgrp;
			   g&i..groupingId as groupingId&i,
			   case g&i..resultsByGroup 
					when 0 then 'FALSE'
	                when 1 then 'TRUE'
					else ''
	           end as resultsByGroup&i,
			   %end;
			   a.dataSubsetId,
			   a.dataset,
			   a.variable,
			   a.methodId as method_id
			   %do i = 1 %to &maxref;
			   ,r&i..referencedOperationRelationshipI as refAnOp_refOperationRelId&i,
			   r&i..analysisId as refAnOp_analysisId&i
			   %end;
		from in.analyses as a
		left join _tmp_analyses_categoryIds as b
		on a.ordinal_analyses = b.ordinal_analyses
		left join in.analyses_reason as c
		on a.ordinal_analyses = c.ordinal_analyses
		left join in.analyses_purpose as d
		on a.ordinal_analyses = d.ordinal_analyses
		%do i = 1 %to &maxgrp;
		left join (select * from in.analyses_orderedGroupings where order = &i) as g&i
		on a.ordinal_analyses = g&i..ordinal_analyses
		%end;
		%do i = 1 %to &maxref;
		left join (select * from _tmp_referencedAnalysisOperation where order = &i) as r&i
		on a.ordinal_analyses = r&i..ordinal_analyses
		%end;;

	quit;

%mend get_analyses;

%get_analyses

/***********************************************************************************\
* Dataset/sheet: AnalysisMethods                                                    *
*                                                                                   *
* This dataset/sheet contains one row for each operation for each defined method.   *
* If the method has more than one operation, method-level information (id, name,    *
* label and description) is copied onto all rows for the method.                    *
*                                                                                   *
* If an operation has referenced operation relationships (i.e., the results of the  *
* operation are to be calculated with reference to the result of one or more other  *
* operations), the id, referencedOperationRole (the role that the referenced        *
* operation plays in the calculation of this operation), operationId (the id of the *
* referenced operation) and description are represented in separate refOpReln_id,   *
* refOpReln_refOperationRole, refOpReln_operationId and refOpReln._description      *
* variables (e.g., separate refOpRel1_id, refOpRel1_refOperationRole,               *
* refOpRel1_operationId, refOpRel1_description, refOpRel2_id,                       *
* refOpRel2_refOperationRole, refOpRel2_operationId and refOpRel2_description for a *
* method that contains an operation that uses the results of two other operations). *
* Note that these variable names do not exactly match the column names in the Excel *
* template, which are too long for SAS variable names.                              *
*                                                                                   *
* Sponsor-defined terminology may be used for the referenced operation role, so     *
* both controlled terms such as NUMERATOR or DENOMINATOR, or the sponsor term id    *
* for a sponsor-defined term are represented in the same refOpReln_refOperationRole *
* variable.                                                                         *
\***********************************************************************************/

/* Add operation order, which in the spreadsheet but not in the model */

data _tmp_methods_operations;
set in.methods_operations;
by ordinal_methods;
if first.ordinal_methods then order = 1;
else order + 1;
run;

/* Add referenced operation order to faciliate transposition */

data _tmp_operations_referencedOp;
set in.operations_referencedOperation;
by ordinal_operations;
if first.ordinal_operations then order = 1;
else order + 1;
run;

/* The GET_METHODS macro combines all pieces of method information into a single
   dataset. The maximum number of referenced operations per method is calculated
   and sets of variables and table joins are added to the query dynamically */

%macro get_methods;

	proc sql noprint;

		select max(order) into : maxref
		from _tmp_operations_referencedOp;

		create table AnalysisMethods as
		select a.id, a.name, a.label, a.description,
		       b.id as operation_id,
			   b.name as operation_name,
			   b.order as operation_order,
			   b.label as operation_label,
			   b.resultPattern as operation_resultPattern
			   %do i = 1 %to &maxref;
			   ,r&i..id as refOpRel&i._id,
			   r&i..referencedOperationRole as refOpRel&i._refOperationRole,
			   r&i..operationId as refOpRel&i._operationId,
			   r&i..description as refOpRel&i._description
			   %end;
		from in.methods as a
		left join _tmp_methods_operations as b
		on a.ordinal_methods = b.ordinal_methods
		%do i = 1 %to &maxref;
		left join (select ra.ordinal_operations, ra.ordinal_referencedOperationRelat, ra.id,
	               coalescec(rb.controlledTerm, rb.sponsorTermId) as referencedOperationRole,
	               ra.operationId, ra.description
	               from _tmp_operations_referencedOp as ra
	               inner join in.refere_referencedOperationRole as rb
	               on ra.ordinal_referencedOperationRelat = rb.ordinal_referencedOperationRelat
				   where ra.order = &i) as r&i
		on b.ordinal_operations = r&i..ordinal_operations
	    %end;;

	quit;

%mend get_methods;

%get_methods

/***********************************************************************************\
* Dataset/sheet: AnalysisResults                                                    *
*                                                                                   *
* This dataset/sheet contains one row per result value. If an analysis does not     *
* have any groupings that generate results by group (i.e., if the analysis has no   *
* groupings or all groupings in the analysis have resultsByGroup = FALSE), there    *
* will be one result value per analysis operation. Alternatively, if the analysis   *
* has any groupings that generate results by group, there will be one result value  *
* for each combination of operation and grouping group(s). For example, there would *
* be six result values for a 'count of subjects' operation in an analysis that has  *
* groupings of sex (with two groups) and treatment (with three groups).             *
*                                                                                   *
* In the model, each result value is associated with an analysis id, an operation   *
* id and (if relevant) a set of grouping group ids. In this dataset/sheet, multiple *
* grouping groups are transposed to represent the grouping id and group id (or      *
* group value for data-driven groupings) in separate resultGroupn_groupingId,       *
* resultGroupn_groupId and resultGroupn_groupValue variables (e.g.,                 *
* resultGroup1_groupingId, resultGroup1_groupId, resultGroup1_groupValue,           *
* resultGroup2_groupingId, resultGroup2_groupId and resultGroup2_groupValue for an  *
* analysis that has two groupings that generate results by group). Additional       *
* descriptive information is also included to make the results more human-readable, *
* including analysis set label (from the analysis set associated with the           *
* analysis), method id and label (from the method associated with the analysis),    *
* operation label and result pattern and the group label for each represented group.*
\***********************************************************************************/

/* Add result group order to faciliate transposition */

data _tmp_results_resultgroups;
set in.results_resultgroups;
by ordinal_results;
if first.ordinal_results then order = 1;
else order + 1;
run;

/* The GET_RESULTS macro combines all pieces of result information into a single
   dataset. The maximum number of result groups per result is calculated
   and sets of variables and table joins are added to the query dynamically */

%macro get_results;

	proc sql noprint;

		select max(order) into : maxgrp
		from in.analyses_orderedGroupings;

		create table AnalysisResults as
		select a.id,
		       b.label as analysisSet_label,
		       a.methodId as method_id,
		       c.label as method_label,
		       d.operationId as operation_id, e.label as operation_label, e.resultPattern as operation_resultPattern,
			   %do i = 1 %to &maxgrp;
			   g&i..groupingId as resultGroup&i._groupingId,
			   g&i..groupId as resultGroup&i._groupId,
			   g&i..group_label as resultGroup&i._group_label,
			   g&i..groupValue as resultGroup&i._groupValue,
			   %end;
			   d.rawValue,
			   d.formattedValue
		from in.analyses as a
		left join in.analysisSets as b
		on a.analysisSetId = b.id
		left join in.methods as c
		on a.methodId = c.id
		inner join in.analyses_results as d
		on a.ordinal_analyses = d.ordinal_analyses
		left join in.methods_operations as e
		on d.operationId = e.id
		%do i = 1 %to &maxgrp;
		left join (select ga.ordinal_results, ga.groupingId, ga.groupId, gb.group_label, ga.groupValue
                   from _tmp_results_resultgroups as ga
                   left join AnalysisGroupings as gb
                   on ga.groupingId = gb.id
                   and ga.groupId = gb.group_id
                   where ga.order = &i) as g&i
		on d.ordinal_results = g&i..ordinal_results
		%end;;

	quit;

%mend get_results;

%get_results

/* Remove temporary interim datasets */

proc datasets library = work nolist;
delete _tmp_:;
quit;


