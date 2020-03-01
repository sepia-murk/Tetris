from import_defaults import *


class Board:
    # takes care about collisions, full rows, score, rotations, movement left and right
    def __init__(self):
        self.block = None
        self.fallenBricks = []
        self.countFallenBricks = [0]*ROWS

    def collided(self):
        # returns true if collided
        if (self.block is not None):
            if (self.block.maxY == ROWS-1):
                return True
            for fallenbrick in self.fallenBricks:
                for brick in self.block.bricks:
                    if ((fallenbrick.positionX == brick.positionX) and (fallenbrick.positionY == brick.positionY+1)):
                        return True
        return False

    def draw(self, canvas):
        # calls Brick.draw function
        if (self.block is not None):
            self.block.draw(canvas)

        for brick in self.fallenBricks:
            brick.draw(canvas)

    def canMoveRight(self):
        # checks the right side of the tetromine for any collisions, returns true if there are no collisions
        if (self.block is None):
            return False

        if (self.block.maxX >= COLUMNS-1):
            return False
        for fallenbrick in self.fallenBricks:
            for brick in self.block.bricks:
                if ((fallenbrick.positionX == brick.positionX+1) and (fallenbrick.positionY == brick.positionY)):
                    return False
        return True

    def canMoveLeft(self):
         # checks the left side of the tetromine for any collisions, returns true if there are no collisions
        if (self.block is None):
            return False

        if (self.block.minX <= 0):
            return False
        for fallenbrick in self.fallenBricks:
            for brick in self.block.bricks:
                if ((fallenbrick.positionX == brick.positionX-1) and (fallenbrick.positionY == brick.positionY)):
                    return False
        return True

    def canRotate(self):
        if (self.block is None):
            return False
        return True

    def gameOver(self):
        if (self.block is None):
            return False
        else:
            if (self.collided()):
                return True

    def moveRight(self):
        # if the condition is satisfied, each brick from the tetromine moves right
        if (self.canMoveRight()):
            for brick in self.block.bricks:
                brick.positionX += 1

    def moveLeft(self):
        # if the condition is satisfied, each brick from the tetromine moves left
        if (self.canMoveLeft()):
            for brick in self.block.bricks:
                brick.positionX -= 1

    def rotate(self):
        # if the condition is satisfied, each brick from the tetromine rotates
        if (self.canRotate()):
            self.block.rotate()

    def checkCollisions(self):
        # if the condition is satisfied, the tetromine falls apart to individual bricks
        # fallenBricks list holds all fallen bricks
        if (self.collided()):
            for brick in self.block.bricks:
                self.fallenBricks.append(brick)
                self.countFallenBricks[brick.positionY] += 1
            self.block = None

    def checkFullRows(self, canvas, score):
        # checks the full rows, if row is full, function deleteRow is called
        # adds score
        # count = 0
        for i in range(len(self.countFallenBricks)):
            rowSize = self.countFallenBricks[i]
            if (rowSize == COLUMNS):
                self.deleteRow(i, canvas)
                # count += 1
                score += 100
                # Display(canvas).spiritusDeletus(canvas)
        # return count, score
        return score

    def deleteRow(self, i, canvas):
        # actually deletes the row by re-creating fallenBricks list
        self.countFallenBricks[i] = 0
        fallenBricksCopy = self.fallenBricks[:]
        self.fallenBricks = []

        for brick in fallenBricksCopy:
            if (brick.positionY != i):
                self.fallenBricks.append(brick)
                if (brick.positionY < i):
                    brick.positionY += 1
            else:
                brick.erase(canvas)

        self.reCountFallen()

    def reCountFallen(self):
        # countFallenBricks is a list which holds current number of fallen bricks in each row
        # this function counts the amount of bricks on each row after being called upon
        self.countFallenBricks = [0]*ROWS
        for fallenbrick in self.fallenBricks:
            self.countFallenBricks[fallenbrick.positionY] += 1
