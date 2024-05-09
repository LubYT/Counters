from decimal import Decimal

class Counter3:
    def __init__(self,game):
        self.game=game
        self.count = float(self.game.Save.counters_data[2][0])
        self.multi = float(self.game.Save.counters_data[2][1])
        self.cost = float(self.game.Save.counters_data[2][2])
        self.cost_up=1e5
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[2][3])
        self.placed = False

    def place(self):
        self.placed = True
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,330,self.game.geometry[0]-(self.game.geometry[0]-60),400,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),360,anchor='w',text=str(self.count),fill='#c22f40',font=('bahnschrift',24))
        if self.multi * self.game.CB.multi_list[2] < 1000:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),
                                                                385,
                                                                anchor='w',
                                                                text='x' + str(self.multi * self.game.CB.multi_list[2]*self.game.Infinity.get_boost()),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        else:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),
                                                                385,
                                                                anchor='w',
                                                                text='x' + str("{:.2e}".format(
                                                                    Decimal(self.multi * self.game.CB.multi_list[2]*self.game.Infinity.get_boost()))),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,340,self.game.geometry[0]-270,390,width=2,fill='#63855a',outline='#95db84')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 365,
                                                            anchor='w', text='Cost: ' + str(self.cost), fill='#61c449',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 340,
                                                                  self.game.geometry[0] - 340, 390, width=2,
                                                                  fill='#63855a',
                                                                  outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 365,
                                                              anchor='center', text='Max', fill='#61c449',
                                                              font=('bahnschrift', 16))
        if self.game.Infinity.first:
            self.return_place()
        if self.first:
            self.game.Counter_4.place()
    def produce(self):
        if self.game.Counter_2.first:
            self.produce_count=(self.produce_base*self.count*self.multi*self.game.Tickspeed.tickspeed*self.game.CB.multi_list[2]
                                *self.game.Infinity.get_boost()/25)
            self.game.Counter_2.get_count(self.produce_count)

    def return_place(self):
        if self.placed and self.game.Menu.curMenu=='Counters':
            self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),360)
            self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),385)
            self.game.main_canvas.coords(self.box,self.game.geometry[0] - 60, 330, self.game.geometry[0] - (self.game.geometry[0] - 130), 400)
            self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-70,340,self.game.geometry[0]-270,390)
            self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-265, 365)
            self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 280, 340,
                                                                  self.game.geometry[0] - 340, 390)
            self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 310, 365)
            self.conf_cur()
        elif self.placed and self.game.Menu.curMenu != 'Counters':
            self.hide()

    def hide(self):
        if self.placed:
            self.game.main_canvas.coords(self.text, -999,-999)
            self.game.main_canvas.coords(self.text_multi, -999,-999)
            self.game.main_canvas.coords(self.box, -999,-999, -999,-999)
            self.game.main_canvas.coords(self.box_buy, -999,-999, -999,-999)
            self.game.main_canvas.coords(self.text_buy, -999,-999)
            self.game.main_canvas.coords(self.box_buy_max, -999,-999, -999,-999)
            self.game.main_canvas.coords(self.text_buy_max, -999,-999)

    def reset(self):
        if self.placed:
            self.game.main_canvas.delete(self.box),self.game.main_canvas.delete(self.text),self.game.main_canvas.delete(self.text_multi)
            self.game.main_canvas.delete(self.box_buy),self.game.main_canvas.delete(self.text_buy)
            self.game.main_canvas.delete(self.box_buy_max), self.game.main_canvas.delete(self.text_buy_max)
        self.count = 0
        self.multi = 1
        self.produce_base = 1
        self.cost = 1000
        self.cost_up = 10000
        self.first=False
    def buy(self):
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                self.game.Counter_4.place()
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
                self.game.Counter_4.place()
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

        if self.multi * self.game.CB.multi_list[2] * self.game.Infinity.get_boost() > 1000:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                "{:.2e}".format(Decimal(self.multi * self.game.CB.multi_list[2] * self.game.Infinity.get_boost()))))
        elif self.multi * self.game.CB.multi_list[2] * self.game.Infinity.get_boost() < 1:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#454443', text='x' + str(
                round(self.multi * self.game.CB.multi_list[2] * self.game.Infinity.get_boost(), 3)))
        else:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                round(self.multi * self.game.CB.multi_list[2] * self.game.Infinity.get_boost(), 1)))

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