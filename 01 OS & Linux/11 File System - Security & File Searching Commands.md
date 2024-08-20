## Commands and Examples
---

### File Access Permissions 
---

**Read ( r )**
- List the contents of directory
- Remove the directory
**Write ( w )**
- copy files to the directory
- remove files from the directory
- rename files in the directory
- make a subdirectory
- remove a subdirectory from the directory
- move files to and from the directory
**Execute ( x )**
- display the contents of a directory file from within the directory
- change to the directory
- display a file in the directory
- copy a file to or from the directory

### chmod
Set file access permissions:
```bash  
chmod nnn [file]  
chmod [who]op[perm] [file]  
```  
Example:  
```bash  
chmod 755 file1  
chmod u=rwx,go=rx file1  
```

### umask  
Set default file permissions : `/etc/profile`
```bash  
umask 022  
```

### chown  
Change file ownership
```bash  
chown [options] user[.group] file  
```  
Example:  
```bash  
chown new_owner file  
```

### chgrp  
Change group ownership
```bash  
chgrp [options] group file  
```  
Example:  
```bash  
chgrp new_group file  
```

### File Searching Commands
---

### find  
Search for files 
```bash  
find directory [search options] [actions]  
```  
Examples:  
```bash  
find / -name passwd -print  
find . -newer library -print  
find . -name "*ar*" -ls  
```

### grep  
- Global Regular Expression Printer
- Search within files using regular expressions  
```bash  
grep [options] pattern [file(s)]  
egrep [options] pattern [file(s)]  
fgrep [options] pattern [file(s)]  
```  
Examples:  
- `-i` : ignore case
- `-c` : outs the count of no of lines containing matches
- `-v` : invert the search, display lines that do not match
- `-n` : display the line number along with the line on which a match was found
```bash  
grep '15' num.list  
grep -c '15' num.list  
grep '^ ' num.list  
grep '^[^ ]' num.list  
grep '^[1-9]' num.list  
```

### whatis  
Get brief information about commands
```bash  
whatis [options] command  
```  
Example:  
```bash  
whatis write 
whatis -s "2" open
whatis -w 'ab*'
```

### whereis  
Locate binary`-b`, source`-s`, and man`-m` pages of commands
```bash  
whereis [options] command  
```  
Example:  
```bash  
whereis open  
whereis -b whereis
```

### which  
Locate executables in the system
```bash  
which [options] command  
```  
Example:  
```bash  
which ls gdb open grep  
```