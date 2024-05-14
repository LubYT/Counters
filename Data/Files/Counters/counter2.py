from decimal import Decimal
import math
class Counter2:
    def __init__(self,game):
        self.game=game
        self.count = float(self.game.Save.counters_data[1][0])
        self.multi = float(self.game.Save.counters_data[1][1])
        self.cost = float(self.game.Save.counters_data[1][2])
        self.cost_up=1000
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[1][3])
        self.placed = False

    def place(self):
        self.placed = True
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,280,self.game.geometry[0]-(self.game.geometry[0]-60),350,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),310,anchor='w',text=str(self.count),fill='#c22f40',font=('bahnschrift',24))
        if self.multi * self.game.CB.multi_list[1]*self.game.Achievements.achieve_mult('2 Counter') < 1000:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),
                                                                335,
                                                                anchor='w',
                                                                text='x' + str(self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1]*self.game.Infinity.get_boost()),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        else:
            self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83),
                                                                335,
                                                                anchor='w',
                                                                text='x' + str("{:.2e}".format(
                                                                    Decimal(self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1]*self.game.Infinity.get_boost()))),
                                                                fill='#61c449',
                                                                font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,290,self.game.geometry[0]-270,340,width=2,fill='black',outline='#95db84')
        self.box_1_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 71, 291,
                                                                self.game.geometry[0] - 269, 339, width=0,
                                                                fill='#63855a')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 315,
                                                            anchor='w', text='Cost: ' + str(self.cost), fill='#e0d900',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 290,
                                                                  self.game.geometry[0] - 340, 340, width=2,
                                                                  fill='#63855a',
                                                                  outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 315,
                                                              anchor='center', text='Max', fill='#61c449',
                                                              font=('bahnschrift', 16))
        if self.game.Infinity.first:
            self.return_place()
        if self.first:
            self.game.Counter_3.place()
    def produce(self):
        if self.game.Counter_1.first:
            self.produce_count=(self.produce_base*self.count*self.multi*self.game.Tickspeed.tickspeed*self.game.Achievements.achieve_mult('2 Counter')*self.game.CB.multi_list[1]
                                *self.game.Infinity.get_boost()/25)
            self.game.Counter_1.get_count(self.produce_count)

    def reset(self):
        if self.placed:
            self.game.main_canvas.delete(self.box),self.game.main_canvas.delete(self.text),self.game.main_canvas.delete(self.text_multi)
            self.game.main_canvas.delete(self.box_buy),self.game.main_canvas.delete(self.text_buy),self.game.main_canvas.delete(self.box_1_buy)
            self.game.main_canvas.delete(self.box_buy_max), self.game.main_canvas.delete(self.text_buy_max)
        self.count = 0
        self.produce_base = 1
        self.multi = 1
        self.cost = 100
        self.cost_up = 1000
        self.first=False
        self.placed = False

    def return_place(self):
        if self.placed and self.game.Menu.curMenu=='Counters':
            self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),310)
            self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),335)
            self.game.main_canvas.coords(self.box,self.game.geometry[0] - 130, 280, self.game.geometry[0] - (self.game.geometry[0] - 130), 350)
            self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-140,290,self.game.geometry[0]-340,340)
            self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141, 291, self.game.geometry[0] - 339,
                                         339)
            self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-335, 315)
            self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 350, 290,
                                                                  self.game.geometry[0] - 410, 340)
            self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 380, 315)
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

    def conf_cur(self):
        if self.first==False:
            self.conf()
            self.game.main_canvas.after(100,self.conf_cur)

    def buy(self):
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                self.game.Counter_3.place()
            else:
                self.multi = self.multi * 2
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(2)
            self.game.Value.value-=self.cost
            self.cost=self.cost*self.cost_up
            self.count+=1
            self.conf()

    def buy_max(self):
        while self.game.Value.value >= self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                self.game.Counter_3.place()
            else:
                self.multi = self.multi * 2
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(2)
            self.game.Value.value -= self.cost
            self.cost = self.cost * self.cost_up
            self.count += 1
        self.conf()

    def get_count(self,count):
        self.count+=count
        self.conf()

    def conf(self):

        if self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1] * self.game.Infinity.get_boost() > 1000:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                "{:.2e}".format(Decimal(self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1] * self.game.Infinity.get_boost()))))
        elif self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1] * self.game.Infinity.get_boost() < 1:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#454443', text='x' + str(
                round(self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1] * self.game.Infinity.get_boost(), 3)))
        else:
            self.game.main_canvas.itemconfigure(self.text_multi, fill='#61c449', text='x' + str(
                round(self.multi*self.game.Achievements.achieve_mult('2 Counter') * self.game.CB.multi_list[1] * self.game.Infinity.get_boost(), 1)))

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
            if self.game.Infinity.first:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141-(198*coords_mult), 291, self.game.geometry[0] - 339, 339)
            else:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 71 - (198 * coords_mult), 291,
                                             self.game.geometry[0] - 269, 339)

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