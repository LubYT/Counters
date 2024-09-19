from decimal import Decimal
import math

class Counter6:
    def __init__(self,game):
        self.game=game
        self.count = float(self.game.Save.counters_data[5][0])
        self.multi = float(self.game.Save.counters_data[5][1])
        self.cost = float(self.game.Save.counters_data[5][2])
        self.cost_up=1e9
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[5][3])
        self.placed=False

    def place(self):
        self.placed = True
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,600,self.game.geometry[0]-(self.game.geometry[0]-60),670,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),630,anchor='w',text=str(self.count),fill='#c22f40',font=('bahnschrift',24))
        if self.multi * self.game.CB.multi_list[5]*self.game.Achievements.achieve_mult('6 Counter') < 1000:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),
                                                                655,
                                                                anchor='w',
                                                                text='x' + str(self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5]*self.game.Infinity.get_boost()),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        else:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),
                                                                655,
                                                                anchor='w',
                                                                text='x' + str("{:.2e}".format(
                                                                    Decimal(self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5]*self.game.Infinity.get_boost()))),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,610,self.game.geometry[0]-270,660,width=2,fill='black',outline='#95db84')
        self.box_1_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 71, 611,
                                                                self.game.geometry[0] - 269, 659, width=0,
                                                                fill='#63855a')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 635,
                                                            anchor='w', text='Cost: ' + str("{:.2e}".format(Decimal(self.cost))), fill='#e0d900',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 610,
                                                                  self.game.geometry[0] - 340, 660, width=2,
                                                                  fill='#63855a',
                                                                  outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 635,
                                                              anchor='center', text='Max', fill='#61c449',
                                                              font=('bahnschrift', 16))
        if self.game.Infinity.first:
            self.return_place()
        if self.first and self.game.CB.amount >= 3:
            self.game.Counter_7.place()
    def produce(self):
        if self.game.Counter_5.first:
            self.produce_count=(self.produce_base*self.count*self.multi*self.game.Achievements.achieve_mult('6 Counter')*self.game.Tickspeed.get_time()*self.game.CB.multi_list[5]
                                *self.game.Infinity.get_boost()/25)
            self.game.Counter_5.get_count(self.produce_count)

    def return_place(self):
        if self.placed and self.game.Menu.curMenu=='Counters':
            self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),630)
            self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),655)
            self.game.main_canvas.coords(self.box,self.game.geometry[0] - 130, 600, self.game.geometry[0] - (self.game.geometry[0] - 130), 670)
            self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-140,610,self.game.geometry[0]-340,660)
            self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-335, 635)
            self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 350, 610,
                                                                  self.game.geometry[0] - 410, 660)
            self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 380, 635)
            self.conf_cur()
        elif self.placed and self.game.Menu.curMenu != 'Counters':
            self.hide()

    def hide(self):
        if self.placed:
            self.game.main_canvas.coords(self.text, -999,-999)
            self.game.main_canvas.coords(self.text_multi, -999,-999)
            self.game.main_canvas.coords(self.box, -999,-999, -999,-999)
            self.game.main_canvas.coords(self.box_buy, -999,-999, -999,-999)
            self.game.main_canvas.coords(self.box_1_buy, -999, -999, -999, -999)
            self.game.main_canvas.coords(self.text_buy, -999,-999)
            self.game.main_canvas.coords(self.box_buy_max, -999,-999, -999,-999)
            self.game.main_canvas.coords(self.text_buy_max, -999,-999)

    def reset(self):
        if self.placed:
            self.game.main_canvas.delete(self.box),self.game.main_canvas.delete(self.text),self.game.main_canvas.delete(self.text_multi)
            self.game.main_canvas.delete(self.box_buy),self.game.main_canvas.delete(self.box_1_buy),self.game.main_canvas.delete(self.text_buy)
            self.game.main_canvas.delete(self.box_buy_max), self.game.main_canvas.delete(self.text_buy_max)
        self.count = 0
        self.produce_base = 1
        self.multi = 1
        self.cost = 1e12
        self.cost_up = 1e8
        self.first=False
        self.placed = False
    def conf_cur(self):
        if self.first==False or self.game.Counter_7.first==False:
            self.conf()
            self.game.main_canvas.after(100,self.conf_cur)

    def buy(self):
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                if self.game.CB.amount >= 3:
                    self.game.Counter_7.place()
            else:
                self.multi = self.multi * 2
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(6)
            self.game.Value.value-=self.cost
            self.cost=self.cost*self.cost_up
            if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                self.cost=self.cost**1.1
            self.count+=1
            self.conf()

    def buy_max(self):
        while self.game.Value.value>=self.cost and not self.game.Value.lock:
            self.buy()
    def get_count(self,count):
        self.count+=count
        self.conf()

    def conf(self):

        if self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5] * self.game.Infinity.get_boost() > 1000:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                "{:.2e}".format(Decimal(self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5] * self.game.Infinity.get_boost()))))
        elif self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5] * self.game.Infinity.get_boost() < 1:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#454443', text='x' + str(
                round(self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5] * self.game.Infinity.get_boost(), 3)))
        else:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                round(self.multi*self.game.Achievements.achieve_mult('6 Counter') * self.game.CB.multi_list[5] * self.game.Infinity.get_boost(), 1)))

        if self.game.Menu.curMenu=='Counters':
            try:
                log=math.log10(self.game.Value.value)
            except:
                log=1
            try:
                log_1=math.log10(self.cost)
            except:
                log_1=1
            try:
                log_2=math.log10(self.cost_up)
            except:
                log_2=1
            main_log=(log_1-log)/log_2
            if main_log<=0:
                self.game.main_canvas.itemconfigure(self.text_buy,fill='#61c449')
                coords_mult=0
            elif main_log>=1:
                self.game.main_canvas.itemconfigure(self.text_buy, fill='#9c3333')
                coords_mult=1
            else:
                self.game.main_canvas.itemconfigure(self.text_buy, fill='#9c3333')
                coords_mult=main_log
            if str(coords_mult)=='nan':
                coords_mult=0
            if self.game.Infinity.first:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141-(198*coords_mult), 611, self.game.geometry[0] - 339, 659)
            else:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 71 - (198 * coords_mult), 611,
                                             self.game.geometry[0] - 269, 659)

        if self.count > 10000:
            self.game.main_canvas.itemconfigure(self.text, text=str("{:.2e}".format(Decimal(self.count))))
        else:
            self.game.main_canvas.itemconfigure(self.text, text=str(round(self.count, 1)))

        if self.cost > 10000:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str("{:.2e}".format(Decimal(self.cost))))
        else:
            self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(round(self.cost, 1)))

    def get_save(self):
        data=''
        data+=str(self.count)+','+str(self.multi)+','+str(self.cost)+','
        if self.first==False:
            data+=''+'\n'
        else:
            data+='True\n'
        return data