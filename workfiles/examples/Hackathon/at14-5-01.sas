**********************************************************************************;
* Program Name:      at14-5-01.sas
* Purpose:           combines adverse event data with subject level analysis data
                     calculates n (%) for body system, preferred term and
                     number of events for both and then produces adverse
                     event table
                     
 *****************************************************************************; 

libname adam "<**CHANGE TO LOCATION OF CDISC PILOT ADAM DATASETS**>";
libname results "<**CHANGE TO LOCATION FOR RESULT OUTPUT DATASETS**>";
proc format;
value trt 0 = "Placebo"
         54 = "Xanomeline Low Dose"
		 81 = "Xanomeline High Dose";
run;

data ADSL;
	set ADAM.ADSL;
	format trt01an trt.;
run;
data ADAE;
	set ADAM.ADAE;
	format trtan trt.;
run;


** GET DESCRIPTIVE STATISTICS - COUNTS FREQUENCIES AND UNIQUE COUNTS AT SUBJECT, SOC AND PT LEVELS**;
PROC SQL;
CREATE TABLE DENOM AS
SELECT COUNT(distinct usubjid) as denom, TRT01AN as TRTAN
FROM ADSL(where=(SAFFL='Y'))
GROUP BY TRTAN
ORDER BY TRTAN;
/* COUNT UNIQUE SUBJECTS BY SOC AND PREFERRED TERM AND TREATMENT */
CREATE TABLE AEPTD AS
SELECT COUNT(distinct usubjid) AS count, AESOC, AEDECOD, TRTAN
FROM ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/))
GROUP BY TRTAN, AESOC, AEDECOD
ORDER BY TRTAN, AESOC, AEDECOD;
** COUNT ALL EVENTS BY SOC AND PREFERRED TERM AND TREATMENT **;
CREATE TABLE AEPTA AS
SELECT COUNT(usubjid) AS events, AESOC, AEDECOD, TRTAN
FROM ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/))
GROUP BY TRTAN, AESOC, AEDECOD
ORDER BY TRTAN, AESOC, AEDECOD;
** GET RESULTS AT PTLEVEL **;
create table RESULTPT as select a.*, 3 as SUMMARYLEVEL, b.DENOM, c.events, (count/denom)*100 as pct,
strip(put(count,best.))||' ('||strip(put((count/denom)*100,8.1))||'%) ['||strip(put(events,best.))||']'
as RESULT LENGTH=50
from AEPTD as A left join DENOM as b
on a.TRTAN=b.TRTAN
left join AEPTA as c
on a.TRTAN=c.TRTAN and a.AESOC=c.AESOC and a.AEDECOD=c.AEDECOD
order by AESOC, AEDECOD, TRTAN;

/* COUNT UNIQUE SUBJECTS BY SOC AND TREATMENT */
CREATE TABLE AESOCD AS
SELECT COUNT(distinct usubjid) AS count, AESOC, TRTAN
FROM ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/))
GROUP BY TRTAN, AESOC
ORDER BY TRTAN, AESOC;
** COUNT ALL EVENTS BY SOC TREATMENT **;
CREATE TABLE AESOCA AS
SELECT COUNT(usubjid) AS events, AESOC, TRTAN
FROM ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/))
GROUP BY TRTAN, AESOC
ORDER BY TRTAN, AESOC;
** GET RESULTS AT SOCLEVEL **;
create table RESULTSOC as select a.*, 2 as SUMMARYLEVEL, b.DENOM, c.events, (count/denom)*100 as pct,
strip(put(count,best.))||' ('||strip(put((count/denom)*100,8.1))||'%) ['||strip(put(events,best.))||']'
as RESULT LENGTH=50
from AESOCD as A left join DENOM as b
on a.TRTAN=b.TRTAN
left join AESOCA as c
on a.TRTAN=c.TRTAN and a.AESOC=c.AESOC
order by AESOC, TRTAN;

/* COUNT UNIQUE SUBJECTS BY TREATMENT */
CREATE TABLE AESUBD AS
SELECT COUNT(distinct usubjid) AS count, TRTAN
FROM ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/))
GROUP BY TRTAN
ORDER BY TRTAN;
** COUNT ALL EVENTS BY TREATMENT **;
CREATE TABLE AESUBA AS
SELECT COUNT(usubjid) AS events, TRTAN
FROM ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/))
GROUP BY TRTAN
ORDER BY TRTAN;
** GET RESULTS AT SUBJECT LEVEL **;
create table RESULTSUB as select a.*, 1 as SUMMARYLEVEL, b.DENOM, c.events, (count/denom)*100 as pct,
strip(put(count,best.))||' ('||strip(put((count/denom)*100,8.1))||'%) ['||strip(put(events,best.))||']'
as RESULT LENGTH=50
from AESUBD as A left join DENOM as b
on a.TRTAN=b.TRTAN
left join AESUBA as c
on a.TRTAN=c.TRTAN
order by TRTAN;
QUIT;
** INFERENTIAL STATISTICS **;
** PT LEVEL **;
proc sql;
create table BACKBONE as select * from
(select distinct USUBJID, TRT01AN as TRTAN from ADSL(where=(SAFFL='Y'))) ,
(select distinct AESOC, AEDECOD from ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/)));
create table HADEVENT as select distinct STUDYID, USUBJID, TRTAN, AESOC, AEDECOD
from ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/));

create table FISHER as select a.USUBJID, a.TRTAN, a.AESOC, a.AEDECOD,
case when STUDYID='CDISCPILOT01' then 1
else 0
end as EVENT
from BACKBONE a left join HADEVENT b
on a.USUBJID=b.USUBJID and a.TRTAN=b.TRTAN and a.AEDECOD=b.AEDECOD
order by a.AESOC, a.AEDECOD, a.TRTAN;
quit;
** HIGH DOSE VERSUS PLACEBO **;
proc freq data=FISHER; 
by AESOC AEDECOD; 
where TRTAN in (0,81);
table TRTAN*EVENT/fisher; 
ods output FishersExact=results.F1PT(where=(Name1='XP2_FISH'));
run;
** LOW DOSE VERSUS PLACEBO **;
proc freq data=FISHER; 
by AESOC AEDECOD; 
where TRTAN in (0,54);
table TRTAN*EVENT/exact; 
ods output FishersExact=results.F2PT(where=(Name1='XP2_FISH'));
run;
** SOC LEVEL**;
proc sql;
create table BACKBONE1 as select * from
(select distinct USUBJID, TRT01AN as TRTAN from ADSL(where=(SAFFL='Y'))) ,
(select distinct AESOC from ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/)));
create table HADEVENT1 as select distinct STUDYID, USUBJID, TRTAN, AESOC
from ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/));

create table FISHER1 as select a.USUBJID, a.TRTAN, a.AESOC,
case when STUDYID='CDISCPILOT01' then 1
else 0
end as EVENT
from BACKBONE1 a left join HADEVENT1 b
on a.USUBJID=b.USUBJID and a.TRTAN=b.TRTAN and a.AESOC=b.AESOC
order by a.AESOC, a.TRTAN;
quit;
** HIGH DOSE VERSUS PLACEBO **;
proc freq data=FISHER1; 
by AESOC; 
where TRTAN in (0,81);
table TRTAN*EVENT/exact; 
ods output FishersExact=results.F1SOC(where=(Name1='XP2_FISH'));
run;
** LOW DOSE VERSUS PLACEBO **;
proc freq data=FISHER1; 
by AESOC; 
where TRTAN in (0,54);
table TRTAN*EVENT/exact; 
ods output FishersExact=results.F2SOC(where=(Name1='XP2_FISH'));
run;
** SUBJECT LEVEL**;
proc sql;
create table BACKBONE2 as select * from
(select distinct USUBJID, TRT01AN as TRTAN from ADSL(where=(SAFFL='Y')));
create table HADEVENT2 as select distinct STUDYID, USUBJID, TRTAN
from ADAE(where=(TRTEMFL='Y' /*and AESER='Y'*/));
create table FISHER2 as select a.USUBJID, a.TRTAN,
case when STUDYID='CDISCPILOT01' then 1
else 0
end as EVENT
from BACKBONE2 a left join HADEVENT2 b
on a.USUBJID=b.USUBJID and a.TRTAN=b.TRTAN
order by a.TRTAN;
quit;
** HIGH DOSE VERSUS PLACEBO **;
proc freq data=FISHER2; 
where TRTAN in (0,81);
table TRTAN*EVENT/exact; 
ods output FishersExact=results.F1SUB(where=(Name1='XP2_FISH'));
run;
** LOW DOSE VERSUS PLACEBO **;
proc freq data=FISHER2; 
where TRTAN in (0,54);
table TRTAN*EVENT/exact; 
ods output FishersExact=results.F2SUB(where=(Name1='XP2_FISH'));
run;
