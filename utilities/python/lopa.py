#
# Name: lopa.py
#
# Description: Reads information in a YAML file containing an ARS ReportingEvent
#              and creates a text file containing a human-readable description
#              of each of the analyses referenced in the ReportingEvent's
#              listOfPlannedAnalyses. The text file is created in the same folder
#              as the YAML file and has the same name as the YAML file with a
#              "-LOPA" suffix. For example, an YAML file called "Study 1 CSR.yaml"
#              will generate a text file called "Study 1 CSR-LOPA.txt.yaml".
#
# Usage: python lopa.py -s <path to ARS model schema file> -r <path to report event YAML file>
#
# Example: python lopa.py -s ..\..\model\ars_ldm.yaml -r '..\..\workfiles\examples\Sprint 12 Examples.yaml'
#

import os
import sys
import argparse
from linkml_runtime.utils.yamlutils import from_yaml
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.utils.formatutils import underscore
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.loaders import json_loader
from linkml_dataops.query.object_queryengine import ObjectQueryEngine
from linkml_dataops.query.queryengine import Database, MatchExpression
from linkml_dataops.query.query_model import FetchQuery, MatchConstraint, OrConstraint, FetchById
from io import TextIOWrapper

# Add top-level folder to path so that project folder can be found
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
if lib_path not in sys.path: sys.path.append(lib_path)

from project.ars_ldm import * 
from project.ars_ldm_api import ArsLdmAPI

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--schema_file", help="YAML file containing the schema definition (e.g., ars_ldm.yaml)")
    parser.add_argument("-r", "--rptevt_file", help="YAML file containing details of reporting event")
    args = parser.parse_args()
    return args

args = parse_arguments()

if not args.schema_file:
    print("The name of the schema file must be specified.")
    exit(1)

if not args.rptevt_file:
    print("The name of the reporting event source file must be specified.")
    exit(1)

filename = os.path.split(args.rptevt_file)[-1]

if "".join(filename.split('.')[-1]).lower() != "yaml":
    print("Only YAML reporting event files are valid.")
    exit(1)

sv: SchemaView
sv = SchemaView(args.schema_file)

rptevt: ReportingEvent

rptevt = yaml_loader.load(args.rptevt_file, target_class=ReportingEvent)

# create an API instance
database=Database(data=rptevt)
engine = ObjectQueryEngine(schemaview=sv,
                           database=database)
ars_api = ArsLdmAPI(engine)

def quote(word):
    return "'%s'" % word

def value_list(value:List[str]):
    return "({})".format(", ".join(quote(x) for x in value))

def where_clause(wc:WhereClause,where:str = "") -> str:

    if wc.condition:
        where += " " if len(where) > 0 else "" + f"{wc.condition.dataset}.{wc.condition.variable} {wc.condition.comparator} {quote(''.join(wc.condition.value)) if len(wc.condition.value) == 1 else value_list(wc.condition.value)}"
    elif wc.compoundExpression.logicalOperator == "NOT":
        where += "NOT ({})".format(where_clause(wc,where))
    else:
        where += "({})".format(" {} ".format(wc.compoundExpression.logicalOperator).join(where_clause(x,where) for x in wc.compoundExpression.whereClauses))

    return where

def print_list(nlist: NestedList, fileref: TextIOWrapper,level: int = 1, pfx:str = "", delim:str = "."):
    itmn = 1
    for litm in nlist.listItems:
        inum = delim.join([pfx,str(itmn)]) if pfx else str(itmn)
        fileref.write(f"{'  '*(level-1)}{inum}. {litm.name}\n")
        if litm.analysisId:
            fileref.write(f"{'  '*level}Analysis: {litm.analysisId}\n")
            analysis = ars_api.fetch_Analysis(litm.analysisId)
            if analysis:
                if analysis.analysisSetId:
                    anset = ars_api.fetch_AnalysisSet(analysis.analysisSetId)
                    if anset: fileref.write(f"{'  '*(level+1)}Population: {anset.label} [{where_clause(anset)}]\n")
                if analysis.dataSubsetId:
                    dss = ars_api.fetch_DataSubset(analysis.dataSubsetId)
                    if dss: fileref.write(f"{'  '*(level+1)}Data Subset: {dss.label} [{where_clause(dss)}]\n")
                if analysis.orderedGroupings:
                    fileref.write(f"{'  '*(level+1)}Groupings:\n")
                    for grp in analysis.orderedGroupings:
                        if grp.groupingId:
                            angrp = ars_api.fetch_SubjectGroupingFactor(grp.groupingId) if ars_api.fetch_SubjectGroupingFactor(grp.groupingId) else ars_api.fetch_DataGroupingFactor(grp.groupingId)
                        else:
                            angrp = grp.dataGrouping
                            #rptevt.dataGroupings.append(angrp)
                        if angrp.dataDriven:
                            fileref.write(f"{'  '*(level+2)}{grp.order}. {angrp.label} [Results per group: {'Y' if grp.resultsByGroup else 'N'}]: [Data-driven]\n")
                        else:
                            fileref.write(f"{'  '*(level+2)}{grp.order}. {angrp.label} [Results per group: {'Y' if grp.resultsByGroup else 'N'}]:\n")
                            for g in angrp.groups:
                                fileref.write(f"{'  '*(level+3)} {g.order}. {g.label} [{where_clause(g)}]\n")
                fileref.write(f"{'  '*(level+1)}Analysis Variable: {analysis.dataset}.{analysis.variable}\n")
                if analysis.methodId:
                    method = ars_api.fetch_AnalysisMethod(analysis.methodId)
                    fileref.write(f"{'  '*(level+1)}Method: {method.name}\n")
                    fileref.write(f"{'  '*(level+2)}Operations:\n")
                    for op in method.operations:
                        fileref.write(f"{'  '*(level+3)}> {op.id}: {op.name} ({op.label})\n")
                        if op.referencedOperationRelationships:
                            for refop in op.referencedOperationRelationships:
                                refanid = ''.join([refanop.analysisId for refanop in analysis.referencedAnalysisOperations if refanop.referencedOperationId == refop.id])
                                fileref.write(f"{'  '*(level+4)}- {str(refop.referencedOperationRole).capitalize()}: result of operation {refop.operationId} for {'this analysis' if refanid == analysis.id else 'analysis '+refanid}\n")
        if litm.outputId:  fileref.write(f"{'  '*level}Output: {litm.outputId}\n")
        if litm.sublist: print_list(litm.sublist,fileref,level+1,inum)
        itmn += 1

with open(os.path.join(''.join(os.path.split(args.rptevt_file)[0:-1]),rptevt.name+'-LOPA.txt'), "w", encoding="utf-8") as f:
    #f.write(yaml_str)
    print_list(rptevt.listOfPlannedAnalyses,f)

