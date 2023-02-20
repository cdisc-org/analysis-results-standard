
# Class: Display




URI: [https://www.cdisc.org/ars/1-0/Display](https://www.cdisc.org/ars/1-0/Display)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedObject],[DisplaySection],[DisplaySection]<displaySections%200..*-++[Display&#124;id:string;version:integer%20%3F;displayTitle:string%20%3F;name(i):string],[OutputDisplay]++-%20display%200..1>[Display],[NamedObject]^-[Display],[OutputDisplay])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedObject],[DisplaySection],[DisplaySection]<displaySections%200..*-++[Display&#124;id:string;version:integer%20%3F;displayTitle:string%20%3F;name(i):string],[OutputDisplay]++-%20display%200..1>[Display],[NamedObject]^-[Display],[OutputDisplay])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Referenced by Class

 *  **None** *[display](display.md)*  <sub>0..1</sub>  **[Display](Display.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [version](version.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [displayTitle](displayTitle.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [displaySections](displaySections.md)  <sub>0..\*</sub>
     * Range: [DisplaySection](DisplaySection.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
