# Vim Cheatsheet

- o or O to insert a blank line
- :!<cmd> to run bash commands in file
- `<,>` is the syntax that indicates the selection including < and to >
- `:r <cmd or filename>` reads the result of the target and puts it below the cursor in the current file

### Normal Mode
#### Actions
##### Insertion related
- o or O to insert a blank line after or before
- a to append to the cursor, A to append to the end of the line
- r to replace target with one written character; R to enter Replace mode
	- Replace mode overwrites
- c to change target with written
- i to enter insert mode, I to enter insert mode at the beginning of the line 
- x to delete character under cursor
- p to put text in the buffer
- deletion
	- d<target> deletes
		- motions
			- D == d$
			- dj deletes this line and next line
			- dk deletes this line and previous line
			- dh deletes previous char
			- dl deletes next char
		- objects
			- daw delete 'around' word
			- diw delete inside word
			- dip delete inside paragraph
			- dap delete 'around' paragraph

#### Targets/objects
- $ to end of line
- 0 beginning of line

### Undo/Redo
- u is undo last edit
	- U is undu all edits to line
- ctrl+r is redo

### Movement
- e moves to end of next word
- w moves to start of next word
	- W moves to start of next word and ONLY stops at whitespace
- b moves backwards to the start of the current/previous word

### Visual Mode
- v to enter visual mode
- y to yank highlighted text

### Insert mode
#### Entering insert mode

#### Movement
- H, L, M move the cursor to start of the top, bottom, and middle lines on the screen
- zz centers the line your cursor is currently on to the center of the screenkkk
