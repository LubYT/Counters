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
                "{:.2e}".format(Decimal(self.cost))) + '\nBoost game speed\nupgrades (*1.03)', fill='#4d00b3',
                                                          font=('bahnschrift', 10))
    def buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock:
            self.game.Value.value -= self.cost
            self.cost = self.cost * self.cost_up
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(9)
                if self.amount>=4:
                    self.game.Achievements.get_achieve(12)
            self.amount+=1
            self.game.main_canvas.itemconfigure(self.text, text='Time accelerators: ' + str(self.amount))
            self.accel*=self.upper
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost))) + '\nBoost game speed\nupgrades (*1.03)')
            self.game.TA_reset()

    def reset(self):
        self.amount = 0
        self.accel = 1.00
        self.upper = 1.03
        self.cost = 1e50
        self.cost_up = 1e75
        self.game.main_canvas.itemconfigure(self.text, text='Time accelerators: ' + str(self.amount))
        self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
            "{:.2e}".format(Decimal(self.cost))) + '\nBoost game speed\nupgrades (*1.03)')

    def get_save(self):
        data=''
        data+=str(self.amount)+','+str(self.accel)+','+str(self.upper)+','+str(self.cost)+'\n'
        return data