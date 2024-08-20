![Exceptions](images/exceptions.png)
### try – throw - catch block
- **try block** : This block contains the code that may generate an exception
- **throw statement** : This is used to signal the occurrence of an exception
- **catch block** : This block handles the exception. It's declared with an exception parameter

```C++
try {
    // Code that may throw an exception
    if (condition) {
        throw exception; // Throw an exception
    }
}
catch (type exception) {
    // Code to handle the exception
}
```

```C++
try {
    // Code that may throw an exception
}
catch (int e) {
    // Handle integer exceptions
}
catch (const char* e) {
    // Handle string exceptions
}
catch (...) {
    // Handle any type of exception - ellipsis
}
```

**Exception Handling - eg**
```C++
#include <iostream>
#include <string>
#include <exception>
#include <stdexcept>
using namespace std;

// Custom exception class
class MyException : public exception {
public:
    const char* what(){
        return "My custom exception";
    }
};

int main() {
	int num1,num2;
    cout << "enter two numbers : ";
    cin >> num1 >> num2;
	
	string str;
	cout << "enter a string : ";
	cin >> str;

	int arr[5] = {1, 2, 3, 4, 5};
    int index = 10;
    
    bool customError = true;
    
    try {
        // Integer exception
        if (num2 == 0) {
            throw runtime_error("Division by zero");
        }
        cout << "Division result: " << num1 / num2 << endl;

        // String exception
        if (str.length() > 5) {
            throw string("String too long");
        }
        cout << "String: " << str << endl;

        // Array out-of-bounds exception
        if (index >= 5) {
            throw out_of_range("Array index out of bounds");
        }
        cout << "Array element: " << arr[index] << endl;

        // Custom exception
        if (customError) {
            throw MyException();
        }
    }
    catch (const runtime_error& e) {
        cout << "Runtime error : " << e.what() << endl;
    }
    catch (const string& e) {
        cout << "String exception : " << e << endl;
    }
    catch (const out_of_range& e) {
        cout << "Out_of_range exception : " << e.what() << endl;
    }
    catch (const MyException& e) {
        cout << "Custom exception: " << e.what() << endl;
    }
    catch (const exception& e) {
        cout << "Caught an exception"<< endl;
    }

    return 0;
}
```