from decimal import Decimal
class Counter_boost:
    def __init__(self,game):
        self.game=game
        self.multi_list=self.game.Save.CB_data[0][3]
        self.amount=self.game.Decimal(self.game.Save.CB_data[0][0][0],self.game.Save.CB_data[0][0][1],self.game)
        self.cost=self.game.Decimal(self.game.Save.CB_data[0][1][0],self.game.Save.CB_data[0][1][1],self.game)
        self.up_cost=self.game.Decimal(self.game.Save.CB_data[0][2][0],self.game.Save.CB_data[0][2][1],self.game)
        self.boost=2
        self.up_cost_up=1e4
    def place(self):
        self.text = self.game.main_canvas.create_text(self.game.geometry[0]//2-320, 86,
                                                      anchor='center', text='Counter boosts: '+self.amount.get('2',4), fill='#5eadbf',
                                                      font=('bahnschrift', 14))
        self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0]//2-240, 110,
                                                              self.game.geometry[0]//2-400, 170,width=1,fill='black',outline='#3e75b3')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]//2-320, 140,
                                                          anchor='center',justify='center', text='Cost: ' + self.cost.get(2,4)+'\nUnlock 5th CNTR\nx2 to 1 CNTR', fill='#3b6ba3',
                                                          font=('bahnschrift', 10))
        self.conf_text()
    def buy(self,*args,limit=1.79e308):
        if self.game.Eternity.upgrades[4]=='N' or 'self' in args:
            if self.game.Value.value >= self.cost and not self.game.Value.lock and self.amount<limit:
                self.game.Value.value -= self.cost
                if not (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                    self.cost = self.cost * self.up_cost
                    print(self.up_cost)
                    self.up_cost *=self.up_cost_up
                    if self.up_cost>1e30:
                        self.up_cost=self.game.Decimal(1,30,self.game)
                    print(self.up_cost)
                else:
                    self.cost = self.cost * self.up_cost
                    self.up_cost = self.up_cost * self.up_cost_up
                    if self.up_cost > 1e10:
                        self.up_cost=self.game.Decimal(1,10,self.game)
                boost=self.boost
                if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                    boost*=2
                self.amount+=1
                self.game.main_canvas.itemconfigure(self.text, text='Counter boosts: '+self.amount.get('2',4))
                if self.amount>=1:
                    self.multi_list[0]*=boost
                if self.amount>=2:
                    self.multi_list[1] *= boost
                if self.amount>=3:
                    self.multi_list[2] *= boost
                if self.amount>=4:
                    self.multi_list[3] *= boost
                if self.amount>=5:
                    self.multi_list[4] *= boost
                if self.amount >= 6:
                    self.multi_list[5] *= boost
                if self.amount >= 7:
                    self.multi_list[6] *= boost
                if self.amount >= 8:
                    self.multi_list[7] *= boost
                if not 'self' in args:
                    self.game.CB_reset()
                self.conf_text()
        else:
            reset=False
            while self.amount<=8 and self.game.Value.value >= self.cost and not self.game.Value.lock and self.amount<limit:
                reset=True
                self.buy('self')
            if self.amount>=8:
                if self.game.Value.value >= self.cost and not self.game.Value.lock and self.amount<limit:
                    times=int((self.game.Value.value.log()-self.cost.log())/self.up_cost.log())
                    am=self.game.Decimal(self.amount.num,self.amount.e,self.game)
                    if am+times>limit:
                        am = self.game.Decimal(self.amount.num, self.amount.e, self.game)
                        times=int(limit-am)
                    cost=self.game.Decimal(self.cost.num,self.cost.e,self.game)
                    cost_up = self.game.Decimal(self.up_cost.num, self.up_cost.e, self.game)
                    cost_up2 = self.game.Decimal(self.up_cost.num, self.up_cost.e, self.game)
                    self.game.Value.value -= (cost*(cost_up**times-1))/(cost_up2-1)
                    boost = self.boost**times
                    cost_up = self.game.Decimal(self.up_cost.num, self.up_cost.e, self.game)
                    self.cost *=cost_up**times
                    if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                        boost *= 2
                    self.amount += times
                    for mult in self.multi_list:
                        mult*=boost
                    self.game.main_canvas.itemconfigure(self.text, text='Counter boosts: ' + self.amount.get('2', 4))
                    self.buy('self')
                    reset = True
            if reset:
                self.game.CB_reset()
                self.conf_text()

    def conf_text(self):
        boost=self.boost
        if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
            boost *= 2
        self.game.main_canvas.itemconfigure(self.text, text='Counter boosts: ' + self.amount.get('2', 4))
        print(self.amount>=1 and self.amount<2)
        if self.amount >= 0 and self.amount<1:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nUnlock 5th CNTR\nx'+str(boost)+' to 1 CNTR')
        elif self.amount >= 1 and self.amount<2:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nUnlock 6th CNTR\nx'+str(boost)+' to 1-2 CNTR')
        elif self.amount >= 2 and self.amount<3:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nUnlock 7th CNTR\nx'+str(boost)+' to 1-3 CNTR')
        elif self.amount >= 3 and self.amount<4:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nUnlock 8th CNTR\nx'+str(boost)+' to 1-4 CNTR')
        elif self.amount >= 4 and self.amount<5:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nx'+str(boost)+' to 1-5 CNTR')
        elif self.amount >= 5 and self.amount<6:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nx'+str(boost)+' to 1-6 CNTR')
        elif self.amount >= 6 and self.amount<7:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nx'+str(boost)+' to 1-7 CNTR')
        elif self.amount >= 7:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nx'+str(boost)+' to 1-8 CNTR')
    def reset(self):
        self.multi_list = [self.game.Decimal(1,0,self.game), self.game.Decimal(1,0,self.game),
                           self.game.Decimal(1,0,self.game), self.game.Decimal(1,0,self.game),
                           self.game.Decimal(1,0,self.game), self.game.Decimal(1,0,self.game),
                           self.game.Decimal(1,0,self.game), self.game.Decimal(1,0,self.game)]
        self.amount = self.game.Decimal(0,0,self.game)
        if not (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
            self.cost = self.game.Decimal(1,10,self.game)
            self.up_cost = self.game.Decimal(1,6,self.game)
            self.up_cost_up = self.game.Decimal(1,4,self.game)
        else:
            self.cost=self.game.Decimal(1,6,self.game)
            self.up_cost=self.game.Decimal(1,4,self.game)
            self.up_cost_up=self.game.Decimal(1,2,self.game)
        self.conf_text()

    def get_save(self):
        data=''
        data+=(str(self.amount.get_save())+','+str(self.cost.get_save())+','+str(self.up_cost.get_save())+',[')
        for i in self.multi_list:
            data+=i.get_save()+','
        data+=']'+'\n'
        return data
