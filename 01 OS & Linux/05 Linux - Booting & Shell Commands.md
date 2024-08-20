
## Man Pages
---

`• $man [section-num] [command/tool name]`

Explanation of different sections in the manual pages
- Section 1 : Executable programs or shell commands.
- Section 2 : System calls provided by the kernel.
- Section 3 : Library calls within program libraries.
- Section 4 : Special files typically found in `/dev`.
- Section 5 : File formats and conventions (e.g., `/etc/passwd`).
- Section 6 : Games.
- Section 7 : Miscellaneous information, including macro packages and conventions.
- Section 8 : System administration commands (usually for root).
- Section 9 : Kernel routines (non-standard).

- a : display all manual pages for a given input
- f : print short descriptions
- k : make man search considering input as regular expression
- w : display location of man files

## Booting Linux
---

1. **BIOS POST**
   - Initial hardware checks and locating boot sectors.
   - boot sector is first stage of boot loader ( GRUB, GRUB2, and LILO )

2. **Kernel**
   - Bootloader loads the kernel from `/boot` to RAM
   - Kernal loads systemd

3. **systemd**
   - Initializes the system.
   - 1st process to run on Linux
   - systemd mounts the filesystems as defined by `/etc/fstab`
   - Uses `/etc/systemd/system/default.target` to determine boot target.

4. **Targets and Runlevels**
   - Runlevels mapped to systemd targets.
     - `runlevel3.target` -> `multi-user.target`
     - `runlevel5.target` -> `graphical.target`

- ![systemd](images/systemd.png)


## Shell Commands
---

1. **Login/Logout** : `login`, `logout`, or `exit`.
2. **Changing Password** : `passwd`
3. **Terminal Type** : Set appropriate terminal type (e.g., `vt100`, `xterms`).
4. **Using Online Help** : `man`

5. **Types of Shells** 
	- Bourne (sys V)
	- Korn (Solaris)
	- 'C’ shell (BSD)
	- Bash shell (Linux)

7. **Bash Shell**
	   - Command line editing
	   - Unlimited command history
	   - Job control
	   - Shell functions and aliases
	   - Indexed array of unlimited size
   
7. **Startup Files**
	   - System-wide: `/etc/profile`, `/etc/bash_profile`
	   - User-specific: `~/.bash_profile`, `~/.bash_login`, `~/.profile`
   
8. **Built-in Commands** - Examples: `cd`, `echo`, `exit` , `break`, `pwd`, `declare`, `help`
   
9. **Variables**
	- Global - exported variables
	- Local - user defined
	- Creating &export variables : 
		   - `var_name = value`
		   - `export var_name`
	- Environment variables : `env`
		- DISPLAY
		- EDITOR
		- GROUP
		- HOME
		- IFS - Internal Field Seperators
		- LOGNAME
		- PATH
## Basic Commands
---

1. **who** 
	- Displays logged-in users.
	- `who -q`
	- `who -H`
	- `who -a`

2. **w** 
	- Displays user activity.
	- `w`, `w -u`, `w username`

	- USER – User name.
	- TTY – Terminal type such as pts/0 or console.
	- FROM – The remote host name or IP address.
	- LOGIN@ – Login time.
	- IDLE – Idel time.
	- JCPU – The JCPU time is the time used by all processes attached to the tty.
	- PCPU – The PCPU time is the time used by the current process displayed in WHAT field.
	- WHAT – The command line of USER’s current process.

3. **whoami** : Displays the current user.
4. **date** : Displays/sets system date and time.
5. **cal** : Displays calendar.
6. **whatis** : Displays brief information about commands.