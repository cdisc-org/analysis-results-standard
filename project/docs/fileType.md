# Slot: fileType

URI: [ars:fileType](https://www.cdisc.org/ars/1-0/fileType)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OutputFile](OutputFile.md) | A file containing analysis output displays |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: fileType
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
alias: fileType
domain_of:
- OutputFile
range: string
inlined: false
any_of:
- range: OutputFileType
- range: SponsorTerm

```
</details>