
### Dynamic memory Concepts using new and delete
- `new` : Allocates memory dynamically and returns a pointer to the allocated memory
- `delete` : Deallocates memory that was previously allocated by `new`

```C++
int number = 88;
int *p1 = &number;  // Static allocation

int *p2 = nullptr;  // Dynamic allocation
p2 = new int;       // Allocates memory dynamically
*p2 = 99;

delete p2;          // Deallocates memory
p2 = nullptr;
```

#### `new[]` and `delete[]` Operators
- Dynamic Arrays : Allocated at runtime using `new[]`
- Deallocating Arrays : Use `delete[]` instead of `delete`

```C++
int *Array = new int[5];
delete[] Array;
```

### Dynamic Memory Allocation and Initialization
- Initializing allocated memory using initializers or constructors

```C++
int *p1 = new int(88);
double *p2 = new double(1.23);

Date *date1 = new Date(1999, 1, 1);
Time *time1 = new Time(12, 34, 56);
```

### Pointers to Classes & Objects
- Objects can be dynamically allocated and pointed to by pointers
- Used for dynamic creation and deallocation of objects

```C++
#include<iostream>
using namespace std;

class Rectangle{
private:
    int width,height;
public:
    Rectangle(int w, int h){
        width = w;
        height = h;
    }
    
    int area(){
        return width*height;
    }
    
    void display(){
        cout << " area : " << area() << endl;
    }
};

int main(){
    Rectangle obj(3,4);
    obj.display();                    // area : 12
    
    Rectangle *rect1,*rect2,*rect3;
    rect1 = &obj;
    rect1->display();                 // area : 12
    
    rect2 = new Rectangle(5,6);
    rect2->display();                 // area : 30
    
    rect3 = new Rectangle[2]{{7,8}, {9,10}};
    rect3[0].display();               // area : 56
    rect3[1].display();               // area : 90
    
    delete rect2;                     // Deallocate memory 
    delete[] rect3;
    return 0;
}
```

```C++
#include<iostream>
using namespace std;

class Student{
private:
    int num;
    string name;
public:
    Student() : num(0), name("") {}
    Student(int n, string s) : num(n), name(s) {}
    
    void setData(int n, string s){
        num = n;
        name = s;
        cout << "roll number : " << num << " name : " << name << endl;
    }
};

int main(){
    Student *ptr;
    int i,j,num;
    string name;
    cout << "No of many students : ";
    cin >> j;
    
    ptr = new Student[j];  // dynamic allocation of array of j student objects	
    for(i=0; i<j; i++){
        cout << "enter student details : ";
        cin >> num >> name;
        ptr[i].setData(num,name);
    }
    
    delete[] ptr;         // deallocate memory
    return 0;
}
```

### Memory Leaks
- Memory leaks occur when dynamically allocated memory is not deallocated

### Dangling Pointers and Wild Pointers
- Pointers that do not point to a valid object of the appropriate type
- **Dangling Pointers** : Pointers that point to memory that has been deallocated
- **Wild Pointers** : Pointers that have not been initialized and point to arbitrary memory locations

```C++
char *dp = nullptr;
{
  char c;
  dp = &c;
}
// dp is now a dangling pointer

char *wp;  // wp is a wild pointer
static char *scp; /* scp is not a wild pointer:
```

### Creation and Using References
- A reference acts as an alias to another object or value
- Can be used as function parameters, return values, or stand-alone references

```C++
int a = 5;
int &ref = a;  // ref is a reference to a
ref = 10;      // a is now 10
```

### Call-by-Value and Call-by-Reference
- **Call-by-Value** : Passing a copy of the argument to the function
- **Call-by-Reference** : Passing the address of the argument to the function

```C++
void fnnegate(int ival) { ival = -ival; } // call-by-value
void fnnegate(int *ival) { *ival = -*ival; } // call-by-reference using pointer
void fnnegate(int &ival) { ival = -ival; } // call-by-reference using reference parameter
```

**Pointers** 
- Can be initialized anytime
- Can be reinitialized any number of time
- Can be null
- Require `*` to dereference

### References
---
- Must be initialized when created
- Cannot reinitialize a reference
- Cannot be null 
- Automatically dereferenced
- Passing object by reference - no copy of obj is made

#### ### Independent References
- References that are variables, must be initialized, cannot change the object they refer to

```C++
int a;
int &ref = a;
a = 10;     // a is now 10
ref = 100;  // a is now 100
```

#### Return by Reference
- `dataType& functionName(parameters)`
- Functions can return references, making code easier to read and maintain

```C++
#include <iostream>
using namespace std;

int x;

int& retByRef() {
    return x;
}

int main() {
    retByRef() = 10;
    cout << x;  // Output will be 10
    return 0;
}
```