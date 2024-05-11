from decimal import Decimal

class Tickspeed:

    def __init__(self,game):
        self.game=game
        self.tickspeed=float(self.game.Save.TS_data[0][0])
        self.tickspeed_upper=float(self.game.Save.TS_data[0][1])
        self.cost=int(self.game.Save.TS_data[0][2])
        self.cost_up=10

    def place(self):
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]//2,120,anchor='center',text='Game speed: '+str(self.tickspeed),fill='#c22f40',font=('bahnschrift',10))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]//2-100,130,self.game.geometry[0]//2+100,170,width=1,fill='black',outline='#c22f40')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]//2, 150,
                                                            anchor='center',justify='center', text='Cost: ' + str(self.cost)+'\n'+'Game speed * '+str(round(self.tickspeed_upper+(self.game.TA.accel-1),2)), fill='#61c449',
                                                            font=('bahnschrift', 12))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 120, 130,
                                                              self.game.geometry[0] // 2 + 170, 170, width=1,
                                                              fill='black', outline='#c22f40')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] //2 + 145, 150,
                                                          anchor='center', justify='center',
                                                          text='Max', fill='#61c449',
                                                          font=('bahnschrift', 12))
        self.conf()

    def get_boost(self,multi):
        self.tickspeed*=multi
        if self.tickspeed > 1e15:
            self.game.main_canvas.itemconfigure(self.text, text='Game speed is extremely altered: ' + str(
                "{:.2e}".format(Decimal(self.tickspeed))), fill='#31bcf7')
        elif self.tickspeed > 10000:
            self.game.main_canvas.itemconfigure(self.text, text='Game speed is massively altered: ' + str(
                "{:.2e}".format(Decimal(self.tickspeed))), fill='#5d2fc2')
        else:
            self.game.main_canvas.itemconfigure(self.text,
                                                text='Game speed is altered: ' + str(round(self.tickspeed, 3)),
                                                fill='#c22fa2')

    def reset(self):
        self.tickspeed = 1.000*self.game.Infinity.get_boost_1()*self.game.Achievements.achieve_mult('Time speed')
        self.tickspeed_upper=1.12
        self.cost = 10
        self.cost_up = 10
        self.game.main_canvas.itemconfigure(self.text,text='Game speed: '+str(self.tickspeed),fill='#c22f40')
        self.game.main_canvas.itemconfigure(self.text_buy,text='Cost: ' + str(self.cost)+'\n'+'Game speed * '+str(round(self.tickspeed_upper+(self.game.TA.accel-1),2)))

    def buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock:
            self.game.Value.value -= self.cost
            self.cost = self.cost * self.cost_up
            self.tickspeed=self.tickspeed*(self.tickspeed_upper+(self.game.TA.accel-1))
            self.conf()
    def max_buy(self):
        while self.game.Value.value >= self.cost and not self.game.Value.lock:
            self.game.Value.value -= self.cost
            self.cost = self.cost * self.cost_up
            self.tickspeed=self.tickspeed*(self.tickspeed_upper+(self.game.TA.accel-1))
            self.conf()

    def conf(self):
        if self.tickspeed > 1e15:
            self.game.main_canvas.itemconfigure(self.text, text='Game speed is extremely altered: ' + str(
                "{:.2e}".format(Decimal(self.tickspeed))), fill='#31bcf7')
        elif self.tickspeed > 10000:
            self.game.main_canvas.itemconfigure(self.text, text='Game speed is massively altered: ' + str(
                "{:.2e}".format(Decimal(self.tickspeed))), fill='#5d2fc2')
        elif self.tickspeed ==1:
            self.game.main_canvas.itemconfigure(self.text, text='Game speed: ' + str(self.tickspeed), fill='#c22f40')
        else:
            self.game.main_canvas.itemconfigure(self.text,
                                                text='Game speed is altered: ' + str(round(self.tickspeed, 3)),
                                                fill='#c22fa2')
        if self.cost > 9999:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                "{:.2e}".format(Decimal(self.cost))) + '\n' + 'Game speed * ' + str(
                round(self.tickspeed_upper + (self.game.TA.accel - 1), 2)))
        else:
            self.game.main_canvas.itemconfigure(self.text_buy,
                                                text='Cost: ' + str(round(self.cost, 1)) + '\n' + 'Game speed * ' + str(
                                                    round(self.tickspeed_upper + (self.game.TA.accel - 1), 2)))

    def get_save(self):
        data=''
        data+=str(self.tickspeed)+','+str(self.tickspeed_upper)+','+str(self.cost)+'\n'
        return data