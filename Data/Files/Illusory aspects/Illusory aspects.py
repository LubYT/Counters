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
        pass

    def hide(self):
        pass