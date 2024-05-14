from decimal import Decimal
import math


class Infinity:
    def __init__(self, game):
        self.game = game
        self.infinities = int(self.game.Save.Infinity_data[0][0])
        self.multi_progressive_7=float(self.game.Save.Infinity_data[0][2])
        self.infinity_counter = float(self.game.Save.Infinity_data[0][1])
        self.cost = 1.8e308
        self.income = 1
        self.upgrades = self.game.Save.Infinity_data[0][3]
        self.first = bool(self.game.Save.Infinity_data[0][4])
        self.placed = False

    def place(self):
        self.placed=True
        if self.infinity_counter < 20:
            self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 520, 86,
                                                          anchor='center',
                                                          text='Infinity Count: ' + str(round(self.infinity_counter,2)),
                                                          fill='#d99000', justify='center',
                                                          font=('bahnschrift', 14))
        elif 20 <= self.infinity_counter < 1000:
            self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 520, 86,
                                                          anchor='center',
                                                          text='Infinity Count: \n' + str(
                                                              round(self.infinity_counter, 2)),
                                                          fill='#d99000', justify='center',
                                                          font=('bahnschrift', 14))
        else:
            self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 520, 86,
                                                          anchor='center',
                                                          text='Infinity Count: \n' + "{:.2e}".format(
                                                              Decimal(self.infinity_counter)),
                                                          fill='#d99000', justify='center',
                                                          font=('bahnschrift', 14))
        self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 440, 110,
                                                              self.game.geometry[0] // 2 - 600, 170, width=1,
                                                              fill='black', outline='#ffbc36')
        self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 520, 140,
                                                          anchor='center', justify='center', text='Cost: ' + str(
                "{:.2e}".format(Decimal(self.cost))) + '\nGet ' + str(self.income) + ' IC', fill='#d99000',
                                                          font=('bahnschrift', 10))

    def hide(self):
        self.game.main_canvas.delete(self.upgr_1_text),self.game.main_canvas.delete(self.upgr_2_text)
        self.game.main_canvas.delete(self.upgr_3_text),self.game.main_canvas.delete(self.upgr_4_text)
        self.game.main_canvas.delete(self.upgr_1_box),self.game.main_canvas.delete(self.upgr_2_box)
        self.game.main_canvas.delete(self.upgr_3_box),self.game.main_canvas.delete(self.upgr_4_box)
        self.game.main_canvas.delete(self.upgr_5_box), self.game.main_canvas.delete(self.upgr_5_text)
        self.game.main_canvas.delete(self.upgr_6_box), self.game.main_canvas.delete(self.upgr_6_text)
        self.game.main_canvas.delete(self.upgr_7_box), self.game.main_canvas.delete(self.upgr_7_text)

    def buy(self):
        if self.game.Value.value >= self.cost:
            if self.first:
                self.game.Achievements.get_achieve(10)
            if self.game.Infinity.first and self.game.TA.amount==0:
                self.game.Achievements.get_achieve(13)
            if self.game.Infinity.first and self.game.CB.amount<=4:
                self.game.Achievements.get_achieve(14)
            if self.first == False:
                self.first = True
                self.game.menu_place()
            self.infinities += 1
            if self.infinities==25:
                self.game.Achievements.get_achieve(15)
            self.get_points(self.income*(self.game.Doom.doom_count**0.8)*self.game.Achievements.achieve_mult('IC'))
            self.game.I_reset()
            if self.game.Menu.curMenu=='Infinity':
                self.conf_upgrades()


    def reset(self):
        self.multi_progressive_7=1

    def get_points(self,value):
        self.infinity_counter += value
        if self.infinity_counter < 20:
            self.game.main_canvas.itemconfigure(self.text, text='Infinity Count: ' + str(round(self.infinity_counter,2)))
        elif self.infinity_counter < 1000:
            self.game.main_canvas.itemconfigure(self.text, text='Infinity Count: \n' + str(round(self.infinity_counter,2)))
        else:
            self.game.main_canvas.itemconfigure(self.text, text='Infinity Count: \n' + "{:.2e}".format(
                Decimal(self.infinity_counter)))

    def buy_upgrade(self, index):
        if index == 1 and self.upgrades[0]=='N':
            if self.infinity_counter >= 1:
                self.get_points(-1)
                self.upgrades[0] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_1_box,fill='#c28e0a')
                y = 1
                if self.infinity_counter > 0:
                    y += round((self.infinity_counter / (5 + math.log(self.infinity_counter))), 1)
                if self.infinities > 0:
                    y += round((self.infinities / (5 + math.log(self.infinities))), 1)
                if 0 < y <= 1000:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text,fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(y))
                elif y > 1000:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                            "{:.2e}".format(y)))
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text,fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1')
        elif index == 2 and self.upgrades[1] == 'N':
            if self.infinity_counter >= 2:
                self.get_points(-2)
                self.game.Tickspeed.get_boost(1.25)
                self.upgrades[1] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_2_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_2_text, fill='#4a1111',
                                                    text='Gain multiplier to\n Game Speed * 1.25')
        elif index == 3 and self.upgrades[2] == 'N':
            if self.infinity_counter >= 2:
                self.get_points(-2)
                self.upgrades[2] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_3_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_3_text, fill='#4a1111',
                                                    text='Start any reset\nwith 1e5 C')
        elif index == 4 and self.upgrades[3] == 'N':
            if self.infinity_counter >= 5:
                self.get_points(-5)
                self.upgrades[3] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_4_box, fill='#c28e0a')
                if 10<self.game.Value.value < 1.8e308:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on Count:\n x ' +
                                                             str(round((math.log(self.game.Value.value, 10) ** 0.75),
                                                                       2)))
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on Count:\n x ' + '1')
        elif index == 5 and self.upgrades[4] == 'N':
            if self.infinity_counter >= 10:
                self.get_points(-10)
                self.upgrades[4] = 'Y'
                self.game.Menu.add('doom')
                self.game.main_canvas.itemconfigure(self.upgr_5_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_5_text, fill='#4a1111',
                                                    text='Doom counters unlocked')
                self.game.Achievements.get_achieve(16)
        elif index == 6 and self.upgrades[5] == 'N':
            if self.infinity_counter >= 2:
                self.get_points(-2)
                self.upgrades[5] = 'Y'
                self.game.Automatick.allowed[0]='Y'
                self.game.Automatick.allowed[1] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_6_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_6_text, fill='#4a1111',
                                                    text='Unlocked boost and\ntime auto-blocks')
        elif index == 7 and self.upgrades[6] == 'N':
            if self.infinity_counter >= 4:
                self.get_points(-4)
                self.upgrades[6] = 'Y'
                self.game.main_canvas.itemconfigure(self.upgr_7_box, fill='#c28e0a')
                self.game.main_canvas.itemconfigure(self.upgr_7_text, fill='#4a1111',text=
                                                    'Gain progressive multi\nto 1 counter\nx' + str(round(
                                                        self.multi_progressive_7, 2)))
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
        x = 1
        if self.first:
            x*=1.15
        if self.upgrades[0] == 'Y':
            y=1
            if self.infinity_counter>0:
                y+=round((self.infinity_counter / (5 + math.log(self.infinity_counter))),1)
            if self.infinities>0:
                y+=round((self.infinities / (5 + math.log(self.infinities))), 1)
            x*=y
        if self.upgrades[3] == 'Y':
            if 10 < self.game.Value.value < 1.8e308:
                x *= round((math.log(self.game.Value.value,10)**0.75),2)
            else:
                x *= 1
        if self.upgrades[4] == 'Y':
            x=x/(self.game.Doom.doom_count**0.8)
        if self.game.boost_cheat:
            x*=5
        if '1 counter' in arg:
            if self.upgrades[6] == 'Y':
                x *= self.multi_progressive_7
        return x

    def get_boost_1(self):
        x=1
        if self.upgrades[1] == 'Y':
            x*=1.25
        return x

    def conf_upgrades(self,*args):
        if self.game.Menu.curMenu=='Infinity':
            if self.upgrades[0]=='N':
                y = 1
                if self.infinity_counter > 0:
                    y += round((self.infinity_counter / (5 + math.log(self.infinity_counter))), 1)
                if self.infinities > 0:
                    y += round((self.infinities / (5 + math.log(self.infinities))), 1)
                if 0 < y <= 1000:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#d99000',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                            round(y,1))+ '\nCost: 1 IC')
                elif y > 1000:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#d99000',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                            "{:.2e}".format(y,1))+ '\nCost: 1 IC')
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#d99000',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1'+ '\nCost: 1 IC')
            elif self.upgrades[0]=='Y' and 'VALUE' in args:
                y = 1
                if self.infinity_counter > 0:
                    y += round((self.infinity_counter / (5 + math.log(self.infinity_counter))), 1)
                if self.infinities > 0:
                    y += round((self.infinities / (5 + math.log(self.infinities))), 1)
                if 0 < y <= 1000:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                            round(y,1)))
                elif y > 1000:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                            "{:.2e}".format(y)))
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#4a1111',
                                                        text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1')
            if self.upgrades[3]=='N' and 'VALUE' in args:
                if 10<self.game.Value.value < 1.8e308:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                         str(round((math.log(self.game.Value.value,10)**0.75),2))+'\nCost: 5 IC')
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+'1'+'\nCost: 5 IC')
            elif self.upgrades[3]=='Y' and 'VALUE' in args:
                if 10<self.game.Value.value < 1.8e308:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                         str(round((math.log(self.game.Value.value,10)**0.75),2)))
                else:
                    self.game.main_canvas.itemconfigure(self.upgr_4_text,text='Gain multiplier to counters\nbased on Count:\n x '+'1')
            if self.upgrades[6] == 'N' and 'MULTI' in args:
                self.game.main_canvas.itemconfigure(self.upgr_7_text,text='Gain progressive multi\nto 1 counter\nx' + str(round(
                                                                         self.multi_progressive_7, 2)) + '\nCost: 4 IC')
            elif self.upgrades[6] == 'Y' and 'MULTI' in args:
                self.game.main_canvas.itemconfigure(self.upgr_7_text,
                                                    text='Gain progressive multi\nto 1 counter\nx' + str(round(
                                                        self.multi_progressive_7, 2)))

            ###
        if self.placed:
            if self.income*(self.game.Doom.doom_count**0.8)*self.game.Achievements.achieve_mult('IC')<10000:
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                        "{:.2e}".format(Decimal(self.cost))) + '\nGet ' + str(round(self.income*(self.game.Doom.doom_count**0.8)*self.game.Achievements.achieve_mult('IC'),1)) + ' IC', fill='#d99000')
            else:
                self.game.main_canvas.itemconfigure(self.text_buy, text='Cost: ' + str(
                    "{:.2e}".format(Decimal(self.cost))) + '\nGet ' + str(
                    "{:.2e}".format(Decimal(round(self.income * (self.game.Doom.doom_count ** 0.8)*self.game.Achievements.achieve_mult('IC'), 1)))) + ' IC', fill='#d99000')

    def place_upgrades(self):
        if self.upgrades[0]=='N':
            self.upgr_1_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 210,
                                                                     self.game.geometry[0] // 2 - 300, 310, width=1,
                                                                     fill='black', outline='#e5b045')
            if 0 < self.infinity_counter <= 1000:
                self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                                         round(1 + (self.infinity_counter / (
                                                                                     5 + math.log(self.infinity_counter))),
                                                                               1)) + '\nCost: 1 IC',
                                                                     fill='#d99000', justify='center',
                                                                     font=('bahnschrift', 12))
            else:
                self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1' +'\nCost: 1 IC',
                                                                     fill='#d99000', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.infinity_counter > 1000:
                self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#d99000',
                                                    text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                        "{:.2e}".format(Decimal(1 + (self.infinity_counter / (
                                                                5 + math.log(self.infinity_counter))) +
                                                                                (self.infinities / (
                                                                                        5 + math.log(
                                                                                    self.infinities)))))))
        else:
            self.upgr_1_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 210,
                                                                     self.game.geometry[0] // 2 - 300, 310, width=1,
                                                                     fill='#c28e0a', outline='#e5b045')
            if 0 < self.infinity_counter <= 1000:
                self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                                         round(1 + (self.infinity_counter / (
                                                                                 5 + math.log(self.infinity_counter))),
                                                                               1)),fill='#4a1111'
                                                                     , justify='center',
                                                                     font=('bahnschrift', 12))
            else:
                self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 400, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x 1',
                                                                     fill='#4a1111', justify='center',
                                                                     font=('bahnschrift', 12))
            if self.infinity_counter > 1000:
                self.game.main_canvas.itemconfigure(self.upgr_1_text, fill='#4a1111',
                                                    text='Gain multiplier to counters\nbased on IC\nand Infinities:\n x' + str(
                                                        "{:.2e}".format(Decimal(1 + (self.infinity_counter / (
                                                                5 + math.log(self.infinity_counter))) +
                                                                                (self.infinities / (
                                                                                        5 + math.log(
                                                                                    self.infinities)))))))

        if self.upgrades[1] == 'N':
            self.upgr_2_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 250, 210,
                                                                     self.game.geometry[0] // 2 - 50, 310, width=1,
                                                                     fill='black', outline='#e5b045')
            self.upgr_2_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 150, 260,
                                                                 anchor='center',
                                                                 text='Gain multiplier to\n Game Speed * 1.25' + '\nCost: 2 IC',
                                                                     fill='#d99000', justify='center',
                                                                     font=('bahnschrift', 12))
        else:
            self.upgr_2_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 250, 210,
                                                                     self.game.geometry[0] // 2 - 50, 310, width=1,
                                                                     fill='#c28e0a', outline='#e5b045')
            self.upgr_2_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 150, 260,
                                                                 anchor='center',
                                                                 text='Gain multiplier to\n Game Speed * 1.25',
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
            if 10<self.game.Value.value < 1.8e308:
                self.upgr_4_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                     str(round((math.log(self.game.Value.value,10)**0.75),2))+'\nCost: 5 IC',
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
            if 10<self.game.Value.value < 1.8e308:
                self.upgr_4_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 400, 260,
                                                                     anchor='center',
                                                                     text='Gain multiplier to counters\nbased on Count:\n x '+
                                                                     str(round((math.log(self.game.Value.value,10)**0.75),2)),
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
                                                                 text='Gain progressive multi\nto 1 counter\nx'+str(round(self.multi_progressive_7,2))+'\nCost: 4 IC',
                                                                     fill='#d99000', justify='center',
                                                                     font=('bahnschrift', 12))
        else:
            self.upgr_7_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 350, 330,
                                                                     self.game.geometry[0] // 2 + 150, 430, width=1,
                                                                     fill='#c28e0a', outline='#e5b045')
            self.upgr_7_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 250, 380,
                                                                 anchor='center',
                                                                 text='Gain progressive multi\nto 1 counter\nx' + str(round(self.multi_progressive_7,2)),
                                                                 fill='#4a1111', justify='center',
                                                                 font=('bahnschrift', 12))

    def other_funcs(self):
        self.multi_progressive_7+=math.log(self.multi_progressive_7+1,(self.multi_progressive_7*50)**(1.6+self.multi_progressive_7/100))/20
        self.conf_upgrades('MULTI')

    def get_save(self):
        data=''
        data+=str(self.infinities)+','+str(self.infinity_counter)+','+str(self.multi_progressive_7)+','
        data+='['
        for upgrade in self.upgrades:
            print(upgrade)
            data+=upgrade+','
        data+='],'
        if self.first:
            data+='True\n'
        else:
            data+='\n'
        print(data)
        return data
