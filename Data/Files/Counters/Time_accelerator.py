from decimal import Decimal

class Time_accelerator:
    def __init__(self,game):
        self.game=game
        self.amount=int(self.game.Save.TA_data[0][0])
        self.accel=float(self.game.Save.TA_data[0][1])
        self.upper=float(self.game.Save.TA_data[0][2])
        self.cost=float(self.game.Save.TA_data[0][3])
        self.cost_up=1e75
    def place(self):
        self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 320, 86,
                                                      anchor='center', text='Time accelerator: ' + str(self.amount),
                                                      fill='#410eb0',
                                                      font=('bahnschrift', 14))
        self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 240, 110,
                                                              self.game.geometry[0] // 2 + 400, 170, width=1,
                                                              fill='black', outline='#4002c4')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 320, 140,
                                                          anchor='center', justify='center', text='Cost: ' + str(
                "{:.2e}".format(Decimal(self.cost))) + '\nBoost counters speed\nupgrades (*1.03)', fill='#4d00b3',
                                                          font=('bahnschrift', 10))
    def buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock:
            if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
                self.spare_time_mult+=0.1
                self.amount += 1
                self.cost = self.cost * self.cost_up
                self.game.main_canvas.itemconfigure(self.text, text='Time chargers: ' + str(self.amount),
                                                    fill='#91fc60')
                if self.amount<5:
                    self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                        "{:.2e}".format(Decimal(self.cost))) + '\nProduce extra time', fill='#91fc60')
                else:
                    self.cost=1.8e308
                    self.game.main_canvas.itemconfigure(self.text_buy, text='No more charge\nProduce extra time', fill='#91fc60')
                self.game.main_canvas.itemconfigure(self.box_buy, fill='#63a682')
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
                self.game.main_canvas.itemconfigure(self.text, text='Time accelerators: ' + str(self.amount))
                self.accel*=self.upper
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost))) + '\nBoost counters speed\nupgrades (*1.03)')
            self.game.TA_reset()

    def reset(self):
        self.amount = 0
        self.accel = 1.00
        self.upper = 1.03
        self.cost = 1e50
        self.cost_up = 1e75
        if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
            self.cost = 1e20
            self.cost_up = 1e15
            try:
                if self.spare_time>0:
                    pass
            except:
                self.spare_time=1
            self.spare_time_mult=0.2
            self.game.main_canvas.itemconfigure(self.text, text='Time chargers: ' + str(self.amount), fill='#91fc60')
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                "{:.2e}".format(Decimal(self.cost))) + '\nProduce extra time', fill='#91fc60')
            self.game.main_canvas.itemconfigure(self.box_buy,fill='#63a682')
        else:
            self.game.main_canvas.itemconfigure(self.box_buy, fill='black')
            self.game.main_canvas.itemconfigure(self.text, text='Time accelerators: ' + str(self.amount),fill='#410eb0')
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                "{:.2e}".format(Decimal(self.cost))) + '\nBoost counters speed\nupgrades (*1.03)', fill='#4d00b3')

    def get_save(self):
        data=''
        data+=str(self.amount)+','+str(self.accel)+','+str(self.upper)+','+str(self.cost)+'\n'
        return data