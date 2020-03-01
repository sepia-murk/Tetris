from import_defaults import *


class Brick:
    # when given parameters, this class created each brick forming the tetromine
    # when created, it draws bricks forming the whole tetromine, after its fall to the bottom of the pop-up window, each tetromine falls apart to bricks and the brick are deleted
    def __init__(self, color, posX, posY):
        self.size = BRICK_SIZE
        self.color = color
        self.positionX = posX
        self.positionY = posY
        # relative position of each brick
        self.rectangle = None

    def draw(self, canvas):
        # draw one brick
        self.erase(canvas)
        self.rectangle = canvas.create_rectangle(
            self.positionX*self.size, self.positionY*self.size, (self.positionX+1)*self.size, (self.positionY+1)*self.size, fill=self.color)

    def erase(self, canvas):
        # delete after fall
        if (self.rectangle is not None):
            canvas.delete(self.rectangle)
