### Access Specifiers
- **private**
	- to encapsulate or hide the member data in the class
- **public** 
	- to expose the member functions to the outside world,\that is, to outside functions as interfaces to the class
### this pointer
- Created automatically by the compiler
- Contains the address of the object through which the function is invoked

```C++
class Simple {
private:
	int id;
public:
	void setID(int id) { 
		this->id = id; 
	}
	int getID() { 
		return this->id; 
	}
};
```

### Scope Resolution Operator ::
- Allows the body of the member functions to be separated from the body of the class
- To define the function outside the class
- To access the global Variables 
- To define the static variables
- To invoke the static functions

```C++
return_type class_name :: function_name () {}

data_type class_name :: variable_name = value ;
```

### Static Class Members – Static Data Members
- Only one copy of that variable will exist
- All objects of that class will share that variable
- Not stored in objects
  
```C++
#include <iostream>
using namespace std;

class static_demo{
private:
    static int a;
    int b;
public:
    void set ( int i, int j){
        a = i; 
        b = j; 
    }
    void showValues();
};

int static_demo :: a = 20; 

void static_demo :: showValues(){
    cout << "static a : " << a << " non-static b : " << b << '\n';
}

int main(){
    static_demo x, y;
    x.set(1, 1); 
    x.showValues(); // a = 1 & b = 1
    y.set(2, 2);
    y.showValues(); // a = 2 & b = 2
    x.showValues(); // a = 2 & b = 1
    return 0;
}
```

### A mutable Object Member
- A const member function cannot modify the state of its object
- A mutable member is never const, even if its object is const ; therefore, it can be modified by a const member function
```C++
#include <iostream>
using namespace std;

class CMF {
    mutable int value;
public:
    CMF(int v = 0) { // constructor
        value = v;
    }

    int getValue() const{ 
        value = 100; /* if mutable keyword was not used, we get compiler error */
        return value;
    }
};

int main(){
    CMF t(50); // calling constructor + object creation
    cout << "value : " << t.getValue() << endl; // value : 100
    return 0;
}
```

### Function Overloading
- Process of using the same name for two or more functions
- Functions either have different types of parameters or a different number of parameters or different return types
