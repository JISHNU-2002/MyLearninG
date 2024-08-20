## IPC Mechanisms
IPC is essential for exchanging data between processes in a multitasking OS

### 1 Pipe (Unnamed Pipe)
- Communication between related processes (siblings of a process)
- **Half-duplex** : Unidirectional data flow
- PIPEs are created by the pipe()
- Local to the system
- Read & Write done at same time
- No control over ownership & permissions
- Vanishes as soon as it is closed or one of the processes completes execution
- ![Pipe](images/pipe.png)
```c
#include <unistd.h>
#include <stdio.h>

int main() {
    int fd[2];
    pipe(fd);
    // fd[0] for reading, fd[1] for writing
    return 0;
}
```

### 2 FIFO (Named Pipe)
- Communication between unrelated processes
- Exists in the filesystem
- Bidirectional data flow
- mknod() to create FIFO in C
- Capable of communicating across different computers & n/ws
- Read & Write doesn't require to be occur at same time
- Ownership & permissions control
- FIFO remain till system reboots

```c
/* reader Process */
if(mknod(FIFO_FILE, S_IFIFO|0666, 0) != 0)
	perror("FIFO creation error in server\n");
if((fp = fopen(FIFO_FILE, "r")) == NULL)
	perror("FIFO openning error\n");
fgets(readbuf, 80, fp);
printf("Server program Received string: %s\n", readbuf);
fclose(fp);
unlink(FIFO_FILE); // to remove fifo

/* Writer Process */
FILE *fp;
if((fp = fopen(FIFO_FILE, "w")) == NULL)
	perror("FIFO openning error\n");
fputs(argv[1], fp);
fclose(fp);
```

### 3 Message Queue
- Sending and receiving messages
- Messages read by type
- Not restricted to FIFO order

```c
#include <sys/msg.h>
int msqid = msgget(key, 0666 | IPC_CREAT);
msgsnd(msqid, &msg, sizeof(msg), 0);
msgrcv(msqid, &msg, sizeof(msg), 0, 0);
```

### 4 Semaphore
- Mutex and Semaphore
- Resource that contains an int value
- Allows ps to synchronize by testing and setting the value
- Coordinate access to resources
- Counting and signaling mechanism
- **Operations** 
	- P (wait) : sem_wait() - decrement : lock
	- V (signal) : sem_post() - increment : unlock

```C
#include <semaphore.h>
int main() {
	sem_t *mySemaphore;
	int count = 0;
	sem_init(mySemaphore, 0, 1);
	sem_wait(mySemaphore);
	count++;
	sem_post(mySemaphore);
	sem_destroy(mySemaphore);
	return 0;
}
```

### 5 Shared Memory
- Share data between multiple processes
- **Steps**
  1. Key generation (`ftok`)
  2. Memory segment creation (`shmget`)
  ```bash
  int shmget(key_t,size_tsize,intshmflg)
```
  3. Attachment (`shmat`)
  ```bash
  void *shmat(int shmid ,void *shmaddr ,int shmflg)
```
  4. Detachment (`shmdt`)  
```bash
int shmdt(void *shmaddr)
```
  5. Destroy (`shmctl`)
```bash
shmctl(int shmid,IPC_RMID,NULL)
```

```c
#include <sys/ipc.h>
#include <sys/shm.h>
int shmid = shmget(key, size, 0666 | IPC_CREAT);
void *shared_memory = shmat(shmid, NULL, 0);
shmdt(shared_memory);
shmctl(shmid, IPC_RMID, NULL);
```

### System V IPC
- Derived from UNIX System V release 4
- This mechanism includes : Message Queues, Semaphores, Shared Memory
- `-q` : Show only message queuesipcs
- `-s` : Show only semaphoresipcs
- `-m` : Show only shared memoryipcs