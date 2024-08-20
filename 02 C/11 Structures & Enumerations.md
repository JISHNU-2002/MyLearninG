### Structure and Functions
- Structure object as an argument to a function
	- object access by `object.memb`
```bash
void print_student (struct student)
```

- Structure pointer as an argument to a function
	-  object access by `object->memb`
	- If p_str is a pointer to the structure str, the following expressions are all equivalent
		- `str.memb`
		- `(*p_str).memb`
		- `p_str->memb`
```bash
void read_student_p(struct student *)
```

### typedef and Structures
- keyword used to create a synonym for a structure or union type
- To create an object, we need not use key word struct

### union
- Derived type of structure
- Provide a way to manipulate different kinds of data in a single area of storage, without embedding any machine-dependent information in the program
- The union variable u will be large enough to hold the largest of the types in it

### enumerations
- user defined types that have integral values, associated with each enumeration is a set of named constants
- Behave like integer constants
- `enum type_name{ value1, value2,...,valueN }`
```c
enum day {sunday = 1, monday, tuesday = 5, wednesday, thursday = 10, friday, saturday};

int main(){
	printf("%d %d %d %d %d %d %d", sunday, monday, tuesday, wednesday, thursday, friday, saturday);
	return 0;
}

1 2 5 6 10 11 12
```

### Bit fields
- Specify size (in bits) of structure and union members
- A special unnamed bit field of size 0 is used to force alignment on next boundary
- Cannot be static
- Cannot have pointers to bit field members

```c
struct test1{
	double d;
	unsigned int data1;
	char c;
	unsigned long long data2;
};
struct test2{
	double d;
	unsigned int data1;
	unsigned long long data2;
	char c;
};

int main(){
	printf("Size of test1 is %d bytes\n", sizeof(struct test1)); // 24 bytes
	printf("Size of test2 is %d bytes\n", sizeof(struct test2)); // 32 bytes
	return 0;
}
```