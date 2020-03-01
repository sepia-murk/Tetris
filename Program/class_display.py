from import_defaults import *
from class_colors import Colors


class Display:
    # creates display for user - shows score and announces game over
    def __init__(self, canvas):
        canvas.create_line(322, 0, 322, 600, fill=COLOR)
        canvas.create_text(370, 40, text='Score', fill=COLOR, font=FONT)

    def gameOver(self, canvas):
        canvas.create_rectangle(110, 250, 300, 350, fill="black")
        canvas.create_text(170, 300, text="GAME OVER",
                           fill=COLOR, font="Courier 18")

        canvas.update()
        canvas.after(1500)
        canvas.destroy()
