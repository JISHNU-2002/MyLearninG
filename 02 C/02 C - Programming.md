### Stages of Compilation
![Stages-Compilation](images/program_2.png)

### Phases of Compiler
![Stages-Compiler](images/program_3.png)

## Introduction to C-Language

![Data-types](images/data_types.png)
### Lexical Elements
- C - Tokens
	1. Identifiers
	2. Keywords
	3. Constants
		- Literal & Character constants
		- `\b` Backspace character
		- `\f` Form feed
		- `\n` Newline character
		- `\r` Carriage return
		- `\t` Horizontal tab
		- `\o, \oo, \ooo` Octal number
		- `\xh, \xhh, \xhhh` Hexadecimal number
	4. Strings
	5. Operators
	6. Special Symbols

### Modifiers 
- Modify the meanings of the predefined built-in data types and expand them to a much larger set
- int ( 2/4 bytes )
- 4 data type modifiers in C
	- **long** ( 4 bytes )
	- **short** ( 2 bytes )
	- **signed**
	- **unsigned**
###  Type Qualifiers
- Can prepend to variable declarations which change how the variables may be accessed
- 2 types type qualifiers in C
	- **const** : causes the variable to be read-only
	- **volatile** : to prevent the compiler from applying any optimizations on objects or variables