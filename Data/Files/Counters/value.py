from decimal import Decimal

class Value:
    def __init__(self,game):
        self.game=game
        self.lock=False
        self.value=self.game.Save.total_count
        self.first_e10=False
        self.first_e50=False
        self.first_inf=False

    def place(self):
        self.line=self.game.main_canvas.create_line(self.game.geometry[0],150,0,150,width=2,fill='#ad0000')
        self.line_2 = self.game.main_canvas.create_line(self.game.geometry[0], 10, 0, 10, width=2, fill='#ad0000')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]//2,30,anchor='center',text=str(self.value),fill='#a9cf9b',font=('bahnschrift',26))
        self.get_count(0)

    def get_count(self,count):
        if self.lock==False:
            self.value+=count
            self.game.Infinity.conf_upgrades('VALUE')
            self.check()

    def check(self):
            if self.value > 10000:
                self.game.main_canvas.itemconfigure(self.text, text=str("{:.2e}".format(Decimal(self.value))))
            else:
                self.game.main_canvas.itemconfigure(self.text,text=str(round(self.value,1)))
            if self.value>1e10 and self.first_e10==False or self.game.CB.amount>0 and self.first_e10==False or self.game.TA.amount>0 and self.first_e10==False or self.first_inf and self.first_e10==False:
                self.first_e10=True
                self.game.CB.place()
            if self.value > 1e50 and self.first_e50 == False or self.game.TA.amount>0 and self.first_e50==False or self.first_inf and self.first_e50==False:
                self.first_e50 = True
                self.game.TA.place()
            if self.value==1.8e308 and self.first_inf==False or self.game.Infinity.first and self.first_inf==False:
                self.first_inf=True
                self.game.Infinity.place()
            if self.value == 1.8e308:
                self.lock=True

    def reset(self):
        self.lock=False
        if self.game.Infinity.upgrades[2]=='Y':
            self.value = 1e5
        else:
            self.value = 100
        self.game.main_canvas.itemconfigure(self.text, text=str(self.value))