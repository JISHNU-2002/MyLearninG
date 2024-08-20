Functions have three parts
- **Function Prototype (declarations)** : consists of information regarding the function's name, return types and names of parameters
- **Function invocation** : calling the function
- **Function Definitions** : body of the function

### Recursion
```c
int factorial(int n){
	if(n == 0)
		return 1;
	return (n * factorial(n - 1));
}
```

```c
int fib(int num){
/* Fibonacci value of a number */
	switch(num) {
		case 0 : return(0); break;
		case 1 : return(1); break;
		default: return(fib(num - 1) + fib(num - 2)); break;
	}
}
```