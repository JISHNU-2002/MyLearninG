## Batch Processing
- Executes a series of programs without human interaction.
-  **Benefits**
  1. Shares computer resources among many users.
  2. Processes jobs during less busy times.
  3. Maximizes utilization of expensive resources.
  4. Historically used with mainframe computers.

## Multiprogramming Batch System
- Executes one job from memory and switches to another during I/O operations.
- Always keeps CPU and OS busy.
- Uses CPU Scheduling to choose jobs to run.
- Ensures CPU never sits idle.

## Time-Sharing Systems
- Extension of multiprogramming systems.
- Shares computing resources among many users simultaneously.
- Focuses on minimizing response time.
- Allocates a small time slice to each user.

## Distributed Operating System
- Utilizes powerful microprocessors and advanced communication technology.
- Comprises many interconnected computers.
- Client/server architecture allows shared database access.
- **Advantages**
  1. Resource sharing.
  2. Fast processing.
  3. Load distribution.
  4. Reliability.
- Requires networking infrastructure (LAN/WAN).

## Client-Server Systems
- Server systems satisfy client requests.
- Compute Servers execute actions and return results.
- File Servers manage file operations.

## Peer-to-Peer Systems
- Consist of processors with local memory communicating through lines like high-speed buses.
- Loosely coupled systems.

## Desktop Systems
- Personal computers dedicated to single users.
- Run various operating systems (Windows, MacOS, UNIX, Linux).

## Parallel Systems
- Multiprocessor systems with shared memory and clock.
- Increased throughput, economical, and reliable.
- Symmetric multiprocessing (SMP) and asymmetric multiprocessing.

## Clustered Systems
- Multiple systems share storage.
- Provides high reliability.
- Types
  1. *Asymmetric Clustering* : One machine in standby mode.
  2. *Symmetric Clustering* : Multiple hosts run applications and monitor each other.
  3. *Parallel Clustering* : Multiple hosts access shared storage.

## Real-Time Systems
- Serve real-time applications with minimal delay.
- Types
  1. Hard Real Time : Strict deadlines.
  2. Firm Real Time : Deadlines with some tolerance.
  3. Soft Real Time : Deadlines with acceptable delays.
- Features
  - Low memory usage.
  - Predictable response times.
- Applications 
  - Airline reservations
  - Traffic control
  - Defence systems, etc.
## Handheld Systems
- PDAs and cellular phones.
- Limited memory, slow processors, small screens.
- Often lack virtual memory techniques.


