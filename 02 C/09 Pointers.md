- A pointer is a variable that contains the address of another variable
```c
int main(){
	int ix = 5;
	int *iPtr = NULL;
	iPtr = &ix;
	printf("ix = %d",ix);       //ix=5
	printf("iPtr = %p",iPtr);   //iPtr=0x7ffe053c3154
	printf("&ix = %p",&ix);     //&ix=0x7ffe053c3154
	printf("*iPtr = %p",*iPtr); //*iPtr=5
	printf("&iPtr = %p",&iPtr); //&iPtr=0x7ffe053c3158
	printf("It is address of x *&p=%p",*&iPtr); //It is address of *&p=0x7ffe053c3154
}
```

### void pointer
- Do not have any type associated with them
- Can hold the address of any type of variable

### Pointers & Arrays
- (data == &data[0]) is true : array name is a pointer to the array's first element
- `*(ptr++)`, `*(++ptr)`, `*ptr++`, `*++ptr` - affects the index
- `(*ptr)++`, `++(*ptr)` - affects the content
```c
ptr_array = iarray;
ptr_array = &iarray[0];
```

```c
int *p, i[10];
p = i;
p[5] = 100;   /* assign using index */
*(p+5) = 100; /* assign using pointer arithmetic */
```

```c
int main(){
    int arr[4]={20,30,40,50};
    int *ptr =arr;
    printf("%p %d \n",(ptr+0),*(ptr+0)); // 0x7fff9ba68ff0 20 
    printf("%p %d \n",(ptr+1),*(ptr+1)); // 0x7fff9ba68ff4 30 
    printf("%p %d \n",(ptr+2),*(ptr+2)); // 0x7fff9ba68ff8 40 
    printf("%p %d \n",(ptr+3),*(ptr+3)); // 0x7fff9ba68ffc 50 
    
    printf("%p %d \n",(arr+0),*(arr+0)); // 0x7fff9ba68ff0 20 
    printf("%p %d \n",(arr+1),*(arr+1)); // 0x7fff9ba68ff4 30 
    printf("%p %d \n",(arr+2),*(arr+2)); // 0x7fff9ba68ff8 40 
    printf("%p %d \n",(arr+3),*(arr+3)); // 0x7fff9ba68ffc 50 
    return 0;
}
```


### Pointers & 2-D Arrays
- `p` pointer to first row
- `p+i` pointer to ith row
- `p+i+j` pointer to ith row jth column
- `*(p+i)` pointer to first element in the ith row
- `*(p+i)+j` pointer to jth element in the ith row
- `*(*(p+i)+j)` value stored in the cell

### Command-Line Arguments
- To pass command-line arguments or parameters to a program when it begins executing\
	- `argc` for argument count
	- `argv` for argument vector

### Pointer constant
- `const int *p`
- Defines p as a pointer to a constant integer

### Constant Pointer
- `int * const p`
- Defines a constant pointer to an integer

### Function Pointer
```bash
returntype (*ptr-to-fn)(arguments if any)
returntype (ptr-to-fn)(arguments if any)
```

### Pointer to Pointer
```c
int x = 12;       // x is a type int variable 
• int *ptr1 = &x; // ptr is a pointer to x
• int **ptr2 = &ptr; //ptr2 is a pointer to a pointer to type int
```

### Type Conversions
- **Automatic Type Conversions** : lower type is promoted to the higher type before the operation proceeds
- **Integral Promotion** : If an int can represent all the values of the original type, then the value is converted to int, otherwise the value is converted to unsigned int

### Dynamic Memory Allocation
#### 1 malloc
- `void *malloc(size_t size)`
- malloc returns a pointer to space(memory) for an object of size size, or NULL if the request cannot be satisfied
- malloc will request space from the OS
- free storage is kept as a list of free blocks - first fit
#### 2 realloc
- `void *realloc(void *p, size_t size)`
- realloc returns a pointer to the new space, or NULL if the request cannot be satisfied
- realloc changes the size of the object pointed to by p to size

#### 3 calloc
- `void *calloc(size_t nobj, size_t size)`
- calloc returns a pointer to space for an array of n obj objects, each of size size, or NULL if the request cannot be satisfied
