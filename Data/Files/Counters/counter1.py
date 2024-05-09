from decimal import Decimal
class Counter1:
    def __init__(self,game):
        self.game=game
        self.count=float(self.game.Save.counters_data[0][0])
        self.multi=float(self.game.Save.counters_data[0][1])
        self.cost=float(self.game.Save.counters_data[0][2])
        self.cost_up=100
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[0][3])

    def place(self):
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,170,self.game.geometry[0]-(self.game.geometry[0]-60),240,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),200,anchor='w',text=str(self.count),fill='#c22f40',font=('bahnschrift',24))
        if self.multi * self.game.CB.multi_list[0]*self.game.Infinity.get_boost('1 counter') < 1000:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83), 225,
                                                          anchor='w', text='x'+str(self.multi*self.game.CB.multi_list[0]*self.game.Infinity.get_boost('1 counter')), fill='#61c449',
                                                          font=('bahnschrift', 12))
        else:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),225,
                                                                anchor='w',
                                                                text='x'+str("{:.2e}".format(Decimal(self.multi*self.game.CB.multi_list[0]*self.game.Infinity.get_boost('1 counter')))),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,180,self.game.geometry[0]-270,230,width=2,fill='#63855a',outline='#95db84')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 205,
                                                            anchor='w', text='Cost: ' + str(self.cost), fill='#61c449',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 180,
                                                              self.game.geometry[0] - 340, 230, width=2, fill='#63855a',
                                                              outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 205,
                                                          anchor='center', text='Max', fill='#61c449',
                                                          font=('bahnschrift', 16))
        if self.first:
            self.game.Counter_2.place()
    def produce(self):
        self.produce_count_PS=(self.produce_base*self.count*self.multi*self.game.Tickspeed.tickspeed*self.game.CB.multi_list[0]
                               *self.game.Infinity.get_boost('1 counter'))
        self.produce_count=(self.produce_base*self.count*self.multi*self.game.Tickspeed.tickspeed*self.game.CB.multi_list[0]
                            *self.game.Infinity.get_boost('1 counter')/25)
        if self.game.Aspects.active_1st:
            self.produce_count=self.produce_count**0.625
            self.produce_count_PS = self.produce_count * 25
            self.game.Value_PS.conf(self.produce_count_PS,'Aspect 1')
        else:
            self.game.Value_PS.conf(self.produce_count_PS)
        self.game.Value.get_count(self.produce_count)

    def reset(self):
        self.count = 0
        self.multi = 1
        self.cost = 10
        self.cost_up = 100
        self.produce_base = 1
        self.first = False
        self.conf()

    def return_place(self):
        self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),200)
        self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),225)
        self.game.main_canvas.coords(self.box,self.game.geometry[0] - 60, 170, self.game.geometry[0] - (self.game.geometry[0] - 130), 240)
        self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-70,180,self.game.geometry[0]-270,230)
        self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-265, 205)
        self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 280, 180,
                                                              self.game.geometry[0] - 340, 230)
        self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 310, 205)
        self.conf_cur()

    def hide(self):
        self.game.main_canvas.coords(self.text, -999,-999)
        self.game.main_canvas.coords(self.text_multi, -999,-999)
        self.game.main_canvas.coords(self.box, -999,-999, -999,-999)
        self.game.main_canvas.coords(self.box_buy, -999,-999, -999,-999)
        self.game.main_canvas.coords(self.text_buy, -999,-999)
        self.game.main_canvas.coords(self.box_buy_max, -999,-999, -999,-999)
        self.game.main_canvas.coords(self.text_buy_max, -999,-999)
    def buy(self):
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                self.game.Counter_2.place()
            else:
                self.multi = self.multi * 2
            self.game.Value.value-=self.cost
            self.cost=self.cost*self.cost_up
            self.count+=1
            self.conf()

    def buy_max(self):
        while self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                self.game.Counter_2.place()
            else:
                self.multi = self.multi * 2
            self.game.Value.value-=self.cost
            self.cost=self.cost*self.cost_up
            self.count+=1
            self.conf()

    def conf_cur(self):
        if self.first==False:
            self.conf()
            self.game.main_canvas.after(100,self.conf_cur)

    def get_count(self,count):
        self.count+=count
        self.conf()

    def conf(self):

        if self.multi * self.game.CB.multi_list[0] * self.game.Infinity.get_boost('1 counter') > 1000:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                "{:.2e}".format(Decimal(self.multi * self.game.CB.multi_list[0] * self.game.Infinity.get_boost('1 counter')))))
        elif self.multi * self.game.CB.multi_list[0] * self.game.Infinity.get_boost('1 counter') < 1:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#454443', text='x' + str(
                round(self.multi * self.game.CB.multi_list[0] * self.game.Infinity.get_boost('1 counter'), 3)))
        else:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                round(self.multi * self.game.CB.multi_list[0] * self.game.Infinity.get_boost('1 counter'), 1)))

        if self.count>10000:
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