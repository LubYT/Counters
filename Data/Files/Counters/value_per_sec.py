from decimal import Decimal
import math

class Value_per_second:
    def __init__(self,game):
        self.game = game
    def place(self):
        self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 95, anchor='center',
                                                      text='CPS: '+str(0), fill='#a9cf9b', font=('bahnschrift', 16))
    def conf(self,count,*args):
        self.game.main_canvas.itemconfigure(self.text, fill='#a9cf9b', text='CPS: '+count)

    def reset(self):
        self.game.main_canvas.itemconfigure(self.text, fill='#a9cf9b', text='CPS: ' + str(0))