### What is a Thread?  
- An execution unit with its own program counter, stack, and set of registers.  
- Also known as lightweight processes.  
- Used to improve application performance through parallelism.  
- CPU switches rapidly among threads, creating an illusion of parallel execution.

### Single Threading  
- Processing one command at a time.  
- Opposite of multithreading.  
- In functional programming, can mean "backtracking within a single thread."

### Multithreading  
- Found in multitasking operating systems.  
- Allows multiple threads within a single process to share resources but execute independently.  
- Provides concurrent execution abstraction.  
- Enables parallel execution on multiprocessor systems.

### Advantages of Multithreaded Applications  
- **Responsiveness**
	- Keeps applications responsive by offloading long tasks to worker threads.  
- **Faster Execution** 
	- Operates faster on multi-core processors or clusters.  
- **Lower Resource Consumption**
	- Uses fewer resources compared to multiple process copies.  
- **Better System Utilization**
	- Higher throughput and lower latency.  
- **Simplified Sharing and Communication**
	- Threads share data, code, and files.  
- **Parallelization**
	- Utilizes multicore systems for parallel task execution.

### Drawbacks of Multithreading  
- **Synchronization Issues**
	- Risk of race conditions and deadlocks.  
- **Process Crashes**
	- A misbehaving thread can crash the entire process.

### Multiple Threads  
- Multiple processes can execute in parallel by increasing the number of threads.

### Thread Credentials  
- **Operations**
	- creation
	- termination
	- synchronization
	- scheduling
	- data management
	- process interaction
- **Shared Resources**
	- instructions
	- open files
	- signals
	- working directory
	- user and group ID 
- **Unique Attributes** 
	- Thread ID
	- registers
	- stack pointer
	- local variables
	- signal mask
	- priority, and scheduling policy.

### Threads vs. Processes  
- **Address Space**
	- Threads share the same address space
	- Processes do not share same address space  
- **Synchronization**
	- Process synchronization - Kernal
	- Thread synchronization - Process
- **Context Switching**
	- Faster between threads than between processes
- **Communication**
	- Easier among threads than processes.

### Types of Threads  
- **User Threads**
	- Managed by user-level thread libraries without kernel support.  
	- Examples: POSIX P threads, Mach C-threads, Solaris threads.  
- **Kernel Threads**
	- Managed by the kernel
	- Supported by all modern OSs.