
# Class: File




URI: [https://www.cdisc.org/ars/1-0/File](https://www.cdisc.org/ars/1-0/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedObject],[Output]++-%20fileSpecifications%200..*>[File&#124;fileType:FileType%20%3F;location:string%20%3F;style:string%20%3F;name(i):string],[NamedObject]^-[File],[Output])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedObject],[Output]++-%20fileSpecifications%200..*>[File&#124;fileType:FileType%20%3F;location:string%20%3F;style:string%20%3F;name(i):string],[NamedObject]^-[File],[Output])

## Parents

 *  is_a: [NamedObject](NamedObject.md)

## Referenced by Class

 *  **None** *[fileSpecifications](fileSpecifications.md)*  <sub>0..\*</sub>  **[File](File.md)**

## Attributes


### Own

 * [fileType](fileType.md)  <sub>0..1</sub>
     * Range: [FileType](FileType.md)
 * [location](location.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [style](style.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Inherited from NamedObject:

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
