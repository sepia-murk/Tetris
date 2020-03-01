from import_importer import *

import random
import keyboard
import sys
sys.setrecursionlimit(10000)


BRICK_SIZE = 20
ROWS = 30
COLUMNS = 16
SCORE = 0
FONT = "Times 18"
COLOR = "white"
FALL = 100
FALLFASTER = 20

main_window = Tk()
main_window.geometry("420x600")
main_window.title("Tetris")
