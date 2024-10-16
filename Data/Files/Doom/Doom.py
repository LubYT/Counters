import random
from decimal import Decimal
from tkinter import *
import math

class Doom:
    def __init__(self,game):
        self.images=[PhotoImage(file='Data/Files/images/play_dd.png'),PhotoImage(file='Data/Files/images/stop_dd.png')]
        self.game=game
        self.doom_count=self.game.Decimal(self.game.Save.Doom_data[0][0][0],int(self.game.Save.Doom_data[0][0][1]),self.game,'Doom')
        self.doom_total=self.game.Decimal(self.game.Save.Doom_data[0][1][0],int(self.game.Save.Doom_data[0][1][1]),self.game,'Doom')
        print('ddoom')
        print(self.game.Save.Doom_data)
        print(self.game.Save.Doom_data[0])
        print(self.game.Save.Doom_data[0][6])
        print(self.game.Save.Doom_data[0][2][0])
        print((self.doom_count.get(2, 0)))
        self.doom_counter_1 = self.game.Decimal(self.game.Save.Doom_data[0][2][0],int(self.game.Save.Doom_data[0][2][1]),self.game,'Doom')
        self.doom_counter_2 = self.game.Decimal(self.game.Save.Doom_data[0][3][0],int(self.game.Save.Doom_data[0][3][1]),self.game,'Doom')
        self.doom_counter_3 = self.game.Decimal(self.game.Save.Doom_data[0][4][0],int(self.game.Save.Doom_data[0][4][1]),self.game,'Doom')
        self.doom_counter_4 = self.game.Decimal(self.game.Save.Doom_data[0][5][0],int(self.game.Save.Doom_data[0][5][1]),self.game,'Doom')
        self.multies=[self.game.Decimal(self.game.Save.Doom_data[0][7][0],int(self.game.Save.Doom_data[0][7][1]),self.game,'Doom'),
                      self.game.Decimal(self.game.Save.Doom_data[0][8][0],int(self.game.Save.Doom_data[0][8][1]),self.game,'Doom'),
                      self.game.Decimal(self.game.Save.Doom_data[0][9][0],int(self.game.Save.Doom_data[0][9][1]),self.game,'Doom'),
                      self.game.Decimal(self.game.Save.Doom_data[0][10][0],int(self.game.Save.Doom_data[0][10][1]),self.game,'Doom')]
        self.costs=[self.game.Decimal(self.game.Save.Doom_data[0][12][0],int(self.game.Save.Doom_data[0][12][1]),self.game,'Doom'),
                    self.game.Decimal(self.game.Save.Doom_data[0][13][0],int(self.game.Save.Doom_data[0][13][1]),self.game,'Doom'),
                    self.game.Decimal(self.game.Save.Doom_data[0][14][0],int(self.game.Save.Doom_data[0][14][1]),self.game,'Doom'),
                    self.game.Decimal(self.game.Save.Doom_data[0][15][0],int(self.game.Save.Doom_data[0][15][1]),self.game,'Doom')]
        self.up_costs=[5,25,500,10000]
        self.bought_counter=[self.game.Decimal(self.game.Save.Doom_data[0][17][0],int(self.game.Save.Doom_data[0][17][1]),self.game,'Doom'),
                             self.game.Decimal(self.game.Save.Doom_data[0][18][0],int(self.game.Save.Doom_data[0][18][1]),self.game,'Doom'),
                             self.game.Decimal(self.game.Save.Doom_data[0][19][0],int(self.game.Save.Doom_data[0][19][1]),self.game,'Doom'),
                             self.game.Decimal(self.game.Save.Doom_data[0][20][0],int(self.game.Save.Doom_data[0][20][1]),self.game,'Doom')]
        self.produce_1=0.05
        self.produce_2 = 0.05
        self.produce_3 = 0.05
        self.produce_4 = 0.05
        self.mult_inf=0.8
        self.mult_doom=0.8
        self.main_texts=[]
        self.count_text=[]
        self.sub_texts=[]
        self.boxes=[]
        self.shop_boxes=[]
        self.len=0
        self.cur_word=[0,'-',60,60]
        self.total_upgrades=[0,0,0,0]
        self.upgrades_costs_up = [1e10, 1e15, 1e8, 1e15]
        reward_1=(self.upgrades_costs_up[0]**self.total_upgrades[0])
        reward_2 =(self.upgrades_costs_up[1]**self.total_upgrades[1])
        reward_3 =(self.upgrades_costs_up[2]**self.total_upgrades[2])
        reward_4 =(self.upgrades_costs_up[3]**self.total_upgrades[3])
        self.upgrades_costs=[1e52*reward_1,1e52*reward_2
            ,1e55*reward_3,1e60*reward_4]
        self.dc_mult=1
        self.upgrader_dc_mult = 2.5
        self.letters=['Δ','Ε','Κ','Λ','Τ','Υ','Ψ','Ω','α','β','γ','ζ','ι',
                      'κ','λ','ν','ξ','σ','χ','￡','ȵ','₰','ᖘ','Θ','Ꮹ','φ',
                      '⥉','ಭ','Ϡ','ᛃ','⌘','ꔆ','ꔙ','ꕫ','ꖢ','ꖴ','꘨']
        for i in range(self.total_upgrades[2]):
            self.dc_mult*=self.upgrader_dc_mult
            self.upgrader_dc_mult+=0.3
        self.mult_doom-=self.total_upgrades[0]*0.02
        self.mult_inf += self.total_upgrades[1] * 0.02
        self.auto_pause='disabled'
        self.auto_pause_num='input'
        if self.auto_pause=='enabled':
            self.color_auto_pause_text='#5bc77a'
        else:
            self.color_auto_pause_text = '#c75b5b'
        self.curbar='N'
        self.colors=['#606060','#404040','#202020']
        self.text='Doomed Destruction'
        self.active=bool(self.game.Save.Doom_data[0][22])

    def init_text(self):
        self.len = 0
        for font_size in range(3):
            print(font_size)
            x = -270
            list = []
            list_2 = []
            for symbol in self.text:
                list.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + x, 240, anchor='center',
                                                              text=symbol,
                                                              fill=self.colors[font_size], justify='center',
                                                              font=('bahnschrift', (30 - font_size * 5))))
                x += 30
            x = 0 - (len(self.doom_count.get(2,0))*20)
            print(self.doom_count.get(2,0))
            for letter in (self.doom_count.get(2,0)):
                list_2.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + x, 300, anchor='center',
                                                                text=letter,
                                                                fill=self.colors[font_size], justify='center',
                                                                font=('bahnschrift', (40 - font_size * 8))))
                x += 40
                self.len += 1
            self.count_text.append(list_2)
            self.main_texts.append(list)
            print(self.count_text)
            print(self.main_texts)
        self.len /= 3

    def place(self):
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            self.init_text()
            if not (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 1):
                self.sub_texts.append(self.game.main_canvas.create_text(self.game.geometry[0]//2,350,anchor='center',
                                                              text='Doomed destruction decrease counters production, but increase infinity count gain.',
                                                              fill=self.colors[0], justify='center',
                                                              font=('bahnschrift', 12)))
            else:
                self.sub_texts.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2, 350, anchor='center',
                                                                        text='Doomed destruction obeys Illusion. It buffs counters production',
                                                                        fill=self.colors[0], justify='center',
                                                                        font=('bahnschrift', 12)))
            dc = self.game.Decimal(self.game.Doom.doom_count.num, self.game.Doom.doom_count.e, self.game)**0.8
            self.text_1=self.game.main_canvas.create_text(self.game.geometry[0]//2,390,anchor='center',
                                                              text='Power of doomed destruction:\n'+dc.get(2,4),
                                                              fill=self.colors[0], justify='center',
                                                              font=('bahnschrift', 12))
            self.button_active=self.game.main_canvas.create_rectangle(self.game.geometry[0]//2+349, 229, self.game.geometry[0] // 2 + 401, 281, width=1,
                                                   fill='#0a0000', outline='#380000')
            if self.active:
                self.image_active=self.game.main_canvas.create_image(self.game.geometry[0]//2+375,255,anchor='center',image=self.images[1])
            else:
                self.image_active = self.game.main_canvas.create_image(self.game.geometry[0] // 2 + 375, 255, anchor='center',
                                                                       image=self.images[0])
            self.button_auto_pause = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 330, 290,
                                                                        self.game.geometry[0] // 2 + 420, 390, width=1,
                                                                        fill='#0a0000', outline='#380000')
            self.text_auto_pause = self.game.main_canvas.create_text(self.game.geometry[0] // 2+ 375, 293, anchor='n',
                                                            text='Limit\n'+self.auto_pause+' on:\n'+'\n\n'+'DD',
                                                            fill=self.color_auto_pause_text, justify='center',
                                                            font=('bahnschrift', 12))
            self.button_auto_pause_input = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 340, 335,
                                                                            self.game.geometry[0] // 2 + 410, 366, width=1,
                                                                            fill='#0a0000', outline='#380000')
            self.text_auto_pause_input = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 375, 350, anchor='center',
                                                                     text=self.auto_pause_num,
                                                                     fill='#606060', justify='center',
                                                                     font=('bahnschrift', 12))
            self.button_max = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 330, 390,
                                                                                  self.game.geometry[0] // 2 - 410, 340,
                                                                                  width=1,fill='#121212', outline='#3b0000')
            self.text_max = self.game.main_canvas.create_text(self.game.geometry[0] // 2 -370, 365,
                                                                           anchor='center',
                                                                           text='Max all DC',
                                                                           fill='#7d0000', justify='center',
                                                                           font=('bahnschrift', 12))
            self.game.window.bind("<KeyPress>",self.add_symbol)
            self.place_shop()
            self.place_counters()
        else:
            self.text_1 = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 290, anchor='center',
                                                            text='Illusion\nThere is no Doom',
                                                            fill='#36ffe7', justify='center',
                                                            font=('bahnschrift', 30))

    def produce(self):
        if self.game.Value.lock==False and self.active:
            self.produce_counts()
            self.conf_counters()

    def add_symbol(self,event):
        if self.curbar!='N':
            try:
                if (int(event.keysym) < 10 and int(event.keysym) > -1) and len(str(self.auto_pause_num))<=8:
                    if self.auto_pause_num[:1:] == 'i':
                        self.auto_pause_num = ''
                    elif self.auto_pause_num == '0':
                        self.auto_pause_num = ''
                    self.auto_pause_num += str(event.keysym)
                    self.game.main_canvas.itemconfigure(self.curbar,
                                                        text=self.auto_pause_num)
            except:
                if event.keysym == 'BackSpace' and self.auto_pause_num != '':
                    if self.auto_pause_num[:1:] == 'i':
                        self.auto_pause_num = '0'
                    self.auto_pause_num = self.auto_pause_num[:-1:]
                    if self.auto_pause_num == '':
                        self.auto_pause_num = '0'
                    self.game.main_canvas.itemconfigure(self.curbar,
                                                            text=self.auto_pause_num)
                elif event.keysym == 'e' and self.auto_pause_num != '' and len(str(self.auto_pause_num))<=8:
                    if self.auto_pause_num[:1:] == 'i':
                        self.auto_pause_num = '0'
                    if self.auto_pause_num!='0':
                        self.auto_pause_num += str(event.keysym)
                        self.game.main_canvas.itemconfigure(self.curbar,
                                                            text=self.auto_pause_num)
            try:
                if (self.auto_pause_num != '' and self.auto_pause_num[-1::]!='e') or self.auto_pause_num[-2::]=='ee':
                    float(self.auto_pause_num)
                    self.game.main_canvas.itemconfigure(self.curbar,fill='#606060')
            except:
                if event.keysym!='BackSpace':
                    self.auto_pause_num = self.auto_pause_num[:-1:]
                    self.game.main_canvas.itemconfigure(self.curbar,
                                                        text=self.auto_pause_num)
            try:
                float(self.auto_pause_num)
                self.game.main_canvas.itemconfigure(self.curbar, fill='#606060')
            except:
                self.game.main_canvas.itemconfigure(self.curbar, fill='#c75b5b')
    def produce_counts(self):
        if not (self.game.Aspects.active == True and self.game.Aspects.cur_ill == 3):
            base = self.game.Decimal(1, 0, self.game)
            income=(base*self.doom_counter_1*self.game.Eternity.time_speed*self.produce_1*self.get_extra_mult(1))/20
            if len(self.doom_count.get(2,0))!=self.len and self.game.Menu.curMenu=='Doom':
                self.hide_text()
                self.init_text()
            self.get_doomed_count(income)
            base=self.game.Decimal(1,0,self.game)
            self.doom_counter_1+=(base*self.doom_counter_2*self.game.Eternity.time_speed*self.produce_2*self.get_extra_mult(2))/20
            if self.doom_counter_1>1.79e308:
                self.doom_counter_1=self.game.Decimal(1.79, 308, self.game,'Doom')
            base = self.game.Decimal(1, 0, self.game)
            self.doom_counter_2 += (base*self.doom_counter_3*self.game.Eternity.time_speed * self.produce_3*self.get_extra_mult(3)) / 20
            if self.doom_counter_2>1.79e308:
                self.doom_counter_2=self.game.Decimal(1.79, 308, self.game,'Doom')
            base = self.game.Decimal(1, 0, self.game)
            self.doom_counter_3 += (base*self.doom_counter_4*self.game.Eternity.time_speed * self.produce_4*self.get_extra_mult(4)) / 20
            if self.doom_counter_3>1.79e308:
                self.doom_counter_3=self.game.Decimal(1.79, 308, self.game,'Doom')

    def get_extra_mult(self,arg):
        x=self.game.Decimal(1, 0, self.game)
        x*=self.game.Aspects.reward_1
        x*=self.dc_mult
        x*=self.multies[arg-1]
        if self.game.Eternity.upgrades[1]=='Y':
            y=self.game.Decimal(1,0,self.game)
            ec = self.game.Decimal(self.game.Eternity.eternity_count.num, self.game.Eternity.eternity_count.e, self.game)
            if self.game.Eternity.eternity_count > 0:
                y += ec ** 0.4 / 10
            e = self.game.Decimal(self.game.Eternity.eternities.num, self.game.Eternity.eternities.e, self.game)
            if self.game.Eternity.eternities > 0:
                y += e ** 0.5 / 10
            x*=y
        if arg==1:
            if self.game.Infinity.upgrades[10]=='Y':
                time=self.game.Stats.time_total[2]
                for i in range(self.game.Stats.time_total[1]):
                    time+=60
                for i in range(self.game.Stats.time_total[0]):
                    time+=1440
                x*=time**0.4
            if self.game.Infinity.upgrades[8] == 'Y':
                inf = self.game.Decimal(self.game.Infinity.infinities.num, self.game.Infinity.infinities.e, self.game) ** 1.3
                if inf < 1:
                    inf = self.game.Decimal(1, 0, self.game)
                x*=inf
        return x

    def reset(self,*args):
        self.get_doomed_count('1')
        if 'full' in args:
            self.doom_total = self.game.Decimal(1,0,self.game,'Doom')
            self.doom_counter_1 = self.game.Decimal(0,0,self.game,'Doom')
            self.doom_counter_2 = self.game.Decimal(0,0,self.game,'Doom')
            self.doom_counter_3 = self.game.Decimal(0,0,self.game,'Doom')
            self.doom_counter_4 = self.game.Decimal(0,0,self.game,'Doom')
            self.mult_inf = 0.8
            self.mult_doom = 0.8
            self.multies = [self.game.Decimal(1,0,self.game,'Doom'),self.game.Decimal(1,0,self.game,'Doom'),self.game.Decimal(1,0,self.game,'Doom'),self.game.Decimal(1,0,self.game,'Doom')]
            self.costs = [self.game.Decimal(1,0,self.game,'Doom'),self.game.Decimal(5,0,self.game,'Doom'),self.game.Decimal(2.5,2,self.game,'Doom'),self.game.Decimal(1,4,self.game,'Doom')]
            self.up_costs = [self.game.Decimal(5,0,self.game,'Doom'), self.game.Decimal(2.5,1,self.game,'Doom'), self.game.Decimal(5,2,self.game,'Doom'), self.game.Decimal(1,4,self.game,'Doom')]
            self.bought_counter = [self.game.Decimal(0,0,self.game,'Doom'),self.game.Decimal(0,0,self.game,'Doom'),self.game.Decimal(0,0,self.game,'Doom'),self.game.Decimal(0,0,self.game,'Doom')]
            self.total_upgrades = [0, 0, 0, 0]
            self.upgrades_costs_up = [1e10, 1e15, 1e8, 1e15]
            reward_1 = (self.upgrades_costs_up[0] ** self.total_upgrades[0])
            reward_2 = (self.upgrades_costs_up[1] ** self.total_upgrades[1])
            reward_3 = (self.upgrades_costs_up[2] ** self.total_upgrades[2])
            reward_4 = (self.upgrades_costs_up[3] ** self.total_upgrades[3])
            self.upgrades_costs = [1e52 * reward_1, 1e52 * reward_2
                , 1e55 * reward_3, 1e60 * reward_4]
            self.doom_count = self.game.Decimal(1,0,self.game)
        else:
            self.doom_counter_1=self.bought_counter[0]
            self.doom_counter_2 = self.bought_counter[1]
            self.doom_counter_3 = self.bought_counter[2]
            self.doom_counter_4 = self.bought_counter[3]
        if 'full' in args:
            if self.game.Menu.curMenu=='Doom':
                self.game.Menu.stage_get(change='doom')
        self.conf_counters()


    def get_doomed_count(self,amount):
        if amount!='1':
            self.game.Achievements.get_achieve(18)
            amm = amount * self.game.Achievements.achieve_mult('DD')
            self.doom_count+=amm
        else:
            amm = 0
            self.doom_total+=1
            self.doom_count=self.game.Decimal(1,0,self.game,'Doom')
        if not (self.game.Aspects.active==True and self.game.Aspects.cur_ill==2) and not (self.game.Aspects.active==True and self.game.Aspects.cur_ill==3):
            try:
                if float(self.auto_pause_num)>=1:
                    if self.auto_pause=='enabled' and float(self.auto_pause_num)<=self.doom_count:
                        self.doom_count.maker_from_float(float(self.auto_pause_num))
                elif float(self.auto_pause_num)==0:
                    if self.auto_pause=='enabled' and float(self.auto_pause_num)<=self.doom_count:
                        self.doom_count=self.game.Decimal(1,0,self.game,'Doom')
                else:
                    self.doom_count=self.game.Decimal(1,0,self.game,'Doom')
            except ValueError:
                pass
            if self.doom_count!=1 or self.auto_pause=='disabled':
                self.doom_total += amm
            if self.doom_count>=1e8:
                self.game.Achievements.get_achieve(20)
                if self.doom_count>=1e15:
                    self.game.Achievements.get_achieve(24)
            if self.doom_count>1.79e308:
                self.doom_count=self.game.Decimal(1.79,308,self.game,'Doom')
            if self.doom_total>1.79e308:
                self.doom_total=self.game.Decimal(1.79,308,self.game,'Doom')
        else:
            if self.game.Aspects.cur_ill==2:
                self.doom_count.maker_from_float(self.game.Aspects.conditions_2[self.game.Aspects.completions_2][1])
            if self.game.Aspects.cur_ill == 3:
                self.doom_count=self.game.Decimal(1,0,self.game,'Doom')
        if self.game.Menu.curMenu=='Doom' and not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if not (self.game.Aspects.active==True and self.game.Aspects.cur_ill==1):
                if self.mult_inf == self.mult_doom:
                    dc = self.game.Decimal(self.doom_count.num, self.doom_count.e, self.game, 'Doom') ** self.mult_doom
                    self.game.main_canvas.itemconfigure(self.text_1,text='Power of doomed destruction:\n'+ self.doom_count.get(2,4) + ' ^ ' + str(round(self.mult_doom,2)) + ' = ' +dc.get(2,4))
                else:
                    dc=self.game.Decimal(self.doom_count.num,self.doom_count.e,self.game,'Doom')** self.mult_doom
                    dc1 = self.game.Decimal(self.doom_count.num, self.doom_count.e, self.game, 'Doom') ** self.mult_inf
                    self.game.main_canvas.itemconfigure(self.text_1, text='Power of doomed destruction:\nCounters: ' + self.doom_count.get(2,4) + ' ^ ' + str(round(self.mult_doom,2)) + ' = ' +dc.get(2,4)
                        +'\nIC: '+ self.doom_count.get(2,4) + ' ^ ' + str(round(self.mult_inf,2)) + ' = ' + dc1.get(2,4))
            else:
                dc = self.game.Decimal(self.doom_count.num, self.doom_count.e, self.game, 'Doom') ** 0.2
                self.game.main_canvas.itemconfigure(self.text_1, text='Power of doomed destruction:\n' + self.doom_count.get(2,4) + ' ^ ' + str(0.2) + ' = ' + dc.get(2,4))
            text_0=str(self.doom_count.get(2,0))
            try:
                for letter in self.count_text:
                    y = 0
                    for letter_2 in letter:
                        letter_1=text_0[y]
                        self.game.main_canvas.itemconfigure(letter_2,text=str(letter_1))
                        y+=1
            except:
                self.hide_text()
                self.init_text()


            y_3 = 60
            if self.cur_word[1] == '-':
                self.cur_word[2] -= 3
                self.cur_word[3] -= 3
                if self.cur_word[2] == 0:
                    self.cur_word[1] = '+'
            elif self.cur_word[1] == '+':
                self.cur_word[2] += 3
                self.cur_word[3] += 3
                if self.cur_word[2] == 60:
                    self.cur_word[1] = '/'
            elif self.cur_word[1]=='/':
                self.cur_word[1]='-'
                self.cur_word[0] += 1
            if self.cur_word[0]>17:
                self.cur_word[0]=0


            for letter in self.main_texts:
                y = 0
                for letter_2 in letter:
                    if y == self.cur_word[0]:
                        if self.cur_word[2] < 10:
                            word_1 = '0' + str(self.cur_word[2])
                        else:
                            word_1 = str(self.cur_word[2])
                        if self.cur_word[3] < 10:
                            word_2 = '0' + str(self.cur_word[3])
                        else:
                            word_2 = str(self.cur_word[3])
                        if self.cur_word[2] > y_3:
                            word_1=str(y_3)
                        if self.cur_word[3] > y_3:
                            word_2=str(y_3)
                        self.game.main_canvas.itemconfigure(letter_2,fill='#'+str(y_3)+word_1+word_2)
                    y += 1

                y_3 -= 20
            if self.game.Aspects.completion_3==False:
                for text in self.shop_boxes[3]:
                    symbols=''
                    for i in range(random.randint(4,6)):
                        symbols+=random.choice(self.letters)
                    self.game.main_canvas.itemconfigure(text, text=symbols)




    def hide_text(self):
        for list_s in self.main_texts:
            for list in list_s:
                self.game.main_canvas.delete(list)
        for text in self.count_text:
            for letter in text:
                self.game.main_canvas.delete(letter)
        self.main_texts,self.count_text=[],[]

    def hide(self):
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            self.hide_text()
            self.hide_shop()
            self.game.window.unbind('<KeyPress>')
            self.game.main_canvas.delete(self.text_1)
            for text in self.sub_texts:
                self.game.main_canvas.delete(text)
            for list in self.boxes:
                if self.boxes.index(list)!=3:
                    for item in list:
                        self.game.main_canvas.delete(item)
                else:
                    for list_2 in list:
                        self.game.main_canvas.delete(list_2[0]),self.game.main_canvas.delete(list_2[1])
            self.game.main_canvas.delete(self.image_active),self.game.main_canvas.delete(self.button_active)
            self.game.main_canvas.delete(self.text_auto_pause_input),self.game.main_canvas.delete(self.button_auto_pause_input)
            self.game.main_canvas.delete(self.text_auto_pause), self.game.main_canvas.delete(self.button_auto_pause)
            self.game.main_canvas.delete(self.text_max), self.game.main_canvas.delete(self.button_max)
            self.boxes=[]
        else:
            self.game.main_canvas.delete(self.text_1)

    def hide_shop(self):
        for item in self.shop_boxes:
            for i in item:
                self.game.main_canvas.delete(i)
        self.shop_boxes=[]

    def place_shop(self):
        box=[]
        box.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 475, 620, self.game.geometry[0] // 2 - 275, 720, width=2,
                                                          fill='#121212', outline='#690000'))
        box.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 225, 620,
                                                          self.game.geometry[0] // 2 - 25, 720, width=2,
                                                          fill='#121212', outline='#690000'))
        box.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 225, 620,
                                                          self.game.geometry[0] // 2 + 25, 720, width=2,
                                                          fill='#121212', outline='#690000'))
        box.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 475, 620,
                                                          self.game.geometry[0] // 2 + 275, 720, width=2,
                                                          fill='#121212', outline='#690000'))
        scales = []
        scales.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 475, 700,
                                                             self.game.geometry[0] // 2 - 275, 720, width=2,
                                                             fill='#121212', outline='#690000'))
        scales.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 225, 700,
                                                             self.game.geometry[0] // 2 - 25, 720, width=2,
                                                             fill='#121212', outline='#690000'))
        scales.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 225, 700,
                                                             self.game.geometry[0] // 2 + 25, 720, width=2,
                                                             fill='#121212', outline='#690000'))
        scales.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 475, 700,
                                                             self.game.geometry[0] // 2 + 275, 720, width=2,
                                                             fill='#121212', outline='#690000'))
        scales_true=[]
        scales_true.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 475, 700,
                                                             self.game.geometry[0] // 2 - 275-((10-self.total_upgrades[0])*20), 719, width=1,
                                                             fill='#ff7a7a', outline='#690000'))
        scales_true.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 225, 700,
                                                             self.game.geometry[0] // 2 - 25-((10-self.total_upgrades[1])*20), 719, width=1,
                                                             fill='#ff7a7a', outline='#690000'))
        scales_true.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 225-((10-self.total_upgrades[2])*20), 700,
                                                             self.game.geometry[0] // 2 + 25, 719, width=1,
                                                             fill='#ff7a7a', outline='#690000'))
        scales_true.append(self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 475 - ((10 - self.total_upgrades[3]) * 20), 700,
                                                             self.game.geometry[0] // 2 + 275, 719, width=1,
                                                             fill='#ff7a7a', outline='#690000'))
        text=[]
        if self.game.Aspects.completion_3:
            if self.total_upgrades[0]<10:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0]//2-375,660,anchor='center',
                                                                      text='Formula DD for counters:\n'+str(round(self.mult_doom,2))+' → '+str(round(self.mult_doom-0.02,2))+'\nCost DD: '+str("{:.2e}".format(Decimal(self.upgrades_costs[0]))),
                                                                      fill='#941313', justify='center',
                                                                      font=('bahnschrift', 12)))
            else:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 375, 660, anchor='center',
                                                              text='Formula DD for counters:\n' + str(
                                                                  round(self.mult_doom, 2)),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
            if self.total_upgrades[1] < 10:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 125, 660, anchor='center',
                                                              text='Formula DD for IC:\n' + str(
                                                                  round(self.mult_inf, 2)) + ' → ' + str(
                                                                  round(self.mult_inf + 0.02, 2)) + '\nCost DD: ' + str(
                                                                  "{:.2e}".format(Decimal(self.upgrades_costs[1]))),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
            else:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 125, 660, anchor='center',
                                                              text='Formula DD for IC:\n' + str(
                                                                  round(self.mult_inf, 2)),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
            if self.total_upgrades[2] < 10:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 125, 660, anchor='center',
                                                              text='Gain multi for DC:\n' + str(
                                                                  round(self.dc_mult, 1)) + ' → ' + str(
                                                                  round(self.dc_mult*self.upgrader_dc_mult,1)) + '\nCost DD: ' + str(
                                                                  "{:.2e}".format(Decimal(self.upgrades_costs[2]))),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
            else:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 125, 660, anchor='center',
                                                              text='Gain multi for DC:\n' + str(
                                                                  round(self.dc_mult, 1)),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
            if self.total_upgrades[3] < 10:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 375, 660, anchor='center',
                                                              text='Decrease automatick\nprogramm cooldown:\n'+str(round(self.game.Automatick.time_cycle/1000,2))+ ' → ' +str(round((self.game.Automatick.time_cycle-150)/1000,2))+' seconds'+ '\nCost DD: ' + str(
                                                                  "{:.2e}".format(Decimal(self.upgrades_costs[3]))),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
            else:
                text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 375, 660, anchor='center',
                                                              text='Decrease automatick\nprogramm cooldown:\n' + str(
                                                                  round(self.game.Automatick.time_cycle / 1000,
                                                                        2)),
                                                              fill='#941313', justify='center',
                                                              font=('bahnschrift', 12)))
        else:
            text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 375, 660, anchor='center',text='&&&&',fill='#941313', justify='center',font=('bahnschrift', 12)))
            text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 125, 660, anchor='center', text='&&&&',fill='#941313', justify='center', font=('bahnschrift', 12)))
            text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 125, 660, anchor='center', text='&&&&',fill='#941313', justify='center', font=('bahnschrift', 12)))
            text.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 375, 660, anchor='center', text='&&&&',fill='#941313', justify='center', font=('bahnschrift', 12)))
        self.shop_boxes.append(box),self.shop_boxes.append(scales),self.shop_boxes.append(scales_true),self.shop_boxes.append(text)

    def place_counters(self):
        box=[]
        box.append(self.game.main_canvas.create_rectangle(130, 430,self.game.geometry[0] // 2 -10, 500,width=1,
                                                            fill='#121212', outline='#3b0000'))
        box.append(
            self.game.main_canvas.create_rectangle(self.game.geometry[0]-130, 430, self.game.geometry[0] // 2 + 10, 500, width=1,
                                               fill='#121212', outline='#3b0000'))
        box.append(
            self.game.main_canvas.create_rectangle(130, 510, self.game.geometry[0] // 2 - 10, 580, width=1,
                                               fill='#121212', outline='#3b0000'))
        box.append(
            self.game.main_canvas.create_rectangle(self.game.geometry[0] - 130, 510, self.game.geometry[0] // 2 + 10, 580,
                                               width=1,
                                               fill='#121212', outline='#3b0000'))
        self.boxes.append(box)
        counters_values=[]
        counters_values.append(self.game.main_canvas.create_text(150, 455,
                                                                     anchor='w',
                                                                     text=self.doom_counter_1.get(2,4),
                                                                     fill='#7d0000', justify='center',
                                                                     font=('bahnschrift', 18)))
        counters_values.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 30, 455,
                                                                         anchor='w',
                                                                         text=self.doom_counter_2.get(2,4),
                                                                         fill='#7d0000', justify='center',
                                                                         font=('bahnschrift', 18)))
        counters_values.append(self.game.main_canvas.create_text(150, 535,
                                                                         anchor='w',
                                                                         text=self.doom_counter_3.get(2,4),
                                                                         fill='#7d0000', justify='center',
                                                                         font=('bahnschrift', 18)))
        counters_values.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 30, 535,
                                                                     anchor='w',
                                                                     text=self.doom_counter_4.get(2,4),
                                                                     fill='#7d0000', justify='center',
                                                                     font=('bahnschrift', 18)))
        self.boxes.append(counters_values)
        multies=[]
        multies.append(self.game.main_canvas.create_text(150, 480,
                                                                         anchor='w',
                                                                         text='x'+self.get_extra_mult(1).get(2,4),
                                                                         fill='#7d0000', justify='center',
                                                                         font=('bahnschrift', 12)))
        multies.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 30, 480,
                                                                     anchor='w',
                                                                     text='x' +self.get_extra_mult(2).get(2,4),
                                                                     fill='#7d0000', justify='center',
                                                                     font=('bahnschrift', 12)))
        multies.append(self.game.main_canvas.create_text(150, 560,
                                                                     anchor='w',
                                                                     text='x'+self.get_extra_mult(3).get(2,4),
                                                                     fill='#7d0000', justify='center',
                                                                     font=('bahnschrift', 12)))
        multies.append(self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 30, 560,
                                                                     anchor='w',
                                                                     text='x' +self.get_extra_mult(4).get(2,4),
                                                                     fill='#7d0000', justify='center',
                                                                     font=('bahnschrift', 12)))
        self.boxes.append(multies)

        boxes_2=[]
        boxes_2.append([self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 200, 440,
                                                                   self.game.geometry[0] // 2 - 20, 490, width=1,
                                                                   fill='#470404', outline='#823535'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 195, 465,
                                                              anchor='w',
                                                              text='Cost: ' +self.costs[0].get(2,4)+' IC',
                                                              fill='#000', justify='center',
                                                              font=('bahnschrift', 14))
                            ])
        boxes_2.append([self.game.main_canvas.create_rectangle(self.game.geometry[0] - 140, 440, self.game.geometry[0] - 320, 490, width=1,
                                                                   fill='#470404', outline='#823535'),
            self.game.main_canvas.create_text(self.game.geometry[0]- 315, 465,
                                                              anchor='w',
                                                              text='Cost: ' + self.costs[1].get(2,4)+' IC',
                                                              fill='#000', justify='center',
                                                              font=('bahnschrift', 14))
                            ])

        boxes_2.append([self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 200, 520,
                                                                   self.game.geometry[0] // 2 - 20, 570, width=1,
                                                                   fill='#470404', outline='#823535'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 195, 545,
                                                              anchor='w',
                                                              text='Cost: ' + self.costs[2].get(2,4)+' IC',
                                                              fill='#000', justify='center',
                                                              font=('bahnschrift', 14))
                            ])
        boxes_2.append([self.game.main_canvas.create_rectangle(self.game.geometry[0] - 140, 520, self.game.geometry[0] - 320, 570, width=1,
                                                                   fill='#470404', outline='#823535'),
                self.game.main_canvas.create_text(self.game.geometry[0]- 315, 545,
                                                              anchor='w',
                                                              text='Cost: ' + self.costs[3].get(2,4)+' IC',
                                                              fill='#000', justify='center',
                                                              font=('bahnschrift', 14))
                            ])
        self.boxes.append(boxes_2)

    def max_dc(self):
        while self.game.Infinity.infinity_counter>=self.costs[0]:
            self.buy_counter(0)
        while self.game.Infinity.infinity_counter>=self.costs[1]:
            self.buy_counter(1)
        while self.game.Infinity.infinity_counter>=self.costs[2]:
            self.buy_counter(2)
        while self.game.Infinity.infinity_counter>=self.costs[3]:
            self.buy_counter(3)
        # label=Label(self.game.window,text=u'\uA506', fg='white',bg='black',font=('bahnschrift', 24))
        # label.place(x=0,y=10)

    def click(self,event):
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            self.curbar = 'N'
            for box in self.boxes[3]:
                coords=self.game.main_canvas.coords(box[0])
                if event.x>=coords[0] and event.y>=coords[1] and event.x<=coords[2] and event.y<=coords[3]:
                    index=self.boxes[3].index(box)
                    self.buy_counter(index)
            coords=self.game.main_canvas.coords(self.button_active)
            if event.x >= coords[0] and event.y >= coords[1] and event.x <= coords[2] and event.y <= coords[3]:
                self.play_pause()
            coords = self.game.main_canvas.coords(self.button_max)
            if event.x >= coords[0] and event.y >= coords[1] and event.x <= coords[2] and event.y <= coords[3]:
                self.max_dc()
            coords = self.game.main_canvas.coords(self.button_auto_pause)
            if event.x >= coords[0] and event.y >= coords[1] and event.x <= coords[2] and event.y <= coords[3]:
                coords = self.game.main_canvas.coords(self.button_auto_pause_input)
                if event.x >= coords[0] and event.y >= coords[1] and event.x <= coords[2] and event.y <= coords[3]:
                    self.curbar=self.text_auto_pause_input
                else:
                    self.click_auto()
            if self.game.Aspects.completion_3:
                for box in self.shop_boxes[0]:
                    coords=self.game.main_canvas.coords(box)
                    index=self.shop_boxes[0].index(box)
                    if event.x >= coords[0] and event.y >= coords[1] and event.x <= coords[2] and event.y <= coords[3] and self.upgrades_costs[index]<=self.doom_count and self.total_upgrades[index]<10:
                        self.doom_count-=self.upgrades_costs[index]
                        self.upgrades_costs[index]=self.upgrades_costs[index]*self.upgrades_costs_up[index]
                        self.total_upgrades[index]+=1
                        if index==0:
                            self.mult_doom-=0.02
                            if self.total_upgrades[0] < 10:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],text='Formula DD for counters:\n'+str(round(self.mult_doom,2))+' → '+str(round(self.mult_doom-0.02,2))+'\nCost DD: '+str("{:.2e}".format(Decimal(self.upgrades_costs[0]))))
                            else:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],
                                                                    text='Formula DD for counters:\n' + str(
                                                                        round(self.mult_doom, 2)))
                            self.game.main_canvas.coords(self.shop_boxes[2][index], self.game.geometry[0] // 2 - 475,
                                                         700,
                                                         self.game.geometry[0] // 2 - 275 - (
                                                                 (10 - self.total_upgrades[0]) * 20), 719)
                        if index==1:
                            self.mult_inf+=0.02
                            if self.total_upgrades[1] < 10:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],text='Formula DD for IC:\n' + str(
                                                                  round(self.mult_inf, 2)) + ' → ' + str(
                                                                  round(self.mult_inf + 0.02, 2)) + '\nCost DD: ' + str(
                                                                  "{:.2e}".format(Decimal(self.upgrades_costs[1]))))
                            else:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],
                                                                    text='Formula DD for IC:\n' + str(
                                                                        round(self.mult_inf, 2)))
                            self.game.main_canvas.coords(self.shop_boxes[2][index], self.game.geometry[0] // 2 - 225,
                                                         700,
                                                         self.game.geometry[0] // 2 - 25 - (
                                                                 (10 - self.total_upgrades[1]) * 20), 719)
                        if index==2:
                            self.dc_mult *= self.upgrader_dc_mult
                            self.upgrader_dc_mult +=0.4
                            if self.total_upgrades[2] < 10:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],text='Gain multi for DC:\n' + str(
                                                                  round(self.dc_mult, 1)) + ' → ' + str(
                                                                  round(self.dc_mult*self.upgrader_dc_mult,1)) + '\nCost DD: ' + str(
                                                                  "{:.2e}".format(Decimal(self.upgrades_costs[2]))))
                            else:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],
                                                                    text='Gain multi for DC:\n' + str(
                                                                        round(self.dc_mult, 1)))
                            self.game.main_canvas.coords(self.shop_boxes[2][index], self.game.geometry[0] // 2 +225- (
                                                                 (10 - self.total_upgrades[2]) * 20),
                                                         700,
                                                         self.game.geometry[0] // 2 + 25, 719)
                        if index == 3:
                            self.game.Automatick.time_cycle -= 150
                            if self.total_upgrades[3] < 10:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],
                                                                    text='Decrease automatick\nprogramm cooldown:\n' + str(
                                                                        round(self.game.Automatick.time_cycle / 1000,
                                                                              2)) + ' → ' + str(
                                                                        round(
                                                                            (self.game.Automatick.time_cycle - 150) / 1000,
                                                                            2)) + ' seconds' + '\nCost DD: ' + str(
                                                                        "{:.2e}".format(Decimal(self.upgrades_costs[3]))))
                            else:
                                self.game.main_canvas.itemconfigure(self.shop_boxes[3][index],
                                                                    text='Decrease automatick\nprogramm cooldown:\n' + str(
                                                                        round(self.game.Automatick.time_cycle / 1000,
                                                                              2)))
                            self.game.main_canvas.coords(self.shop_boxes[2][index], self.game.geometry[0] // 2 + 475- (
                                                                 (10 - self.total_upgrades[3]) * 20),
                                                         700,
                                                         self.game.geometry[0] // 2 + 275, 719)

    def click_auto(self):
        if self.auto_pause=='enabled':
            self.auto_pause='disabled'
        else:
            self.auto_pause = 'enabled'
        if self.auto_pause=='enabled':
            self.color_auto_pause_text='#5bc77a'
        else:
            self.color_auto_pause_text = '#c75b5b'
        self.game.main_canvas.itemconfigure(self.text_auto_pause,text='Limit\n'+self.auto_pause+' on:\n'+'\n\n'+'DD',fill=self.color_auto_pause_text)
    def play_pause(self):
        if self.active:
            self.active=False
            self.game.main_canvas.itemconfigure(self.image_active,image=self.images[0])
        else:
            self.active=True
            self.game.main_canvas.itemconfigure(self.image_active, image=self.images[1])


    def conf_counters(self):
        if not (self.game.Aspects.active == True and (self.game.Aspects.cur_ill == 3 or self.game.Aspects.cur_ill == 4)):
            if self.game.Menu.curMenu=='Doom':
                list=[self.doom_counter_1,self.doom_counter_2,self.doom_counter_3,self.doom_counter_4]
                x_2 = 0
                x_1=0
                x=0
                for counter in self.boxes[1]:
                    self.game.main_canvas.itemconfigure(counter,text=list[x].get(2,4))
                    x+=1
                for counter in self.boxes[2]:
                    self.game.main_canvas.itemconfigure(counter,text='x'+self.get_extra_mult(x_1+1).get(2,4))
                    x_1+=1
                for counter in self.boxes[3]:
                    self.game.main_canvas.itemconfigure(counter[1],text='Cost: ' + self.costs[x_2].get(2,4)+' IC')
                    x_2+=1

    def buy_counter(self,num):
        if num == 0:
            if self.game.Infinity.infinity_counter>=self.costs[0]:
                self.game.Infinity.get_points(self.costs[0], 'buy')
                self.costs[0]*=self.up_costs[0]
                self.doom_counter_1+=1
                if self.bought_counter[0]>=1:
                    self.multies[0]*=2
                self.bought_counter[0]+=1
                print(self.doom_counter_1.get(2,4))
                self.game.main_canvas.itemconfigure(self.boxes[3][num][1],text='Cost: '+self.costs[0].get(2,4)+' IC')
        elif num == 1:
            if self.game.Infinity.infinity_counter>=self.costs[1]:
                self.game.Infinity.get_points(self.costs[1], 'buy')
                self.costs[1]*=self.up_costs[1]
                self.doom_counter_2+=1
                if self.bought_counter[1]>=1:
                    self.multies[1]*=2
                self.bought_counter[1]+=1
                self.game.main_canvas.itemconfigure(self.boxes[3][num][1],text='Cost: '+self.costs[1].get(2,4)+' IC')
        elif num == 2:
            if self.game.Infinity.infinity_counter>=self.costs[2]:
                self.game.Infinity.get_points(self.costs[2], 'buy')
                self.costs[2]*=self.up_costs[2]
                self.doom_counter_3+=1
                if self.bought_counter[2]>=1:
                    self.multies[2]*=2
                self.bought_counter[2]+=1
                self.game.main_canvas.itemconfigure(self.boxes[3][num][1],text='Cost: '+self.costs[2].get(2,4)+' IC')
        elif num == 3:
            if self.game.Infinity.infinity_counter>=self.costs[3]:
                self.game.Achievements.get_achieve(19)
                self.game.Infinity.get_points(self.costs[3], 'buy')
                self.costs[3]*=self.up_costs[3]
                self.doom_counter_4+=1
                if self.bought_counter[3]>=1:
                    self.multies[3]*=2
                self.bought_counter[3]+=1
                self.game.main_canvas.itemconfigure(self.boxes[3][num][1],text='Cost: '+self.costs[3].get(2,4)+' IC')


    def get_save(self):
        data = ''
        data+=str(self.doom_count.get_save())+','
        data += str(self.doom_total.get_save()) + ','
        data+='['+str(self.doom_counter_1.get_save())+','+str(self.doom_counter_2.get_save())+','+str(self.doom_counter_3.get_save())+','+str(self.doom_counter_4.get_save())+',],['
        for multi in self.multies:
            data+=str(multi.get_save())+','
        data+='],['
        for cost in self.costs:
            data += str(cost.get_save()) + ','
        data+='],['
        for bought in self.bought_counter:
            data += str(bought.get_save()) + ','
        data += '],'
        if self.active==True:
            data+=str(self.active)
        else:
            data+=''
        data+='\n'
        return data





#ΑΒΓΔΕΖΗΘΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ, αβγδεζηθικλμνξοπρστυφχψω, ￡ ȵ ₰ ᖘ Θ Ꮹ φ ⥉ ಭ Ϡ ᛃ ⌘ ꔆ ꔙ ꕫ ꖢ ꖴ ꘨