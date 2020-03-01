from tkinter import *
from import_defaults import *
from class_display import Display
from class_board import Board
from class_blockFactory import BlockFactory
from class_block import *


class Game:
    # the whole game is coordinated from here
    # creates the tetromine, by user's input it calls functions to move and rotate the tetromine
    # if there's no place for the tetromine to fall (after it has been created), the game over function is called and the game ends.
    def __init__(self):
        self.c = Canvas(width=420, height=600, bg='black')
        self.c.pack()
        self.display = Display(self.c)
        self.board = Board()
        self.moves = 0
        self.rotations = 0
        self.t = 0
        self.score = SCORE
        self.updateMe = FALL
        keyboard.on_press_key("right", self.moveRight, suppress=False)
        keyboard.on_press_key("left", self.moveLeft, suppress=False)
        keyboard.on_press_key("r", self.rotate, suppress=False)
        keyboard.on_press_key("d", self.moveRight, suppress=False)
        keyboard.on_press_key("a", self.moveLeft, suppress=False)
        keyboard.on_press_key("up", self.rotate, suppress=False)
        keyboard.on_press_key("space", self.turbo, suppress=False)
        keyboard.on_release_key("space", self.slowDown, suppress=False)
        keyboard.on_press_key("down", self.turbo, suppress=False)
        keyboard.on_release_key("down", self.slowDown, suppress=False)

    def moveRight(self, event):
        self.moves += 1

    def moveLeft(self, event):
        self.moves -= 1

    def rotate(self, event):
        self.rotations += 1

    def turbo(self, event):
        self.t = 1

    def slowDown(self, event):
        self.t = 0

    def mainLoop(self):
        self.score = self.board.checkFullRows(self.c, self.score)
        sc = self.c.create_text(
            370, 80, text=self.score, fill=COLOR, font=FONT)
        if (not self.board.gameOver()):
            if (self.board.block is None):
                self.board.block = BlockFactory.create()
            else:
                while (self.moves > 0):
                    self.board.moveRight()
                    self.board.checkCollisions()
                    self.moves -= 1

                while (self.moves < 0):
                    self.board.moveLeft()
                    self.board.checkCollisions()
                    self.moves += 1

                while (self.rotations > 0):
                    self.board.rotate()
                    self.board.checkCollisions()
                    self.rotations -= 1

                if (self.board.block is not None):
                    self.board.block.fallingDown()
                    self.board.checkCollisions()

            if (self.t == 1):
                self.updateMe = FALLFASTER
            else:
                self.updateMe = FALL

            self.board.draw(self.c)

            self.c.update()
            self.c.after(self.updateMe)
            self.c.delete(sc)
            self.mainLoop()
        else:
            self.display.gameOver(self.c)
