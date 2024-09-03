from decimal import Decimal
from tkinter import *
import math

class Illusory_aspects:
    def __init__(self,game):
        self.game=game
        self.active_1st=False
        self.save=self.game.Save.Aspect_data
        if self.save=='True':
            self.game.Menu.add('Illusory')

    def place(self):
        self.box1=self.game.main_canvas.create_rectangle(10,10,990,990, fill='#303030', outline='a0a000', borderwidth=4)

    def hide(self):
        self.game.main_canvas.delete(self.box1)