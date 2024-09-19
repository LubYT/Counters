from decimal import Decimal
from tkinter import *
import math

class Eternity:
    def __init__(self,game):
        self.game=game
        self.eternity_count=1
        self.save=self.game.Save.Stats_data

    def place(self):
        pass

    def hide(self):
        pass

    def get_save(self):
        return self.save+'\n'