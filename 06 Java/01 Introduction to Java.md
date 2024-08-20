- December '90 by Patrick Naughton, Mike Sheridan and James Gosling 
- January 27, 2010, Oracle - Sun Microsystems
- Java is case-sensitive ; maxval, maxVal, and MaxVal are three different names

![Java Environment](java_env.png)

- Simple and Powerful
- Object Oriented
- Portable
- Distributed
- Multi-threaded
- Robust, Secure/Safe
- Interpreted
- High Performance
- Dynamic programming language/platform

```Java
import java.Math.*;       // all classes from java.Math

public class HelloWorld { // starts a class
	public static void main (String[] args) {
	    // public = can be seen from any package
        // static = not “part of” an object
		// starts a main method
		// in: array of String; out: none (void)
		System.out.println("Hello World");
	}
}
```

```bash
javac HelloWorld.java  // Produces HelloWorld.class (byte code)

java HelloWorld        // Starts the JVM and runs the main method
```

### Data types & Variables
- byte 8 bit 
- short 16 bit 
- int 32 bit 
- long 64 bit
- float 32 bit 
- double 64 bit 
- boolean true or false
- char 16 bit, Unicode

- Use the keyword final to specify a constant

- **Enumeration (enum)**
	- enum in java is a data type that contains fixed set of constants
```Java
class EnumExample1{
	public enum Season { WINTER, SPRING, SUMMER, FALL }
	public static void main(String[] args) {
		for (Season s : Season.values())
			System.out.println(s);
		}
		for (Season s : Season.valueOf()){
			System.out.println(s+" "+s.value);
		}
	}
}
```

- **Annotation**
	- Java Annotation is a tag that represents the metadata
	- Attached with class, interface, methods or fields to indicate some additional information which can be used by java compiler & JVM
	- It is an alternative option for XML and java marker interfaces
		1. @override
		2. @Depricated
		3. @SupressWarning

#### Enhanced for loop
```Java
public static int sumListEnhanced(int[] list){
	int total = 0;
	for(int val : list){
		total += val;
		System.out.println( val );
	}
	return total;
}
```

### Arrays of objects
```Java
public void objectArrayExamples(){
	Rectangle[] rectList = new Rectangle[10];
	// How many Rectangle objects exist?
	rectList[5].setSize(5,10);
	for(int i = 0; i < rectList.length; i++){
		rectList[i] = new Rectangle();
	}
	rectList[3].setSize(100,200);
}
```


### Object Oriented View
- Class & Objects
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

#### Static Initializer Block (SIB)
- If we wanted some statements to execute before the main function starts, then write the code in SIB
#### Scanner class
```Java
Scanner sc = new Scanner(System.in);
int x = sc.nextInt();

float y = sc.nextFloat();

String str = sc.next();
```

#### The protected Modifier
- Allows a child class to reference a variable or method directly in the child class
- It provides more encapsulation than public visibility, but is not as tightly encapsulated as private visibility
- A protected variable is visible to any class in the same package as the parent class

#### The super Reference
- If the child constructor invokes the parent (constructor) by using the super reference, it must be the first line of code of the constructor

#### Method Overriding
- If a method is declared with the final modifier, it cannot be overridden

#### The Object Class
- java.lang package
- Ultimate root of all class hierarchies
- eg methods : toString, equals

### Abstraction
- An abstract method cannot be defined as `final` or `static`

### Exception Handling
![Exception Handling](exception_java.png)
- **Checked Exceptions** 
	- The compiler will issue an error if a checked exception is not caught or asserted in a throws clause
	- eg : IOException - file handling
- **Unchecked Exceptions**
	- Does not require explicit handling
	- RuntimeException or any of its descendants