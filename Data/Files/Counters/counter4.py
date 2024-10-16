from decimal import Decimal
import math

class Counter4:
    def __init__(self,game):
        self.game=game
        self.count = game.Decimal(self.game.Save.counters_data[3][0][0],self.game.Save.counters_data[3][0][1],game)
        self.multi = game.Decimal(self.game.Save.counters_data[3][1][0],self.game.Save.counters_data[3][1][1],game)
        self.cost = game.Decimal(self.game.Save.counters_data[3][2][0],self.game.Save.counters_data[3][2][1],game)
        self.cost_up=game.Decimal(1,5,game)
        self.cost_up_inf=8
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[3][3])
        self.placed = False

    def place(self):
        self.placed = True
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,440,self.game.geometry[0]-(self.game.geometry[0]-60),510,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),470,anchor='w',text=self.notation('total'),fill='#c22f40',font=('bahnschrift',24))
        self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83), 495,
                                                            anchor='w', text='x' + str(self.notation('x_val')),
                                                            fill=self.notation('color_x'),
                                                            font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,450,self.game.geometry[0]-270,500,width=2,fill='black',outline='#95db84')
        self.box_1_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 71, 451,
                                                                self.game.geometry[0] - 269, 499, width=0,
                                                                fill='#63855a')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 475,
                                                            anchor='w', text='Cost: ' + self.notation('cost'), fill='#e0d900',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 450,
                                                                  self.game.geometry[0] - 340, 500, width=2,
                                                                  fill='#63855a',
                                                                  outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 475,
                                                              anchor='center', text='Max', fill='#61c449',
                                                              font=('bahnschrift', 16))
        if self.game.Infinity.first:
            self.return_place()
        if self.first and self.game.CB.amount >= 1:
            self.game.Counter_5.place()
    def produce(self):
        if self.game.Counter_3.first:
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            self.produce_count=(mult*self.count*self.produce_base*self.game.Tickspeed.get_time()*self.game.Achievements.achieve_mult('4 Counter')*self.game.Eternity.time_speed*self.game.CB.multi_list[3]
                                *self.game.Infinity.get_boost()/25)
            self.game.Counter_3.get_count(self.produce_count)

    def conf_cur(self):
        if self.first==False or self.game.Counter_5.first==False:
            self.conf()
            self.game.main_canvas.after(50,self.conf_cur)

    def return_place(self):
        if self.placed and self.game.Menu.curMenu=='Counters':
            self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),470)
            self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),495)
            self.game.main_canvas.coords(self.box,self.game.geometry[0] - 130, 440, self.game.geometry[0] - (self.game.geometry[0] - 130), 510)
            self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-140,450,self.game.geometry[0]-340,500)
            self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-335, 475)
            self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 350, 450,
                                                                  self.game.geometry[0] - 410, 500)
            self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 380, 475)
            self.conf_cur()
        elif self.placed and self.game.Menu.curMenu != 'Counters':
            self.hide()

    def notation(self,type):
        if type=='total':
            return self.count.get(2,4)
        elif type=='x_val':
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            mult * self.game.CB.multi_list[3]*self.game.Achievements.achieve_mult('4 Counter') * self.game.Infinity.get_boost('4 counter')
            return mult.get(2,4)
        elif type=='color_x':
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            mult * self.game.CB.multi_list[3]* self.game.Achievements.achieve_mult('4 Counter') * self.game.Infinity.get_boost('4 counter')
            if mult>= 1:
                return '#61c449'
            else:
                return '#454443'
        elif type=='cost':
            return self.cost.get(2, 4)

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
            self.game.main_canvas.delete(self.box_buy),self.game.main_canvas.delete(self.text_buy),self.game.main_canvas.delete(self.box_1_buy)
            self.game.main_canvas.delete(self.box_buy_max), self.game.main_canvas.delete(self.text_buy_max)
        self.count = self.game.Decimal(0, 0, self.game)
        self.multi = self.game.Decimal(1, 0, self.game)
        self.cost = self.game.Decimal(1, 5, self.game)
        self.cost_up = self.game.Decimal(1, 5, self.game)
        self.produce_base = self.game.Decimal(1, 0, self.game)
        self.first=False
        self.placed = False
    def buy(self):
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                if self.game.CB.amount>=1:
                    self.game.Counter_5.place()
            else:
                self.multi = self.multi * 2
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(4)
            self.game.Value.value-=self.cost
            self.cost = self.cost * self.cost_up
            if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                self.cost=self.cost**1.1
            self.count+=1
            print(self.count.get())
            self.conf()

    def buy_max(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock:
            times = int((self.game.Value.value.log() - self.cost.log()) / self.cost_up.log())

            if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                while self.game.Value.value >= self.cost and not self.cost>1.8e308:
                    self.buy()
                    pass
            else:
                cost = self.game.Decimal(self.cost.num, self.cost.e)
                cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                cost_up2 = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                while self.game.Value.value<(cost*(cost_up**times-1))/(cost_up2-1):
                    cost = self.game.Decimal(self.cost.num, self.cost.e)
                    cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                    cost_up2 = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                    times-=1
                self.count+=times
                ##
                if self.first == False and times!=0:
                    self.first = True
                    if self.game.Infinity.first:
                        self.game.Achievements.get_achieve(4)
                    if self.game.CB.amount >= 1:
                        self.game.Counter_5.place()
                    if times-1>0:
                        self.multi *= self.game.Decimal(2,0)**(times-1)
                else:
                    self.multi *= self.game.Decimal(2, 0) ** times
                ##
                cost=self.game.Decimal(self.cost.num,self.cost.e)
                cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                cost_up2 = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                self.game.Value.value -= (cost*(cost_up**times-1))/(cost_up2-1)
                ##

                cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                self.cost = self.cost * (cost_up**times)
                self.buy()

    def get_count(self,count):
        self.count+=count
        self.conf()

    def conf(self):

        self.game.main_canvas.itemconfigure(self.text_multi, text='x' + str(self.notation('x_val')),
                                            fill=self.notation('color_x'))

        if self.game.Menu.curMenu=='Counters':
            try:
                log = self.game.Value.value.log()
            except:
                log = 1
            try:
                log_1 = self.cost.log()
            except:
                log_1 = 1
            try:
                log_2 = self.cost_up.log()
            except:
                log_2 = 1
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
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141-(198*coords_mult), 451, self.game.geometry[0] - 339, 499)
            else:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 71 - (198 * coords_mult), 451,
                                             self.game.geometry[0] - 269, 499)

        self.game.main_canvas.itemconfigure(self.text, text=self.notation('total'))

        self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.notation('cost'))

    def get_save(self):
        data=''
        data+=str(self.count.get_save())+','+str(self.multi.get_save())+','+str(self.cost.get_save())+','
        if self.first==False:
            data+=''+'\n'
        else:
            data+='True\n'
        return data