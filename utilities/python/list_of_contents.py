#
# Name: list_of_contents.py
#
# Description: Reads information in a YAML file containing an ARS ReportingEvent
#              and creates a text file containing a human-readable description
#              of each of the analyses referenced in the ReportingEvent's
#              mainListOfContents. The text file is created in the same folder
#              as the YAML file and has the same name as the YAML file with a
#              "-LOC" suffix. For example, an YAML file called "Study 1 CSR.yaml"
#              will generate a text file called "Study 1 CSR-LOPA.txt".
#
# Usage: python lopa.py -s <path to ARS model schema file> -r <path to report event YAML file>
#
# Example: python lopa.py -s ..\..\model\ars_ldm.yaml -r '..\..\workfiles\examples\Sprint 12 Examples.yaml'
#

import os
import sys
import argparse
from typing import Type
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.loaders import yaml_loader
from linkml_dataops.query.object_queryengine import ObjectQueryEngine
from linkml_dataops.query.queryengine import Database
from io import TextIOWrapper

# Add top-level folder to path so that project folder can be found
lib_path = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
if lib_path not in sys.path:
    sys.path.append(lib_path)

from project.ars_ldm import *
from project.ars_ldm_api import ArsLdmAPI


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--schema_file",
        help="YAML file containing the schema definition (e.g., ars_ldm.yaml)",
    )
    parser.add_argument(
        "-r", "--rptevt_file", help="YAML file containing details of reporting event"
    )
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

if "".join(filename.split(".")[-1]).lower() != "yaml":
    print("Only YAML reporting event files are valid.")
    exit(1)

sv: SchemaView
sv = SchemaView(args.schema_file)

rptevt: ReportingEvent

rptevt = yaml_loader.load(args.rptevt_file, target_class=ReportingEvent)

# create an API instance
database = Database(data=rptevt)
engine = ObjectQueryEngine(schemaview=sv, database=database)
ars_api = ArsLdmAPI(engine)


def quote(word):
    return "'%s'" % word


def value_list(value: List[str]):
    return "({})".format(", ".join(quote(x) for x in value))


fetchlist = [ars_api.fetch_AnalysisSet, ars_api.fetch_DataSubset, ars_api.fetch_Group]


def where_clause(wc: Union[WhereClause, SubClause], where: str = "") -> str:

    if isinstance(wc, SubClause) and wc.subClauseId:
        for fetch_xx in fetchlist:
            rwc = fetch_xx(wc.subClauseId)
            if rwc:
                wc = rwc
                break
        else:
            print(f"Invalid subClauseId found: '{wc.subClauseId}'")
    if wc.condition:
        where += (
            " "
            if len(where) > 0
            else ""
            + f"{wc.condition.dataset}.{wc.condition.variable} {wc.condition.comparator} {quote(''.join(wc.condition.value)) if len(wc.condition.value) == 1 else value_list(wc.condition.value)}"
        )
    elif str(wc.compoundExpression.logicalOperator) == "NOT":
        if len(wc.compoundExpression.whereClauses) > 1:
            print(
                f"Only one subclause is allowed when logicalOperator = 'NOT'. The following subclauses were ignored:\n{wc.compoundExpression.whereClauses[1:]}"
            )
        where += "NOT ({})".format(
            where_clause(wc.compoundExpression.whereClauses[0], where)
        )
    else:
        where += "({})".format(
            " {} ".format(wc.compoundExpression.logicalOperator).join(
                where_clause(x, where) for x in wc.compoundExpression.whereClauses
            )
        )

    return where


def get_sponsorterm(enum: str, id: SponsorTermId) -> SponsorTerm:

    exterms = engine._yield_path(path="/terminologyExtensions/*", element=rptevt)

    for exterm in exterms:
        if exterm.enumeration == ExtensibleTerminologyEnum(enum):
            spterms = engine._yield_path(path="/sponsorTerms/*", element=exterm)
            for spterm in spterms:
                if spterm.id == id:
                    return spterm
            else:
                print(
                    f"Sponsor term {id} not found in terminology extension for the {enum} enumeration"
                )
                return None
    else:
        print(
            f"No terminology extensions defined for the {enum} enumeration, so sponsor term {id} is invalid"
        )
        return None


def get_category(
    id: AnalysisOutputCategoryId,
    element: YAMLRoot = rptevt,
    attribute: str = "analysisOutputCategorizations",
) -> AnalysisOutputCategory:

    catns = engine._yield_path(path=f"/{attribute}/*", element=element)

    for catn in catns:
        cats = engine._yield_path(path="/categories/*", element=catn)
        for cat in cats:
            if cat.id == id:
                return cat
            elif cat.subCategorizations:
                scat = get_category(id=id, element=cat, attribute="subCategorizations")
                if scat:
                    return scat
    else:
        if element == rptevt:
            print(
                f"A category with id '{id}' was not found in any categorization or subcategorization"
            )
        return None


def get_subsection(
    id: DisplaySubSectionId, element: YAMLRoot = rptevt
) -> DisplaySubSection:
    glbsscts = engine._yield_path(
        path="/globalDisplaySections/*/subSections/*", element=element
    )

    for glbssct in glbsscts:
        if glbssct.id == id:
            return glbssct
    else:
        dspsscts = engine._yield_path(
            path="/outputs/*/displays/*/display/displaySections/*/orderedSubSections/*/subSection",
            element=element,
        )
        for dspssct in dspsscts:
            if dspssct:
                if dspssct.id == id:
                    return dspssct
        else:
            print(
                f"A display sub-section with id '{id}' was not found in any display section."
            )
            return None


def get_pagerefs(docref: DocumentReference, level: int) -> str:

    preftxt = ""
    for pref in docref.pageRefs:
        preftxt += f"\n{'  '*(level)}- "
        if pref.pageNumbers:
            preftxt += "Page" if len(pref.pageNumbers) == 1 else "Pages"
            preftxt += " {}".format(str(pref.pageNumbers[0]))
            for pn in pref.pageNumbers[1:-2]:
                preftxt += ", {}".format(str(pn))
            if len(pref.pageNumbers) > 1:
                preftxt += " and {}".format(str(pref.pageNumbers[-1]))
        elif pref.firstPage:
            preftxt += "Pages " + str(pref.firstPage) + "-" + str(pref.lastPage)
        elif pref.pageNames:
            preftxt += "Section" if len(pref.pageNames) == 1 else "Sections"
            preftxt += ' "{}"'.format(str(pref.pageNames[0]))
            for pnm in pref.pageNames[1:-2]:
                preftxt += ', "{}"'.format(pnm)
            if len(pref.pageNames) > 1:
                preftxt += ' and "{}"'.format(str(pref.pageNames[-1]))
        if pref.label:
            preftxt += " [" + pref.label + "]"

    return preftxt


def print_nobj(
    nobj: Type[NamedObject],
    fileref: TextIOWrapper,
    level: int = 1,
    lnnum: str = None,
    lnlbl: str = None,
):
    if lnnum:
        fileref.write(f"{'  '*(level-1)}{lnnum}. ")
    else:
        fileref.write(f"{'  '*(level)}")
    if lnlbl:
        fileref.write(f"{lnlbl}: ")
    if hasattr(nobj, "id"):
        fileref.write(f"{getattr(nobj,'id')} - ")
    fileref.write(f"{nobj.name}")
    if nobj.label:
        fileref.write(f" ({nobj.label})")
    fileref.write("\n")
    if nobj.description:
        fileref.write(
            f"{'  '*(level-1 if lnnum else level)}{' '*(len(lnnum) + 2 if lnnum else 0)}{' '*(len(lnlbl) + 2 if lnlbl else 0)}{nobj.description}\n"
        )


def print_list(
    nlist: NestedList,
    fileref: TextIOWrapper,
    level: int = 1,
    pfx: str = "",
    delim: str = ".",
):
    itmn = 1
    for litm in nlist.listItems:
        inum = delim.join([pfx, str(itmn)]) if pfx else str(itmn)
        print_nobj(nobj=litm, fileref=fileref, level=level, lnnum=inum)
        if litm.outputId:
            output = ars_api.fetch_Output(litm.outputId)
            if output:
                print_nobj(nobj=output, fileref=fileref, level=level, lnlbl="Output")
                if output.documentRefs:
                    fileref.write(f"{'  '*(level+1)}Documentation:\n")
                    for docref in output.documentRefs:
                        refdoc = ars_api.fetch_ReferenceDocument(
                            docref.referenceDocumentId
                        )
                        fileref.write(
                            f"{'  '*(level+2)}> {refdoc.name} ({refdoc.location}){get_pagerefs(docref,level+3)}\n"
                        )
                if output.categoryIds:
                    fileref.write(f"{'  '*(level+1)}Categories:\n")
                    for catid in output.categoryIds:
                        fileref.write(
                            f"{'  '*(level+2)}> {get_category(id=catid).label}\n"
                        )
                if output.fileSpecifications:
                    fileref.write(f"{'  '*(level+1)}Output File(s):\n")
                    for filespec in output.fileSpecifications:
                        fileref.write(
                            f"{'  '*(level+2)}> {str(filespec.fileType.controlledTerm if filespec.fileType.controlledTerm else get_sponsorterm(enum='OutputFileTypeEnum',id=filespec.fileType.sponsorTermId).submissionValue).upper()} Format: {filespec.name} ({filespec.location})\n"
                        )
                if output.displays:
                    fileref.write(f"{'  '*(level+1)}Displays:\n")
                    for ordisp in output.displays:
                        print_nobj(
                            nobj=ordisp.display,
                            fileref=fileref,
                            level=level + 3,
                            lnnum=str(ordisp.order),
                        )
                        fileref.write(
                            f"{'  '*(level+3)}Display Title: {ordisp.display.displayTitle}\n"
                        )
                        fileref.write(f"{'  '*(level+3)}Sections:\n")
                        for dspsct in ordisp.display.displaySections:
                            fileref.write(f"{'  '*(level+4)}> {dspsct.sectionType}:\n")
                            for dspssct in dspsct.orderedSubSections:
                                fileref.write(
                                    f"{'  '*(level+5)}{dspssct.order}. {dspssct.subSection.text if dspssct.subSection else get_subsection(dspssct.subSectionId).text}\n"
                                )
            else:
                fileref.write(
                    f"{'  '*level}Output: {litm.outputId} (**INVALID OUTPUT ID**')\n"
                )
        if litm.analysisId:
            analysis = ars_api.fetch_Analysis(litm.analysisId)
            if analysis:
                print_nobj(
                    nobj=analysis, fileref=fileref, level=level, lnlbl="Analysis"
                )
                fileref.write(f"{'  '*(level+1)}Documentation:\n")
                fileref.write(
                    f"{'  '*(level+2)}Reason: {analysis.reason.controlledTerm if analysis.reason.controlledTerm else get_sponsorterm(enum='AnalysisReasonEnum',id=analysis.reason.sponsorTermId).submissionValue}\n"
                )
                fileref.write(
                    f"{'  '*(level+2)}Purpose: {analysis.purpose.controlledTerm if analysis.purpose.controlledTerm else get_sponsorterm(enum='AnalysisPurposeEnum',id=analysis.purpose.sponsorTermId).submissionValue}\n"
                )
                if analysis.documentRefs:
                    fileref.write(f"{'  '*(level+2)}See:\n")
                    for docref in analysis.documentRefs:
                        refdoc = ars_api.fetch_ReferenceDocument(
                            docref.referenceDocumentId
                        )
                        fileref.write(
                            f"{'  '*(level+3)}> {refdoc.name} ({refdoc.location}){get_pagerefs(docref,level+4)}\n"
                        )
                if analysis.categoryIds:
                    fileref.write(f"{'  '*(level+1)}Categories:\n")
                    for catid in analysis.categoryIds:
                        fileref.write(
                            f"{'  '*(level+2)}> {get_category(id=catid).label}\n"
                        )
                if analysis.analysisSetId:
                    anset = ars_api.fetch_AnalysisSet(analysis.analysisSetId)
                    if anset:
                        print_nobj(
                            nobj=anset,
                            fileref=fileref,
                            level=level + 1,
                            lnlbl="Population",
                        )
                        fileref.write(
                            f"{'  '*(level+2)}Selection Criteria: {where_clause(anset)}\n"
                        )
                if analysis.dataSubsetId:
                    dss = ars_api.fetch_DataSubset(analysis.dataSubsetId)
                    if dss:
                        print_nobj(
                            nobj=dss,
                            fileref=fileref,
                            level=level + 1,
                            lnlbl="Data Subset",
                        )
                        fileref.write(
                            f"{'  '*(level+2)}Selection Criteria: {where_clause(dss)}\n"
                        )
                if analysis.orderedGroupings:
                    fileref.write(f"{'  '*(level+1)}Groupings:\n")
                    for grp in analysis.orderedGroupings:
                        angrp = ars_api.fetch_GroupingFactor(grp.groupingId)
                        if angrp:
                            print_nobj(
                                nobj=angrp,
                                fileref=fileref,
                                level=level + 3,
                                lnnum=str(grp.order),
                            )
                            if angrp.groupingVariable:
                                fileref.write(
                                    f"{'  '*(level+3)}Grouping Variable: {angrp.groupingDataset}.{angrp.groupingVariable}\n"
                                )
                            if angrp.dataDriven:
                                fileref.write(
                                    f"{'  '*(level+3)}Data-driven [Results per group: {'Y' if grp.resultsByGroup else 'N'}]\n"
                                )
                            else:
                                fileref.write(
                                    f"{'  '*(level+3)}Groups [Results per group: {'Y' if grp.resultsByGroup else 'N'}]:\n"
                                )
                                for g in angrp.groups:
                                    print_nobj(
                                        nobj=g,
                                        fileref=fileref,
                                        level=level + 5,
                                        lnnum=str(g.order),
                                    )
                                    fileref.write(
                                        f"{'  '*(level+5)} Selection Criteria: {where_clause(g)}\n"
                                    )
                        else:
                            fileref.write(
                                f"{'  '*(level+2)}{grp.order}. {grp.groupingId} (**INVALID GROUPING ID**)\n"
                            )
                fileref.write(
                    f"{'  '*(level+1)}Analysis Variable: {analysis.dataset}.{analysis.variable}\n"
                )
                if analysis.methodId:
                    method = ars_api.fetch_AnalysisMethod(analysis.methodId)
                    if method:
                        print_nobj(
                            nobj=method,
                            fileref=fileref,
                            level=level + 1,
                            lnlbl="Method",
                        )
                        fileref.write(f"{'  '*(level+2)}Operations:\n")
                        for op in method.operations:
                            print_nobj(
                                nobj=op,
                                fileref=fileref,
                                level=level + 4,
                                lnnum=op.order,
                            )
                            if op.referencedOperationRelationships:
                                for refop in op.referencedOperationRelationships:
                                    refanid = "".join(
                                        [
                                            refanop.analysisId
                                            for refanop in analysis.referencedAnalysisOperations
                                            if refanop.referencedOperationRelationshipId
                                            == refop.id
                                        ]
                                    )
                                    fileref.write(
                                        f"{'  '*(level+5)}- {str(refop.referencedOperationRole.controlledTerm if refop.referencedOperationRole.controlledTerm else get_sponsorterm(enum='OperationRoleEnum',id=refop.referencedOperationRole.sponsorTermId).submissionValue).capitalize()}: result of operation {refop.operationId} for {'this analysis' if refanid == analysis.id else 'analysis '+refanid}\n"
                                    )
                    else:
                        fileref.write(
                            f"{'  '*level+1}Method: {analysis.methodId} (**INVALID METHOD ID**)\n"
                        )
            else:
                fileref.write(
                    f"{'  '*level}Analysis: {litm.analysisId} (**INVALID ANALYSIS ID**)\n"
                )

        if litm.sublist:
            print_list(litm.sublist, fileref, level + 1, inum)
        itmn += 1


with open(
    os.path.join(
        "".join(os.path.split(args.rptevt_file)[0:-1]), rptevt.name + "-LOC.txt"
    ),
    "w",
    encoding="utf-8",
) as f:
    print_nobj(nobj=rptevt, fileref=f, level=0, lnlbl="Reporting Event")
    print_nobj(
        nobj=rptevt.mainListOfContents, fileref=f, level=0, lnlbl="List of Contents"
    )
    print_list(rptevt.mainListOfContents.contentsList, f)
