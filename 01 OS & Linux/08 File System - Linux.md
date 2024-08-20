
## What are filesystems?
- File system is the way files are organized on the disk.
- A filesystem is the methods and data structures that an OS uses to keep track of files on a disk or partition.
- Different kinds of file systems vary in structure, logic, speed, flexibility, security, size, etc.
- Common Linux file systems: ext2, ext3, ext4, XFS, JFS, btrfs, VFS, ReiserFS

## Ext, Ext2, Ext3, Ext4, JFS, XFS, btrfs and swap
- **Ext** : Old and no longer used due to limitations.
- **Ext2** : First Linux FS allowing 2TB data.
- **Ext3** : Ext2 with upgrades, lacks file recovery or snapshots.
- **Ext4** : Faster, supports larger files.
- **JFS** : Made by IBM, works with small and big files, prone to corruption over time.
- **XFS** : Slow with small files, great with large files.
- **Btrfs** : Made by Oracle, good performance, still under development.

## The file system layout

![FS Layout](images/file_system_layout.png)
- **Boot block** : Contains bootstrap code for booting.
- **Super block** : Describes the state of the FS (size, max files, free space).
- **Inode list** : Contains the inode table, used by the kernel to get file info.
- **Data block** : Stores user files, administrative files at the start.

## Virtual File System (VFS)

![VFS](images/vfs.png)
- Provides a single set of commands for the kernel to access all types of filesystems.
- VFS software calls specific device drivers to interface with various filesystems.

## Ext2 / ext3 / ext4 file system

![Ext FS](images/ext_fs.png)
- **Boot sector** : Includes a small boot record and partition table.
- **Superblock** : Contains metadata defining filesystem structures.
  - Total inode count
  - Total block count
  - Free block count
  - Free inode count
  - Blocks per group
  - Inodes per group
  - Mount time
  - Number of mounts since last fsck

## i-node block
- Contains numbers of data blocks for storing file data.
- **File mode** : Determines file type and access rights.
- **Link count** : Number of hard links pointing to the inode.
- **User ID and Group ID** : Owner identifiers.
- **Device ID** : If the file is a device file.
- **File size** : In bytes.
- **Timestamps** : ctime, mtime, atime.
- **Preferred I/O block size**.
- **Number of blocks allocated**.

## Accessing data block
- Inode does not contain the file name.
- Access to a file is via the directory entry, which contains the file name and a pointer to the inode.

## VFS

![VFS](images/vfs_2.png)
- Manages all mounted file systems.
- Keeps data structures describing the virtual file system and real mounted file systems.
- Each filesystem registers itself with the VFS during OS initialization.
- VFS inodes describe files and directories.
- Frequently accessed inodes are kept in the inode cache for quicker access.
- VFS superblock contains device identifier, inode pointers, block size, and superblock operations.

## Mounting a File System
- The superuser validates arguments passed in the system call.
- VFS searches through known filesystems by looking at the `file_system_type` data structures.
- Example mount command: `mount -t iso9660 -o ro /dev/cdrom /mnt/cdrom`

## Data structures

- When a process opens a file the following in formations are maintained by the kernel.
- These structures are maintained in the kernel tree `/usrc/src/linux/include/linux`

- **Task_struct** (sched.h) points to **Files_struct** (fdtable.h).
- **Files_struct** points to **struct file** (fs.h).
- **struct file** points to **struct path** (path.h).
- **struct path** points to **struct dentry** (dcache.h).
- **struct dentry** points to **struct inode** (fs.h).


