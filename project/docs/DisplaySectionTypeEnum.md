# Enum: DisplaySectionTypeEnum




_Types of display section that contain one or more pieces of informational text._



URI: [DisplaySectionTypeEnum](DisplaySectionTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Header | None | Lines of text appearing above the title and containing additional generic inf... |
| Title | None | The title is a caption of a table beginning with "Table" followed by sequence... |
| Rowlabel Header | None | Optional text placed in the column header for a column containing row/stub la... |
| Legend | None | Lines of text placed immediately after the body of the table containing state... |
| Abbreviation | None | Lines of text defining abbreviations, acronyms, and terms used in the body of... |
| Footnote | None | Placed after the abbreviations and definitions, if any |
| Footer | None | Lines of text appearing below any footnote and containing additional informat... |




## Slots

| Name | Description |
| ---  | --- |
| [sectionType](sectionType.md) | The type of display section that contains one or more pieces of informational... |






## Identifier and Mapping Information







### Schema Source


* from schema: https://www.cdisc.org/ars/1-0




## LinkML Source

<details>
```yaml
name: DisplaySectionTypeEnum
description: Types of display section that contain one or more pieces of informational
  text.
from_schema: https://www.cdisc.org/ars/1-0
rank: 1000
permissible_values:
  Header:
    text: Header
    description: Lines of text appearing above the title and containing additional
      generic information such as study identifier or page numbering.
  Title:
    text: Title
    description: The title is a caption of a table beginning with "Table" followed
      by sequenced numbers or letters and separated by full stops. The title includes
      additional lines describing the content.
  Rowlabel Header:
    text: Rowlabel Header
    description: Optional text placed in the column header for a column containing
      row/stub labels.
  Legend:
    text: Legend
    description: Lines of text placed immediately after the body of the table containing
      statements explaining the use of terms or values. May be prefaced with a word
      such as 'Note:'.
  Abbreviation:
    text: Abbreviation
    description: Lines of text defining abbreviations, acronyms, and terms used in
      the body of the display.
  Footnote:
    text: Footnote
    description: Placed after the abbreviations and definitions, if any. Footnotes
      lead with symbols (asterisk, dagger, double dagger, or section symbol) or superscripted
      letters (a, b, c) or numbers (1, 2, 3) which are in the table behind units of
      measure or words. Footnotes add information regarding the associated values
      where they occur in the body.
  Footer:
    text: Footer
    description: Lines of text appearing below any footnote and containing additional
      information such as traceability of the source program or page numbering.

```
</details>
