from decimal import Decimal
import math

class Counter7:
    def __init__(self,game):
        self.game=game
        self.count = game.Decimal(self.game.Save.counters_data[6][0][0],self.game.Save.counters_data[6][0][1],game)
        self.multi = game.Decimal(self.game.Save.counters_data[6][1][0],self.game.Save.counters_data[6][1][1],game)
        self.cost = game.Decimal(self.game.Save.counters_data[6][2][0],self.game.Save.counters_data[6][2][1],game)
        self.cost_up = game.Decimal(1,12,game)
        self.cost_up_inf=8
        self.produce_base=1
        self.first=bool(self.game.Save.counters_data[6][3])
        self.placed=False

    def place(self):
        self.placed = True
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0]-60,680,self.game.geometry[0]-(self.game.geometry[0]-60),750,width=2,fill='black',outline='#a244ab')
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]-(self.game.geometry[0]-85),710,anchor='w',text=self.notation('total'),fill='#c22f40',font=('bahnschrift',24))
        self.text_multi = self.game.main_canvas.create_text(self.game.geometry[0] - (self.game.geometry[0] - 83), 735,
                                                            anchor='w', text='x' + str(self.notation('x_val')),
                                                            fill=self.notation('color_x'),
                                                            font=('bahnschrift', 12))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]-70,690,self.game.geometry[0]-270,740,width=2,fill='black',outline='#95db84')
        self.box_1_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 71, 691,
                                                                self.game.geometry[0] - 269, 739, width=0,
                                                                fill='#63855a')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]-265, 715,
                                                            anchor='w', text='Cost: ' + self.notation('cost'), fill='#e0d900',
                                                            font=('bahnschrift', 16))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] - 280, 690,
                                                                  self.game.geometry[0] - 340, 740, width=2,
                                                                  fill='#63855a',
                                                                  outline='#95db84')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] - 310, 715,
                                                              anchor='center', text='Max', fill='#61c449',
                                                              font=('bahnschrift', 16))
        if self.game.Infinity.first:
            self.return_place()
        if self.first and self.game.CB.amount >= 4:
            self.game.Counter_8.place()
    def produce(self):
        if self.game.Counter_6.first:
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            self.produce_count=(mult*self.produce_base*self.count*self.game.Tickspeed.get_time()*self.game.Eternity.time_speed*self.game.Achievements.achieve_mult('7 Counter')*self.game.CB.multi_list[6]
                                *self.game.Infinity.get_boost()/25)
            self.game.Counter_6.get_count(self.produce_count)

    def return_place(self):
        if self.placed and self.game.Menu.curMenu=='Counters':
            self.game.main_canvas.coords(self.text,self.game.geometry[0]-(self.game.geometry[0]-155),710)
            self.game.main_canvas.coords(self.text_multi, self.game.geometry[0] - (self.game.geometry[0] - 153),735)
            self.game.main_canvas.coords(self.box,self.game.geometry[0] - 130, 680, self.game.geometry[0] - (self.game.geometry[0] - 130), 750)
            self.game.main_canvas.coords(self.box_buy, self.game.geometry[0]-140,690,self.game.geometry[0]-340,740)
            self.game.main_canvas.coords(self.text_buy, self.game.geometry[0]-335, 715)
            self.game.main_canvas.coords(self.box_buy_max, self.game.geometry[0] - 350, 690,
                                                                  self.game.geometry[0] - 410, 740)
            self.game.main_canvas.coords(self.text_buy_max, self.game.geometry[0] - 380, 715)
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

    def notation(self,type):
        if type=='total':
            return self.count.get(2,4)
        elif type=='x_val':
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            mult * self.game.CB.multi_list[4]*self.game.Achievements.achieve_mult('5 Counter') * self.game.Infinity.get_boost('5 counter')
            return mult.get(2,4)
        elif type=='color_x':
            mult = self.game.Decimal(self.multi.num, self.multi.e, self.game)
            mult * self.game.CB.multi_list[4]* self.game.Achievements.achieve_mult('5 Counter') * self.game.Infinity.get_boost('5 counter')
            if mult>= 1:
                return '#61c449'
            else:
                return '#454443'
        elif type=='cost':
            return self.cost.get(2, 4)

    def reset(self):
        if self.placed:
            self.game.main_canvas.delete(self.box),self.game.main_canvas.delete(self.text),self.game.main_canvas.delete(self.text_multi)
            self.game.main_canvas.delete(self.box_buy),self.game.main_canvas.delete(self.box_1_buy),self.game.main_canvas.delete(self.text_buy)
            self.game.main_canvas.delete(self.box_buy_max), self.game.main_canvas.delete(self.text_buy_max)
        self.count = self.game.Decimal(0, 0, self.game)
        self.multi = self.game.Decimal(1, 0, self.game)
        self.cost = self.game.Decimal(1, 17, self.game)
        self.cost_up = self.game.Decimal(1, 10, self.game)
        self.produce_base = self.game.Decimal(1, 0, self.game)
        self.first=False
        self.placed = False

    def conf_cur(self):
        if self.first==False or self.game.Counter_8.first==False:
            self.conf()
            self.game.main_canvas.after(50,self.conf_cur)

    def buy(self):
        if self.game.Value.value>=self.cost and not self.game.Value.lock:
            if self.first == False:
                self.first = True
                if self.game.CB.amount >= 4:
                    self.game.Counter_8.place()
            else:
                self.multi = self.multi * 2
            if self.game.Infinity.first:
                self.game.Achievements.get_achieve(7)
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
                        self.game.Achievements.get_achieve(7)
                    if self.game.CB.amount >= 4:
                        self.game.Counter_8.place()
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
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 141-(198*coords_mult), 691, self.game.geometry[0] - 339, 739)
            else:
                self.game.main_canvas.coords(self.box_1_buy, self.game.geometry[0] - 71 - (198 * coords_mult), 691,
                                             self.game.geometry[0] - 269, 739)

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