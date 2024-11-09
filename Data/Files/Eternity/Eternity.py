import random
from decimal import Decimal
from tkinter import *
import math



class Eternity:
    def __init__(self,game):
        self.game=game
        self.eternity_count=self.game.Decimal(0,0,self.game,'EC')
        self.total_ec=self.game.Decimal(0,0,self.game,'EC')
        self.first=False
        self.eternities=self.game.Decimal(0,0,self.game)
        self.save=self.game.Save.Stats_data
        self.available='False'
        self.move_fr=False
        self.time_speed=self.game.Decimal(1,0,self.game,'time')
        self.income=1
        self.cost=1.79e308
        self.image_1 = PhotoImage(file='Data/Files/images/eternity_1.png')
        self.image_2 = PhotoImage(file='Data/Files/images/eternity_2.png')
        self.image_3 = PhotoImage(file='Data/Files/images/eternity_3.png')
        self.image_4 = PhotoImage(file='Data/Files/images/eternity_4.png')
        self.circles=[]
        self.upgrades=['N','N','N','N','N','N','N','N','N']
        self.menus_list=['Buy','Upgrades','Time','Eternities']
        self.menu_cur='Buy'
        self.sized=[1,0,'+']
        self.placed=False
        if self.available=='True':
            self.game.Menu.add('Eternity')
        if self.first == True:
            self.text_count = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 520, 86,
                                                          anchor='center', text='Eternity Count: ' + str(self.eternity_count.get(2,4)),
                                                          fill='#b552e3',
                                                          font=('bahnschrift', 14))
            self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 440, 110,
                                                                  self.game.geometry[0] // 2 + 600, 170, width=1,
                                                                  fill='black', outline='#840fba')
            self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 520, 140,
                                                          anchor='center', justify='center',
            text='Cost: ' + str("{:.2e}".format(Decimal(self.cost))) + ' IC\nGet ' + str(self.income) + ' EC',
                                                          fill='#b552e3',
                                                          font=('bahnschrift', 10))

    def place(self):
        if self.placed==False:
            self.box = self.game.main_canvas.create_rectangle(200, 200,
                                                              self.game.geometry[0] - 200, self.game.geometry[1] - 100,
                                                              outline='#ac40ff', width=2)
            x = int(self.eternities)
            if x > 50:
                x = 50
            for i in range(x):
                coords_x = random.randint(205, self.game.geometry[0] - 205)
                coords_y = random.randint(205, self.game.geometry[1] - 105)
                speed = [random.randint(-1, 1), random.randint(-1, 1)]
                if speed[0] == 0 and speed[1] == 0:
                    speed[0], speed[1] = 1, 1
                circle = self.game.main_canvas.create_oval(coords_x - 10, coords_y - 10, coords_x + 10, coords_y + 10,
                                                           width=3, outline='#682194', fill='#9c33de')
                self.circles.append([circle, speed])
        if self.menu_cur=='Buy':
            self.text=self.game.main_canvas.create_text(self.game.geometry[0] // 2, 250,
                                                                    text="Eternity",
                                                                    anchor='center',
                                                                    fill='#e98fff', justify='center',
                                                                    font=('bahnschrift', 26))
            self.sub_text = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 300,
                                                          text="Time is relative. No matter how long are you here. Time is nothing and everything. Break all Illusions and Infinities.\nUnlock the Great Knowledge of time",
                                                          anchor='center',
                                                          fill='#e98fff', justify='center',
                                                          font=('bahnschrift', 14))
            self.box_buy_b = self.game.main_canvas.create_rectangle(self.game.geometry[0]//2 - 160, 400,
                                                              self.game.geometry[0]//2 + 160, 500, outline='#ac40ff', width=2)
            self.text_buy_b = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 450,
                                                          text="Make new Eternity\nGain 1 EC and Eternity\nCost: 1.79e308 IC",
                                                          anchor='center',
                                                          fill='#e98fff', justify='center',
                                                          font=('bahnschrift', 18))
        if self.menu_cur == 'Upgrades':
            self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 250,
                                                          text="Upgrades",
                                                          anchor='center',
                                                          fill='#e98fff', justify='center',
                                                          font=('bahnschrift', 26))
            self.upgr_1_box=self.game.main_canvas.create_rectangle(self.game.geometry[0]//4 - 100, 300,
                                                              self.game.geometry[0]//4 + 100, 400, outline='#781bb3',fill=self.get_full('1.2'), width=self.sized[0])
            self.upgr_1_text = self.game.main_canvas.create_text(self.game.geometry[0] // 4, 350,
                                                          text=self.get_full(1),
                                                          anchor='center',
                                                          fill=self.get_full('1.1'), justify='center',
                                                          font=('bahnschrift', 12))
            self.upgr_2_box = self.game.main_canvas.create_rectangle((self.game.geometry[0] // 8*3) - 100, 300,
                                                                     (self.game.geometry[0] // 8*3) + 100, 400,
                                                                     outline='#781bb3', fill=self.get_full('2.2'),
                                                                     width=self.sized[0])
            self.upgr_2_text = self.game.main_canvas.create_text((self.game.geometry[0] // 8*3), 350,
                                                                 text=self.get_full(2),
                                                                 anchor='center',
                                                                 fill=self.get_full('2.1'), justify='center',
                                                                 font=('bahnschrift', 12))
            self.upgr_3_box = self.game.main_canvas.create_rectangle((self.game.geometry[0] // 8 * 5) - 100, 300,
                                                                     (self.game.geometry[0] // 8 * 5) + 100, 400,
                                                                     outline='#781bb3', fill=self.get_full('3.2'),
                                                                     width=self.sized[0])
            self.upgr_3_text = self.game.main_canvas.create_text((self.game.geometry[0] // 8 * 5), 350,
                                                                 text=self.get_full(3),
                                                                 anchor='center',
                                                                 fill=self.get_full('3.1'), justify='center',
                                                                 font=('bahnschrift', 12))
            self.upgr_4_box = self.game.main_canvas.create_rectangle(self.game.geometry[0]-self.game.geometry[0]//4 - 100, 300,
                                                              self.game.geometry[0]-self.game.geometry[0]//4 + 100, 400,
                                                                     outline='#781bb3', fill=self.get_full('4.2'),
                                                                     width=self.sized[0])
            self.upgr_4_text = self.game.main_canvas.create_text( self.game.geometry[0]-self.game.geometry[0]//4, 350,
                                                                 text=self.get_full(4),
                                                                 anchor='center',
                                                                 fill=self.get_full('4.1'), justify='center',
                                                                 font=('bahnschrift', 12))
            self.upgr_5_box = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 4 - 100, 450,
                                                                     self.game.geometry[0] // 4 + 100, 550,
                                                                     outline='#781bb3', fill=self.get_full('5.2'),
                                                                     width=self.sized[0])
            self.upgr_5_text = self.game.main_canvas.create_text(self.game.geometry[0] // 4, 500,
                                                                 text=self.get_full(5),
                                                                 anchor='center',
                                                                 fill=self.get_full('5.1'), justify='center',
                                                                 font=('bahnschrift', 12))
            self.upgr_6_box = self.game.main_canvas.create_rectangle((self.game.geometry[0] // 8*3) - 100, 450,
                                                                     (self.game.geometry[0] // 8*3) + 100, 550,
                                                                     outline='#781bb3', fill=self.get_full('6.2'),
                                                                     width=self.sized[0])
            self.upgr_6_text = self.game.main_canvas.create_text((self.game.geometry[0] // 8*3),500,
                                                                 text=self.get_full(6),
                                                                 anchor='center',
                                                                 fill=self.get_full('6.1'), justify='center',
                                                                 font=('bahnschrift', 12))
            self.upgr_7_box = self.game.main_canvas.create_rectangle((self.game.geometry[0] // 8 * 5) - 100, 450,
                                                                     (self.game.geometry[0] // 8 * 5) + 100, 550,
                                                                     outline='#781bb3', fill=self.get_full('7.2'),
                                                                     width=self.sized[0])
            self.upgr_7_text = self.game.main_canvas.create_text((self.game.geometry[0] // 8 * 5), 500,
                                                                 text=self.get_full(7),
                                                                 anchor='center',
                                                                 fill=self.get_full('7.1'), justify='center',
                                                                 font=('bahnschrift', 12))
            self.upgr_8_box = self.game.main_canvas.create_rectangle(
                    self.game.geometry[0] - self.game.geometry[0] // 4 - 100, 450,
                    self.game.geometry[0] - self.game.geometry[0] // 4 + 100, 550,
                    outline='#781bb3', fill=self.get_full('8.2'),
                    width=self.sized[0])
            self.upgr_8_text = self.game.main_canvas.create_text(self.game.geometry[0] - self.game.geometry[0] // 4,
                                                                 500,
                                                                 text=self.get_full(8),
                                                                 anchor='center',
                                                                 fill=self.get_full('8.1'), justify='center',
                                                                 font=('bahnschrift', 12))
        if self.first == True and self.placed==False:
            self.menus_box = self.game.main_canvas.create_rectangle(self.game.geometry[0]/2-100, self.game.geometry[1] - 150,
                                                          self.game.geometry[0]/2+100, self.game.geometry[1] - 100,outline='#ac40ff',width=2)
            self.menu_box_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] / 2 - 100, self.game.geometry[1] - 150,
                                                                    self.game.geometry[0] / 2 -50, self.game.geometry[1] - 100,
                                                                    outline='#ac40ff', width=2)
            self.menu_box_2 = self.game.main_canvas.create_rectangle(self.game.geometry[0] / 2 , self.game.geometry[1] - 150,
                                                                     self.game.geometry[0] / 2 - 50, self.game.geometry[1] - 100,
                                                                     outline='#ac40ff', width=2)
            self.menu_box_3 = self.game.main_canvas.create_rectangle(self.game.geometry[0] / 2 , self.game.geometry[1] - 150,
                                                                     self.game.geometry[0] / 2 + 50, self.game.geometry[1] - 100,
                                                                     outline='#ac40ff', width=2)
            self.menu_box_4 = self.game.main_canvas.create_rectangle(self.game.geometry[0] / 2 + 100, self.game.geometry[1] - 150,
                                                                     self.game.geometry[0] / 2 + 50, self.game.geometry[1] - 100,
                                                                     outline='#ac40ff', width=2)
            self.menu_image_1 = self.game.main_canvas.create_image(self.game.geometry[0] / 2 - 75, self.game.geometry[1] - 125,anchor='center',image=self.image_1)
            self.menu_image_2 = self.game.main_canvas.create_image(self.game.geometry[0] / 2 - 25, self.game.geometry[1] - 125,anchor='center',image=self.image_2)
            self.menu_image_3 = self.game.main_canvas.create_image(self.game.geometry[0] / 2 + 25, self.game.geometry[1] - 125,anchor='center',image=self.image_3)
            self.menu_image_4 = self.game.main_canvas.create_image(self.game.geometry[0] / 2 + 75, self.game.geometry[1] - 125,anchor='center',image=self.image_4)
        self.placed = True
        if self.move_fr == False:
            self.move()
            self.move_fr = True

    def get_full(self,arg):
        if arg==1:
            if self.total_ec>=1:
                if self.upgrades[0] == 'N':
                    return "Gain IC multiplier\nbased on EC and Eternities\nx"+self.notation('upgr1')+'\nCost: 1 EC'
                else:
                    return "IC multiplier\nbased on EC and Eternities\nx" + self.notation('upgr1')
            else:
                return "????"
        if arg=='1.1':
            if self.upgrades[0]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='1.2':
            if self.upgrades[0]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==2:
            if self.total_ec >= 1:
                if self.upgrades[1] == 'N':
                    return "Gain DC multiplier\nbased on EC and Eternities\nx" + self.notation('upgr2') + '\nCost: 1 EC'
                else:
                    return "DC multiplier\nbased on EC and Eternities\nx" + self.notation('upgr2')
            else:
                return "????"
        if arg=='2.1':
            if self.upgrades[1]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='2.2':
            if self.upgrades[1]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==3:
            if self.total_ec >= 5:
                if self.upgrades[2] == 'N':
                    return "Unlock Infinity ignition\nCost: 5 EC"
                else:
                    return "Unlocked Infinity ignition\nMadness incoming"
            else:
                return "????"

        if arg=='3.1':
            if self.upgrades[2]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='3.2':
            if self.upgrades[2]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==4:
            if self.total_ec >= 10:
                if self.upgrades[3] == 'N':
                    return "Unleash time power\nCost: 10 EC"
                else:
                    return "Unleashed time power\nUncontrolled"
            else:
                return "????"

        if arg=='4.1':
            if self.upgrades[3]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='4.2':
            if self.upgrades[3]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==5:
            if self.total_ec >= 2:
                if self.upgrades[4] == 'N':
                    return "Unlock max CB buy\nCost: 2 EC"
                else:
                    return "Unlocked max CB buy\nFaster than before"
            else:
                return "????"

        if arg=='5.1':
            if self.upgrades[4]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='5.2':
            if self.upgrades[4]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==6:
            if self.total_ec >= 2:
                if self.upgrades[5] == 'N':
                    return "Start any reset with 10 IC\nCost: 2 EC"
                else:
                    return "Start any reset with 10 IC\nExtra power"
            else:
                return "????"

        if arg=='6.1':
            if self.upgrades[5]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='6.2':
            if self.upgrades[5]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==7:
            if self.total_ec >= 3:
                if self.upgrades[6] == 'N':
                    return "Get multi to counters\nBased on EC and Eternities\nx" + self.notation('upgr7')+"\nCost: 3 EC"
                else:
                    return "Get multi to counters\nBased on EC and Eternities\nx" + self.notation('upgr7')
            else:
                return "????"

        if arg=='7.1':
            if self.upgrades[6]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='7.2':
            if self.upgrades[6]=='N':
                return '#000'
            else:
                return '#9d00ff'
        if arg==8:
            if self.total_ec >= 5:
                if self.upgrades[7] == 'N':
                    return "Unlock more Infinity power\nCost: 5 EC"
                else:
                    return "Unlocked more Infinity power\nInfinity reborn"
            else:
                return "????"

        if arg=='8.1':
            if self.upgrades[7]=='N':
                return '#e98fff'
            else:
                return '#1a0726'
        if arg=='8.2':
            if self.upgrades[7]=='N':
                return '#000'
            else:
                return '#9d00ff'



    def notation(self,arg):
        if arg=='upgr1':
            x=self.game.Decimal(1,0,self.game)
            ec=self.game.Decimal(self.eternity_count.num,self.eternity_count.e,self.game)
            if self.eternity_count>0:
                x+=ec**0.5/5
            e = self.game.Decimal(self.eternities.num, self.eternities.e, self.game)
            if self.eternities>0:
                x+=e**0.7/5
            return x.get(2,4)
        if arg=='upgr2':
            x = self.game.Decimal(1, 0, self.game)
            ec = self.game.Decimal(self.eternity_count.num, self.eternity_count.e, self.game)
            if self.eternity_count>0:
                x+=ec**0.4/10
            e = self.game.Decimal(self.eternities.num, self.eternities.e, self.game)
            if self.eternities>0:
                x+=e**0.5/10
            return x.get(2,4)
        if arg=='upgr7':
            x = self.game.Decimal(1, 0, self.game)
            ec = self.game.Decimal(self.eternity_count.num, self.eternity_count.e, self.game)
            if self.eternity_count>0:
                x+=ec**0.6/3
            e = self.game.Decimal(self.eternities.num, self.eternities.e, self.game)
            if self.eternities>0:
                x+=e**0.8/3
            return x.get(2,4)



    def conf(self,*args):
        self.game.main_canvas.itemconfigure(self.text_count,text='Eternity Count: ' + str(self.eternity_count.get(2,4)))
        if 'upgr' in args:
            self.game.main_canvas.itemconfigure(self.upgr_1_box,width=self.sized[0],fill=self.get_full('1.2'))
            self.game.main_canvas.itemconfigure(self.upgr_1_text, text=self.get_full(1), fill=self.get_full('1.1'))
            self.game.main_canvas.itemconfigure(self.upgr_2_box, width=self.sized[0], fill=self.get_full('2.2'))
            self.game.main_canvas.itemconfigure(self.upgr_2_text, text=self.get_full(2), fill=self.get_full('2.1'))
            self.game.main_canvas.itemconfigure(self.upgr_3_box, width=self.sized[0], fill=self.get_full('3.2'))
            self.game.main_canvas.itemconfigure(self.upgr_3_text, text=self.get_full(3), fill=self.get_full('3.1'))
            self.game.main_canvas.itemconfigure(self.upgr_4_box, width=self.sized[0], fill=self.get_full('4.2'))
            self.game.main_canvas.itemconfigure(self.upgr_4_text, text=self.get_full(4), fill=self.get_full('4.1'))
            self.game.main_canvas.itemconfigure(self.upgr_5_box, width=self.sized[0], fill=self.get_full('5.2'))
            self.game.main_canvas.itemconfigure(self.upgr_5_text, text=self.get_full(5), fill=self.get_full('5.1'))
            self.game.main_canvas.itemconfigure(self.upgr_6_box, width=self.sized[0], fill=self.get_full('6.2'))
            self.game.main_canvas.itemconfigure(self.upgr_6_text, text=self.get_full(6), fill=self.get_full('6.1'))
            self.game.main_canvas.itemconfigure(self.upgr_7_box, width=self.sized[0], fill=self.get_full('7.2'))
            self.game.main_canvas.itemconfigure(self.upgr_7_text, text=self.get_full(7), fill=self.get_full('7.1'))
            self.game.main_canvas.itemconfigure(self.upgr_8_box, width=self.sized[0], fill=self.get_full('8.2'))
            self.game.main_canvas.itemconfigure(self.upgr_8_text, text=self.get_full(8), fill=self.get_full('8.1'))

    def move(self):
        if self.placed:
            for circle in self.circles:
                coords=self.game.main_canvas.coords(circle[0])
                coords[0]+=circle[1][0]
                coords[1] += circle[1][1]
                coords[2] += circle[1][0]
                coords[3] += circle[1][1]
                if coords[0]<200:
                    x_pas=coords[0]-200
                    coords[0]-=x_pas
                    coords[2] -= x_pas
                    circle[1][0]=0-circle[1][0]
                elif coords[2]>self.game.geometry[0]-200:
                    x_pas=coords[2]-(self.game.geometry[0]-200)
                    coords[0]-=x_pas
                    coords[2] -= x_pas
                    circle[1][0]=0-circle[1][0]
                if coords[1]<200:
                    y_pas=coords[1]-200
                    coords[1]-=y_pas
                    coords[3] -= y_pas
                    circle[1][1]=0-circle[1][1]
                elif coords[3]>self.game.geometry[1] - 100:
                    y_pas=coords[3]-(self.game.geometry[1] - 100)
                    coords[1]-=y_pas
                    coords[3] -= y_pas
                    circle[1][1]=0-circle[1][1]
                self.game.main_canvas.coords(circle[0],coords[0],coords[1],coords[2],coords[3])
            if self.menu_cur == 'Upgrades':
                self.sized[1]+=1
                if self.sized[1]==10:
                    self.sized[1]=0
                    if self.sized[2]=='+':
                        self.sized[0]+=1
                        if self.sized[0]>=5:
                            self.sized[2]='-'
                    elif self.sized[2]=='-':
                        self.sized[0]-=1
                        if self.sized[0]<=1:
                            self.sized[2]='+'
                    self.conf('upgr')
            self.game.main_canvas.after(30,self.move)
        else:
            self.move_fr=False

    def get_total(self):
        return self.income

    def buy_e(self):
        if self.game.Infinity.infinity_counter >= 1.79e308:
            self.eternity_count += self.get_total()
            self.total_ec+=self.get_total()
            self.eternities += 1
            if self.first == False:
                self.text_count = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 520, 86,
                                                                    anchor='center',
                                                                    text='Eternity Count: ' + str(self.eternity_count.get(2,4)),
                                                                    fill='#b552e3',
                                                                    font=('bahnschrift', 14))
                self.box_buy = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 440, 110,
                                                                      self.game.geometry[0] // 2 + 600, 170,
                                                                      width=1,
                                                                      fill='black', outline='#840fba')
                self.text_buy = self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 520, 140,
                                                                  anchor='center', justify='center',
                                                                  text='Cost: ' + str("{:.2e}".format(
                                                                      Decimal(self.cost))) + ' IC\nGet ' + str(self.get_total()) + ' EC',
                                                                  fill='#b552e3',
                                                                  font=('bahnschrift', 10))
            if self.game.Menu.curMenu=='Eternity':
                x = int(self.eternities)
                if x < 50:
                    coords_x = random.randint(205, self.game.geometry[0] - 205)
                    coords_y = random.randint(205, 695)
                    speed = [random.randint(-1, 1), random.randint(-1, 1)]
                    if speed[0] == 0 and speed[1] == 0:
                        speed[0], speed[1] = 1, 1
                    circle = self.game.main_canvas.create_oval(coords_x - 10, coords_y - 10, coords_x + 10,
                                                               coords_y + 10, width=3,
                                                               outline='#682194', fill='#9c33de')
                    self.circles.append([circle, speed])
            if self.first==False:
                self.hide('first')
            self.game.E_reset()
            self.conf()
            self.game.Menu.base = ['Basic Eternity', '#d38ff2', '#ad0048']
            self.game.Menu.stage_get()
            if self.game.Menu.curMenu=='Eternity':
                self.hide('refresh')
                self.place()

    def buy_upgrade(self,index):
        if index==1:
            if self.eternity_count>=1 and self.upgrades[0]=='N':
                self.eternity_count-=1
                self.upgrades[0]='Y'
        if index==2:
            if self.eternity_count>=1 and self.upgrades[1]=='N':
                self.eternity_count-=1
                self.upgrades[1]='Y'
        if index==3:
            if self.eternity_count>=5 and self.upgrades[2]=='N':
                self.eternity_count-=5
                self.upgrades[2]='Y'
        if index==4:
            if self.eternity_count>=10 and self.upgrades[3]=='N':
                self.eternity_count-=10
                self.upgrades[3]='Y'
        if index==5:
            if self.eternity_count>=2 and self.upgrades[4]=='N':
                self.eternity_count-=2
                self.upgrades[4]='Y'
        if index==6:
            if self.eternity_count>=2 and self.upgrades[5]=='N':
                self.eternity_count-=2
                self.upgrades[5]='Y'
        if index==7:
            if self.eternity_count>=3 and self.upgrades[6]=='N':
                self.eternity_count-=3
                self.upgrades[6]='Y'
        if index==8:
            if self.eternity_count>=5 and self.upgrades[7]=='N':
                self.eternity_count-=5
                self.upgrades[7]='Y'
        self.conf()



    def click(self,event):
        if self.menu_cur=='Buy':
            coords = self.game.main_canvas.coords(self.box_buy_b)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_e()
        elif self.menu_cur == 'Upgrades':
            coords = self.game.main_canvas.coords(self.upgr_1_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(1)
            coords = self.game.main_canvas.coords(self.upgr_2_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(2)
            coords = self.game.main_canvas.coords(self.upgr_3_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(3)
            coords = self.game.main_canvas.coords(self.upgr_4_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(4)
            coords = self.game.main_canvas.coords(self.upgr_5_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(5)
            coords = self.game.main_canvas.coords(self.upgr_6_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(6)
            coords = self.game.main_canvas.coords(self.upgr_7_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(7)
            coords = self.game.main_canvas.coords(self.upgr_8_box)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.buy_upgrade(8)
        if self.first == True:
            coords = self.game.main_canvas.coords(self.menu_box_1)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.change_page(1)
            coords = self.game.main_canvas.coords(self.menu_box_2)
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.change_page(2)

    def change_page(self,arg):
        if arg==1:
            self.hide('refresh')
            self.menu_cur='Buy'
            self.place()
        if arg==2:
            self.hide('refresh')
            self.menu_cur='Upgrades'
            self.place()



    def hide(self,*arg):
        if not 'refresh' in arg:
            self.placed = False
            for circle in self.circles:
                self.game.main_canvas.delete(circle[0])
            self.circles = []
            self.game.main_canvas.delete(self.box)
            if self.first:
                self.game.main_canvas.delete(self.menus_box)
                self.game.main_canvas.delete(self.menu_box_1), self.game.main_canvas.delete(self.menu_box_2)
                self.game.main_canvas.delete(self.menu_box_3), self.game.main_canvas.delete(self.menu_box_4)
                self.game.main_canvas.delete(self.menu_image_1), self.game.main_canvas.delete(self.menu_image_2)
                self.game.main_canvas.delete(self.menu_image_3), self.game.main_canvas.delete(self.menu_image_4)
        if self.menu_cur == 'Buy':
            self.game.main_canvas.delete(self.box_buy_b),self.game.main_canvas.delete(self.text_buy_b)
            self.game.main_canvas.delete(self.text),self.game.main_canvas.delete(self.sub_text)
        if self.menu_cur == 'Upgrades':
            self.game.main_canvas.delete(self.text)
            self.game.main_canvas.delete(self.upgr_1_box),self.game.main_canvas.delete(self.upgr_2_box)
            self.game.main_canvas.delete(self.upgr_3_box),self.game.main_canvas.delete(self.upgr_4_box)
            self.game.main_canvas.delete(self.upgr_5_box),self.game.main_canvas.delete(self.upgr_6_box)
            self.game.main_canvas.delete(self.upgr_7_box), self.game.main_canvas.delete(self.upgr_8_box)

            self.game.main_canvas.delete(self.upgr_1_text), self.game.main_canvas.delete(self.upgr_2_text)
            self.game.main_canvas.delete(self.upgr_3_text), self.game.main_canvas.delete(self.upgr_4_text)
            self.game.main_canvas.delete(self.upgr_5_text),self.game.main_canvas.delete(self.upgr_6_text)
            self.game.main_canvas.delete(self.upgr_7_text), self.game.main_canvas.delete(self.upgr_8_text)
        if 'first' in arg:
            self.first=True
            self.place()


    def get_save(self):
        return self.save+'\n'