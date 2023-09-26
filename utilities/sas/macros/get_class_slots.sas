%macro get_class_slots(jschmafl=,outds=);

/***********************************************************************************\
*                                                                                   *
* Name: get_class_slots.sas                                                         *
*                                                                                   *
* Description: Reads in a JSON-Schema representation of the ARS Model to create a   *
*              dataset containing class attribute/slot properties.                  *
*                                                                                   *
* Input parameters:                                                                 *
*                                                                                   *
* JSCHMAFL: The path to the local copy of the JSON-Schema definition file for the   *
*           ARS model, ars_ldm.json, which has been downloaded from the model       *
*           folder for the ARS GitHub repository.                                   *
*                                                                                   *
* OUTDS: The name to be assigned to the WORK dataset containing class/slot          *
*        definitions read in from the JSON schema file.                             *
*                                                                                   *
\***********************************************************************************/

  /* Assign a library using the JSON libname engine */

  filename model "&jschmafl";
  libname model json;

  /*
     Create a reference dataset of unused slots (which are identified as having a
     description of "NOT USED").
  */

  data unused_slots;
  set model.alldata (rename = (p = idxp));
  array p{*} p:;
  if p{idxp} eq 'description' and value = 'NOT USED';
  parent_class = p2;
  slot = p4;
  keep parent_class slot;
  run;

  /* Create the output dataset from the mapped ALLDATA dataset */

  data &outds;
  set model.alldata (where = (p1 eq '$defs' and idxp gt 4) rename = (p = idxp)) end = lastone;
  array p{*} p:;
  if _n_ eq 1 then
    do;
      /* Hash table used to check for unused slots */
      declare hash is_used(dataset: "work.unused_slots");
      is_used.definekey('parent_class','slot');
      is_used.definedone();
      /* Hash table of attributes/slots defined as required */
      declare hash reqd(dataset: "model.alldata (where = (p1 eq '$defs' and p3 eq 'required' and v eq 1) rename = (p2 = parent_class value = slot))");
      reqd.definekey('parent_class','slot');
      reqd.definedone();
    end;
  if p{idxp} in ('$ref','type') and value ne 'array' then
    do;
    parent_class = p2;
    slot = p4;
    /* Exclude unused slots */
    if is_used.check(); /* Returns non-zero code if not found in unused_slots dataset */
    /* Check if attribute/slot is listed as required */
    is_reqd = (reqd.check() eq 0);
    if idxp gt 5 then 
      do _i_ = 5 to idxp - 1;
        if p{_i_} eq 'items' then is_array = 1;
        if p{_i_} eq 'anyOf' then is_anyOf = 1;
      end;
    range = scan(value,-1,'/');
    output;
    end;
  /* Create an entry for the "root" entry */
  if lastone then
    do;
      call missing (of parent_class is_:);
      slot = 'root';
      range = 'ReportingEvent';
      is_reqd = 1;
    output;
    end;
  keep parent_class slot is_: range is_reqd;
  run;

%mend;
