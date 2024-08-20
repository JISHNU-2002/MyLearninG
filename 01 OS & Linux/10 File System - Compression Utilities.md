## Key Commands and Utilities
---

### cmp  
- Compares two files byte by byte
- If a difference is found, it reports the byte and line number where the first difference is found

-  `cmp file1.txt file2.txt`  

 ```sh  
  cmp file1.txt file2.txt  
```

### diff  
- Shows differences between files
- `-b` ignore trailing blanks
- `-i` ignore the case of letters
- `-w` ignore space and tab characters
- `-r` apply diff recursively through common sub-directories

- `diff [options] file1 file2`  

  ```sh  
  diff -i file1.txt file2.txt  
  ```

### file  
- Determines the file type

- `file [options] filename`  

  ```sh  
  file -i file1.txt  
  ```

### cut  
- Removes sections from each line of files  
- `-b` select only these bytes
- `-c` select only these characters
- `-d` use DELIM instead of TAB for field delimiter
- `-f` select only these fields

- `cut [OPTIONS] [FILE]`  

  ```sh  
  cut -d ":" -f1,2 /etc/passwd  
  ```

### paste  
- Merges files line by line

- `paste [options] file1 file2`  

  ```sh  
  paste file1.txt file2.txt  
  ```

### touch  
- Creates an empty file or updates the timestamp of an existing file

- `touch [options] [date_time] file`  

  ```sh  
  touch newfile.txt  
  ```

### sort  
- Sorts contents of text files based on 1st char of each line

- `sort [options] [file]`  

  ```sh  
  sort -k2 file.txt  
  ```

### uniq  
- Filters out or reports repeated lines in a file \
- `-c` prefix lines by the number of occurrences
- `-d` only print duplicate lines, one for each group
- `-D` print all duplicate lines
- `-f` avoid comparing the first N fields

- `uniq [options] [file]`  

  ```sh  
  uniq -c file.txt  
  ```

### tr  
- Translates or deletes characters

- `tr [options] SET1 SET2`  

  ```sh  
  echo "hello" | tr 'a-z' 'A-Z'  
  ```


## File Compression & Archiving
---
### compress  
- Compresses files, creating a `.Z` extension

- `compress [options] file`  

  ```sh  
  compress file.txt  
  ```

### uncompress  
- Decompresses files compressed by `compress`

- `uncompress [options] file.Z`  

  ```sh  
  uncompress file.txt.Z  
  ```

### gzip  
- Compresses files, creating a `.gz` extension

- `gzip [options] filename`  

  ```sh  
  gzip file.txt  
  ```

### gunzip  
- Decompresses `.gz` files

- `gunzip [options] filename.gz`  

  ```sh  
  gunzip file.txt.gz  
  ```

### tar  
- tape archive
- Archives files into a single file

- **Options**
  - `-c` create a new archive  
  - `-t` list the contents of an archive  
  - `-x` extract the contents of an archive

 - - `tar [options] [file(s)]`  

  ```sh  
  tar -cvzf archive.tar.gz *.txt  
  ```  

### df
command to summarize disk block and file usage
### size
### du
command to summarize disk block and file usage