# Operating System (OS)

## Definition

- A collection of programs to control/manage computer systems.
- Acts as an intermediary between the user and computer components.

## Goals

- Execute user programs and solve user problems.
- Make the computer system convenient to use.
- Use hardware efficiently.

## Computer System Components

1. **Hardware** : CPU, memory, I/O devices.
2. **Operating System** : Controls hardware use among applications.
3. **Applications Programs** : Use APIs to interact with the OS.
4. **Users** : People, machines, other computers.

## Components of OS

![Operating System Diagram](images/os.png)


- **Bootloader** : Manages the boot process (e.g., ntldr, BOOTMGR, LILO, GRUB).
- **Kernel** : Core of the OS, manages CPU, memory, and devices.
- **Daemons** : Background services (e.g., printing, sound, network services).
- **Shell** : Command interpreter interface between kernel and user applications.
- **Applications** : Software to perform specific tasks.


# The Kernel

## Definition

- Central core of an OS, first program loaded into memory during booting.
- Interacts with the shell, programs, and hardware.

## Tasks/Components

![Kernal Layout](images/kernal_layout.png)
- **Process Management** : Manages application execution.
- **Device Management** : Controls access to peripherals.
- **Memory Management** : Allocates memory to processes.
- **Interrupt Handling, I/O Communication, File System** : Other critical functions.

## Categories of Kernels

![Diff kernals comparision](images/kernals.png)


1. **Monolithic Kernels**
   - Entire kernel operates in kernel space.
   - Unix kernels (BSD, Linux, Solaris), DOS, Windows 9x, OpenVMS.
2. **Microkernels** 
   - Minimal set of functions, other functions run on top.
   - AmigaOS, MINIX, Symbian.
3. **Hybrid Kernels**
   - Combination of microkernel and monolithic kernel.
   - Windows NT, 2000, XP, Vista, 7, DragonFly BSD.
4. **Exo Kernels**
   - Limited to protection and multiplexing of raw hardware.
   - Allows programmers to choose what level of abstraction they want, such as one for Linux and one for Microsoft Windows, thus making it possible to simultaneously run both Linux and Windows applications
   - MIT's Aegis, XOK.
