- Stream : a sequence of characters flowing from one place to another
	- input stream : data flows from input device (keyboard, file, etc) into memory
	- output stream : data flows from memory to output device (monitor, file, printer, etc)

### Precision Modifier
- `h` the argument is a pointer to type short instead of type int
- `l` the argument is a pointer to type long or double
- `L` the argument is a pointer to type long double

- `#` ensures that there will be a decimal point even if there are no decimal digits
- `*` ensures that minimum field width and precision specifiers can be provided by arguments

## Strings & Formatting

### sprintf
- Write formatted data to string
- `int sprintf ( char * str, const char * format, ... )`

```c
int main (){
	char buffer [50];
	int n, a=5, b=3;
	n = sprintf (buffer, "%d + %d = %d", a, b, a+b);
	printf ("[%s] is a string %d chars long\n",buffer,n);
	return 0;
}
```

### sscanf
- Read formatted data from string
- `int sscanf ( const char * s, const char * format, ...)`
```c
int main() {
	char* buffer = "Hello";
	char store_value[10];
	int total_read;
	total_read = sscanf(buffer, "%s" , store_value);
	printf("Value in buffer : %s\n",store_value);
	printf("Total items read : %d",total_read);
	return 0;
}
```

### strtof
- Convert string to float
- `float strtof (const char* str, char** endptr)`
### strtod
- Convert string to double
- `double strtod (const char* str, char** endptr)`
### strtol
- Convert string to long integer
- `long int strtol (const char* str, char** endptr, int base)`
### Strtoll
- Convert string to long long integer
- `long long int strtoll (const char* str, char** endptr, int base)`
### strtoull
- Convert string to unsigned long long integer
- `unsigned long long int strtoull (const char* str, char** endptr, int base)`
### atoi
- Convert string to integer
- `int atoi (const char * str)`
### atol
- Convert string to long integer
- `long int atol ( const char * str )`
### atof
- Convert string to double
- `double atof (const char* str)`
### fflush
- Flush stream
- The data is forced to be written to disk
- If stream is a null pointer, all such streams are flushed.
- `int fflush ( FILE * stream )`
### fpurge
- Data is discarded
- `void __fpurge(FILE *stream)`
### getc, fgetc& gets
- getc & fgetc are primarily used to read characters from disk files
- `int getc ( FILE * stream )`
- gets reads characters from the standard input (stdin)
- `char * gets ( char * str )`