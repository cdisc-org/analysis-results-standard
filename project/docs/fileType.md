# Slot: fileType


_The format of the output file._



URI: [ars:fileType](https://www.cdisc.org/ars/1-0/fileType)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OutputFile](OutputFile.md) | A file containing analysis output displays |  no  |







## Properties

* Range: [ExtensibleTerminologyTerm](ExtensibleTerminologyTerm.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: fileType
description: The format of the output file.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: fileType
domain_of:
- OutputFile
range: ExtensibleTerminologyTerm
any_of:
- range: OutputFileType
- range: SponsorOutputFileType

```
</details>