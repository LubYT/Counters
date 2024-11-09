from decimal import Decimal

class Tickspeed:

    def __init__(self,game):
        self.game=game
        self.tickspeed=game.Decimal(self.game.Save.TS_data[0][0][0],self.game.Save.TS_data[0][0][1],game)
        self.tickspeed_upper=game.Decimal(self.game.Save.TS_data[0][1][0],self.game.Save.TS_data[0][1][1],game)
        self.cost=game.Decimal(self.game.Save.TS_data[0][2][0],self.game.Save.TS_data[0][2][1],game)
        self.max_cost=game.Decimal(self.game.Save.TS_data[0][3][0],self.game.Save.TS_data[0][3][1],game)
        self.cost_up=game.Decimal(1,1,game)

    def place(self):
        self.text=self.game.main_canvas.create_text(self.game.geometry[0]//2,120,anchor='center',text=self.get_not('text'),fill=self.get_not('text_c'),font=('bahnschrift',10))
        self.box_buy=self.game.main_canvas.create_rectangle(self.game.geometry[0]//2-100,130,self.game.geometry[0]//2+100,170,width=1,fill='black',outline='#c22f40')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0]//2, 150,
                                                            anchor='center',justify='center', fill='#61c449',
                                                            font=('bahnschrift', 12))
        self.box_buy_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 120, 130,
                                                              self.game.geometry[0] // 2 + 170, 170, width=1,
                                                              fill='black', outline='#c22f40')
        self.text_buy_max = self.game.main_canvas.create_text(self.game.geometry[0] //2 + 145, 150,
                                                          anchor='center', justify='center',
                                                          text='Max', fill='#61c449',
                                                          font=('bahnschrift', 12))

    def get_not(self,type):
        if type=='text':
            if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
                time_t=self.game.Decimal(self.tickspeed.num,self.tickspeed.e,self.game)
                time_t=time_t ** (self.game.TA.spare_time ** self.game.TA.spare_time_mult)
                return 'Counters speed: ' + str(self.tickspeed.get(2,4)) + ' ^ ' + str(
                    round((self.game.TA.spare_time ** self.game.TA.spare_time_mult), 1)) + ' = ' + str(time_t.get(2,4))
            else:
                if self.tickspeed>1e15:
                    return 'Counters speed is extremely altered: '+str(self.tickspeed.get(2,4))
                if self.tickspeed>10000:
                    return 'Counters speed is massively altered: '+str(self.tickspeed.get(2,4))
                else:
                    return 'Counters speed: ' + str(self.tickspeed.get(2, 4))
        elif type=='text_c':
            if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
                return '#d4f065'
            else:
                if self.tickspeed>1e15:
                    return '#31bcf7'
                if self.tickspeed>10000:
                    return '#5d2fc2'
                else:
                    return '#c22fa2'
        elif type=='cost':
            if self.cost>=self.max_cost:
                if self.game.Eternity.first:
                    return 'Upgrade blocked by Eternity\non '+self.max_cost.get(2,4)
                else:
                    return 'Upgrade limited'
            time_accel = self.game.Decimal(self.game.TA.accel.num, self.game.TA.accel.e, self.game)
            t_u=self.game.Decimal(self.tickspeed_upper.num,self.tickspeed_upper.e,self.game)
            t_u += (time_accel - 1)
            return 'Cost: ' + str(self.cost.get(2,4)) + '\n' + 'Counters speed * ' + str(t_u.get(2,4))

    def get_boost(self,multi):
        self.tickspeed*=multi
        self.game.main_canvas.itemconfigure(self.text,text=self.get_not('text'),fill=self.get_not('text_c'))

    def reset(self):
        self.tickspeed = self.game.Decimal(1,0,self.game)*self.game.Infinity.get_boost_1()*self.game.Achievements.achieve_mult('Time speed')
        self.game.main_canvas.itemconfigure(self.text,text=self.get_not('text'),fill=self.get_not('text_c'))
        self.tickspeed_upper=self.game.Decimal(1.12,0,self.game)
        self.cost = self.game.Decimal(1,1,self.game)
        self.cost_up = self.game.Decimal(1,1,self.game)

    def get_time(self):
        tick=self.game.Decimal(self.tickspeed.num,self.tickspeed.e,self.game)
        if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
            tick=tick**(self.game.TA.spare_time ** self.game.TA.spare_time_mult)
        return tick
    def buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock:
            if self.cost<self.max_cost:
                self.game.Value.value -= self.cost
                self.cost = self.cost * self.cost_up
                time_accel=self.game.Decimal(self.game.TA.accel.num,self.game.TA.accel.e,self.game)
                t_u = self.game.Decimal(self.tickspeed_upper.num, self.tickspeed_upper.e, self.game)
                t_u += (time_accel - 1)
                self.tickspeed=self.tickspeed*(t_u)
                if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4 and self.tickspeed > 2.5:
                    self.tickspeed = self.game.Decimal(2.5, 0, self.game)
    def max_buy(self):
        if self.game.Value.value >= self.cost and not self.game.Value.lock and self.cost<self.max_cost:
                if self.game.Value.value<self.max_cost:
                    times=int((self.game.Value.value.log() - self.cost.log()) / self.cost_up.log())
                else:
                    times=int((self.max_cost.log()- self.cost.log()) / self.cost_up.log())
                print(times)
                cost = self.game.Decimal(self.cost.num, self.cost.e)
                cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                cost_up2 = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                while self.game.Value.value < (cost * (cost_up ** times - 1)) / (cost_up2 - 1):
                    cost = self.game.Decimal(self.cost.num, self.cost.e)
                    cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                    cost_up2 = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                    times -= 1
                cost = self.game.Decimal(self.cost.num, self.cost.e)
                cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                cost_up2 = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                self.game.Value.value -= ((cost * (cost_up ** times - 1)) / (cost_up2 - 1))
                cost_up = self.game.Decimal(self.cost_up.num, self.cost_up.e)
                self.cost = self.cost * (cost_up ** times)
                time_accel = self.game.Decimal(self.game.TA.accel.num, self.game.TA.accel.e, self.game)
                t_u = self.game.Decimal(self.tickspeed_upper.num, self.tickspeed_upper.e, self.game)
                t_u += (time_accel - 1)
                while t_u.e<1 and times>=100:
                    t_u=t_u**100
                    times-=100
#problem
                self.tickspeed *= (t_u**times)

                if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4 and self.tickspeed > 2.5:
                    self.tickspeed = self.game.Decimal(2.5, 0, self.game)
                self.buy()
    def tick(self):
        self.game.main_canvas.itemconfigure(self.text, text=self.get_not('text'), fill=self.get_not('text_c'))
        self.game.main_canvas.itemconfigure(self.text_buy, text=self.get_not('cost'))
        if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 4:
            self.game.TA.spare_time+=0.05

    def get_save(self):
        data=''
        data+=str(self.tickspeed.get_save())+','+str(self.tickspeed_upper.get_save())+','+str(self.cost.get_save())+','+str(self.max_cost.get_save())+'\n'
        return data