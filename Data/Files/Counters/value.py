from decimal import Decimal

class Value:
    def __init__(self,game):
        self.game=game
        self.lock=False
        self.value=game.Decimal(self.game.Save.total_count[0],self.game.Save.total_count[1],game)
        self.first_e10=False
        self.first_e50=False
        self.first_inf=False

    def place(self):
        self.line=self.game.main_canvas.create_line(self.game.geometry[0],180,0,180,width=2,fill='#ad0000')
        self.line_2 = self.game.main_canvas.create_line(self.game.geometry[0], 10, 0, 10, width=2, fill='#ad0000')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]//2,60,anchor='center',text=self.value.get(2,4),fill='#a9cf9b',font=('bahnschrift',26))
        self.get_count(0)

    def get_count(self,count):
        if self.lock==False:
            self.value+=count
            self.game.Infinity.conf_upgrades('VALUE')
            self.check()

    def check(self):
            self.game.main_canvas.itemconfigure(self.text,fill='#a9cf9b', text=self.value.get(2,4))
            if self.value>1e10 and self.first_e10==False or self.game.CB.amount>0 and self.first_e10==False or self.game.TA.amount>0 and self.first_e10==False or self.first_inf and self.first_e10==False:
                self.first_e10=True
                self.game.CB.place()
            if self.value > 1e50 and self.first_e50 == False or self.game.TA.amount>0 and self.first_e50==False or self.first_inf and self.first_e50==False:
                self.first_e50 = True
                self.game.TA.place()
            if self.value>=1.8e308 and self.first_inf==False or self.game.Infinity.first and self.first_inf==False:
                self.first_inf=True
                self.game.Infinity.place()
            if self.value >= 1.8e308 and (self.game.Eternity.upgrades[2]=='N' or self.game.Aspects.active==True):
                self.lock=True

    def Illusion(self):
        if self.game.Aspects.active:
            self.game.main_canvas.itemconfigure(self.text,text='Illusion',fill='#93d9d9')
            self.game.window.after(610,self.Illusion)



    def reset(self):
        self.lock=False
        if self.game.Infinity.upgrades[2]=='Y' and not (self.game.Aspects.active==True and (self.game.Aspects.cur_ill==1 or self.game.Aspects.cur_ill==4 or self.game.Aspects.cur_ill==3)):
            self.value = self.value=self.game.Decimal(1,5,self.game)
        else:
            self.value = self.value=self.game.Decimal(1,2,self.game)
        self.game.main_canvas.itemconfigure(self.text, text=self.value.get(1,4))