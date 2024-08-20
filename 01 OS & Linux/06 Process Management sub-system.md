## Process Creation  
- **System Calls :** `fork`, `spawn`  
- **Parent and Child** 
	- Parent process creates child process  
	- Resource sharing
	- Execution
	- Address space
- **Identifiers :** PID, PPID  
- **Init Process :** PID 1, parent of all processes

## Process State  
- **States :** Ready, Running, Wait/Sleep, Stopped, Zombie
- ![Process states](images/process_states.png)

## Process Scheduling  
- **Scheduling :** 
	- Determines process execution order
	- CPU Scheduler
- **Dispatcher**
	- Gives control of the CPU to the selected process
	- context switching
	- switching to user mode
	- jump in user program 
- **Categories**
	- Non-preemptive
	- Preemptive  
- **Criteria**
	- CPU utilization : keep CPU busy
	- Throughput : no of process completed per time
	- Turnaround time : time to execute a process
	- Waiting time : waiting in ready queue
	- Response time : time from a request submission to 1st response

## Scheduling Algorithms  
- **FCFS** 
	- First-Come, First-Served  
	- Poor performance
	- High avg-wait time
- **SJF** 
	- Shortest-Job-First (Non-preemptive, Preemptive)  
	- Optimal - min avg-wait time
- **Priority Scheduling** 
	- Based on priority number, with aging to prevent starvation  
	- starvation - low priority ps may never execute
	- aging - as time progresses increase the priority of ps
- **RR :** Round Robin with fixed time slices

## Commands  
- **ps :** Show current processes  
- **pstree :** Display process tree  
- **bg :** Move suspended process to background  
- **fg :** Bring background job to foreground  
- **jobs :** List background/foreground jobs  
- **top :** Real-time system view  
- **kill :** Terminate a process  