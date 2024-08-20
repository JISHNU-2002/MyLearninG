### Static Member Functions
---
- Static member functions can only access static data members
- They do not have a `this` pointer
- Cannot be virtual or const/volatile
- Useful for initializing static data before any object is created

```C++
#include <iostream>
using namespace std;

class DemoStatic {
private:
    static int i;  // Static data member

public:
    static void init(int x) {
        i = x;  // Static member function
    }

    void show() const {
        cout << i << endl;  // Non-static member function
    }
};

int DemoStatic::i = 0; // Define the static member variable

int main() {
    DemoStatic::init(100); // Initialize static data before object creation
    DemoStatic obj1;
    obj1.show();  // Displays : 100

    // Modify the static member through another object
    DemoStatic obj2;
    obj2.init(200);
    obj1.show();  // Displays : 200

    return 0;
}
```

#### Initialization of const static Data Members
- Integral types can be initialized inside the class
- Non-integral types must be defined outside the class

```C++
#include <iostream>
#include <string>
using namespace std;

class Buff {
private:
    static const int MAX = 512;  // Initialization & definition inside the class
    static const char FLAG = 'a';// Initialization & definition inside the class
    static const string MSG;// Declaration inside the class - non-intergral type

public:
    void show() const {
        cout << "MAX: " << MAX << endl;
        cout << "FLAG: " << FLAG << endl;
        cout << "MSG: " << MSG << endl;
    }
};

// Definition outside the class for non-integral types
const string Buff :: MSG = "Hello, World!";

int main() {
    Buff b;
    b.show();  // Displays MAX, FLAG, and MSG values
    return 0;
}
```

#### Call by Reference
- Copies the reference of an argument into the formal parameter
- Changes made to the parameter affect the actual argument

```C++
void swap(int &x, int &y) { 
	int temp = x; 
	x = y; 
	y = temp; 
} // swap(a,b);
```

### Inline Functions
---
- Declared with the `inline` keyword or defined inside a class
- Can be used instead of macros for small functions to improve performance

```C++
#include <iostream>
using namespace std;

class Math {
public:
    inline int add(int a, int b) {
        return a + b;
    }

    inline int subtract(int a, int b);
};

inline int Math :: subtract(int a, int b) {
    return a - b;
}

int main() {
    Math math;
    int x = 10;
    int y = 5;
    cout << x << "+" << y << "=" << math.add(x, y) << endl;
    cout << x << "-" << y << "=" << math.subtract(x, y) << endl;
    return 0;
}
```

#### Default Function Arguments
- Default values must be specified once in the function declaration
- Parameters with default values must appear to the right of non-default parameters
#### Constant Arguments
- Parameters passed as constant cannot be changed inside the function
#### Objects as Arguments
- Objects can be passed as arguments to initialize data members of another object

```C++
#include <iostream>
using namespace std;

class Circle {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}
    
    double getRadius() const {
        return radius;
    }
};

// Function that calculates the area of a Circle object
double calculateArea(const Circle &c) {
    const double PI = 3.14159265358979323846;
    return (PI * c.getRadius() * c.getRadius());
}

int main() {
    Circle circle(5.0);
    // Calculate the area by passing the Circle object to the function
    double area = calculateArea(circle);
    
    cout << "The area of the circle " <<  " = " << area << endl;
    return 0;
}
```

- Functions can return objects

```C++
#include <iostream>
using namespace std;

class Rectangle {
private:
    double length, width;

public:
    Rectangle(double l, double w) : length(l), width(w) {}

    void display() const {
        cout << "Length: " << length << " Width: " << width << endl;
    }

    // Static method to create a square
    static Rectangle createSquare(double sideLength) {
        return Rectangle(sideLength, sideLength);
    }
};

int main() {
    // Using the static method to create a square
    Rectangle square = Rectangle :: createSquare(7.0);
    cout << "Square dimensions : " << endl;
    square.display();
    return 0;
}
```

#### Function Overloading and Ambiguity
- Ambiguity occurs when the compiler cannot decide between overloaded functions
- Main cause of ambiguity involves C++'s automatic type conversions
- Ambiguity can be caused by using default arguments in overloaded functions
- Two functions cannot be overloaded when the only difference is that call-by-reference & call-by-value parameter

```C++
#include <iostream>
using namespace std;

void f(int x) {
    cout << "In f(int)" << endl;
}

void f(int &x) {
    cout << "In f(int &)" << endl;
}

int main() {
    int a = 10;
    f(a); // This will call f(int &)
    f(10); // This will call f(int)
    return 0;
}
```