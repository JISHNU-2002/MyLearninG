- These specifiers tell the compiler how to store the subsequent variable
- `storage_specifier type var_name`
### 1 auto
- automatic / local variables
- auto variables are stored in stack segment of the process address space

### 2 static
- Permanent variables within their own function or file
- They are not known outside their function or file, but they maintain their values between calls
- The key difference between a static local variable and a global variable is that the static local variable remains known only to the block in which it is declared

### 3 extern
- Allows separate modules of a large program to be compiled and linked together
- `extern` informs the compiler of the types and names of global variables without creating storage for them again
### 4 register 

- Originally applied only to `int`, `char`, or pointer types, but now applies to any type
- To keep the value of a variable kept in a CPU register for faster access

### Memory Layout in C

![Memory layout in C](images/memory_layout_c.png)