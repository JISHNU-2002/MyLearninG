### File System Basics  
- **File System :** Controls how data is stored and retrieved.  
- **Aspects** 
	- space management
	- filenames
	- directories
	- metadata
	- abstract user interface

### File Naming Conventions  
- Avoid special characters (@#$%^&*).  
- Case sensitive.  
- Avoid spaces use underscores   
- **Paths:**  
  - Absolute: `/home/user/file.txt`  
  - Relative: `file.txt`

### Important Directories  
- **/home :** User home directories.  
- **/bin :** Executable files.  
- **/sbin :** System executables.  
- **/lib :** Essential libraries.  
- **/etc :** System configuration files.  
- **/dev :** Device files.  
- **/mnt :** Mount points for external file systems.  
- **/tmp :** Temporary files.  
- **/var :** Variable data files.
- **/root**
- **/usr**
- **/usr/bin**
- **/sys**
- **/proc :** information about kernel components 

### Common Commands
---

#### pwd - Print Working Directory  
- Displays current directory.  
  - Example: `$ pwd` -> `/home/user`

#### cd - Change Directory  
- Changes the current directory.  
  - Examples:  
    - `cd /` (root directory)  
    - `cd ..` (one level up)  
    - `cd ~/folder` (user's folder)

#### ls - List Directory Contents  
- Lists files and directories.  
  - Options:  
    - `-l`: Long format  
    - `-a`: All files (including hidden)  
    - `-i`: list inode no of file in first column
    - `-s`: reports disk blocks occupied by file
    - `-R`: Recursive  
    - `-F`: Classify files by type
    - `-C`: display files in columns

#### cat - Concatenate and Display Files  
- Displays file content.  
  - Examples:  
    - `cat file1` (display file1)  
    - `cat > file1` (create/overwrite file1)  
    - `cat >> file1` (append to file1)

#### cp - Copy Files  
- Copies files or directories.  
  - Examples:  
    - `cp file1 file2` (copy file1 to file2)  
    - `cp -r dir1 dir2` (copy directory)

#### mv - Move/Rename Files  
- Moves or renames files.  
  - Example: `mv file1 file2` (rename file1 to file2)

#### rm - Remove Files  
- Deletes files or directories.  
  - Options:  
    - `-r`: Recursive (directories)  
    - `-i`: Interactive (confirm deletion)

#### mkdir - Create Directory  
- Creates directories.  
  - Examples:  
    - `mkdir folder1`  
    - `mkdir -p parent/child` (create parent and child directories)

#### rmdir - Remove Directory  
- Deletes empty directories.  
  - Example: `rmdir folder1`

#### more & less - View File Content  
- View content page by page.  
  - Controls: `space` (next page), `q` (quit)

#### wc - Word Count  
- Counts lines, words, and characters.  
  - Options:  
    - `-l`: Lines  
    - `-w`: Words  
    - `-c`: Characters

#### ln - Link Files  
- Creates hard or soft links.  
- Hard link 
	- Same inode
	- Can't cross file systems
	- Survives original deletion
	- There is link count maintained by the file system
	- Only one data copy
	- `ln file1 file2`  
- Soft link 
	- Different inode
	- Can cross file systems
	- Can't survive original deletion
	- There is no link count maintained by the file system
	- Only one data copy
	- `ln -s file1 file2`
