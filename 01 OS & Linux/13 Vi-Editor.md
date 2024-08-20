
## Visual Editor

- Visual editor for entering and editing text files
- Screen-oriented text editor included with most UNIX system distributions
- Command driven

### Categories of Commands
---

- General administration
- Cursor movement
- Insert text
- Delete text
- Paste text
- Modify text

## Editing Commands
---

### Invoking Vi Editor

- To edit a file : `vi [filename]`
- To recover an editing session : `vi -r [filename]`

### Text Insertion / Replacement

- `i` - inserts text to the left of the cursor
- `a` - inserts text to the right of the cursor
- `I` - inserts text at the beginning of the line
- `A` - appends text at end of the line
- `o` - opens line below
- `O` - opens line above
- `R` - replaces text from cursor to right
- `s` - replaces a single character with any number of characters
- `S` - replaces entire line

## Vi Commands
---

### Exiting Vi Editor

- `:x<Return>` - quit vi, writing modified file
- `:wq<Return>` - quit vi, writing modified file
- `:q<Return>` - quit vi
- `:q!<Return>` - quit vi without saving changes

### Moving the Cursor

- `j` or `<Return>` (down-arrow) - move cursor down one line
- `k` (up-arrow) - move cursor up one line
- `h` or `<Backspace>` (left-arrow) - move cursor left one character
- `l` or `<Space>` (right-arrow) - move cursor right one character
- `0` (zero) - move cursor to start of current line
- `$` - move cursor to end of current line

## Deletion Commands
---

- `x` - delete character at cursor position
- `3x` - delete 3 characters at cursor position
- `dw` - delete word
- `2dw` - delete 2 words
- `dd` - delete a line
- `2dd` - delete 2 lines

## Yanking Commands
---

- `Y` - copy line into buffer
- `3Y` - copy 3 lines into buffer
- `p` - paste buffer below cursor
- `P` - paste buffer above cursor

### Save and Quit
- `:w` - save
- `:w!` - save as `:w! filename`
- `:x` - save and quit
- `:q` - cancel changes
- `:q!` - cancel and quit

## Screen Manipulation Commands
---

### Saving Files
- `^f` - move forward one screen
- `^b` - move backward one screen
- `^d` - move down (forward) one half screen
- `^u` - move up (back) one half screen
- `^l` - redraw screen
- `^r` - redraw screen, removing deleted lines

### Write Commands
- `:w<Return>` - write current contents to file
- `:w newfile<Return>` - write current contents to a new file named newfile
- `:12,35w smallfile<Return>` - write contents of lines 12-35 to a new file named smallfile

## Search & Replace Commands
---

### Searching Through Text
- `?pattern` : Backward for pattern
- `/pattern` : Forward for pattern
- `n` : Repeat previous search
- `N` : Reverse direction of previous search
- `:beg,end g/pattern/p` : Show all lines containing pattern
- `:1,$g/compiler/p` : prints all lines with the pattern "compiler"

### Substitute Patterns
- `:%s/notfound/found/g` - change all occurrences of "notfound" to "found"

## Useful ex Commands
---

- `:set all` - Display all Set options
- `:set autoindent` - Automatically indent following lines
- `:set ignorecase` - Ignore case during pattern matching
- `:set list` - Show special characters in the file
- `:set number` - Display line numbers
- `:set shiftwidth=n` - Set width for shifting operators `<<` and `>>`
- `:set showmode` - Display mode when in Insert, Append, or Replace mode
- `:set wrapmargin=n` - Set right margin for auto-wrapping lines (0 turns it off)

