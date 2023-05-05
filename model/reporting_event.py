from typing import List, Union
from uuid import UUID

class ReportingEvent():
  reportingEventId: Union[UUID, None] = None
  plannedAnalyses: List = []
  plannedOutputs: List = []
  analysisSets: List = []
  analysisGroupings: List = []
  dataSubsets: List = []
  globalDisplaySections: List = []
  analysisCategorizations: List = []
  analyses: List = []
  methods: List = []
  outputs: List = []