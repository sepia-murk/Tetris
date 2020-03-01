# Tetris

## Installation

This project requires certain Python packages to run properly.

To install package for keyboard input, run: 
```console
pip install keyboard
```

 or clone the repository: 
```console
git clone https://github.com/boppreh/keyboard
```

or download and extract the zip file:

```console
https://github.com/boppreh/keyboard/archive/master.zip
```

If you previously haven’t been using Python’s tkinter library, install it by running either:

```console
sudo pacman -Syu tk
```

or:

```console
pip install tkinter
```


## Running

To start the game, run this command from the project root directory:


```console
[user@device]$ sudo python index.py
```


After this, the game will run in its main window until terminated or until the user loses the game.

## File structure

The file structure is as follows:


```console
.
├── README.md
└── Program
    ├── class_block.py
    ├── class_blockFactory.py
    ├── class_board.py
    ├── class_brick.py
    ├── class_colors.py
    ├── class_display.py
    ├── class_gameMain.py
    ├── import_defaults.py
    ├── import_importer.py
    ├── index.py
```


`index.py` is the core file. All other files are of either category:



*   **Class** (`class_<class_name>.py`) - Class definition.
*   **Import file** (`import_<import_file_name>.py`) - Import files. Files which give index.py access to constants and to other classes. Also give all classes access to constants.

## Mechanics


```console
class_block.py
```


This class holds properties of each tetromine. Children classes determine each tetromine.


```console
class_blockFactory.py
```


This class randomly selects one type of tetromine and returns it.


```console
class_board.py
```


This class controls the falling tetromine - collisions, rotations, movements; also updates score.


```console
class_brick.py
```


This class creates individual bricks forming the falling tetromine.


```console
class_colors.py
```


This class randomly selects one color and returns it.


```console
class_display.py
```


This class creates the visual side of the main window. After the condition is satisfied, function `gameOver()` destroys the main window.


```console
class_gameMain.py
```


This class manages the whole game. It holds definitions for key control of the game, initializes all other classes.


```console
import_importer.py
```


This file contains connection for index.py to all other files.


```console
import_defaults.py
```


This file contains constants used in the game and calls tkinter.


```console
index.py
```


This file starts the game by calling the `mainLoop()` function from `class_gameMain.py`

The game begins in `index.py` by calling the `mainLoop()` function in `class_gameMain.py`. `class_gameMain.py` initializes canvas - background for the main window, class Display, class Board, sets score to 0 and creates the first tetromine by calling class BlockFactory.

Class BlockFactory randomly selects a tetromine and returns it to `self.board.block`. This calls the `class_board.py` file and by function `draw(self, canvas)` it calls `class_brick.py` file where the drawing takes place.

After the tetromine exists, it begins to fall down. It falls in constantly unless space is pressed, then it falls faster. While it is falling, the user can move the tetromine left and right and rotate it. In case, the user manages to complete one full row, the row is deleted by calling upon `deleteRow(self, i, canvas)` in `class_board.py` file. 

The games ends either by command in terminal `(^C)` or when there is no space for the tetromines to fall, ie. the board is full. Termination of the game in the `mainLoop()` is called with `self.display.gameOver(canvas)` where this refers to `gameOver(self, canvas)` function in `class_display.py`. The function writes text `"GAME OVER"` and destroys the main window after 1500ms.

## User interface

In `__init__()` in file `class_gameMain.py` there are keys bounded for user’s control of the game.

The user moves the tetromine left by pressing either left arrow or key for letter a. Number of presses means number of moves of the tetromine to the left.

The user moves the tetromine right by pressing either right arrow or key for letter d. Number of presses means number of moves of the tetromine to the right.

The user lets the tetromine fall down faster by holding either space key or arrow down. When released, the tetromine falls down at normal rate.

The user rotates the tetromine by pressing either arrow up or key for letter r.  Number of presses means number of rotations. The tetromine rotates clockwise only.
