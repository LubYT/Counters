from decimal import Decimal
import math

class Value_per_second:
    def __init__(self,game):
        self.game = game
    def place(self):
        self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 95, anchor='center',
                                                      text='CPS: '+str(0), fill='#a9cf9b', font=('bahnschrift', 16))
    def conf(self,count,*args):
        if 'Aspect 1' in args:
            try:
                if count > 10000:
                    self.game.main_canvas.itemconfigure(self.text, fill='#590000', text='CPS: '+str("{:.2e}".format(Decimal(count)))+'('+(str("{:.2e}".format(Decimal(math.pow(count, 1/0.625)))))+')')
                else:
                    self.game.main_canvas.itemconfigure(self.text, fill='#590000', text='CPS: '+str(round(count, 1))+'('+(str(round(math.pow(count, 1/0.625))))+')')
            except OverflowError:
                self.game.Value.get_count(1.8e308)
        else:
            if count > 10000:
                self.game.main_canvas.itemconfigure(self.text, fill='#a9cf9b', text='CPS: '+str("{:.2e}".format(Decimal(count))))
            else:
                self.game.main_canvas.itemconfigure(self.text, fill='#a9cf9b', text='CPS: '+str(round(count, 1)))

    def reset(self):
        self.game.main_canvas.itemconfigure(self.text, fill='#a9cf9b', text='CPS: ' + str(0))