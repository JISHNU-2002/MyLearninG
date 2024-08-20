### Constructors
---
- Invoked automatically when an object is created
- Declared in the public section
- Does not have return types
```C++
class_name()
```

#### Constructor - Initializing using initializer list
- Initialization list executes more faster than normal constructor
- Assignment within constructor cannot be used if try-throw-catch statements have to be included
```C++
class X{
	int a;
	float f;
public:
	X(int j, float x) : a(j) , f(x) , b(a) {} /* this->a = j, this->f = x,      b = this->a */
```

#### Named constructors
---
- Declare all the constructors in the private section and you provide public static methods to return an object
- These static methods are called the Named Constructors

```C++
inline class_name :: constructor ( ) {}

inline class_name constructor :: function_name ( ) {}
```
- `inline` suggests that the compiler should replace the function call with the function code to reduce overhead
- object initialization is efficient, especially since it's a simple assignment operation


```C++
#include <iostream>
#include <cmath>  
using namespace std;

class Point {
    float x, y;
    Point(float x, float y) : x(x), y(y) { }
public:
    static Point rectangular(float x, float y) {
        return Point(x, y);
    }
    
    static Point polar(float radius, float angle) {
        return Point(radius * cos(angle), radius * sin(angle));
    }
    
    void show() const {
        cout << "x = " << x << ", y = " << y << endl;
    }
};

int main() {
    Point p1 = Point :: rectangular(3.0, 4.0);
    Point p2 = Point :: polar(5.0, 0.927295);
    p1.show();
    p2.show();
    return 0;
}
```

#### Copy constructors
---
- Constructor function with the same name as the class and used to make deep copy of objects
- if a class has a pointer variable, a copy constructor has to be defined

- When an object is created from another object of the same type
- When an object is passed by value as a parameter to a function
- When an object is returned from a function

```C++
constructor a;
constructor b(a);
```

#### Explicit constructors
---
- Constructor with only one required parameter is considered an implicit conversion function
- It converts the parameter type to the class type
- Not depends on the semantics of the constructor
```C++
test() { i=100; j=200; }
explicit test(int x) { i=x; j=x+10; }
test(int x , int y){ i = x; j = y; }
```

#### Array of objects
```C++
class Array{
	int i, j;
public:
	Array(int x, int y) : x(i), y(j) { }
};

int main() {
	Array obj[3] = { Array(1,2), Array(3,4), Array(5,6) };
	// Array obj[3] = { (1,2), (3,4), (5,6) };
	return 0;
}
```

### Destructors
---
- Invoked implicitly when the object is destroyed
- Clean up and release resources
- Never call a destructor
- Does not take any parameter and does not return any value
```bash
~class_name(){
	delete variable;
}
```
