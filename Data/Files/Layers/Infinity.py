from decimal import Decimal
import math


class Infinity:
    def __init__(self, game):
        self.game = game
        self.infinities = self.game.Decimal(self.game.Save.Infinity_data[0][0][0],self.game.Save.Infinity_data[0][0][1],self.game)
        self.multi_progressive_7=self.game.Decimal(self.game.Save.Infinity_data[2][0][0],self.game.Save.Infinity_data[2][0][1],self.game,'n')
        self.infinity_counter = self.game.Decimal(self.game.Save.Infinity_data[1][0][0],self.game.Save.Infinity_data[1][0][1],self.game,'IC')
        self.total_count=self.game.Decimal(self.game.Save.Infinity_data[4][0][0],self.game.Save.Infinity_data[4][0][1],self.game,'IC')
        self.cost = 1.8e308
        self.income = 1
        self.cur_page='Surpassings'
        self.color_bord=[120,'-']
        self.infinity_surpassings=[self.infinity_counter]
        self.upgrades = self.game.Save.Infinity_data[3][0]
        self.first = bool(self.game.Save.Infinity_data[5][0])
        self.placed = False

    def place(self):
        self.placed=True
        self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 520, 86,
                                                          anchor='center',
                                                          text=self.get_not('text'),
                                                          fill=self.get_not('text_c'), justify='center',
                                                          font=('bahnschrift', 14))
        self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 440, 110,
                                                              self.game.geometry[0] // 2 - 600, 170, width=1,
                                                              fill='black', outline='#ffbc36')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 520, 140,
                                                          anchor='center', justify='center', text=self.get_not('text_buy'), fill=self.get_not('text_buy_c'),
                                                          font=('bahnschrift', 10))

    def get_not(self,type):
        if type=='text':
            return 'Infinity Count: ' + self.infinity_counter.get(2,4)
        elif type=='text_c':
            return '#d99000'
        elif type=='text_buy':
            return 'Cost: Infinity\nGet ' + str(self.get_total()) + ' IC'
        elif type=='text_buy_c':
            return '#d99000'
        elif type=='fill_1':
            x = self.game.Decimal(1, 0, self.game, 'n')
            if self.infinity_counter>=1:
                x*=self.infinity_counter.log()**0.8
            return x


    def hide(self):
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            self.game.main_canvas.delete(self.upgr_1_text),self.game.main_canvas.delete(self.upgr_2_text)
            self.game.main_canvas.delete(self.upgr_3_text),self.game.main_canvas.delete(self.upgr_4_text)
            self.game.main_canvas.delete(self.upgr_1_box),self.game.main_canvas.delete(self.upgr_2_box)
            self.game.main_canvas.delete(self.upgr_3_box),self.game.main_canvas.delete(self.upgr_4_box)
            self.game.main_canvas.delete(self.upgr_5_box), self.game.main_canvas.delete(self.upgr_5_text)
            self.game.main_canvas.delete(self.upgr_6_box), self.game.main_canvas.delete(self.upgr_6_text)
            self.game.main_canvas.delete(self.upgr_7_box), self.game.main_canvas.delete(self.upgr_7_text)
            if self.game.Aspects.completion_4:
                self.game.main_canvas.delete(self.upgr_8_box), self.game.main_canvas.delete(self.upgr_8_text)
                self.game.main_canvas.delete(self.upgr_9_box), self.game.main_canvas.delete(self.upgr_9_text)
                self.game.main_canvas.delete(self.upgr_10_box), self.game.main_canvas.delete(self.upgr_10_text)
                self.game.main_canvas.delete(self.upgr_11_box), self.game.main_canvas.delete(self.upgr_11_text)
        else:
            self.game.main_canvas.delete(self.text_1)

    def buy(self):
        if self.game.Value.value >= self.cost:
            if self.first:
                self.game.Achievements.get_achieve(10)
            if self.game.Infinity.first and self.game.TA.amount<0.9:
                self.game.Achievements.get_achieve(13)
            if self.game.Infinity.first and self.game.CB.amount<=4:
                self.game.Achievements.get_achieve(14)
            if self.game.CB.amount<0.9 and  self.game.TA.amount<0.9:
                self.game.Achievements.get_achieve(26)
            if self.first == False:
                self.first = True
                self.game.menu_place()
            if self.game.Aspects.active==True:
                self.game.Aspects.reward()
            self.infinities += 1
            if self.infinities>=25:
                self.game.Achievements.get_achieve(15)
            total=self.get_total()
            self.get_points(total)
            self.game.I_reset()
            if self.game.Menu.curMenu=='Infinity':
                self.conf_upgrades()

    def get_total(self):
        dc=self.game.Decimal(self.game.Doom.doom_count.num,self.game.Doom.doom_count.e,self.game)
        total=self.game.Decimal(1,0,self.game)
        total *= self.income
        value=self.game.Value.value.log()
        if self.game.Eternity.upgrades[2]=='Y' and self.game.Value.value>1.8e308:
            total *=((value/308)*1.5)**5
        total*=(dc** self.game.Doom.mult_inf)
        total*=self.game.Achievements.achieve_mult('IC') * self.game.Aspects.reward_2
        if self.game.Eternity.upgrades[0]=='Y':
            y = self.game.Decimal(1, 0, self.game)
            ec = self.game.Decimal(self.game.Eternity.eternity_count.num, self.game.Eternity.eternity_count.e, self.game)
            if self.game.Eternity.eternity_count > 0:
                y += ec ** 0.5 / 5
            e = self.game.Decimal(self.game.Eternity.eternities.num, self.game.Eternity.eternities.e, self.game)
            if self.game.Eternity.eternities > 0:
                y += e ** 0.7 / 5
            total*=y
        if self.upgrades[7]=='Y':
            inf=self.game.Decimal(self.infinities.num,self.infinities.e,self.game)
            total *= inf** 1.2
        if self.upgrades[9]=='Y':
            total *= self.game.Decimal(1,int(self.game.TA.amount),self.game)
        return total
    def reset(self,*args):
        self.multi_progressive_7=self.game.Decimal(1,0,self.game)
        if 'full' in args:
            self.infinities = self.game.Decimal(1,0,self.game)
            self.multi_progressive_7 = self.game.Decimal(1,0,self.game)
            self.get_points('reset')
            self.cost = 1.8e308
            self.income = 1
            self.upgrades = ['N','N','N','N','Y','N','N','N','N','N','N']
            self.conf_upgrades()
            if self.game.Menu.curMenu=='Infinity':
                self.game.Menu.stage_get(change='infinity')

    def get_points(self,value,*args):
        if self.game.Aspects.active==False:
            if value!='reset':
                if not 'buy' in args:
                    self.total_count+=value
                    self.infinity_counter += value
                else:
                    self.infinity_counter -= value
                if self.infinity_counter>1.79e308 and self.game.Eternity.upgrades[3]=='N':
                    self.infinity_counter=self.game.Decimal(1.79,308,self.game)
                self.game.main_canvas.itemconfigure(self.text, text=self.get_not('text'))
            else:
                if self.game.Eternity.upgrades[5] == 'Y':
                    self.infinity_counter = self.game.Decimal(1.000001, 1, self.game)
                    self.total_count = self.game.Decimal(1, 1, self.game)
                else:
                    self.infinity_counter=self.game.Decimal(0,0,self.game)
                    self.total_count=self.game.Decimal(0,0,self.game)
                self.game.main_canvas.itemconfigure(self.text, text=self.get_not('text'))

    def buy_upgrade(self, index):
        if index == 1 and self.upgrades[0]=='N':
            if self.infinity_counter >= 1:
                self.get_points(1, 'buy')
                self.upgrades[0] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_1_box,fill='#c28e0a')
                y = self.game.Decimal(1, 0, self.game, 'n')
                infi = self.game.Decimal(self.infinities.num, self.infinities.e, self.game)
                infc = self.game.Decimal(self.infinity_counter.num, self.infinity_counter.e, self.game)
                log_1 = self.infinity_counter.log()
                log_2 = self.infinities.log()
                if self.infinity_counter > 0:
                    y += (infc / (5 + log_1))
                if self.infinities > 0:
                    y += (infi / (5 + log_2))
                if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 2:
                    y = y ** 1.25
                if y>=1:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text,fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + y.get(2,4))
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text,fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1')
        elif index == 2 and self.upgrades[1] == 'N':
            if self.infinity_counter >= 2:
                self.get_points(2, 'buy')
                self.game.Tickspeed.get_boost(1.25)
                self.upgrades[1] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_2_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_2_text, fill='#4a1111',
                                                    text='Gain multiplier to\n counters speed * 1.25')
        elif index == 3 and self.upgrades[2] == 'N':
            if self.infinity_counter >= 2:
                self.get_points(2, 'buy')
                self.upgrades[2] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_3_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_3_text, fill='#4a1111',
                                                    text='Start any reset\nwith 1e5 C')
        elif index == 4 and self.upgrades[3] == 'N':
            if self.infinity_counter >= 5:
                self.get_points(5, 'buy')
                self.upgrades[3] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_4_box, fill='#c28e0a')
                if 10<self.game.Value.value:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on Count:\n x ' +
                                                             str(self.game.Value.value.log() ** 0.75))
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on Count:\n x ' + '1')
        elif index == 5 and self.upgrades[4] == 'N':
            if self.infinity_counter >= 10:
                self.get_points(10, 'buy')
                self.upgrades[4] = 'Y'
                self.game.Menu.add('doom')
                self.game.main_canvas.itemconfigure(self.upgr_5_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_5_text, fill='#4a1111',
                                                    text='Doom counters unlocked')
                self.game.Achievements.get_achieve(16)
        elif index == 6 and self.upgrades[5] == 'N':
            if self.infinity_counter >= 2:
                self.get_points(2, 'buy')
                self.upgrades[5] = 'Y'
                self.game.Automatick.allowed[0]='Y'
                self.game.Automatick.allowed[1] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_6_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_6_text, fill='#4a1111',
                                                    text='Unlocked boost and\ntime auto-blocks')
        elif index == 7 and self.upgrades[6] == 'N':
            if self.infinity_counter >= 4:
                self.get_points(4, 'buy')
                self.upgrades[6] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_7_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_7_text, fill='#4a1111',text=
                                                    'Gain progressive multi\nto 1 counter\nx' +
                                                        self.multi_progressive_7.get(2,4))
        elif index == 8 and self.upgrades[7] == 'N':
            if self.infinity_counter >= 1e220:
                self.get_points(1e220, 'buy')
                self.upgrades[7] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_8_text, fill='#4a1111', text='Infinities boost IC gain\nx' + self.get_value(8))
                self.game.main_canvas.itemconfigure(self.upgr_8_box, fill='#c28e0a')

        elif index == 9 and self.upgrades[8] == 'N':
            if self.infinity_counter >= 1e230:
                self.get_points(1e230, 'buy')
                self.upgrades[8] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_9_text, fill='#4a1111', text='Infinities boost DD gain\nx' + self.get_value(9))
                self.game.main_canvas.itemconfigure(self.upgr_9_box, fill='#c28e0a')

        elif index == 10 and self.upgrades[9] == 'N':
            if self.infinity_counter >= 1e240:
                self.get_points(1e240, 'buy')
                self.upgrades[9] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_10_text, fill='#4a1111', text='TA boost IC gain\nx' + self.get_value(10))
                self.game.main_canvas.itemconfigure(self.upgr_10_box, fill='#c28e0a')

        elif index == 11 and self.upgrades[10] == 'N':
            if self.infinity_counter >= 1e250:
                self.get_points(1e250, 'buy')
                self.upgrades[10] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_11_text, fill='#4a1111', text='Total time in game\nboost DD gain\nx'+self.get_value(11))
                self.game.main_canvas.itemconfigure(self.upgr_11_box, fill='#c28e0a')


        if self.upgrades[0]=='Y' and self.upgrades[1]=='Y' and self.upgrades[2]=='Y' and self.upgrades[3]=='Y' and self.upgrades[4]=='Y' and self.upgrades[5]=='Y' and self.upgrades[6]=='Y':
            self.game.Achievements.get_achieve(17)
        self.conf_upgrades()

    def post_save(self):
        if self.upgrades[4]=='Y':
            self.game.Menu.add('doom')
        if self.upgrades[5]=='Y':
            self.game.Automatick.allowed[0] = 'Y'
            self.game.Automatick.allowed[1] = 'Y'
    def get_boost(self,*arg):
        x = self.game.Decimal(1,0,self.game)
        #inf
        if not (self.game.Aspects.active==True and self.game.Aspects.cur_ill==1) and not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if self.first:
                x*=1.15
            if self.upgrades[0] == 'Y':
                y = self.game.Decimal(1, 0, self.game, 'n')
                infi = self.game.Decimal(self.infinities.num, self.infinities.e, self.game)
                infc = self.game.Decimal(self.infinity_counter.num, self.infinity_counter.e, self.game)
                log_1 = self.infinity_counter.log()
                log_2 = self.infinities.log()
                if self.infinity_counter >= 1:
                    y += (infc / (5 + log_1))
                if self.infinities >= 1:
                    y += (infi / (5 + log_2))
                if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 2:
                    y = y ** 1.25
                x*=y
            if self.upgrades[3] == 'Y':
                value = self.game.Decimal(self.game.Value.value.num, self.game.Value.value.e, self.game).log()
                value = value ** 0.75
                if 10<self.game.Value.value:
                    x *= value
                else:
                    x *= 1
        #doom
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if not (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 1):
                if self.upgrades[4] == 'Y':
                    dc = self.game.Decimal(self.game.Doom.doom_count.num, self.game.Doom.doom_count.e, self.game)
                    x=x/(dc**self.game.Doom.mult_doom)
            else:
                dc = self.game.Decimal(self.game.Doom.doom_count.num, self.game.Doom.doom_count.e, self.game)
                x = x *(dc ** 0.2)
                x= x/75
        #cheat
        if self.game.boost_cheat:
            x*=5
        #eternity
        if self.game.Eternity.upgrades[6]=='Y':
            y = self.game.Decimal(1, 0, self.game)
            ec = self.game.Decimal(self.game.Eternity.eternity_count.num, self.game.Eternity.eternity_count.e, self.game)
            if self.game.Eternity.eternity_count > 0:
                y += ec ** 0.6 / 3
            e = self.game.Eternity.game.Decimal(self.game.Eternity.eternities.num, self.game.Eternity.eternities.e, self.game)
            if self.game.Eternity.eternities > 0:
                y += e ** 0.8 / 3
            x*=y
        #spec
        if not (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 1) and not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if '1 counter' in arg:
                if self.upgrades[6] == 'Y':
                    x *= self.multi_progressive_7
        return x

    def get_boost_1(self):
        x=1
        if self.upgrades[1] == 'Y' and not (self.game.Aspects.active==True and self.game.Aspects.cur_ill==1):
            x*=1.25
        return x

    def conf_upgrades(self,*args):
        if self.game.Menu.curMenu=='Infinity' and not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if self.cur_page == 'Upgrades':
                if self.upgrades[0]=='N':
                    y = self.game.Decimal(1,0,self.game,'n')
                    infi=self.game.Decimal(self.infinities.num,self.infinities.e,self.game)
                    infc=self.game.Decimal(self.infinity_counter.num,self.infinity_counter.e,self.game)
                    log_1=self.infinity_counter.log()
                    log_2=self.infinities.log()
                    if self.infinity_counter > 0:
                        y += (infc / (5 + log_1))
                    if self.infinities > 0:
                        y += (infi / (5 + log_2))
                    if self.game.Aspects.active==True and self.game.Aspects.cur_ill==2:
                        y=y**1.25
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#d99000',
                                                            text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                                y.get(2,4))+ '\nCost: 1 IC')
                elif self.upgrades[0]=='Y' and 'VALUE' in args:
                    y = self.game.Decimal(1, 0, self.game, 'n')
                    infi = self.game.Decimal(self.infinities.num, self.infinities.e, self.game)
                    infc = self.game.Decimal(self.infinity_counter.num, self.infinity_counter.e, self.game)
                    log_1 = self.infinity_counter.log()
                    log_2 = self.infinities.log()
                    if self.infinity_counter >= 1:
                        y += (infc / (5 + log_1))
                    if self.infinities >= 1:
                        y += (infi / (5 + log_2))
                    if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 2:
                        y = y ** 1.25
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#4a1111',
                                                            text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                                y.get(2,4)))
                if self.upgrades[3]=='N' and 'VALUE' in args:
                    value=self.game.Value.value.log()
                    value=value**0.75
                    if 10<self.game.Value.value:
                        self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                             str(round(value,2))+'\nCost: 5 IC')
                    else:
                        self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+'1'+'\nCost: 5 IC')
                elif self.upgrades[3]=='Y' and 'VALUE' in args:
                    value = self.game.Value.value.log()
                    value = value ** 0.75
                    if 10<self.game.Value.value:
                        self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                             str(round(value,2)))
                    else:
                        self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+'1')
                if self.upgrades[6] == 'N' and 'MULTI' in args:
                    self.game.main_canvas.itemconfigure(self.upgr_7_text,text='Gain progressive multi\nto 1 counter\nx' +
                                                                             self.multi_progressive_7.get(2,4) + '\nCost: 4 IC')
                elif self.upgrades[6] == 'Y' and 'MULTI' in args:
                    self.game.main_canvas.itemconfigure(self.upgr_7_text,
                                                        text='Gain progressive multi\nto 1 counter\nx' + self.multi_progressive_7.get(2,4))

                ###

                if self.game.Aspects.completion_4 and 'MULTI' in args:
                    if self.upgrades[7] == 'N':
                        text='Infinities boost IC gain\nx' + self.get_value(8) + '\nCost: 1e220 IC'
                    else:
                        text='Infinities boost IC gain\nx' + self.get_value(8)
                    self.game.main_canvas.itemconfigure(self.upgr_8_text,text=text)
                    if self.upgrades[8] == 'N':
                        text='Infinities boost DD gain\nx' + self.get_value(9) + '\nCost: 1e230 IC'
                    else:
                        text='Infinities boost DD gain\nx' + self.get_value(9)
                    self.game.main_canvas.itemconfigure(self.upgr_9_text,text=text)
                    if self.upgrades[9] == 'N':
                        text='TA boost IC gain\nx' + self.get_value(10) + '\nCost: 1e240 IC'
                    else:
                        text='TA boost IC gain\nx' + self.get_value(10)
                    self.game.main_canvas.itemconfigure(self.upgr_10_text,text=text)
                    if self.upgrades[10] == 'N':
                        text = 'Total time in game\nboost DD gain\nx'+self.get_value(11) + '\nCost: 1e250 IC'
                    else:
                        text = 'Total time in game\nboost DD gain\nx'+self.get_value(11)
                    self.game.main_canvas.itemconfigure(self.upgr_11_text, text=text)
            elif self.cur_page == 'Surpassings':
                log = self.infinity_surpassings[0].log() / 1000
                if log > 1:
                    log = 1
                self.infinity_surpassings[0]*=20
                if self.color_bord[1]=='-':
                    self.color_bord[0]-=2
                    if self.color_bord[0]==0:
                        self.color_bord[1]='+'
                else:
                    self.color_bord[0] += 2
                    if self.color_bord[0] == 120:
                        self.color_bord[1] = '-'
                self.game.main_canvas.itemconfigure(self.filled, fill="#%02x%02x%02x" % (255, self.color_bord[0], 0))
                self.game.main_canvas.coords(self.filled,self.game.geometry[0] // 2 - self.game.geometry[0] // 20 +3,
                    self.game.geometry[1] - 200,
                    self.game.geometry[0] // 2 + self.game.geometry[0] // 20 - 2,
                    self.game.geometry[1] - 200 - ((self.game.geometry[1] - 450) * log))
                self.game.main_canvas.coords(self.box_bank, self.game.geometry[0] // 2 + self.game.geometry[0] // 20 + 50,
                    self.game.geometry[1] - 200 - ((self.game.geometry[1] - 450) * log),
                    self.game.geometry[0] // 2 + self.game.geometry[0] // 20 + 250,
                    self.game.geometry[1] - 100 - ((self.game.geometry[1] - 450) * log))
                self.game.main_canvas.itemconfigure(self.bank_box_text, text=self.infinity_surpassings[0].get(2, 4) + ' / 1.00e1000 IC\n\nClick to drain your IC')
                self.game.main_canvas.coords(self.bank_box_text, self.game.geometry[0] // 2 + self.game.geometry[0] // 20 + 150,
                    self.game.geometry[1] - 150 - ((self.game.geometry[1] - 450) * log))
                self.game.main_canvas.itemconfigure(self.list_boxes_goals[0][1],text='1e50 IC\nGain more IC based on IC\nx'+self.get_not('fill_1').get(2,4))


            ###
        if self.placed:
            if self.game.Aspects.active == False:
                self.game.main_canvas.itemconfigure(self.box_buy, outline='#ffbc36')
                if self.get_total()>1.79e308 and self.game.Eternity.upgrades[3]=='N':
                    self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: Infinity\nGet Limited 1.79e308 IC', fill='#d99000')
                else:
                    self.game.main_canvas.itemconfigure(self.text_buy,
                                                        text='Cost: Infinity\nGet ' + self.get_total().get(2,4) + ' IC',
                                                        fill='#d99000')
            elif self.game.Aspects.active==True:
                if self.game.Aspects.cur_ill==1:
                    self.game.main_canvas.itemconfigure(self.box_buy,outline='#93d9d9')
                    self.game.main_canvas.itemconfigure(self.text_buy, text='Reach 1.8e308\nInfinity obeys Illusion\nThere is no IC', fill='#93d9d9')
                elif self.game.Aspects.cur_ill==2:
                    self.game.main_canvas.itemconfigure(self.box_buy, outline='#05f')
                    self.game.main_canvas.itemconfigure(self.text_buy,
                                                        text='Reach 1.8e308\nInfinity obeys Illusion\nThere is no IC',
                                                        fill='#05f')
                elif self.game.Aspects.cur_ill == 3:
                    self.game.main_canvas.itemconfigure(self.box_buy, outline='#36ffe7')
                    self.game.main_canvas.itemconfigure(self.text_buy,
                                                        text='Reach 1.8e308\nInfinity obeys Illusion\nThere is no IC',
                                                        fill='#36ffe7')
                elif self.game.Aspects.cur_ill == 4:
                    self.game.main_canvas.itemconfigure(self.box_buy, outline='#bf0fff')
                    self.game.main_canvas.itemconfigure(self.text_buy,
                                                        text='Reach 1.8e308\nIllusion destroy Infinity\nThere is no IC',
                                                        fill='#bf0fff')
    def place_menu(self):
        if self.game.Eternity.upgrades[7]=='N':
            self.place_upgrades()
        else:
            self.place_menu_box()
            if self.cur_page=='Upgrades':
                self.place_upgrades()
            elif self.cur_page=='Surpassings':
                self.place_sur()

    def place_menu_box(self):
        if self.cur_page == 'Upgrades':
            fill_1=['#fa0','#241800']
            fill_2=['black', '#d99000']
        else:
            fill_1 = ['black', '#d99000']
            fill_2 = ['#fa0','#241800']
        self.menu_box_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 150, self.game.geometry[1]-50,
                                                                 self.game.geometry[0] // 2, self.game.geometry[1]-130, width=1,
                                                                 fill=fill_1[0], outline='#e5b045')
        self.menu_box_2 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 150,
                                                                 self.game.geometry[1] - 50,
                                                                 self.game.geometry[0] // 2,
                                                                 self.game.geometry[1] - 130, width=1,
                                                                 fill=fill_2[0], outline='#e5b045')
        self.menu_text_1 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 75,self.game.geometry[1]-90,
                                                             anchor='center',
                                                             text='Infinity\nUpgrades',
                                                             fill=fill_1[1], justify='center',
                                                             font=('bahnschrift', 12))
        self.menu_text_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 75,
                                                             self.game.geometry[1] - 90,
                                                             anchor='center',
                                                             text='Infinity\nSurpassings',
                                                             fill=fill_2[1], justify='center',
                                                             font=('bahnschrift', 12))

    def place_sur(self):
        log = self.infinity_surpassings[0].log() / 1000
        if log > 1:
            log = 1
        self.bank=self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 -self.game.geometry[0] // 20,
                                                                 250,
                                                                 self.game.geometry[0] // 2 +self.game.geometry[0] // 20,
                                                                 self.game.geometry[1] - 200, width=5,
                                                                 fill='black', outline='#f7b86f')
        self.filled = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 -self.game.geometry[0] // 20+3,
                                                                 self.game.geometry[1] - 200,
                                                                 self.game.geometry[0] // 2 +self.game.geometry[0] // 20-2,
                                                                 self.game.geometry[1] - 200-((self.game.geometry[1]-450)*log), width=0,
                                                                 fill="#%02x%02x%02x" % (255, self.color_bord[0], 0))
        self.box_bank=self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +self.game.geometry[0] // 20+50,
                                                                 self.game.geometry[1] - 200-((self.game.geometry[1]-450)*log),
                                                                 self.game.geometry[0] // 2 +self.game.geometry[0] // 20+250,
                                                                 self.game.geometry[1] - 100-((self.game.geometry[1]-450)*log), width=2,
                                                                 fill='black', outline='#f7b86f')
        self.bank_box_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 +self.game.geometry[0] // 20+150,
                                                             self.game.geometry[1] - 150-((self.game.geometry[1]-450)*log),
                                                             anchor='center',
                                                             text=self.infinity_surpassings[0].get(2,4)+' / 1.00e1000 IC\n\nClick to drain your IC',
                                                             fill='#ff9c40', justify='center',
                                                             font=('bahnschrift', 12))
        self.list_boxes_goals=[[
            self.game.main_canvas.create_rectangle(
            self.game.geometry[0] // 2 - self.game.geometry[0] // 20 - 50,
            self.game.geometry[1] - 200-((self.game.geometry[1]-450)*0.05),
            self.game.geometry[0] // 2 - self.game.geometry[0] // 20 - 250,
            self.game.geometry[1] - 120-((self.game.geometry[1]-450)*0.05), width=2,
            fill='black', outline='#f7b86f'),
            self.game.main_canvas.create_text(
            self.game.geometry[0] // 2 - self.game.geometry[0] // 20 - 150,
            self.game.geometry[1] - 160 - ((self.game.geometry[1] - 450) * 0.05),
            anchor='center',
            text='1e50 IC\nGain more IC based on IC\nx'+self.get_not('fill_1').get(2,4),
            fill='#ff9c40', justify='center',
            font=('bahnschrift', 12),width=200)

            ]
        ]

    def place_upgrades(self):
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if self.upgrades[0]=='N':
                self.upgr_1_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 210,
                                                                         self.game.geometry[0] // 2 - 300, 310, width=1,
                                                                         fill='black', outline='#e5b045')
                y = self.game.Decimal(1, 0, self.game, 'n')
                infi = self.game.Decimal(self.infinities.num, self.infinities.e, self.game)
                infc = self.game.Decimal(self.infinity_counter.num, self.infinity_counter.e, self.game)
                log_1 = self.infinity_counter.log()
                log_2 = self.infinities.log()
                if self.infinity_counter >= 1:
                    y += (infc / (5 + log_1))
                if self.infinities >= 1:
                    y += (infi / (5 + log_2))
                if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 2:
                    y = y ** 1.25
                if y>=1:
                    self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + y.get(2,4) + '\nCost: 1 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1' +'\nCost: 1 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_1_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 210,
                                                                         self.game.geometry[0] // 2 - 300, 310, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                y = self.game.Decimal(1, 0, self.game, 'n')
                infi = self.game.Decimal(self.infinities.num, self.infinities.e, self.game)
                infc = self.game.Decimal(self.infinity_counter.num, self.infinity_counter.e, self.game)
                log_1 = self.infinity_counter.log()
                log_2 = self.infinities.log()
                if self.infinity_counter > 0:
                    y += (infc / (5 + log_1))
                if self.infinities > 0:
                    y += (infi / (5 + log_2))
                if self.game.Aspects.active == True and self.game.Aspects.cur_ill == 2:
                    y = y ** 1.25
                if y >= 1:
                    self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + y.get(2, 4),
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))

            if self.upgrades[1] == 'N':
                self.upgr_2_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 250, 210,
                                                                         self.game.geometry[0] // 2 - 50, 310, width=1,
                                                                         fill='black', outline='#e5b045')
                self.upgr_2_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 150, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to\n counters speed * 1.25' + '\nCost: 2 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_2_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 250, 210,
                                                                         self.game.geometry[0] // 2 - 50, 310, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                self.upgr_2_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 150, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to\n counters speed * 1.25',
                                                                     fill='#4a1111', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.upgrades[2] == 'N':
                self.upgr_3_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 250, 210,
                                                                         self.game.geometry[0] // 2 + 50, 310, width=1,
                                                                         fill='black', outline='#e5b045')
                self.upgr_3_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 150, 260,
                                                                     anchor='center',
                                                                     text='Start any reset\nwith 1e5 C' + '\nCost: 2 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_3_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 250, 210,
                                                                         self.game.geometry[0] // 2 + 50, 310, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                self.upgr_3_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 150, 260,
                                                                     anchor='center',
                                                                     text='Start any reset\nwith 1e5 C',
                                                                     fill='#4a1111', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.upgrades[3] == 'N':
                self.upgr_4_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 500, 210,
                                                                         self.game.geometry[0] // 2 + 300, 310, width=1,
                                                                         fill='black', outline='#e5b045')
                if 10<self.game.Value.value:
                    self.upgr_4_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                         str((self.game.Value.value.log()**0.75))+'\nCost: 5 IC',
                                                                             fill='#d99000', justify='center',
                                                                             font=('bahnschrift', 12))
                else:
                    self.upgr_4_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on Count:\n x ' +
                                                                              '1'+'\nCost: 5 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_4_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 500, 210,
                                                                         self.game.geometry[0] // 2 + 300, 310, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                if 10<self.game.Value.value:
                    self.upgr_4_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                         str((self.game.Value.value.log()**0.75)),
                                                                         fill='#4a1111', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_4_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 260,
                                                                         anchor='center',
                                                                         text='Gain multiplier to counters\nbased on Count:\n x ' +
                                                                              '1',
                                                                         fill='#4a1111', justify='center',
                                                                         font=('bahnschrift', 12))
            if self.upgrades[4] == 'N':
                self.upgr_5_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 100, 330,
                                                                         self.game.geometry[0] // 2 + 100, 430, width=1,
                                                                         fill='black', outline='#e5b045')
                self.upgr_5_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 , 380,
                                                                     anchor='center',
                                                                     text='Unlock Doom counter\nCost: 10 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_5_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 100, 330,
                                                                         self.game.geometry[0] // 2 + 100, 430, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                self.upgr_5_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 380,
                                                                     anchor='center',
                                                                     text='Doom counters unlocked',
                                                                     fill='#4a1111', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.upgrades[5] == 'N':
                self.upgr_6_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 350, 330,
                                                                         self.game.geometry[0] // 2 - 150, 430, width=1,
                                                                         fill='black', outline='#e5b045')
                self.upgr_6_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 250, 380,
                                                                     anchor='center',
                                                                     text='Unlock boost and\ntime auto-blocks\nCost: 2 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_6_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 350, 330,
                                                                         self.game.geometry[0] // 2 - 150, 430, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                self.upgr_6_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2-250, 380,
                                                                     anchor='center',
                                                                     text='Unlocked boost and\ntime auto-blocks',
                                                                     fill='#4a1111', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.upgrades[6] == 'N':
                self.upgr_7_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 350, 330,
                                                                         self.game.geometry[0] // 2 + 150, 430, width=1,
                                                                         fill='black', outline='#e5b045')
                self.upgr_7_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 250, 380,
                                                                     anchor='center',
                                                                     text='Gain progressive multi\nto 1 counter\nx'+self.multi_progressive_7.get(2,4)+'\nCost: 4 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
            else:
                self.upgr_7_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 350, 330,
                                                                         self.game.geometry[0] // 2 + 150, 430, width=1,
                                                                         fill='#c28e0a', outline='#e5b045')
                self.upgr_7_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 250, 380,
                                                                     anchor='center',
                                                                     text='Gain progressive multi\nto 1 counter\nx' +self.multi_progressive_7.get(2,4),
                                                                     fill='#4a1111', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.game.Aspects.completion_4:
                if self.upgrades[7] == 'N':
                    self.upgr_8_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 450,
                                                                             self.game.geometry[0] // 2 - 300, 550, width=1,
                                                                             fill='black', outline='#e5b045')
                    self.upgr_8_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 500,
                                                                         anchor='center',
                                                                         text='Infinities boost IC gain\nx'+self.get_value(8)+'\nCost: 1e220 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_8_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 450,
                                                                             self.game.geometry[0] // 2 - 300, 550, width=1,
                                                                             fill='#c28e0a', outline='#e5b045')
                    self.upgr_8_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 500,
                                                                         anchor='center',
                                                                         text='Infinities boost IC gain\nx'+self.get_value(8),
                                                                         fill='#4a1111', justify='center',
                                                                         font=('bahnschrift', 12))
                if self.upgrades[8] == 'N':
                    self.upgr_9_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 250, 450,
                                                                             self.game.geometry[0] // 2 - 50, 550, width=1,
                                                                             fill='black', outline='#e5b045')
                    self.upgr_9_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 150, 500,
                                                                         anchor='center',
                                                                         text='Infinities boost DD gain\nx'+self.get_value(9)+'\nCost: 1e230 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_9_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 250, 450,
                                                                             self.game.geometry[0] // 2 - 50, 550, width=1,
                                                                             fill='#c28e0a', outline='#e5b045')
                    self.upgr_9_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 150, 500,
                                                                         anchor='center',
                                                                         text='Infinities boost DD gain\nx'+self.get_value(9),
                                                                         fill='#4a1111', justify='center',
                                                                         font=('bahnschrift', 12))
                if self.upgrades[9] == 'N':
                    self.upgr_10_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 250, 450,
                                                                             self.game.geometry[0] // 2 + 50, 550, width=1,
                                                                             fill='black', outline='#e5b045')
                    self.upgr_10_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 150, 500,
                                                                         anchor='center',
                                                                         text='TA boost IC gain\nx'+self.get_value(10)+'\nCost: 1e240 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_10_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 250, 450,
                                                                             self.game.geometry[0] // 2 + 50, 550, width=1,
                                                                             fill='#c28e0a', outline='#e5b045')
                    self.upgr_10_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 150, 500,
                                                                         anchor='center',
                                                                         text='TA boost IC gain\nx'+self.get_value(10),
                                                                         fill='#4a1111', justify='center',
                                                                         font=('bahnschrift', 12))
                if self.upgrades[10] == 'N':
                    self.upgr_11_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 500, 450,
                                                                             self.game.geometry[0] // 2 + 300, 550, width=1,
                                                                             fill='black', outline='#e5b045')
                    self.upgr_11_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 500,
                                                                         anchor='center',
                                                                         text='Total time in game\nboost DD gain\nx'+self.get_value(11)+'\nCost: 1e250 IC',
                                                                         fill='#d99000', justify='center',
                                                                         font=('bahnschrift', 12))
                else:
                    self.upgr_11_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 500, 450,
                                                                             self.game.geometry[0] // 2 + 300, 550, width=1,
                                                                             fill='#c28e0a', outline='#e5b045')
                    self.upgr_11_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 500,
                                                                         anchor='center',
                                                                         text='Total time in game\nboost DD gain\nx'+self.get_value(11),
                                                                         fill='#4a1111', justify='center',
                                                                         font=('bahnschrift', 12))
        else:
            self.text_1=self.game.main_canvas.create_text(self.game.geometry[0] // 2, 290, anchor='center',
                                                            text='Illusion\nThere are no Infinity upgrades',
                                                            fill='#36ffe7', justify='center',
                                                            font=('bahnschrift', 30))

    def get_value(self,num):
        if num==8:
            inf=self.game.Decimal(self.infinities.num,self.infinities.e,self.game)**1.2
            if inf<1:
                inf=self.game.Decimal(1,0,self.game)
            return inf.get(2,4)
        if num==9:
            inf = self.game.Decimal(self.infinities.num, self.infinities.e, self.game) ** 1.3
            if inf<1:
                inf=self.game.Decimal(1,0,self.game)
            return inf.get(2, 4)
        if num==10:
            ta=self.game.Decimal(self.game.TA.amount.num,self.game.TA.amount.e,self.game)**10
            if ta<1:
                ta=self.game.Decimal(1,0,self.game)
            return ta.get(2,4)
        if num == 11:
            time=self.game.Stats.time_total[2]
            for i in range(self.game.Stats.time_total[1]):
                time+=60
            for i in range(self.game.Stats.time_total[0]):
                time+=1440
            if time**0.4 > 1000:
                value = "{:.2e}".format(Decimal(time**0.4))
            else:
                value = round(time**0.4, 1)
            if value<1:
                value=1
            return str(value)

    def other_funcs(self):
        log_2=self.game.Decimal(self.multi_progressive_7.num,self.multi_progressive_7.e,self.game).log()**0.6
        log_3=(self.game.Decimal(self.multi_progressive_7.num, self.multi_progressive_7.e, self.game).log()*10)
        if log_2==0:
            log_2=self.game.Decimal(1,0,self.game)
        if log_3==0:
            log_3=self.game.Decimal(1,0,self.game)
        log_3/=log_2
        time=self.game.Decimal(self.game.Eternity.time_speed.num,self.game.Eternity.time_speed.e,self.game)
        self.multi_progressive_7+=time*((log_2/log_3)/5+0.0001)
        self.conf_upgrades('MULTI')

    def get_save(self):
        data=''
        data+=str(self.infinities.get_save())+','+str(self.infinity_counter.get_save())+','+str(self.multi_progressive_7.get_save())+','
        data+='['
        for upgrade in self.upgrades:
            print(upgrade)
            data+=upgrade+','
        data+='],'
        data+=str(self.total_count.get_save())+','
        if self.first:
            data+='True\n'
        else:
            data+='\n'
        print(data)
        return data
