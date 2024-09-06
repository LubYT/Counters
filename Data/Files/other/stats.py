import time
from decimal import Decimal
from tkinter import *
import math
import datetime

class Stats:
    def __init__(self,game):
        self.game=game
        self.time_total=[self.game.Save.Stats_data[0][0],self.game.Save.Stats_data[0][1],self.game.Save.Stats_data[0][2],self.game.Save.Stats_data[0][3]]
        self.tick=0
        self.time_get_in=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
        self.time_in_inf=[self.game.Save.Stats_data[1][0],self.game.Save.Stats_data[1][1],self.game.Save.Stats_data[1][2],self.game.Save.Stats_data[1][3]]
        self.fastest_inf=[self.game.Save.Stats_data[2][0],self.game.Save.Stats_data[2][1],self.game.Save.Stats_data[2][2],self.game.Save.Stats_data[2][3]]
        self.save=self.game.Save.Stats_data

    def place(self):
        self.text_0=self.game.main_canvas.create_text(self.game.geometry[0]//2,240,text="You've been in the game for \n"+self.time_get('total'),anchor='center',
                                                                     fill='white', justify='center',
                                                                     font=('bahnschrift', 18))
        self.text_1 = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 320,
                                                        text="You've been in this infinity for \n" + self.time_get('inf'),
                                                        anchor='center',
                                                        fill='#a48820', justify='center',
                                                        font=('bahnschrift', 14))
        self.text_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 380,
                                                        text="Your fastest infinity: \n" + self.time_get(
                                                            'inf fast'),
                                                        anchor='center',
                                                        fill='#d99000', justify='center',
                                                        font=('bahnschrift', 14))
        self.text_3 = self.game.main_canvas.create_text(self.game.geometry[0] // 2, 420,
                                                        text="During all "+str(self.game.Infinity.infinities)+" infinities you have received " +self.time_get('IC')+" IC",
                                                        anchor='center',
                                                        fill='#d99000', justify='center',
                                                        font=('bahnschrift', 12))
        self.conf()


    def conf(self):
        if self.game.Menu.curMenu=='Stats':
            self.game.main_canvas.itemconfigure(self.text_0,text="You've been in the game for \n"+self.time_get('total'))
            self.game.main_canvas.itemconfigure(self.text_1,
                                                text="You've been in this infinity for \n" + self.time_get('inf'))
            self.game.main_canvas.itemconfigure(self.text_2,
                                                text="Your fastest infinity: \n" + self.time_get(
                                                    'inf fast'))
            self.game.main_canvas.itemconfigure(self.text_3,
                                                text="During all "+str(self.game.Infinity.infinities)+" infinities you have received " +self.time_get('IC')+" IC")
            self.game.window.after(40,self.conf)

    def time_get(self,arg):
        if arg=='total':
            time=''
            if self.time_total[0]!=0:
                time+='days: '+str(self.time_total[0])+', '
            time+='hours: '+str(self.time_total[1])+', '+'minutes: '+str(self.time_total[2])+', '+'seconds: '+str(int(round(self.time_total[3],0)))+'.'
            return time
        if arg=='inf':
            time=''
            if self.time_in_inf[0]!=0:
                time+='days: '+str(self.time_in_inf[0])+', '
            time+='hours: '+str(self.time_in_inf[1])+', '+'minutes: '+str(self.time_in_inf[2])+', '+'seconds: '+str(int(round(self.time_in_inf[3],0)))+'.'
            return time
        if arg=='inf fast':
            time=''
            if self.fastest_inf[0]>0:
                time+='days: '+str(self.fastest_inf[0])+', '
            time+='hours: '+str(self.fastest_inf[1])+', '+'minutes: '+str(self.fastest_inf[2])+', '+'seconds: '+str(int(round(self.fastest_inf[3],0)))+'.'
            return time
        if arg=='IC':
            if self.game.Infinity.total_count>=1000:
                x="{:.2e}".format(Decimal(self.game.Infinity.total_count))
            else:
                x=self.game.Infinity.total_count
            return str(x)

    def time(self):
        addd=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
        if self.time_get_in<addd:
            time_add=addd-self.time_get_in
            self.time_get_in=addd
            self.time_total[3]+=time_add
            if self.time_total[3]>=60:
                self.time_total[3] -= 60
                self.time_total[2]+=1
            if self.time_total[2]==60:
                self.time_total[2] -= 60
                self.time_total[1]+=1
            if self.time_total[1]==24:
                self.time_total[1] -= 24
                self.time_total[0]+=1
            if self.game.Value.lock==False:
                self.time_in_inf[3] += time_add
            if self.time_in_inf[3] >= 60:
                self.time_in_inf[3] -= 60
                self.time_in_inf[2] += 1
            if self.time_in_inf[2] == 60:
                self.time_in_inf[2] -= 60
                self.time_in_inf[1] += 1
            if self.time_in_inf[1] == 24:
                self.time_in_inf[1] -= 24
                self.time_in_inf[0] += 1

    def inf(self):
        if self.fastest_inf[0]!=-1:
            if self.fastest_inf[0]>=self.time_in_inf[0]:
                print('d')
                if self.fastest_inf[1] >= self.time_in_inf[1] or self.fastest_inf[0]>self.time_in_inf[0]:
                    if self.fastest_inf[2] >= self.time_in_inf[2] or self.fastest_inf[1]>self.time_in_inf[1] or self.fastest_inf[0]>self.time_in_inf[0]:
                        if self.fastest_inf[3] >= self.time_in_inf[3] or self.fastest_inf[2] > self.time_in_inf[2] or self.fastest_inf[1] > self.time_in_inf[1] or\
                                self.fastest_inf[0] > self.time_in_inf[0]:
                            self.fastest_inf[3],self.fastest_inf[2],self.fastest_inf[1],self.fastest_inf[0] = self.time_in_inf[3],self.time_in_inf[2],self.time_in_inf[1],self.time_in_inf[0]
        else:
            self.fastest_inf[3],self.fastest_inf[2],self.fastest_inf[1],self.fastest_inf[0] = self.time_in_inf[3],self.time_in_inf[2],self.time_in_inf[1],self.time_in_inf[0]
        self.time_in_inf[3],self.time_in_inf[2],self.time_in_inf[1],self.time_in_inf[0]=0,0,0,0


    def hide(self):
        self.game.main_canvas.delete(self.text_0),self.game.main_canvas.delete(self.text_1),self.game.main_canvas.delete(self.text_3),self.game.main_canvas.delete(self.text_2)

    def get_save(self):
        save='['
        for time in self.time_total:
            save+=str(time)+','
        save+='],['
        for time in self.time_in_inf:
            save+=str(time)+','
        save+='],['
        for time in self.fastest_inf:
            save+=str(time)+','
        save+='],'
        return save+'\n'