#
# Name: excel2yaml.py
#
# Description: Reads information in an Excel file (based on "ARS Template.xlsx")
#              and creates a YAML file containing an ARS ReportingEvent. Both the
#              YAML file and the ReportingEvent will be named according to the
#              name of the input Excel file. For example, an Excel file called
#              "Study 1 CSR.xlsx" will generate a YAML file called "Study 1 CSR.yaml"
#              (in the same folder as the original Excel file) containing a
#              ReportingEvent named "Study 1 CSR".
#
# Usage: python excel2yaml.py -x <path to Excel file>
#
# Example: python excel2yaml.py -x '..\..\workfiles\examples\Sprint 12 Examples.xlsx'
#

import os
import sys
import argparse
from copy import deepcopy
from openpyxl.reader.excel import ExcelReader,load_workbook
from linkml_runtime.dumpers import yaml_dumper
from openpyxl import load_workbook,Workbook

# Add top-level folder to path so that project folder can be found
lib_path = os.path.abspath(os.path.join(__file__, '..', '..', '..'))
if lib_path not in sys.path: sys.path.append(lib_path)

from project import ars_ldm

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--excel_file", help="Excel file containing details of reporting event")
    args = parser.parse_args()
    return args

args = parse_arguments()

if not args.excel_file:
    print("The name of the Excel file must be specified.")
    exit(1)

filename = os.path.split(args.excel_file)[-1]

if "".join(filename.split('.')[-1]).lower() != "xlsx":
    print("Only xlsx files are valid.")
    exit(1)

rptevtname = "".join(filename.split(".")[0])

wb: Workbook

wb = load_workbook(filename = args.excel_file)

nlists = {}

wsLopa = wb["ListOfPlannedAnalyses"]
lvl = 0
for value in wsLopa.iter_rows(
    min_row=2, values_only=True):    
    if value[2] == 1:
        nlists[value[0]] = ars_ldm.NestedList(listItems=[ars_ldm.OrderedListItem(name=value[1],level=value[0],order=value[2],analysisId=value[3],outputId=value[4])])
        lvl = value[0]
    elif value[0] <= lvl:
        if value[0] < lvl:
            for _i in range(lvl)[:(value[0]-1):-1]:
                nlists[_i].listItems[-1].sublist = nlists.pop(_i+1)
                lvl = value[0]
        nlists[value[0]].listItems.append(ars_ldm.OrderedListItem(name=value[1],level=value[0],order=value[2],analysisId=value[3],outputId=value[4]))
    else:
        print(f"Unexpected entry in ListOfPlannedAnalyses: level={value[0]}, order={value[2]}")
else:
    for _i in range(lvl)[:0:-1]:
        nlists[_i].listItems[-1].sublist = nlists.pop(_i+1)
    rptevt = ars_ldm.ReportingEvent(name = rptevtname,
        listOfPlannedAnalyses = nlists[1])

wsAnSet = wb["AnalysisSets"]

for value in wsAnSet.iter_rows(
    min_row=2, values_only=True):
    anset = ars_ldm.AnalysisSet(id=value[0],label=value[1],order=value[2],condition=ars_ldm.Condition(dataset=value[3],variable=value[4],comparator=value[5],value=value[6]))
    rptevt.analysisSets.append(anset)

wsAnGrp = wb["AnalysisGroupings"]
grpid = ""
angrp = ars_ldm.GroupingFactor ("dummy",False,"dummy")
for value in wsAnGrp.iter_rows(
    min_row=2, values_only=True):
    # If this is a new grouping...
    if str(value[1]) != grpid:
        # Store what's been built for the previous grouping
        if isinstance(angrp,ars_ldm.SubjectGroupingFactor):
            rptevt.analysisGroupings.append(angrp)
        elif isinstance(angrp,ars_ldm.DataGroupingFactor):
            rptevt.dataGroupings.append(angrp)
        grpid = str(value[1])
        # Then process the new grouping
        if value[8] == "ADSL":
            angrp = ars_ldm.SubjectGroupingFactor(id=grpid,dataDriven=value[4],label=value[2],groupingVariable=value[3],groups=[ars_ldm.AnalysisGroup(id=value[5],label=value[6],order=value[7],condition=ars_ldm.Condition(dataset=value[8],variable=value[9],comparator=value[10],value=value[11].split(" | ") if value[11] != None and value[11].find(" | ") > -1 else value[11]))] if value[5] != None else [])
        else:
            angrp = ars_ldm.DataGroupingFactor(id=grpid,dataDriven=value[4],label=value[2],groupingVariable=value[3],groups=[ars_ldm.DataGroup(id=value[5],label=value[6],order=value[7],condition=ars_ldm.Condition(dataset=value[8],variable=value[9],comparator=value[10],value=value[11].split(" | ") if value[11] != None and value[11].find(" | ") > -1 else value[11]))] if value[5] != None else [])
    else:
        angrp.groups.append(ars_ldm.DataGroup(id=value[5],label=value[6],order=value[7],condition=ars_ldm.Condition(dataset=value[8],variable=value[9],comparator=value[10],value=value[11].split(" | ") if value[11] != None and value[11].find(" | ") > -1 else value[11])))
else:
    if isinstance(angrp,ars_ldm.SubjectGroupingFactor):
        rptevt.analysisGroupings.append(angrp)
    else:
        rptevt.dataGroupings.append(angrp)

wsDss = wb["DataSubsets"]

dssid = ""
wcs = {}

for value in wsDss.iter_rows(
    min_row=2, values_only=True):

    if value[4] == None:
        wc = ars_ldm.WhereClause(level=value[2],order=value[3],condition=ars_ldm.Condition(dataset=value[5],variable=value[6],comparator=value[7],value=value[8].split(" | ") if value[8] != None and value[8].find(" | ") > -1 else value[8]) if value[6] != None else None)
    else:
        wc = ars_ldm.WhereClause(level=value[2],order=value[3],compoundExpression=ars_ldm.CompoundSubsetExpression(logicalOperator=value[4]) if value[4] != None else None)
        wcs[value[2]] = wc
        
    if value[0] != dssid:
        if dssid != "":
            rptevt.dataSubsets.append(dss)
        dss = ars_ldm.DataSubset(id=value[0],label=value[1],
                                 level=wc.level,order=wc.order,                                 
                                 condition=wc.condition,
                                 compoundExpression=wc.compoundExpression)
        dssid = value[0]
    else:
        wcs[value[2]-1].compoundExpression.whereClauses.extend([wc])
else:
    rptevt.dataSubsets.append(dss)

results = {}

wsRslts = wb["AnalysisResults"]
anid = ""
for value in wsRslts.iter_rows(
    min_row=2, values_only=True):
    if str(value[0]) != anid:
        results[value[0]] = [ars_ldm.OperationResult(operationId=value[4],rawValue=value[19],formattedValue=value[20],resultGroups=[ars_ldm.ResultGroup(groupingId=value[x],groupId=value[y],groupValue=value[z]) for x, y, z in [[7,8,10],[11,12,14],[15,16,18]] if value[x] != None])]
        anid = str(value[0])
    else:
        results[value[0]].append(ars_ldm.OperationResult(operationId=value[4],rawValue=value[19],formattedValue=value[20],resultGroups=[ars_ldm.ResultGroup(groupingId=value[x],groupId=value[y],groupValue=value[z]) for x, y, z in [[7,8,10],[11,12,14],[15,16,18]] if value[x] != None]))

wsMth = wb["AnalysisMethods"]
mthid = ""
method = ars_ldm.AnalysisMethod(id="dummy",name="dummy",operations=[{"dummy": "dummy"}])
for value in wsMth.iter_rows(
    min_row=2, values_only=True):
    # If this is a new method...
    if str(value[0]) != mthid:
        # Store what's been built for the previous method
        if method.id != "dummy":
            rptevt.methods.append(method)
        mthid = str(value[0])
        # Then process the new method
        method = ars_ldm.AnalysisMethod(id=mthid,
                                        name=value[1],
                                        label=value[2],
                                        description=value[3],
                                        operations=[ars_ldm.Operation(id=value[4],
                                                    name=value[5],
                                                    label=value[7],
                                                    resultPattern=value[8],
                                                    referencedOperationRelationships=[ars_ldm.ReferencedOperationRelationship(
                                                                                   referencedOperationRole="NUMERATOR",
                                                                                   id=value[9],
                                                                                   operationId=value[10],description=value[11]),
                                                                                   ars_ldm.ReferencedOperationRelationship(
                                                                                   referencedOperationRole="DENOMINATOR",
                                                                                   id=value[12],
                                                                                   operationId=value[13],description=value[14])] if value[9]!=None else None)])
    else:
        method.operations.append(ars_ldm.Operation(id=value[4],
                                                    name=value[5],
                                                    label=value[7],
                                                    resultPattern=value[8],
                                                    referencedOperationRelationships=[ars_ldm.ReferencedOperationRelationship(
                                                                                   referencedOperationRole="NUMERATOR",
                                                                                   id=value[9],
                                                                                   operationId=value[10],description=value[11]),
                                                                                   ars_ldm.ReferencedOperationRelationship(
                                                                                   referencedOperationRole="DENOMINATOR",
                                                                                   id=value[12],
                                                                                   operationId=value[13],description=value[14])] if value[9]!=None else None))
else:
    rptevt.methods.append(method)

wsAn = wb["Analyses"]

for value in wsAn.iter_rows(
    min_row=2, values_only=True):
    analysis = ars_ldm.Analysis(id=value[0],version=value[1],name=value[2],analysisSetId=value[4],dataSubsetId=value[11],dataset=value[12],variable=value[13],methodId=value[14],
                                referencedAnalysisOperations=[ars_ldm.ReferencedAnalysisOperation(referencedOperationId=value[x],analysisId=value[y]) for x, y in [[15,16],[17,18]] if value[x] != None],
                                results=results[value[0]] if value[0] in results else None)
    grpord = 0
    for _i in [5,7,9]:
        if value[_i] == None:
            break
        grpord += 1
        analysis.orderedGroupings.append(ars_ldm.OrderedGroupingFactor(order=grpord,groupingId=value[_i],resultsByGroup=value[_i+1]))
    rptevt.analyses.append(analysis)

wsDisp = wb["Displays"]

displays = {}
dispid = ""
for value in wsDisp.iter_rows(
    min_row=2, values_only=True):
    if str(value[0]) != dispid:
        if dispid != "":
            displays[dispid] = display
        display = ars_ldm.Display(id=value[0],name=value[1],version=value[2],displayTitle=value[3],displaySections=[ars_ldm.DisplaySection(sectionType=value[4],subSections=[ars_ldm.DisplaySubSection(id=value[5],order=value[6],text=value[7])])])
        dispid = str(value[0])
        scttype = str(value[4])
    elif value[4] != scttype:
        display.displaySections.append(ars_ldm.DisplaySection(sectionType=value[4],subSections=[ars_ldm.DisplaySubSection(id=value[5],order=value[6],text=value[7])]))
        scttype = value[4]
    else:
        display.displaySections[-1].subSections.append(ars_ldm.DisplaySubSection(id=value[5],order=value[6],text=value[7]))
else:
    displays[dispid] = display
    
wsOutput = wb["Outputs"]

for value in wsOutput.iter_rows(
    min_row=2, values_only=True):
    output = ars_ldm.Output(id=value[0],version=value[1],outputDisplays=[ars_ldm.OutputDisplay(order=1,display=displays[value[3]])])
    for fType in value[6].split(" | "):
        output.fileSpecifications.append(ars_ldm.File(name=value[4],fileType=fType,location=value[5]))
    rptevt.outputs.append(output)

yaml_str = yaml_dumper.dumps(rptevt)

with open(os.path.join(''.join(os.path.split(args.excel_file)[0:-1]),rptevtname+'.yaml'), "w", encoding="utf-8") as f:
    f.write(yaml_str)