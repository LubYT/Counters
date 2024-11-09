from decimal import Decimal

class Time_accelerator:
    def __init__(self,game):
        self.game=game
        self.amount=self.game.Decimal(self.game.Save.TA_data[0][0][0],self.game.Save.TA_data[0][0][1],self.game)
        self.accel=self.game.Decimal(self.game.Save.TA_data[0][1][0],self.game.Save.TA_data[0][1][1],self.game)
        print(self.accel.get(2,4))
        self.upper=self.game.Decimal(self.game.Save.TA_data[0][2][0],self.game.Save.TA_data[0][2][1],self.game)
        self.cost=self.game.Decimal(self.game.Save.TA_data[0][3][0],self.game.Save.TA_data[0][3][1],self.game)
        self.cost_up=self.game.Decimal(1,75,self.game)
        self.max_amount=self.game.Decimal(self.game.Save.TA_data[0][4][0],self.game.Save.TA_data[0][4][1],self.game)
        if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
            self.spare_time = float(self.game.Save.Aspect_data[4][0])
            self.spare_time_mult = float(self.game.Save.Aspect_data[4][1])
        else:
            self.spare_time = 1
            self.spare_time_mult = 0.2
    def place(self):
        self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 320, 86,
                                                      anchor='center', text='Time accelerator: ' + self.amount.get('2',4),
                                                      fill='#410eb0',
                                                      font=('bahnschrift', 14))
        self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 240, 110,
                                                              self.game.geometry[0] // 2 + 400, 170, width=1,
                                                              fill='black', outline='#4002c4')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 320, 140,
                                                          anchor='center', justify='center', text='Cost: ' + self.cost.get(2,4) + '\nBoost counters speed\nupgrades (*1.03)', fill='#4d00b3',
                                                          font=('bahnschrift', 10))
        self.conf()
    def buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock and self.amount<self.max_amount:
            if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4 and self.amount<5:
                self.spare_time_mult+=0.1
                self.amount += 1
                self.cost = self.cost * self.cost_up
            else:
                self.game.Value.value -= self.cost
                self.cost = self.cost * self.cost_up
                print(self.game.Infinity.first)
                if self.game.Infinity.first:
                    print('hi')
                    self.game.Achievements.get_achieve(9)
                    if self.amount>=3:
                        self.game.Achievements.get_achieve(12)
                self.amount+=1
                self.accel *= self.upper
            self.conf()
            self.game.TA_reset()

    def conf(self):
        if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
            self.game.main_canvas.itemconfigure(self.text, text='Time chargers: ' + self.amount.get('2', 4),
                                                fill='#91fc60')
            if self.amount < 5:
                self.game.main_canvas.itemconfigure(self.text_buy,
                                                    text='Cost: ' + self.cost.get(2, 4) + '\nProduce extra time',
                                                    fill='#91fc60')
            else:
                self.game.main_canvas.itemconfigure(self.text_buy, text='No more charge\nProduce extra time',
                                                    fill='#91fc60')
            self.game.main_canvas.itemconfigure(self.box_buy, fill='#63a682')
        else:
            self.game.main_canvas.itemconfigure(self.text, text='Time accelerators: ' + self.amount.get('2', 4),fill='#410eb0')
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.cost.get(2,4) + '\nBoost counters speed\nupgrades (*1.03)',fill='#4d00b3')
            self.game.main_canvas.itemconfigure(self.box_buy, fill='black')
            if self.max_amount <= self.amount:
                self.game.main_canvas.itemconfigure(self.text_buy, text='Limited by Eternity')

    def reset(self):
        self.amount = self.game.Decimal(0,0,self.game)
        self.accel = self.game.Decimal(1.00,0,self.game)
        self.upper = self.game.Decimal(1.03,0,self.game)
        self.cost = self.game.Decimal(1,50,self.game)
        self.cost_up = self.game.Decimal(1,75,self.game)
        if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
            self.cost = self.game.Decimal(1,20,self.game)
            self.cost_up = self.game.Decimal(1,15,self.game)
            try:
                if self.spare_time>0:
                    pass
            except:
                self.spare_time=1
            self.spare_time_mult=0.2
        self.conf()

    def get_save(self):
        data=''
        data+=str(self.amount.get_save())+','+str(self.accel.get_save())+','+str(self.upper.get_save())+','+str(self.cost.get_save())+','+str(self.max_amount.get_save())+'\n'
        return data