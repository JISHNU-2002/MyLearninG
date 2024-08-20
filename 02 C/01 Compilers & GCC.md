### Program Development Process
- **Problem solving & Implementation phase**
1. Program documentation
2. User needs determination
3. Design & Review program specifications
4. Design the Algorithm
5. Coding
6. Compile, Test & Debug
7. Program deployment

### Language-Translators Programs
- **Assembler** : assembly -> machine
- **Compiler** : high-level -> machine
- **Interpreter** : high-level -> machine

### Stages of Compilation
1. **Preprocessing** : processes include-files, conditional compilation instructions and macros
2. **Compilation** : takes the output of the preprocessor, and the source code, and generates assembler source code
3. **Assembly** : takes the assembly source code and produces an assembly listing with offsets (object file)
4. **Linking** : takes one or more object files or libraries as input and combines them to produce a single(usually executable) file

![Stages](images/program.png)

## Introduction to C-Programming
- C programming language was developed in 1972 by Dennis Ritchie at bell laboratories of AT&T and BELL LABS.
### GCC (GNU Compiler Collection)
```c
gcc main.c
gcc main.c -o main

gcc -Wall main.c -o main // enable all warnings
gcc -Wall -E print.c // print the preprocessed output to stdout
gcc -S main.c > main.s // produce only the assembly code
gcc -C main.c // produce only compiled code
gcc -save-temps main.c // produce all the intermediate files
```
