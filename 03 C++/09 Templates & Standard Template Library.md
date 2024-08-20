### Templates in C++
---
- Templates allow writing generic and reusable code
- They enable functions and classes to operate with generic types, reducing code duplication
- Fall under the category of "meta-programming" and auto code generation

#### Function Templates
- Function templates define a pattern for functions that can operate on different data types
- The compiler generates the specific function code based on the types used

```C++
template <typename T>
T maximum(T a, T b, T c) {
    T max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    return max;
}

int main() {
    int i1 = 1, i2 = 2, i3 = 3;
    double d1 = 1.1, d2 = 2.2, d3 = 3.3;

    cout << "Max int: " << maximum(i1, i2, i3) << endl;
    cout << "Max double: " << maximum(d1, d2, d3) << endl;

    return 0;
}
```

#### Class Templates
- Class templates define a blueprint for a class that can handle different data types, allowing for the creation of type-specific instances

```C++
template <typename T1, typename T2>
class Pair {
public:
    T1 first;
    T2 second;
    Pair(T1 f, T2 s) : first(f), second(s) {}
};

int main() {
    Pair<int, double> p1(1, 2.2);
    Pair<string, string> p2("Hello", "World");

    cout << "Pair 1: " << p1.first << ", " << p1.second << endl;
    cout << "Pair 2: " << p2.first << ", " << p2.second << endl;

    return 0;
}
```

#### Template with Multiple Generic Types
- This allows a function or a class to accept parameters of different types while still maintaining type safety and flexibility

```C++
#include <iostream>
using namespace std;

template<class T, class U, class V>
void tempfun(T a, U b, V c) {
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
}

int main() {
    int i = 10;
    float j = 3.14f;
    char k = 'T';
    tempfun(i, j, k);  // Calls tempfun with int, float, and char
    return 0;
}
```

#### Template Function Overloading
- Define several template functions with the same name but with different type parameters or different numbers of parameters

```C++
template <typename T> 
T add(T a, T b) {      // Template function to add two integers 
	return a + b; 
} 

template <typename T> 
T add(T a, T b, T c) { // Template function to add three integers 
	return a + b + c; 
} 

template <> 
string add<string>(string a, string b) { // Template function to add two strings 
	return a + " " + b; 
}
```

#### Explicitly Overloading a Generic Function
- If you overload a generic function, that overloaded function overrides (or hides) the generic function relative to that specific version
---

## Standard Template Library
---
- STL is a library in C++ that provides a set of common classes and interfaces for DSA
#### 1 Containers
- Data structures like arrays, lists, and queues
- Functions shared by all containers
	- Default constructor, copy constructor, destructor
	- = < <= > >= == !=
	- size queries (`size()`, `empty()`, etc.)

1. **Sequence Containers**
	- Store data in a linear sequence
	- eg : `vector`, `deque`, `list`
2. **Associative Containers** 
	- Store data in key-value pairs for quick access
	- eg : `set`, `map`, `multimap`
3. **Container Adapters** 
	- Provide different interface for existing sequence containers
	- eg : `stack`, `queue`, `priority_queue`

#### 2 Algorithms
- Functions for data manipulation like searching and sorting
#### 3 Iterators
- Objects that allow traversing elements in a container, similar to pointers
- `*` : Dereferences the iterator to access the element
- `++` : Moves the iterator to the next element
- `begin()` : Returns an iterator to the first element
- `end()` : Returns an iterator to the past-the-end element


#### Sequence Containers : Vector Container
- Have to include the following header file `<vector>`
- Data structure with contiguous memory locations

- `push_back(value)` : Adds an element to the end
- `size()` : Returns the number of elements
- `capacity()` : Returns the size of the allocated storage
- `insert(iterator, value)` : Inserts an element before the specified position
- `erase(iterator)` : Removes the element at the specified position
- `clear()` : Removes all elements
- `begin()`, `end()` : Returns iterators to the beginning and end of the vector

```C++
#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int>v;
    
    v.push_back(100);
    v.push_back(1000);    
    v.push_back(10000);
    v.insert(v.begin(), 10);  
    v.insert(v.end(),100000);
    v.erase(v.begin() + 3);  
    
    for(int i : v){
        cout << i << endl;  // 10 100 1000 100000 
    }
    return 0;
}
```

#### Associative Container : Map
```C++
#include <iostream>
#include <map>
using namespace std;

int main() {
    map<int, string> myMap;
    myMap[1] = "One";
    myMap[2] = "Two";
    myMap[3] = "Three";
    for(const auto &pair : myMap) {
        cout << pair.first << ": " << pair.second << endl;
    }

	/*for (const auto &[key, value] : myMap) { 
		cout << key << ": " << value << endl; 
	}*/
	
    // 1: One
    // 2: Two
    // 3: Three
    return 0;
}
```

#### Container Adapter : Stack
```C++
#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<int>s;
    for(int i=0;i<5;i++){
        s.push(i);
    }
    
    while(!s.empty()){
        cout << " " << s.top(); // 4 3 2 1 0 
        s.pop();
    }
    return 0;
}
```

#### Algorithm
```C++
#include <iostream>
#include<algorithm>
#include <vector>
using namespace std;

int main(){
    vector<int>v(5);
    bool found;
    
    for(int i=0;i<5;i++){
        v[i]=i; // v.push_back(i)
    }
    
    found = binary_search(v.begin(), v.end(), 3);
    cout << found << endl;
    
    found = binary_search(v.begin(), v.end(), 9);
    cout << found << endl;
    
    sort(v.begin(), v.end());
    for(int i : v){
        cout << i << "->";
    }
    return 0;
}
```

#### Iterator
```C++
#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int>v;
    
    v.push_back(100);
    v.push_back(1000);    
    v.push_back(10000);
    v.insert(v.begin(), 10);  
    v.insert(v.end(),100000);
    v.erase(v.begin() + 3);  
    
    for(auto i = v.begin(); i != v.end(); i++) {
        cout << *i << " ";  // 10 100 1000 100000 
    }
    return 0;
}
```