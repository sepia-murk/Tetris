from import_defaults import *
from class_colors import Colors
from class_brick import Brick


class Block:
    # this class holds bricks from Brick and assigns properties to the whole tetromine after it has been created
    def __init__(self, bricks):
        self.bricks = bricks

    def fallingDown(self):
        # add one to Y position of each brick when falling down
        for brick in self.bricks:
            brick.positionY += 1

    def draw(self, canvas):
        # calls the draw function in Brick
        for brick in self.bricks:
            brick.draw(canvas)

    @property
    def maxY(self):
        # maximal Y coordinate of the tetromine
        maxY = self.bricks[0].positionY
        for brick in self.bricks:
            if (brick.positionY > maxY):
                maxY = brick.positionY

        return maxY

    # @property
    # def minY(self):
    #     minX = self.bricks[-1].positionY
    #     for brick in self.bricks:
    #         if (brick.positionY < minY):
    #             minY = brick.positionY

    @property
    def maxX(self):
        # maximal X coordinate of the tetromine
        maxX = self.bricks[-1].positionX
        for brick in self.bricks:
            if (brick.positionX > maxX):
                maxX = brick.positionX

        return maxX

    @property
    def minX(self):
        # minimal Y coordinate of the tetromine
        minX = self.bricks[0].positionX
        for brick in self.bricks:
            if (brick.positionX < minX):
                minX = brick.positionX

        return minX


# following classes are children classes to class Block, each one creates one unique tetromine in its default state (not rotated) and when called rotate function, the function rotates the tetromine according to user's input
class I_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-3)
        super().__init__([Brick(color, posX, 0), Brick(
            color, posX+1, 0), Brick(color, posX+2, 0), Brick(color, posX+3, 0)])
        self.rotated = 0

    def rotate(self):
        if (self.rotated % 2 == 0):
            self.bricks[1].positionX -= 1
            self.bricks[1].positionY += 1
            self.bricks[2].positionX -= 2
            self.bricks[2].positionY += 2
            self.bricks[3].positionX -= 3
            self.bricks[3].positionY += 3
            self.rotated += 1

        else:
            self.bricks[1].positionX += 1
            self.bricks[1].positionY -= 1
            self.bricks[2].positionX += 2
            self.bricks[2].positionY -= 2
            self.bricks[3].positionX += 3
            self.bricks[3].positionY -= 3
            self.rotated += 1


class O_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-1)
        super().__init__([Brick(color, posX, 0), Brick(
            color, posX+1, 0), Brick(color, posX, 1), Brick(color, posX+1, 1)])

    def rotate(self):
        # square doesn't rotate
        pass


class Z_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-3)
        super().__init__([Brick(color, posX, 0), Brick(
            color, posX+1, 0), Brick(color, posX+1, 1), Brick(color, posX+2, 1)])
        self.rotated = 0

    def rotate(self):
        if (self.rotated % 2 == 0):
            self.bricks[0].positionX += 1
            self.bricks[1].positionY += 1
            self.bricks[2].positionX -= 1
            self.bricks[3].positionX -= 2
            self.bricks[3].positionY += 1
            self.rotated += 1

        else:
            self.bricks[0].positionX -= 1
            self.bricks[1].positionY -= 1
            self.bricks[2].positionX += 1
            self.bricks[3].positionX += 2
            self.bricks[3].positionY -= 1
            self.rotated += 1


class S_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-3)
        super().__init__([Brick(color, posX+1, 0), Brick(color,
                                                         posX+2, 0), Brick(color, posX, 1), Brick(color, posX+1, 1)])
        self.rotated = 0

    def rotate(self):
        if (self.rotated % 2 == 0):
            self.bricks[0].positionY += 1
            self.bricks[1].positionX -= 1
            self.bricks[1].positionY += 2
            self.bricks[2].positionY -= 1
            self.bricks[3].positionX -= 1
            self.rotated += 1

        else:
            self.bricks[0].positionY -= 1
            self.bricks[1].positionX += 1
            self.bricks[1].positionY -= 2
            self.bricks[2].positionY += 1
            self.bricks[3].positionX += 1
            self.rotated += 1


class J_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-2)
        super().__init__([Brick(color, posX, 1), Brick(
            color, posX+1, 1), Brick(color, posX+2, 1), Brick(color, posX, 0)])
        self.rotated = 0

    def rotate(self):
        if (self.rotated % 4 == 0):
            self.bricks[0].positionY -= 1
            self.bricks[1].positionX -= 1
            self.bricks[2].positionX -= 2
            self.bricks[2].positionY += 1
            self.bricks[3].positionX += 1
            self.rotated += 1

        elif (self.rotated % 4 == 1):
            self.bricks[0].positionX += 2
            self.bricks[1].positionX += 1
            self.bricks[1].positionY -= 1
            self.bricks[2].positionY -= 2
            self.bricks[3].positionX += 1
            self.bricks[3].positionY += 1
            self.rotated += 1

        elif(self.rotated % 4 == 2):
            self.bricks[0].positionX -= 1
            self.bricks[0].positionY += 2
            self.bricks[1].positionY += 1
            self.bricks[2].positionX += 1
            self.bricks[3].positionX -= 2
            self.bricks[3].positionY += 1
            self.rotated += 1

        else:
            self.bricks[0].positionX -= 1
            self.bricks[0].positionY -= 1
            self.bricks[2].positionX += 1
            self.bricks[2].positionY += 1
            self.bricks[3].positionY -= 2
            self.rotated += 1


class L_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-2)
        super().__init__([Brick(color, posX, 1), Brick(
            color, posX+1, 1), Brick(color, posX+2, 1), Brick(color, posX+2, 0)])
        self.rotated = 0

    def rotate(self):
        if (self.rotated % 4 == 0):
            self.bricks[0].positionY -= 1
            self.bricks[1].positionX -= 1
            self.bricks[2].positionX -= 2
            self.bricks[2].positionY += 1
            self.bricks[3].positionX -= 1
            self.bricks[3].positionY += 2
            self.rotated += 1

        elif (self.rotated % 4 == 1):
            self.bricks[0].positionX += 2
            self.bricks[1].positionX += 1
            self.bricks[1].positionY -= 1
            self.bricks[2].positionY -= 2
            self.bricks[3].positionX -= 1
            self.bricks[3].positionY -= 1
            self.rotated += 1

        elif(self.rotated % 4 == 2):
            self.bricks[0].positionX -= 1
            self.bricks[0].positionY += 2
            self.bricks[1].positionY += 1
            self.bricks[2].positionX += 1
            self.bricks[3].positionY -= 1
            self.rotated += 1

        else:
            self.bricks[0].positionX -= 1
            self.bricks[0].positionY -= 1
            self.bricks[2].positionX += 1
            self.bricks[2].positionY += 1
            self.bricks[3].positionX += 2
            self.rotated += 1


class T_Block(Block):
    def __init__(self):
        color = Colors.color()
        posX = random.randrange(0, COLUMNS-2)
        super().__init__([Brick(color, posX, 1), Brick(
            color, posX+1, 1), Brick(color, posX+2, 1), Brick(color, posX+1, 0)])
        self.rotated = 0

    def rotate(self):
        if(self.rotated % 4 == 0):
            self.bricks[3].positionY += 1
            self.bricks[1].positionX -= 1
            self.bricks[2].positionX -= 2
            self.bricks[2].positionY += 1
            self.bricks[0].positionY -= 1
            self.rotated += 1

        elif(self.rotated % 4 == 1):
            self.bricks[1].positionX += 1
            self.bricks[1].positionY -= 1
            self.bricks[2].positionY -= 2
            self.bricks[0].positionX += 2
            self.rotated += 1

        elif(self.rotated % 4 == 2):
            self.bricks[3].positionX -= 1
            self.bricks[1].positionY += 1
            self.bricks[2].positionX += 1
            self.bricks[0].positionX -= 1
            self.bricks[0].positionY += 2
            self.rotated += 1

        else:
            self.bricks[3].positionX += 1
            self.bricks[3].positionY -= 1
            self.bricks[2].positionX += 1
            self.bricks[2].positionY += 1
            self.bricks[0].positionX -= 1
            self.bricks[0].positionY -= 1
            self.rotated += 1
