import math
from decimal import Decimal
class Counter1:
    def __init__(self,game):
        self.game=game
        self.count=game.Decimal(self.game.Save.counters_data[0][0][0],self.game.Save.counters_data[0][0][1],game)
        self.multi=game.Decimal(self.game.Save.counters_data[0][1][0],self.game.Save.counters_data[0][1][1],game)
        self.cost=game.Decimal(self.game.Save.counters_data[0][2][0],self.game.Save.counters_data[0][2][1],game)
        self.cost_up=game.Decimal(1,2,game)
        self.cost_up_inf=8
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[0][3])

    def place(self):
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,200,self.game.geometry[0]-(self.game.geometry[0]-60),270,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),230,anchor='w',text=self.notation('total'),fill='#c22f40',font=('bahnschrift',24))
        self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83), 255,
                                                          anchor='w', text='x'+str(self.notation('x_val')), fill=self.notation('color_x'),
                                                          font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,210,self.game.geometry[0]-270,260,width=2,fill='black',outline='#95db84')
        self.box_1_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 71, 211,
                                                              self.game.geometry[0] - 269, 259, width=0, fill='#63855a')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 235,
                                                            anchor='w', text='Cost: ' + self.notation('cost'), fill='#e0d900',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 210,
                                                              self.game.geometry[0] - 340, 260, width=2, fill='#63855a',
                                                              outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 235,
                                                          anchor='center', text='Max', fill='#61c449',
                                                          font=('bahnschrift', 16))
        if self.first:
            self.game.Counter_2.place()
    def produce(self):
        mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
        self.produce_count_PS=(mult*self.produce_base*self.count*self.game.Tickspeed.get_time()*self.game.Achievements.achieve_mult('1 Counter')*self.game.CB.multi_list[0]
                               *self.game.Infinity.get_boost('1 counter'))
        mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
        self.produce_count=(mult*self.produce_base*self.count*self.game.Eternity.time_speed*self.game.Tickspeed.get_time()*self.game.Achievements.achieve_mult('1 Counter')*self.game.CB.multi_list[0]
                            *self.game.Infinity.get_boost('1 counter')/25)
        self.game.Value_PS.conf(self.produce_count_PS.get(2,4))
        self.game.Value.get_count(self.produce_count)

    def reset(self):
        self.count = self.game.Decimal(0,0,self.game)
        self.multi = self.game.Decimal(1,0,self.game)
        self.cost = self.game.Decimal(1,1,self.game)
        self.cost_up = self.game.Decimal(1,2,self.game)
        self.produce_base = self.game.Decimal(1,0,self.game)
        self.first = False
        self.conf()
        self.game.main_canvas.itemconfigure(self.text_buy, fill='#e0d900')

    def notation(self,type):
        if type=='total':
            return self.count.get(2,4)
        elif type=='x_val':
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            mult * self.game.CB.multi_list[0] * self.game.Infinity.get_boost(
                '1 counter') * self.game.Achievements.achieve_mult('1 Counter')
            return mult.get(2,4)
        elif type=='color_x':
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            mult * self.game.CB.multi_list[0] * self.game.Infinity.get_boost(
                '1 counter') * self.game.Achievements.achieve_mult('1 Counter')
            if mult>= 1:
                return '#61c449'
            else:
                return '#454443'
        elif type=='cost':
            return self.cost.get(2, 4)



    def return_place(self):
        self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),230)
        self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),255)
        self.game.main_canvas.coords(self.box,self.game.geometry[0] - 130, 200, self.game.geometry[0] - (self.game.geometry[0] - 130), 270)
        self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-140,210,self.game.geometry[0]-340,260)
        self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141, 211, self.game.geometry[0] - 339, 259)
        self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-335, 235)
        self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 350, 210,
                                                              self.game.geometry[0] - 410, 260)
        self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 380, 235)
        self.conf_cur()

    def hide(self):
        self.game.main_canvas.coords(self.box_1_buy, -999,-999,-999,-999)
        self.game.main_canvas.coords(self.text, -999,-999)
        self.game.main_canvas.coords(self.text_multi, -999,-999)
        self.game.main_canvas.coords(self.box, -999,-999, -999,-999)
        self.game.main_canvas.coords(self.box_buy, -999,-999, -999,-999)
        self.game.main_canvas.coords(self.text_buy, -999,-999)
        self.game.main_canvas.coords(self.box_buy_max, -999,-999, -999,-999)
        self.game.main_canvas.coords(self.text_buy_max, -999,-999)
    def buy(self):
        print(self.game.Value.value.num)
        print(self.cost.num)
        print(self.game.Value.value>=self.cost)
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                print('placed 1')
                self.game.Counter_2.place()
            else:
                self.multi = self.multi * 2
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(1)
            self.game.Value.value-=self.cost
            self.cost = self.cost * self.cost_up
            if (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
                self.cost=self.cost**1.1
            self.count+=1
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
                        self.game.Achievements.get_achieve(1)
                    print('placed')
                    self.game.Counter_2.place()
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
    def conf_cur(self):
        if self.first==False:
            self.conf()
            self.game.main_canvas.after(50,self.conf_cur)

    def get_count(self,count):
        self.count+=count
        self.conf()

    def conf(self):
        mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
        mult * self.game.CB.multi_list[0] * self.game.Infinity.get_boost(
            '1 counter') * self.game.Achievements.achieve_mult('1 Counter')
        self.game.main_canvas.itemconfigure(self.text_multi, text='x'+str(self.notation('x_val')), fill=self.notation('color_x'))

        if self.game.Infinity.first and mult * self.game.CB.multi_list[0] * self.game.Infinity.get_boost('1 counter')*self.game.Achievements.achieve_mult('1 Counter')>=1e50:
            self.game.Achievements.get_achieve(11)

        self.game.main_canvas.itemconfigure(self.text, text=self.notation('total'))

        if self.game.Menu.curMenu == 'Counters':
            try:
                log=self.game.Value.value.log()
            except:
                log=1
            try:
                log_1=self.cost.log()
            except:
                log_1=1
            try:
                log_2=self.cost_up.log()
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
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141-(198*coords_mult), 211, self.game.geometry[0] - 339, 259)
            else:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 71 - (198 * coords_mult), 211,
                                             self.game.geometry[0] - 269, 259)

        self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + self.notation('cost'))

    def get_save(self):
        data=''
        data+=str(self.count.get_save())+','+str(self.multi.get_save())+','+str(self.cost.get_save())+','
        if self.first==False:
            data+=''+'\n'
        else:
            data+='True\n'
        return data