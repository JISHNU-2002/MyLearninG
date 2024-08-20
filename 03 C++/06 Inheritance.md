### Inheritance Basics
- Inheritance is a mechanism where a new class (derived class) is created from an existing class (base class), inheriting its properties and behaviors
- Reuse existing code and create a hierarchical relationship between classes
- `class derived-class-name : access base-class-name`

#### Access Specifiers
- **Public** : Members of the base class are accessible by the derived class and other parts of the program
- **Private** : Members of the base class are not accessible by the derived class (default)
- **Protected** : Members of the base class are accessible by derived classes but not by other parts of the program

#### Types of Inheritance
- **Single Inheritance** : A class inherits from one base class
- **Multiple Inheritance** : A class inherits from more than one base class
- **Multilevel Inheritance** : A class inherits from a derived class, forming a chain
- **Hierarchical Inheritance** : Multiple classes inherit from a single base class
- **Hybrid Inheritance** : A combination of two or more types of inheritance

![Inheritance types](images/inheritance.png)

#### Constructors and Destructors in Inheritance
- Constructors of the base class are executed before the derived class
- Destructors of the derived class are executed before the base class
- In multiple inheritance, constructors are executed in the order of derivation and destructors in the reverse order

**Single Inheritance** : Constructor & Destructor
```C++
#include<iostream>
using namespace std;

class base{
public:
    base(){
        cout << "constructing base\n";
    }
    ~base(){ 
        cout << "destructing base\n";
    }
};

class derived : public base{
public:
    derived(){
        cout << "constructing derived\n";
    }
    ~derived(){
        cout << "destructing derived\n";
    }
};

int main(){
    derived ob;
    return 0;
}
```

**Multi-Level Inheritance** : Constructor & Destructor
```C++
#include<iostream>
using namespace std;

class base{
public:
    base(){
        cout << "constructing base\n";
    }
    ~base(){ 
        cout << "destructing base\n";
    }
};

class derived1 : public base{
public:
    derived1(){
        cout << "constructing derived1\n";
    }
    ~derived1(){
        cout << "destructing derived1\n";
    }
};

class derived2 : public base{
public:
    derived2(){
        cout << "constructing derived2\n";
    }
    ~derived2(){
        cout << "destructing derived2\n";
    }
};

int main(){
    derived1 obj1;
    derived2 obj2;
    return 0;
}
```

**Multiple Inheritance** : Constructor & Destructor
```C++
#include<iostream>
using namespace std;

class base1{
public:
    base1(){
        cout << "constructing base1\n";
    }
    ~base1(){ 
        cout << "destructing base1\n";
    }
};

class base2{
public:
    base2(){
        cout << "constructing base2\n";
    }
    ~base2(){ 
        cout << "destructing base2\n";
    }
};


class derived : public base1, public base2{
public:
    derived(){
        cout << "constructing derived\n";
    }
    ~derived(){
        cout << "destructing derived\n";
    }
};

int main(){
    derived ob;
    return 0;
}
```

#### Replicated base classes
- Derived classes will have duplicate sets of members inherited from the base 
- More than one copy of the base is visible
- This creates ambiguity
- If the base class has a public member i, they can be accessed by specifying derived1::i, derived2::i

```C++
#include<iostream>
using namespace std;

class base{
    public: int i; 
};

class derived1 : public base{ 
    public: int j; 
};

class derived2 : public base{ 
    public: int k; 
};

class derived3 : public derived1, public derived2{
public:
    int sum;
};

int main(){
    derived3 ob;
    ob.derived1::i = 50;
    ob.j=90;
    ob.k=80;
    int sum = ob.derived1::i + ob.j + ob.k;
    cout << sum << endl;
}
```

#### Virtual base classes
- Duplication of inherited members due to these multiple paths can be avoided
- When a class is made a virtual base class, only one copy of the class is inherited

```C++
#include<iostream>
using namespace std;

class base{
    public: int i;
};

class derived1 : virtual public base{
    public:int j;
};

class derived2 : virtual public base{
    public:int k;
};

class derived3 : public derived1, public derived2{ 
    public: int sum; 
};

int main(){
    derived3 ob;
    ob.i = 50; ob.j = 20; ob.k = 30;
    int sum = ob.i + ob.j + ob.k;
    cout << sum << endl;
    return 0;
}
```