*options mprint;

libname adam "C:\CDISC\ars\pilot\datasets";
libname anin "C:\CDISC\ars\auto\anin";
libname anout "C:\CDISC\ars\auto\anout";

proc datasets library=anin nolist kill;
quit;

proc datasets library=anout nolist kill;
quit;

data vartype;
set sashelp.vcolumn (where = (libname eq 'ADAM') rename = (memname = dataset name = variable));
variable = upcase(variable);
keep dataset variable type;
run;

proc sql;

  /* Need to add compoundsetexpression and compoundgroupexpression with expanded whereClauses if they exist */
  create table analysiscompoundexpression as
  select a.id as analysisId,c.*
  from classds.analysis as a
  inner join classds.datasubset as b
  on b.id = a.dataSubsetId
  inner join (select * from classds.compoundsubsetexpression
              union all
              select * from classds.whereclausecompoundexpression) as c
  on substr(c.datapath,1,length(b.datapath)+1) = cats(b.datapath,'/');

  create table analysiscondition as
  select c.id as analysisId,c.dataset as analysisDataset,
         case 
           when d.dataset = 'ADSL'
               and exists(select *
                           from sashelp.vcolumn as vc
                           where vc.libname = 'ADAM'
                           and vc.memname = c.dataset
                           and vc.name = d.variable)
              then c.dataset
            else d.dataset
          end as conditionDataset,d.*
  from (select a.id,a.dataset,a.analysisSetId,b.datapath
        from classds.analysis as a
        inner join classds.analysisset as b
        on b.id = a.analysisSetId
        union all
        select a.id,a.dataset,a.dataSubsetId,b.datapath
        from classds.analysis as a
        inner join classds.datasubset as b
        on b.id = a.dataSubsetId) as c
  left join
  classds.whereclausecondition as d
  on substr(d.datapath,1,length(c.datapath)+1) = cats(c.datapath,'/')
  union all
  select e.id as analysisId,e.dataset as analysisDataset,
         case 
           when l.dataset = 'ADSL'
               and exists(select *
                     from sashelp.vcolumn as vc
                     where vc.libname = 'ADAM'
                     and vc.memname = e.dataset
                     and vc.name = l.variable)
              then e.dataset
            else l.dataset
          end as conditionDataset,l.*
  from classds.analysis as e
  inner join classds.orderedgroupingfactor as f
  on substr(f.datapath,1,length(e.datapath)+1) = cats(e.datapath,'/')
  inner join (select h.id as groupingId,i.* from classds.subjectgroupingfactor as h
              inner join classds.analysisgroup as i
              on substr(i.datapath,1,length(h.datapath)+1) = cats(h.datapath,'/')
              union all
              select j.id as groupingId,k.* from classds.datagroupingfactor as j
              inner join classds.datagroup as k
              on substr(k.datapath,1,length(j.datapath)+1) = cats(j.datapath,'/')) as g
  on g.groupingId = f.groupingId  
  inner join
  classds.whereclausecondition as l
  on substr(l.datapath,1,length(g.datapath)+1) = cats(g.datapath,'/');

quit;

data cce;
set analysiscompoundexpression
    analysiscondition (in = cond drop = analysisDataset dataset rename = (conditionDataset = dataset));
length type $ 4 condition $ 200;
if _n_ eq 1 then
  do;
    declare hash vartype(dataset:"work.vartype");
    vartype.definekey("dataset","variable");
    vartype.definedata("type");
    vartype.definedone();
    call missing(type);
  end;
array values{*} value:;
if cond then
  do;
    condition = catx(' ',catx('.',dataset,variable),comparator);
    vartype.find();
    if comparator in ('IN','NOTIN') then
      do;
        condition = cats(catx(' ',condition,'('),ifc(type eq 'char',quote(strip(value1)),value1));
          do i = 2 to dim(values);
            condition = catx(',',condition,ifc(type eq 'char',quote(strip(values{i})),values{i}));
          end;
        condition = cats(condition,')');
      end;
    else condition = catx(' ',condition,ifc(type eq 'char',quote(strip(value1)),value1));
  end;
keep analysisId tablepath datapath logicalOperator condition;
run;

proc sql;

  create table wc as
  select dss.id, dss.label, wc.*
  from (select * from classds.analysisset
        union all
        select * from classds.datasubset
        union all
        select * from classds.analysisgroup
        union all
        select * from classds.datagroup) as dss
  left join (select a.level, a.order, b.*
              from (select * from classds.analysisset (drop = id label)
                    union all
                    select * from classds.datasubset (drop = id label)
                    union all
                    select * from classds.analysisgroup (drop = id label)
                    union all
                    select * from classds.datagroup (drop = id label)
                    union all
                    select * from classds.whereclause) as a
              left join cce as b
              on substr(b.datapath,1,length(a.datapath)+1) = cats(a.datapath,'/')
              and substr(b.tablepath,1,findc(b.tablepath,'/','b')-1) = a.tablepath) as wc
  on substr(wc.datapath,1,length(dss.datapath)+1) = cats(dss.datapath,'/')
  order by wc.analysisId, dss.id, wc.level, wc.order;

quit;

data wheretxt;
set wc;
by analysisId id level;
length ret_logop $ 3 wheretxt $ 200;
retain ret_logop wheretxt;
if first.id then
  do;
    ret_logop = '';
    wheretxt = '';
  end;
select(logicalOperator);
  when('')
    do;
      if first.level then wheretxt = cats(wheretxt,condition);
      else wheretxt = catx(' ',wheretxt,ret_logop,condition);
    end;
  when('NOT') wheretxt = catx(' ',wheretxt,ret_logop,'NOT','(');
  otherwise 
    do;
      wheretxt = catx(' ',wheretxt,ret_logop,'(');
      ret_logop = logicalOperator;
    end;
end;
if last.level and logicalOperator eq '' and ret_logop ne '' then
  wheretxt = cats(wheretxt,ifc(level gt 2,repeat(')',level-2),')')); /* logic won't work for things like (a and b) or (c and d) */
if last.id;
keep analysisId id label wheretxt;
run;

%macro get_wheretxt(analysisId=, id=);
  %let wtdsid = %sysfunc(open(work.wheretxt (where = (analysisId eq "&analysisId" and id eq "&id")),i));
  %let rc=%sysfunc(fetch(&wtdsid));
  %sysfunc(getvarc(&wtdsid,%sysfunc(varnum(&wtdsid,WHERETXT))))
  %let rc = %sysfunc(close(&wtdsid));
%mend;

proc sql;

  create table adamuvars as
  select memname,name
          from sashelp.vcolumn as vc
          where vc.libname = 'ADAM'
          and not (vc.memname ^= 'ADSL'
                   and vc.name in (select name from sashelp.vcolumn 
                   where libname = 'ADAM'
                   and memname = 'ADSL'));

  create table gfgp as
  select an.id as analysisId, ogf.order, ogf.resultsByGroup, gf.id, gf.label, gf.dataDriven, 
         case 
          when 1 eq (select count(*) from adamuvars as av1
                     where av1.name = gf.groupingVariable)
            then (select av2.memname
                   from adamuvars as av2
                   where av2.name = gf.groupingVariable)
          else (select vc.memname
          from adamuvars as vc
          inner join classds.whereclausecondition as wcc
          on vc.memname = wcc.dataset
          and substr(wcc.datapath,1,length(gp.datapath)+1) = cats(gp.datapath,'/')
          where vc.name = gf.groupingVariable) end as groupingDataset,
          gf.groupingVariable,gp.order as groupOrder,gp.groupId,gp.groupLabel
  from classds.analysis as an
  inner join classds.orderedgroupingfactor as ogf
  on substr(ogf.datapath,1,length(an.datapath)+1) = cats(an.datapath,'/')
  inner join (select * from classds.subjectgroupingfactor
        union all
        select * from classds.datagroupingfactor) as gf
  on gf.id = ogf.groupingId
  left join (select * from classds.analysisgroup (rename = (id = groupId label = groupLabel))
              union all
              select * from classds.datagroup (rename = (id = groupId label = groupLabel))) as gp
  on substr(gp.datapath,1,length(gf.datapath)+1) = cats(gf.datapath,'/')
  order by an.id, gf.id, gp.order;

  create table ctxlkp as
  select a.id length = 40, 'analysisSet_label' as key length = 40, b.label as value length = 200
  from classds.analysis as a
  inner join classds.analysisset b
  on a.analysisSetId = b.id
  union all
  select a.id, 'method_id', a.methodId
  from classds.analysis as a
  union all
  select a.id, 'method_label', b.label
  from classds.analysis as a
  inner join classds.analysisMethod as b
  on a.methodId = b.id
  union all
  select a.id, 'operation_label', a.label
  from classds.operation as a
  union all
  select a.id, 'operation_resultPattern', a.resultPattern
  from classds.operation as a
  union all
  select distinct analysisId, cats('resultGroup',a.order,'_groupingId'), a.id
  from gfgp as a
  union all
  select distinct a.groupId, 'group_label', a.groupLabel
  from gfgp as a
  where dataDriven = 0;

quit;

proc sql;
create table patt as
select distinct resultPattern
from classds.operation;
quit;

data pics;
length fmtname start end label $ 20;
set patt;
retain start "LOW" end "HIGH" type "P" hlo "RLH";
i+1;
fmtname = cats("pic",i,"_");
label = resultPattern;
xcnt = countc(scan(resultPattern,1,'.'),'X');
if countc(scan(resultPattern,1,'.'),'X') gt 1 then substr(label,find(resultPattern,'X'),xcnt-1) = substr(repeat('0',xcnt),xcnt-1);
label = translate(label,"9","X");
default = length(resultPattern);
if findc(resultPattern,'.') then mult = 10**length(scan(compress(resultPattern,'X.','k'),2,'.'));
else mult = 1;
if resultPattern =: '(' then prefix = substr(resultPattern,1,findc(resultPattern,'X')-1);
drop resultPattern i;
run;

data pmap;
length fmtname start end label $ 20;
set patt;
i+1;
retain fmtname "pmap" type "I";
start = resultPattern;
end = start;
label = put(i,8.-l);
drop resultPattern i;
run;

data cntlin;
length fmtname start end label $ 20;
set pics pmap;
run;

proc format cntlin=cntlin;
run;

%macro make_data_index();

  proc sql noprint;

    select memname into : dss separated by ' '
    from sashelp.vtable
    where libname = 'CLASSDS';

    %let nds = &sqlobs;

    create table dataindex as
    %do i = 1 %to &nds;
    %let ds = %scan(&dss,&i);
    %if &i gt 1 %then union;
    select datapath,"&ds" as classds length = 32
    from classds.&ds
    %end;;

  quit;

%mend;

%make_data_index;

proc sql;

  create table parmvs as
  select distinct e.*,f.classds,
         substr(scan(e.kcond,1,'','ka'),1,min(32,findc(e.kcond,'','ka'))) as kcndvar,
         scan(e.kcond,2,'=') as kcndval
  from (select d.*,
         case
            when d.allinst then tranwrd(d.vpath,catx('/',ifc(d.allinst,scan(d.vpath,2,'/','b'),''),scan(d.vpath,1,'/','b')),'%')
            else tranwrd(d.vpath,'/'||catx('/',scan(d.vpath,1,'/','b')),'')
         end as kpath,
         case
            when d.allinst then compress(scan(d.vpath,2,'/','b'),'[*]')
            else ''
         end as kcond
  from (select a.id as analysisId,a.datapath,c.name,transtrn(c.valuesource,'#',trim(a.datapath)) as vpath,
               upcase(scan(c.valuesource,1,'/','b')) as pattr,(scan(c.valuesource,2,'/','b') like '[%]') as allinst
        from classds.analysis as a
        inner join classds.analysismethod as b
        on a.methodId = b.id
        inner join classds.templatecodeparameter as c
        on substr(c.datapath,1,length(b.datapath)+1) = cats(b.datapath,'/')) as d) as e
  left join dataindex as f on
  (e.allinst = 0 and f.datapath = e.kpath)
  or (e.allinst = 1 and f.datapath like e.kpath);

quit;

%macro make_macro(mthid=);

  proc sql noprint;
    select code into : mcode
    from classds.analysismethod (where = (id="&mthid")) as a
    inner join classds.analysisprogrammingcodetemplate as b
      on substr(b.datapath,1,length(a.datapath)+1) = cats(a.datapath,'/');
  quit;

  &mcode;

%mend;

%macro getparmv(anid=,pname=);

  %let anpdsid = %sysfunc(open(work.parmvs (where = (analysisId eq "&anid" and name eq "&pname")),i));
  %syscall set(anpdsid);
  %let anprc = %sysfunc(fetch(&anpdsid));
  %let anprc = %sysfunc(close(&anpdsid));

  %let prmval = %str();

  %if &allinst %then %let cond = %str(datapath like "%trim(&kpath)");
  %else %let cond = %str(datapath eq "&kpath");
  %if &kcndvar ne %str() %then %let cond = %str(&cond and &kcndvar eq &kcndval);
  %let pvdsid = %sysfunc(open(classds.&classds (where = (&cond)),i));
  %let pvrc = %sysfunc(fetch(&pvdsid));
  %if &pvrc eq 0 %then
    %do;
    %let prmval = %sysfunc(getvarc(&pvdsid,%sysfunc(varnum(&pvdsid,&pattr))));
    %if &allinst eq 1 %then
      %do;
          %let pvrc = %sysfunc(fetch(&pvdsid));
          %do %while(&pvrc eq 0);
            %let prmval = &prmval %sysfunc(getvarc(&pvdsid,%sysfunc(varnum(&pvdsid,&pattr))));
            %let pvrc = %sysfunc(fetch(&pvdsid));
          %end;
      %end;
    %end;
  %let pvrc = %sysfunc(close(&pvdsid));

  &prmval

%mend getparmv;

%macro run_analysis(anid=,mthid=);

  proc sql noprint;
    select b.name into : mparms separated by ' '
    from classds.analysismethod (where = (id = "&mthid")) as a
    inner join classds.templatecodeparameter as b
      on substr(b.datapath,1,length(a.datapath)+1) = cats(a.datapath,'/');
    %let nparms = &sqlobs;
  quit;

  %do pidx = 1 %to &nparms;
    %let pname = %scan(&mparms,&pidx,%str( ));
    %if &pidx eq 1 %then %let aparms = %str(&pname=)%getparmv(anid=&anid,pname=&pname);
    %else %let aparms = %str(&aparms,&pname=)%getparmv(anid=&anid,pname=&pname);
  %end;

  data _null_;
  mcall = cats('%',"&mthid",'(',"&aparms",')');
  call symput('mcall',mcall);
  run;

  &mcall;

%mend run_analysis;

%macro do_analyses();

  proc sql noprint;

    select distinct outputId into : outids separated by ' '
    from classds.OrderedListItem (where = (tablepath like "/root/listOfPlannedAnalyses%" and outputId is not missing));

    %let nouts = &sqlobs;
  quit;

  %do outidx = 1 %to &nouts;
    %let outputId = %scan(&outids,&outidx,%str( ));

    proc sql noprint;

      select b.analysisId,quote(trim(b.analysisId))
      into : anids separated by ' ', : qanids separated by ','
      from classds.OrderedListItem (where = (tablepath like "/root/listOfPlannedAnalyses%" and outputId eq "&outputId")) as a
      inner join classds.OrderedListItem (where = (analysisId is not missing)) as b
      on substr(b.datapath,1,length(a.datapath)+1) = cats(a.datapath,'/');
      %let nanids = &sqlobs;

    quit;

    %let ogfs = 0;

    %let andsid = %sysfunc(open(classds.Analysis (where = (id in (&qanids))),i));
    %syscall set(andsid);

    %let rc=%sysfunc(fetch(&andsid));
    %do %while(&rc eq 0);

      %if not(%sysfunc(exist(anin.%substr(&id,1,%sysfunc(min(%length(&id),32)))))) %then
        %do;

          proc sql noprint;

          %let joinds = %str();

          select dataset into : joinds separated by ' '
          from (select conditionDataset as dataset
                from analysisCondition
                where analysisId = "&id"
                and conditionDataset ^= "&dataset"
                union
                select groupingDataset as dataset
                from gfgp
                where analysisId = "&id"
                and groupingDataset ^= "&dataset");

          select distinct id into : gfs separated by ' '
          from gfgp
          where analysisId = "&id";

          %let ngfs = &sqlobs;
          %if &ngfs gt &ogfs %then %let ogfs = &ngfs;

          %let cgfs = %str();

          select distinct id into : cgfs separated by ' '
          from gfgp
          where analysisId = "&id"
          and resultsByGroup = 0;

          %let bgfs = %str();

          select distinct id into : bgfs separated by ' '
          from gfgp
          where analysisId = "&id"
          and resultsByGroup = 1;

          %if &cgfs ne %str() and (&joinds ne %str() or &bgfs ne %str()) %then %let dsalias = TMPLT;
          %else %let dsalias = &dataset;            

          create table anin.%substr(&id,1,%sysfunc(min(%length(&id),32))) as
          select &dsalias..&variable
          %let gfidx = 1;
          %do %while(%scan(&gfs,&gfidx,%str( )) ne %str());
            %let gfid = %scan(&gfs,&gfidx,%str( ));

            %let gpdsid = %sysfunc(open(work.gfgp (where = (analysisId eq "&id" and id eq "&gfid")),i));
            %let gprc=%sysfunc(fetch(&gpdsid));
            %if &gprc eq 0 %then
              %do;
                %if &cgfs ne %str() and (&joinds ne %str() or &bgfs ne %str()) %then %let gpgds = TMPLT;
                %else %let gpgds = %sysfunc(getvarc(&gpdsid,%sysfunc(varnum(&gpdsid,GROUPINGDATASET))));
                %let gpgvar = %sysfunc(getvarc(&gpdsid,%sysfunc(varnum(&gpdsid,GROUPINGVARIABLE))));
                , &gpgds..&gpgvar
                %if %sysfunc(getvarn(&gpdsid,%sysfunc(varnum(&gpdsid,DATADRIVEN)))) eq 1 %then
                  %do;
                    , &gpgds..&gpgvar
                  %end;
                %else
                  %do;
                    , case
                    %do %while(&gprc eq 0);
                      %let grid = %sysfunc(getvarc(&gpdsid,%sysfunc(varnum(&gpdsid,GROUPID))));
                      when %sysfunc(tranwrd(%get_wheretxt(analysisId=&id,id=&grid),%str(&dataset..),%str(&dsalias..))) then "&grid"
                      %let gprc=%sysfunc(fetch(&gpdsid));
                    %end;
                    else '' end
                  %end;
                as &gfid
              %end;
            %let gprc = %sysfunc(close(&gpdsid));
            %let gfidx = %eval(&gfidx + 1);
          %end;
          
          %if &cgfs ne %str() and (&joinds ne %str() or &bgfs ne %str()) %then
            %do;
              %if &joinds eq %str() %then %let joinds = &dataset;
              , (&joinds..usubjid ne '') as _occurred_
              from (select *
                   from (select distinct usubjid /*adsl grouping variables*/
                          %let gpdsid = %sysfunc(open(work.gfgp (where = (analysisId eq "&id" and groupingDataset eq "&dataset" and resultsByGroup eq 0)),i));
                          %let gprc=%sysfunc(fetch(&gpdsid));
                          %let dvlist = %str();
                          %do %while(&gprc eq 0);
                            %let gpgvar = %sysfunc(getvarc(&gpdsid,%sysfunc(varnum(&gpdsid,GROUPINGVARIABLE))));
                            %if not(%sysfunc(indexw(&dvlist,&gpgvar,%str(,)))) %then %let dvlist = &dvlist%str(,)&gpgvar;
                            %let gprc=%sysfunc(fetch(&gpdsid));
                          %end;
                          %let gprc=%sysfunc(close(&gpdsid));
                        &dvlist
                         from adam.&dataset
                         ),
                        (select distinct '' as dummy /*joinds grouping and data subset variables*/
                          %let jvlist = %str();
                          %let gpdsid = %sysfunc(open(work.gfgp (where = (analysisId eq "&id" and groupingDataset eq "&joinds" and resultsByGroup eq 1)),i));
                          %let gprc=%sysfunc(fetch(&gpdsid));
                          %do %while(&gprc eq 0);
                            %let gpgvar = %sysfunc(getvarc(&gpdsid,%sysfunc(varnum(&gpdsid,GROUPINGVARIABLE))));
                            %if not(%sysfunc(indexw(&jvlist,&gpgvar,%str(,)))) %then %let jvlist = &jvlist%str(,)&gpgvar;
                            %let gprc=%sysfunc(fetch(&gpdsid));
                          %end;
                          %let gprc=%sysfunc(close(&gpdsid));
                          %let dssdsid = %sysfunc(open(work.analysisCondition (where = (analysisId eq "&id" and conditionDataset eq "&joinds" and scan(datapath,1,'/') in ('analysisSets','dataSubsets'))),i));
                          %let dssrc=%sysfunc(fetch(&dssdsid));
                          %do %while(&dssrc eq 0);
                            %let dssvar = %sysfunc(getvarc(&dssdsid,%sysfunc(varnum(&dssdsid,VARIABLE))));
                            %if not(%sysfunc(indexw(&jvlist,&dssvar,%str(,)))) %then %let jvlist = &jvlist%str(,)&dssvar;
                            %let dssrc=%sysfunc(fetch(&dssdsid));
                          %end;
                          %let dssrc=%sysfunc(close(&dssdsid));
                          &jvlist
                           from adam.&joinds)
                  %if &analysisSetId ne %str() or &dataSubsetId ne %str() %then
                    %do;
                      where 
                      %if &analysisSetId ne %str() %then
                        %do;
                          %get_wheretxt(analysisId=&id,id=%str(&analysisSetId))
                          %if &dataSubsetId ne %str() %then and ;
                        %end;
                      %if &dataSubsetId ne %str() %then %get_wheretxt(analysisId=&id,id=%str(&dataSubsetId));
                    %end;
                  ) as tmplt
              left join (select distinct usubjid /*joinds grouping and data subset variables*/
                          &jvlist
                         from adam.&joinds) as &joinds
              on &dsalias..usubjid = &joinds..usubjid
            /*joinds grouping and data subset variables*/
              %let vidx = 1;
              %do %while(%scan(&jvlist,&vidx,%str(,)) ne %str());
                %let jvar = %scan(&jvlist,&vidx,%str(,));
                and &dsalias..&jvar = &joinds..&jvar
                %let vidx = %eval(&vidx + 1);
              %end;
              %if &jvlist ne %str() %then
                %do;
                  %let vidx = 1;
                  %do %while(%scan(&jvlist,&vidx,%str(,)) ne %str());
                    %let jvar = %scan(&jvlist,&vidx,%str(,));
                    %if &vidx eq 1 %then order by; %else %str(,); &dsalias..&jvar
                    %let vidx = %eval(&vidx + 1);
                  %end;
                %end;
            %end;
          %else
            %do;
              %if &joinds ne %str() %then
                %do;
                  from adam.&dataset
                  inner join adam.&joinds as &joinds
                  on &dsalias..usubjid = &joinds..usubjid /* Assumes USUBJID is the join key for all simple dataset joins */
                %end;
              %else from adam.&dataset;
            %end;
          %if not(&cgfs ne %str() and (&joinds ne %str() or &bgfs ne %str())) and (&analysisSetId ne %str() or &dataSubsetId ne %str()) %then
            %do;
              where 
              %if &analysisSetId ne %str() %then
                %do;
                  %get_wheretxt(analysisId=&id,id=%str(&analysisSetId))
                  %if &dataSubsetId ne %str() %then and ;
                %end;
              %if &dataSubsetId ne %str() %then %get_wheretxt(analysisId=&id,id=%str(&dataSubsetId));            
            %end;;
           quit;

        %end;
      %else %put NOTE: [AUTO_ANALYSIS] Dataset ANIN.%upcase(%substr(&id,1,%sysfunc(min(%length(&id),32)))) already exists.;

      %if not(%sysfunc(exist(anout.%substr(&id,1,%sysfunc(min(%length(&id),32)))))) %then
        %do;
          %if not(%sysmacexist(&methodid)) %then %make_macro(mthid=&methodid);
          %run_analysis(anid=&id,mthid=&methodid);
        %end;
      %let rc=%sysfunc(fetch(&andsid));
    %end;

    %let rc = %sysfunc(close(&andsid));

    data anout."&outputId"n;
    length analysis_id $ 100 analysisSet_label $ 100 method_id $ 40 method_label $ 100 operation_id $ 40 operation_label $ 100 operation_resultPattern $ 40 
    %do gfidx = 1 %to &ogfs;
        resultGroup&gfidx._groupingId resultGroup&gfidx._groupId $ 40 resultGroup&gfidx._group_label $ 100 resultGroup&gfidx._groupValue $ 200
    %end;
    rawValue 8 formattedValue $ 20 id $40 key $ 40 value $ 200;
    format rawValue best12.;
    set
    %do anidx = 1 %to &nanids;
      %let anid = %scan(&anids,&anidx,%str( ));
      anout.%substr(&anid,1,%sysfunc(min(%length(&anid),32))) 
      %let ogdsid = %sysfunc(open(work.gfgp(where = (analysisId = "&anid" and resultsByGroup = 1)),i));
      %syscall set(ogdsid);
      %let ogrc = %sysfunc(fetch(&ogdsid));
      %if &ogrc eq 0 %then
        %do; 
          (rename = (
          %do %while(&ogrc eq 0);
            %if &dataDriven eq 1 or &groupOrder eq 1 %then
              %do;
                grouping&order._id = %if &DataDriven eq 0 %then resultGroup&order._groupId; %else resultGroup&order._groupValue;
              %end;
            %let ogrc = %sysfunc(fetch(&ogdsid));
          %end;))
        %end;
      %let ogrc = %sysfunc(close(&ogdsid));
    %end;;
    if _n_ eq 1 then
      do;
        declare hash ctx(dataset:"work.ctxlkp");
        ctx.definekey("id","key");
        ctx.definedata("value");
        ctx.definedone();
        call missing(id,key,value);
      end;
    array ctxvs{%eval(5+(&ogfs*2))} analysisSet_label method_id method_label operation_label operation_resultPattern 
                    %do gfidx = 1 %to &ogfs;
                        resultGroup&gfidx._groupingId resultGroup&gfidx._group_label
                    %end;;
    array ctxidvs{%eval(5+(&ogfs*2))} $ 40 _temporary_ ('analysis_id','analysis_id','analysis_id','operation_id','operation_id' 
                    %do gfidx = 1 %to &ogfs;
                        ,'analysis_id',"resultGroup&gfidx._groupId"
                    %end;);
    array ctxks{%eval(5+(&ogfs*2))} $ 40 _temporary_ ('analysisSet_label','method_id','method_label','operation_label','operation_resultPattern' 
                    %do gfidx = 1 %to &ogfs;
                        ,"resultGroup&gfidx._groupingId",'group_label'
                    %end;);
    do _i_ = 1 to dim(ctxvs);   
      id = vvaluex(ctxidvs{_i_});
      key = ctxks{_i_};
      if id ne '' and key ne '' then
        do;
          rc = ctx.find();      
          if rc eq 0 then ctxvs{_i_} = value;
        end;
    end;
    formattedValue = putn(rawValue,cats("pic",input(operation_resultPattern,pmap.),"_-l"));
    drop _i_ id key value rc;
    run;

  %end;

%mend;

%do_analyses;




