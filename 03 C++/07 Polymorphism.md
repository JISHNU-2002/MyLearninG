### Virtual Functions (Polymorphism)
---
- `virtual return_type function`
- Declared in a base class and can be overridden by derived classes.
- Virtual Functions are Hierarchical : If not overridden in a derived class, the base class’s function is used

```C++
#include <iostream>
using namespace std;

class Base {
public:
    virtual void display() {
        cout << "Display Base class" << endl;
    }
};

class Derived : public Base {
public:
    void display() override { // Overriding the base class method
        cout << "Display Derived class" << endl;
    }
};

int main() {
    Base *ptr;          // Base class pointer
    Base base;
    Derived obj;
    
    ptr = &base;        // Pointing to Base class object
    ptr->display();     // Display Base class

    ptr = &obj;         // Pointing to Derived class object
    ptr->display();     // Display Derived class
    
    return 0;
}
```
### Pure Virtual Functions(Abstract Class)
---
- `virtual type func_name (parameter_list) = 0`
- A pure virtual function is a virtual function that has no definition in the base class
- Derived class must provide its own definition of the virtual function
- We cannot create an object or cannot be instantiated for an abstract class
- We can create a pointer variable for abstract class which can refer to any of its derived class

```C++
#include<iostream>
using namespace std;

class Shape{
public:
    virtual void draw() = 0;
    virtual ~Shape(){}
};

class Circle : public Shape{
public:
    void draw() override{
        cout << "circle" << endl;
    }
};

class Rectangle : public Shape{
public:
    void draw() override{
        cout << "rectangle" << endl;
    }
};

int main(){
    Shape *c = new Circle();
    Shape *r = new Rectangle();
    
    c->draw();  // circle
    r->draw();  // rectangle
    
    delete c;
    delete r;
    return 0;
}
```

#### Virtual Function Mechanics – The Virtual Table
- Late binding : The table contains pointers to virtual functions of a class
- The compiler places the addresses of the virtual functions for that particular class in the VTABLE

#### Virtual Destructor
- call the inherited class destructor as well, thus properly disposing the class instances
- Ensure proper cleanup of derived class objects when deleting a pointer to a base class

### Friend functions
---
- Can access private and protected members of a class.
- The function can be invoked without the use of an object
- The friend function can have its argument as objects

```C++
#include<iostream>
using namespace std;

class Box{
private:
    double width;
public:
    Box() : width(0) {}
    
    friend void setW(Box &obj, double w); // friend function declaration
    
    void display(){
        cout << "width of box : " << width << endl;
    }
};

void setW(Box &obj, double w){
    obj.width = w;
}

int main(){
    Box obj;
    setW(obj,3.4);
    obj.display();
    return 0;
}
```

### Friend Classes
- One class can be a friend of another, gaining access to its private members

```C++
#include<iostream>
using namespace std;

class B; // forward declaration

class A{
private:
    int data;
public:
    A() : data(0) {}
    friend class B;
};

class B{
public:
    void setData(A &obj, int value){
        obj.data = value;
        cout << "Data in class A : " << obj.data << endl;
    }
};

int main(){
    A aobj;
    B bobj;
    bobj.setData(aobj,100);  // Data in class A : 100
    return 0;
}
```
### Namespaces
- Group classes, objects, and functions under a single name to avoid name conflicts
- `namespace identifier { entities }`


### Operator Overloading
---
- It is a type of polymorphism in which an operator is overloaded to give user defined meaning to it
- These below operators can be overloaded
	- new delete
	- +-*/%^&|~
	- ! = < > += -= *= /= %=
	- ^= &= |= << >> >>= <<= == !=
	- <= >= && || ++ -- , ->* ->
	- () []
- Operator that are not overloaded are
	- scope operator - ::
	- sizeof
	- Period - .
	- ternary operator - ?:
	- typeid() operator

```C++
#include <iostream>
using namespace std;

class FLOAT {
    float no;
public:
    FLOAT() : no(0.0) {}  // Default constructor initializing no to 0.0
    FLOAT(float n) : no(n) {}  // Parameterized constructor

    void getdata() {
        cout << "Enter a float number : ";
        cin >> no;
    }

    void putdata() const {
        cout << "Result : " << no << endl;
    }

    FLOAT operator+(FLOAT f) {
        return FLOAT(no + f.no);
    }

    FLOAT operator*(FLOAT f) {
        return FLOAT(no * f.no);
    }

    FLOAT operator-(FLOAT f) {
        return FLOAT(no - f.no);
    }

    FLOAT operator/(FLOAT f) {
        if (f.no != 0) {
            return FLOAT(no / f.no);
        } else {
            cout << "\nDivision by zero error!";
            return FLOAT(0);  // Return zero if division by zero
        }
    }
};

int main() {
    FLOAT f1, f2, result;

    f1.getdata();
    f2.getdata();

    result = f1 + f2;
    cout << "\nAddition";
    result.putdata();

    result = f1 - f2;
    cout << "\nSubtraction";
    result.putdata();

    result = f1 * f2;
    cout << "\nMultiplication";
    result.putdata();

    result = f1 / f2;
    cout << "\nDivision";
    result.putdata();

    return 0;
}
```