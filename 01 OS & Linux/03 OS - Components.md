## Operating System Components
1. Signals and system calls
2. Process management
3. Memory management
4. File subsystem
5. Device drivers

## 1 Signals and System Calls
- Signals : Event notifications sent to a process.
- System calls : Interfaces provided by programming languages to access OS functions.

## Multiprogramming
- Multiple instances of a program can be loaded in memory.
- Concurrent execution : Multiple processes executed over time.

## 2 Process Management
### What is a Process?
- A program in execution.
- Foreground and background processes.
- Process control block (PCB) : Contains descriptive information about a process.
- Task - Job - Thread

### Process Creation
- Created by system initialization, user request, batch job, or other processes.
- Uses `fork()` or `clone()` in UNIX/Linux.
- Threads : Sub-processes within a process.

### Process Architecture
- Address space divided into : Code(text) , data, heap, and stack segments.
- code - compiled program code (non-volatile)
- data - global & static variables
- heap - dynamic memory allocation
- stack - local variables

## 3 Memory Management
- Controls and coordinates memory blocks.
- Physical vs. virtual memory.
- Allocation techniques: Single contiguous, partitioned, paged, and segmented memory management.

### Memory Allocation
- Low Memory : For the OS.
- High Memory : For user processes.

### Partition Allocation
- Schemes : First fit, best fit, worst fit, next fit.

### Memory Management sub-system 
- **Dynamic Loading** : Loading parts of a program as needed.
- **Dynamic Linking** : Linking dependent programs at runtime.

## 4 File Subsystem
- Files : Collection of information on non-volatile storage.
- File systems manage file content and metadata.
- Types : Native, virtual (VFS), pseudo (procfs, sysfs).

- #### File Attributes
   - Include name, identifier, location, type, size, protection, time, date, and security.

- #### File Types
   - Character special files, ordinary files, directory files, special device files.

- #### File Functions
   - create, write, read, delete, and reposition.

- #### File Access Methods
   - Sequential, direct random, and index sequential access.

## 5 Device Drivers
- Control peripheral devices.
- Types : Character, block, network device drivers.
1. Character 
    - perform I/O in a byte stream
    - keyboard, mouse, printer
1. Block 
    - supports  FS
    - Tape drive, HDD, CDROM, ROM, RAM
1. Network 
	- receive and transmit data packets on h/w interface 
	- HUB, Switches , Bridges

