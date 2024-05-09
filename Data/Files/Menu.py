from tkinter import *

class Menu:
    def __init__(self,game):
        self.image_1=PhotoImage(file='Data/Files/images/counters.png')
        self.image_2 = PhotoImage(file='Data/Files/images/infinity.png')
        self.image_3 = PhotoImage(file='Data/Files/images/automatick.png')
        self.image_4 = PhotoImage(file='Data/Files/images/doom.png')
        self.game=game
        self.active=False
        self.curMenu='Counters'
        self.Allowed_menus=[]

    def place_menus(self):
        self.active=True
        self.Allowed_menus.append('counters'),self.Allowed_menus.append('infinity'),self.Allowed_menus.append('automatick')
        self.box=self.game.main_canvas.create_rectangle(0,160,110,240,width=2,fill='black',outline='#e80923')
        self.box_1 = self.game.main_canvas.create_rectangle(0, 250, 110, 330, width=2, fill='black', outline='#e88009')
        self.box_2 = self.game.main_canvas.create_rectangle(0, 340, 110, 420, width=2, fill='black', outline='#4ac9ff')
        self.image_1_cnvs=self.game.main_canvas.create_image(55,200,anchor='center',image=self.image_1)
        self.image_2_cnvs = self.game.main_canvas.create_image(55, 290, anchor='center', image=self.image_2)
        self.image_3_cnvs = self.game.main_canvas.create_image(55, 380, anchor='center', image=self.image_3)

    def open_new_cur(self,argument):
        self.close_cur()
        if argument=='counters' and argument in self.Allowed_menus:
            self.curMenu='Counters'
            self.game.return_counters()
        if argument=='infinity' and argument in self.Allowed_menus:
            self.curMenu='Infinity'
            self.game.Infinity.place_upgrades()
        if argument=='automatick' and argument in self.Allowed_menus:
            self.curMenu='Automatick'
            self.game.Automatick.place()
        if argument=='doom' and argument in self.Allowed_menus:
            self.curMenu='Doom'
            self.game.Doom.place()

    def add(self,argument):
        self.Allowed_menus.append(argument)
        if argument=='doom':
            self.box_3 = self.game.main_canvas.create_rectangle(0, 430, 110, 510, width=2, fill='black', outline='#691913')
            self.image_4_cnvs = self.game.main_canvas.create_image(55, 470, anchor='center', image=self.image_4)


    def close_cur(self):
        if self.curMenu=='Counters':
            self.game.hide_counters()
        elif self.curMenu=='Infinity':
            self.game.Infinity.hide()
        elif self.curMenu=='Automatick':
            self.game.Automatick.hide()
        elif self.curMenu=='Doom':
            self.game.Doom.hide()
