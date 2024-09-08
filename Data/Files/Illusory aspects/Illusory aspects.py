from decimal import Decimal
from tkinter import *
import math
import datetime


class Illusory_aspects:
    def __init__(self,game):
        self.game=game
        self.left=PhotoImage(file='Data/Files/images/illusory/left_arr.png')
        self.right = PhotoImage(file='Data/Files/images/illusory/right_arr.png')
        self.active_1st=False
        self.save=self.game.Save.Aspect_data
        self.available=self.game.Save.Aspect_data
        self.color_bord = [0,'+']
        self.size_rect=[0,'+']
        self.illusions=['U','U','U','U']
        self.completions=['-']
        self.completions_2=3
        self.reward_2=1
        self.conditions_2=[[300,1e15,2.5],[280,1e17,6.3],[260,1e19,15.6],[240,1e21,39],[220,1e23,98],
                           [200,1e25,244],[180,1e27,610],[160,1e29,1526],[140,1e31,3815],[120,1e33,9537],
                           [100,1e35,23842],[90,1e37,59605],[80,1e39,149012],[70,1e41,372529],[60,1e43,931323],
                           [50,1e45,2328306]]
        self.reward_1=1
        self.cur_page=1
        self.active=False
        self.confed=False
        self.cur_ill=1
        if self.available=='True':
            self.game.Menu.add('Illusory')

    def add(self):
        self.available = 'True'
        self.game.Menu.add('Illusory')

    def place(self):
        self.place_gui()
        if self.confed==False:
            self.conf()
            self.confed = True

    def place_gui(self):
        self.box=self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 200,
                                                              self.game.geometry[0] // 2 + 500, 700, width=2,
                                                              fill="#%02x%02x%02x" % (0,0,0), outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
        self.box_r = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 450, 425,
                                                            self.game.geometry[0] // 2 + 500, 475, width=2,
                                                            fill="#%02x%02x%02x" % (0, 0, 0),
                                                            outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
        self.box_l = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 425,
                                                            self.game.geometry[0] // 2 - 450, 475, width=2,
                                                            fill="#%02x%02x%02x" % (0, 0, 0),
                                                            outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
        self.image_l=self.game.main_canvas.create_image(self.game.geometry[0] // 2 - 475,450,anchor='center',image=self.left)
        self.image_r = self.game.main_canvas.create_image(self.game.geometry[0] // 2 + 475, 450, anchor='center',
                                                          image=self.right)
        self.box_sub = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 450, 200,
                                                          self.game.geometry[0] // 2 + 450, 700, width=2,
                                                          fill="#%02x%02x%02x" % (0, 0, 0),
                                                          outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
        self.box_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 200-self.size_rect[0], 350,
                                                          self.game.geometry[0] // 2 + 200+self.size_rect[0], 430, width=3,
                                                          fill="#%02x%02x%02x" % (0, 0, 0),
                                                          outline="#%02x%02x%02x" % (0, 255-self.color_bord[0], 255))
        self.box_2 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 350, 200,
                                                            self.game.geometry[0] // 2 + 350, 320, width=2,
                                                            fill="#%02x%02x%02x" % (0,0,0), outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
        self.box_3 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 350, 460,
                                                            self.game.geometry[0] // 2 + 350, 700, width=2,
                                                            fill="#%02x%02x%02x" % (0, 0, 0),
                                                            outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
        if self.active==False:
            self.text=self.game.main_canvas.create_text(self.game.geometry[0] // 2, 390,
                                                                text="Start Illusion",
                                                                anchor='center',
                                                                fill="#%02x%02x%02x" % (0, 255-self.color_bord[0], 255), justify='center',
                                                                font=('bahnschrift', 22))
        else:
            self.text = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 390,
                                                          text="Escape Illusion",
                                                          anchor='center',
                                                          fill="#%02x%02x%02x" % (0, 255-self.color_bord[0], 255), justify='center',
                                                          font=('bahnschrift', 22))
        if self.cur_page==1:
            self.text_1=self.game.main_canvas.create_text(self.game.geometry[0] // 2, 260,
                                                                text="The First Illusory Aspect\nCondition: Infinity upgrades disabled\nDoomed Destruction buff your Counters with ^0.2 power instead debuff\nCounters multi divided by 75",
                                                                anchor='center',
                                                                fill='#81d6d6', justify='center',
                                                                font=('bahnschrift', 15))
            self.text_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 540,
                                                            text="The faster you complete Illusion, the stronger the power..\nDoom Counters multi:\nx"+str(round(self.reward_1,2))+"\nBest time: "+self.get_time(),
                                                            anchor='center',
                                                            fill='#81d6d6', justify='center',
                                                            font=('bahnschrift', 15))
        elif self.cur_page==2 and self.illusions[1]=="U":
            self.text_1=self.game.main_canvas.create_text(self.game.geometry[0] // 2, 260,
                                                                text="The Second Illusory Aspect\nCondition: You have "+str(self.conditions_2[self.completions_2][0])+' seconds to reach Infinity.\nDoom Destruction locked on '+str("{:.2e}".format(
                    Decimal(self.conditions_2[self.completions_2][1])))+'\nInfinity upgrades are more stronger',
                                                                anchor='center',
                                                                fill='#81d6d6', justify='center',
                                                                font=('bahnschrift', 15))
            self.text_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 540,
                                                            text="The more times you complete Illusion, the more Ifninity rewards..\nIC gain:\nx"+str(round(self.reward_2))+"\nBest time: "+self.get_time(),
                                                            anchor='center',
                                                            fill='#81d6d6', justify='center',
                                                            font=('bahnschrift', 15))
            self.list_circles=[]
            for num in range(16):
                if num<self.completions_2:
                    self.game.main_canvas.create_oval(self.game.geometry[0] // 2 - 320 + (num * 40), 640,
                                                      self.game.geometry[0] // 2 - 290 + (num * 40), 670, fill='#00c4ff',
                                                      outline='#56cccc', width=2)
                else:
                    self.game.main_canvas.create_oval(self.game.geometry[0] // 2 - 320+(num*40), 640,
                                                                self.game.geometry[0] // 2 - 290+(num*40), 670,fill='#000',
                                                                outline='#56cccc',width=2)
        if self.active and self.cur_ill==1:
            self.timer = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 630,
                                                           text="This Illusion lasts for:\nhours: 0 minutes: 0 seconds: 0",
                                                           anchor='center',
                                                           fill='#81d6d6', justify='center',
                                                           font=('bahnschrift', 15))

    def get_time(self):
        if self.completions[0]!='-':
            time=self.completions[0]
            list = [0, 0, 0]
            while time > 3600:
                list[0] += 1
                time -= 3600
            while time > 60:
                list[1] += 1
                time -= 60
            list[2] += time
            if list[0]==0:
                if list[1]==0:
                    return 'seconds: '+str(float(round(list[2],1)))
                else:
                    return 'minutes: ' + str(int(round(list[1], 0)))+', seconds: ' + str(int(round(list[2], 0)))
            else:
                return 'hours: ' + str(int(round(list[0], 0))) + ', minutes: ' + str(int(round(list[1], 0))) + ', seconds: ' + str(int(round(list[2], 0)))
        else:
            return 'No record'


    def conf(self):
        if self.game.Menu.curMenu=="Illusory":
            self.colorful()
            self.game.main_canvas.itemconfigure(self.box,outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
            self.game.main_canvas.itemconfigure(self.box_sub, outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
            self.game.main_canvas.itemconfigure(self.box_r, outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
            self.game.main_canvas.itemconfigure(self.box_l, outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
            self.game.main_canvas.coords(self.box_1,self.game.geometry[0] // 2 - 200-self.size_rect[0], 350,
                                                          self.game.geometry[0] // 2 + 200+self.size_rect[0], 430)
            self.game.main_canvas.itemconfigure(self.box_1, outline="#%02x%02x%02x" % (0, 255-self.color_bord[0], 255))
            self.game.main_canvas.itemconfigure(self.text,
                                                fill="#%02x%02x%02x" % (0, 255 - self.color_bord[0], 255))
            self.game.main_canvas.itemconfigure(self.box_2, outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
            self.game.main_canvas.itemconfigure(self.box_3, outline="#%02x%02x%02x" % (0, self.color_bord[0], 255))
            if self.cur_ill==1 and self.active:
                time=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()-self.time
                list=[0,0,0]
                while time>3600:
                    list[0]+=1
                    time-=3600
                while time>60:
                    list[1]+=1
                    time-=60
                list[2]+=time
                self.game.main_canvas.itemconfigure(self.timer,text="This Illusion lasts for:\nhours: "+str(int(round(list[0],0)))+" minutes: "+str(int(round(list[1],0)))+" seconds: "+str(int(round(list[2],0))))
            self.game.window.after(40,self.conf)

    def colorful(self):
        if self.color_bord[1]=='+':
            self.color_bord[0]+=5
            if self.color_bord[0]==255:
                self.color_bord[1]='-'
        else:
            self.color_bord[0] -= 5
            if self.color_bord[0]==0:
                self.color_bord[1]='+'
        if self.size_rect[1]=='+' and self.active==False:
            self.size_rect[0]+=2
            if self.size_rect[0]==150:
                self.size_rect[1]='-'
        elif self.size_rect[1]=='-' and self.active==False:
            self.size_rect[0] -= 2
            if self.size_rect[0]==0:
                self.size_rect[1]='+'

    def hide(self):
        self.confed = False
        self.game.main_canvas.delete(self.box),self.game.main_canvas.delete(self.box_1),self.game.main_canvas.delete(self.box_2),self.game.main_canvas.delete(self.box_3),self.game.main_canvas.delete(self.box_sub),
        self.game.main_canvas.delete(self.text), self.game.main_canvas.delete(self.text_1),self.game.main_canvas.delete(self.text_2)
        self.game.main_canvas.delete(self.box_l),self.game.main_canvas.delete(self.box_r),self.game.main_canvas.delete(self.image_l),self.game.main_canvas.delete(self.image_r),
        try:
            if self.active and self.cur_ill == 1:
                self.game.main_canvas.delete(self.timer)
        except:
            pass

    def click(self,event):
        coords=self.game.main_canvas.coords(self.box_1)
        if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
            if self.active==False:
                if self.cur_page==1:
                    self.active=True
                    self.cur_ill=int(self.cur_page)
                    self.time = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
                    self.game.Menu.stage_get('First Illusion', '#56c7c7','counters','#00d4d4')
                    self.game.I_reset()
                    self.game.Value.Illusion()
            else:
                self.active = False
                self.cur_page = int(self.cur_ill)
                self.game.Menu.stage_get(stage='Basic mode', change='Illusory')
                self.game.I_reset()
        coords = self.game.main_canvas.coords(self.box_l)
        if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
            self.change_page('-')
        coords = self.game.main_canvas.coords(self.box_r)
        if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
            self.change_page('+')

    def change_page(self,arg):
        if arg=='-':
            self.cur_page-=1
            if self.cur_page<1:
                self.cur_page=1
        if arg=='+':
            self.cur_page+=1
            if self.cur_page>4:
                self.cur_page=4
        self.hide()
        self.place_gui()




    def reward(self):
        if self.cur_ill==1:
            time=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
            if self.completions[0]!='-':
                if self.completions[0]>time-self.time:
                    self.completions[0]=time-self.time
                    self.reward_1=(1800/self.completions[0])**1.15
                    if self.reward_1<1:
                        self.reward_1=1
            else:
                self.completions[0] = time - self.time
                self.reward_1 = (1800 / self.completions[0]) ** 1.15
                if self.reward_1 < 1:
                    self.reward_1 = 1
            try:
                if self.active and self.cur_ill == 1:
                    self.game.main_canvas.delete(self.timer)
            except:
                pass
        self.active=False
        self.cur_page=int(self.cur_ill)
        self.game.Menu.stage_get(stage='Basic mode', change='Illusory')
        self.game.I_reset()


    def get_save(self):
        return self.available+'\n'
