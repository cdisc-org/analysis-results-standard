**********************************************************************************;
* Program Name:      table2.sas
* Purpose:           Creates summary demographics for the FDA STF table 2 example
**********************************************************************************; 

libname adam "<**CHANGE TO LOCATION OF CDISC PILOT ADAM DATASETS**>";
libname results "<**CHANGE TO LOCATION FOR RESULT OUTPUT DATASETS**>";

data ADSL1;
	set ADAM.ADSL;
attrib AGEGR2 length = $ 10
                label = 'Age Sub-Group'
       AGEGR3 length = $ 10
                label = 'Age Sub-Group';
if age < 65 then
	do;
		agegr2 = '<65';
		if AGE >= 17 then AGEGR3 = '17-<65';
	end;
else
	do;
		agegr2 = '65+';
		if age < 75 then AGEGR3 = '65-<75';
		else AGEGR3 = '75+';
	end;
run;

proc sql noprint;

create table adsl2 as
select a.*,
		case TRT01A
			when 'Placebo' then 'AG_TRT_1'
			when 'Xanomeline Low Dose' then 'AG_TRT_2'
			when 'Xanomeline High Dose' then 'AG_TRT_3'
		end as AG_TRT,
		case SEX
			when 'M' then 'AG_SEX_1'
			when 'F' then 'AG_SEX_2'
		end as AG_SEX,
		case AGEGR2
			when '<65' then 'AG_AGEGR2_1'
			when '65+' then 'AG_AGEGR2_2'
		end as AG_AGEGR2,
		case AGEGR3
			when '17-<65' then 'AG_AGEGR3_1'
			when '65-<75' then 'AG_AGEGR3_2'
			when '75+' then 'AG_AGEGR3_3'
		end as AG_AGEGR3,
		case 
			when RACE eq 'AMERICAN INDIAN OR ALASKA NATIVE' then 'AG_RACE_1'
			when RACE eq 'BLACK OR AFRICAN AMERICAN' then 'AG_RACE_2'
			when RACE eq 'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER' then 'AG_RACE_3'
			when RACE eq 'WHITE' then 'AG_RACE_4'
			else 'AG_RACE_5'
		end as AG_RACE,
		case ETHNIC
			when 'HISPANIC OR LATINO' then 'AG_ETHNIC_1'
			when 'NOT HISPANIC OR LATINO' then 'AG_ETHNIC_2'
		end as AG_ETHNIC
		from adsl1 as a;

quit;

proc freq data=ADSL2 noprint;
table AG_TRT/out=A_SAF_SUM_USUBJID_TRT (rename = (AG_TRT = GROUPING1_ID count = M_GRP_CNT_1_N) drop = percent);
run;

proc transpose data = A_SAF_SUM_USUBJID_TRT
               out=results.A_SAF_SUM_USUBJID_TRT (rename = (_name_ = OPERATION_ID col1 = rawValue) drop = _LABEL_);
by GROUPING:;
var M_:;
run;

%macro M_GRP_SUM_CATEG(inds=,anid=,grpvars=);

	proc freq data=&inds noprint;
	table %scan(&GRPVARS,1)
	      %let i = 2;
          %do %while(%scan(&GRPVARS,&I) ne %str());
		  	%str(*)%scan(&GRPVARS,&I)
	        %let i = %eval(&i + 1);
          %end;
		  /out=&anid (rename = (%scan(&GRPVARS,1) = GROUPING1_ID 
	      %let i = 2;
          %do %while(%scan(&GRPVARS,&I) ne %str());
		  	%scan(&GRPVARS,&I) = GROUPING&I._ID
	        %let i = %eval(&i + 1);
          %end;
		count = M_GRP_SUM_CATEG_1_N
      ) drop = percent);
	run;

	data &anid;
	merge &anid
	      A_SAF_SUM_USUBJID_TRT;
	by GROUPING1_ID;
	M_GRP_SUM_CATEG_2_PCT = 100 * (M_GRP_SUM_CATEG_1_N / M_GRP_CNT_1_N);
	drop M_GRP_CNT_1_N;
	run;

	proc transpose data = &anid
	               out=results.&anid (rename = (_name_ = OPERATION_ID col1 = rawValue) drop = _LABEL_);
	by GROUPING:;
	var M_GRP_SUM_CATEG_1_N M_GRP_SUM_CATEG_2_PCT;
	run;

%mend M_GRP_SUM_CATEG;

%M_GRP_SUM_CATEG(inds=ADSL2,anid=A_SAF_SUM_USUBJID_TRT_SEX,grpvars=AG_TRT AG_SEX)

proc means data=ADSL2 noprint;
var AGE;
class AG_TRT;
output out=A_SAF_SUM_AGE_TRT (where = (_type_ eq 1) rename = (AG_TRT = GROUPING1_ID))
       mean = M_GRP_SUM_CONTIN_1_MEAN
       std = M_GRP_SUM_CONTIN_2_SD
       median = M_GRP_SUM_CONTIN_3_MEDIAN
       min = M_GRP_SUM_CONTIN_4_MIN
       max = M_GRP_SUM_CONTIN_5_MAX;
run;

proc transpose data = A_SAF_SUM_AGE_TRT
               out=results.A_SAF_SUM_AGE_TRT (rename = (_name_ = OPERATION_ID col1 = rawValue) drop = _LABEL_);
by GROUPING:;
var M_:;
run;

%M_GRP_SUM_CATEG(inds=ADSL2,anid=A_SAF_SUM_USUBJID_TRT_AGEGRP,grpvars=AG_TRT AG_AGEGR2 AG_AGEGR3)
%M_GRP_SUM_CATEG(inds=ADSL2,anid=A_SAF_SUM_USUBJID_TRT_RACE,grpvars=AG_TRT AG_RACE)
%M_GRP_SUM_CATEG(inds=ADSL2,anid=A_SAF_SUM_USUBJID_TRT_ETHNIC,grpvars=AG_TRT AG_ETHNIC)

proc sql noprint;
	create table results.table2 as 
	select 'A_SAF_SUM_USUBJID_TRT' as ANALYSIS_ID length = 40,
		   OPERATION_ID,
	       GROUPING1_ID length = 40,
		   '' AS GROUPING2_ID length = 40,
		   '' AS GROUPING3_ID length = 40,
		   rawValue
	from results.A_SAF_SUM_USUBJID_TRT
	union all
	select 'A_SAF_SUM_USUBJID_TRT_SEX' as ANALYSIS_ID,
		   OPERATION_ID,
	       GROUPING1_ID,
		   GROUPING2_ID,
		   '',
		   rawValue
	from results.A_SAF_SUM_USUBJID_TRT_SEX
	union all
	select 'A_SAF_SUM_AGE_TRT' as ANALYSIS_ID,
		   OPERATION_ID,
	       GROUPING1_ID,
		   '',
		   '',
		   rawValue
	from results.A_SAF_SUM_AGE_TRT
	union all
	select 'A_SAF_SUM_USUBJID_TRT_AGEGRP' as ANALYSIS_ID,
		   OPERATION_ID,
	       GROUPING1_ID,
		   GROUPING2_ID,
		   GROUPING3_ID,
		   rawValue
	from results.A_SAF_SUM_USUBJID_TRT_AGEGRP
	union all
	select 'A_SAF_SUM_USUBJID_TRT_RACE' as ANALYSIS_ID,
		   OPERATION_ID,
	       GROUPING1_ID,
		   GROUPING2_ID,
		   '',
		   rawValue
	from results.A_SAF_SUM_USUBJID_TRT_RACE
	union all
	select 'A_SAF_SUM_USUBJID_TRT_ETHNIC' as ANALYSIS_ID,
		   OPERATION_ID,
	       GROUPING1_ID,
		   GROUPING2_ID,
		   '',
		   rawValue
	from results.A_SAF_SUM_USUBJID_TRT_ETHNIC;
quit;
