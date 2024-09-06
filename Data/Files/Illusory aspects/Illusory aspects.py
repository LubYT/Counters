from decimal import Decimal
from tkinter import *
import math

class Illusory_aspects:
    def __init__(self,game):
        self.game=game
        self.active_1st=False
        self.save=self.game.Save.Aspect_data
        self.available=self.game.Save.Aspect_data
        if self.available=='True':
            self.game.Menu.add('Illusory')

    def add(self):
        self.available = 'True'
        self.game.Menu.add('Illusory')

    def place(self):
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]//2,220,text='hi, it is still in work',anchor='center',fill='white',
                                          justify='center',font=('bahnschrift', 18))

    def hide(self):
        self.game.main_canvas.delete(self.text)

    def get_save(self):
        return self.available+'\n'
