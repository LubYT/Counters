from decimal import Decimal
class Counter_boost:
    def __init__(self,game):
        self.game=game
        self.multi_list=self.game.Save.CB_data[0][3]
        self.amount=int(self.game.Save.CB_data[0][0])
        self.cost=float(self.game.Save.CB_data[0][1])
        self.up_cost=float(self.game.Save.CB_data[0][2])
        print(self.multi_list)
        self.up_cost_up=1e4
    def place(self):
        self.text = self.game.main_canvas.create_text(self.game.geometry[0]//2-320, 56,
                                                      anchor='center', text='Counter boosts: '+str(self.amount), fill='#5eadbf',
                                                      font=('bahnschrift', 14))
        self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0]//2-240, 80,
                                                              self.game.geometry[0]//2-400, 140,width=1,fill='black',outline='#3e75b3')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]//2-320, 110,
                                                          anchor='center',justify='center', text='Cost: ' + str("{:.2e}".format(Decimal(self.cost)))+'\nUnlock 5th CNTR\nx2 to 1 CNTR', fill='#3b6ba3',
                                                          font=('bahnschrift', 10))
    def buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock:
            self.game.Value.value -= self.cost
            self.cost = self.cost * self.up_cost
            self.up_cost = self.up_cost*self.up_cost_up
            if self.up_cost>1e30:
                self.up_cost=1e30
            self.amount+=1
            self.game.main_canvas.itemconfigure(self.text, text='Counter boosts: '+str(self.amount))
            if self.amount==1:
                self.multi_list[0]*=2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost)))+'\nUnlock 6th CNTR\nx2 to 1-2 CNTR')
            if self.amount==2:
                self.multi_list[0]*=2
                self.multi_list[1] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost)))+'\nUnlock 7th CNTR\nx2 to 1-3 CNTR')
            if self.amount==3:
                self.multi_list[0]*=2
                self.multi_list[1] *= 2
                self.multi_list[2] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost)))+'\nUnlock 8th CNTR\nx2 to 1-4 CNTR')
            if self.amount==4:
                self.multi_list[0]*=2
                self.multi_list[1] *= 2
                self.multi_list[2] *= 2
                self.multi_list[3] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost)))+'\nx2 to 1-5 CNTR')
            if self.amount==5:
                self.multi_list[0]*=2
                self.multi_list[1] *= 2
                self.multi_list[2] *= 2
                self.multi_list[3] *= 2
                self.multi_list[4] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost)))+'\nx2 to 1-6 CNTR')
            if self.amount == 6:
                self.multi_list[0] *= 2
                self.multi_list[1] *= 2
                self.multi_list[2] *= 2
                self.multi_list[3] *= 2
                self.multi_list[4] *= 2
                self.multi_list[5] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                    "{:.2e}".format(Decimal(self.cost))) + '\nx2 to 1-7 CNTR')
            if self.amount == 7:
                self.multi_list[0] *= 2
                self.multi_list[1] *= 2
                self.multi_list[2] *= 2
                self.multi_list[3] *= 2
                self.multi_list[4] *= 2
                self.multi_list[5] *= 2
                self.multi_list[6] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                    "{:.2e}".format(Decimal(self.cost))) + '\nx2 to 1-8 CNTR')
            if self.amount > 7:
                self.multi_list[0] *= 2
                self.multi_list[1] *= 2
                self.multi_list[2] *= 2
                self.multi_list[3] *= 2
                self.multi_list[4] *= 2
                self.multi_list[5] *= 2
                self.multi_list[6] *= 2
                self.multi_list[7] *= 2
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                    "{:.2e}".format(Decimal(self.cost))) + '\nx2 to 1-8 CNTR')
            self.game.CB_reset()

    def reset(self):
        self.multi_list = [1, 1, 1, 1, 1, 1, 1, 1]
        self.amount = 0
        self.cost = 1e10
        self.up_cost = 1e6
        self.up_cost_up = 1e4
        self.game.main_canvas.itemconfigure(self.text, text='Counter boosts: ' + str(self.amount))
        self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
            "{:.2e}".format(Decimal(self.cost))) + '\nUnlock 5th CNTR\nx2 to 1 CNTR')

    def get_save(self):
        data=''
        data+=str(self.amount)+','+str(self.cost)+','+str(self.up_cost)+','+str(self.multi_list)[:-1:]+',]'+'\n'
        return data
