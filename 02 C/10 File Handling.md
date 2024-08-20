### C Stream
- **Text stream** : it is sequence of characters. C allows a text stream to be organized into lines terminated by a new line character
- **Binary streams**

### fopen
- `FILE *fopen(const char *path, const char *mode)`
- **file opening modes**
	- `r` read-only
	- `r+` read & write
	- `w` write/create/over-write
	- `w+` read & write/create/over-write
	- `a` append
	- `a+` read & append/create
### fclose
- `int fclose(FILE *fp)`
- Upon successful completion this function returns 0 else end of file (eof) is returned
### fgetc
- `int fgetc ( FILE * stream )`
- Get character from stream
### fputc
- `int fputc ( int character, FILE * stream )`
- Write character to stream and advances the position indicator
### fgets
- `char * fgets ( char * str, int num, FILE * stream )`
- Reads characters from stream and stores them as a C string into str until (num-1)
### fputs
- `int fputs ( const char * str, FILE * stream )`
- Writes the C string pointed by str to the stream
### fprintf
- `int fprintf ( FILE * stream, const char * format, variable )`
- Write formatted data to stream
### fscanf
- `int fscanf ( FILE * stream, const char * format, variable )`
- Read formatted data from stream
### fread & fwrite
- for reading/writing data from/to the file opened by fopen function

 ```bash
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)

size_t fwrite(void *ptr, size_t size, size_t nmemb,FILE *stream)
```
### fseek
- `int fseek(FILE *stream, long offset, int whence)`
- To set the file position indicator for the stream to a new position
- SEEK_SET, SEEK_CUR, SEEK_END
### rewind
- `void rewind ( FILE * stream )`
- Set position of stream to the beginning
### ftell
- `ftell(FILE *fp)`
- To determine the current location of a file
### feof
- `int feof ( FILE * stream )`
- Check end-of-file indicator
### ferror
- `int ferror ( FILE * stream )`
- Check error indicator