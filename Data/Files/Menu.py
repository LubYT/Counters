from tkinter import *

class Menu:
    def __init__(self,game):
        self.image_1=PhotoImage(file='Data/Files/images/counters.png')
        self.image_2 = PhotoImage(file='Data/Files/images/infinity.png')
        self.image_3 = PhotoImage(file='Data/Files/images/automatick.png')
        self.image_4 = PhotoImage(file='Data/Files/images/doom.png')
        self.image_5 = PhotoImage(file='Data/Files/images/achievementes.png')
        self.image_6 = PhotoImage(file='Data/Files/images/illusory_aspect.png')
        self.image_7 = PhotoImage(file='Data/Files/images/stats.png')
        self.image_8 = PhotoImage(file='Data/Files/images/Eternity.png')
        self.game=game
        self.active=False
        self.curMenu='Counters'
        self.Allowed_menus=[]
        self.base=['Basic mode','#707070','#ad0000']
        self.curStage='Basic mode'
        self.colorStage = '#707070'
        self.textStage=self.game.main_canvas.create_text(self.game.geometry[0] // 2, 10, anchor='n',
                                                        text=self.curStage,
                                                        fill=self.colorStage, justify='center',
                                                        font=('bahnschrift', 12))

    def stage_get(self,stage=0,color=1,change='-',color_box=2):
        if stage==0:
            stage=self.base[0]
        if color == 1:
            color = self.base[1]
        if color_box == 2:
            color_box = self.base[2]
        self.curStage=stage
        self.colorStage=color
        self.game.main_canvas.itemconfigure(self.textStage,text=self.curStage,fill=self.colorStage)
        self.game.color_box(color_box)
        if change!='-':
            self.open_new_cur(change)

    def place_menus(self):
        self.active=True
        if self.game.Eternity.first:
            self.base=['Basic Eternity','#d38ff2','#ad0048']
        self.Allowed_menus.append('counters'),self.Allowed_menus.append('infinity'),self.Allowed_menus.append('automatick'),self.Allowed_menus.append('achievements'),self.Allowed_menus.append('Stats')
        self.box=self.game.main_canvas.create_rectangle(0,190,110,270,width=2,fill='black',outline='#e80923')
        self.box_1 = self.game.main_canvas.create_rectangle(0, 280, 110, 360, width=2, fill='black', outline='#e88009')
        self.box_2 = self.game.main_canvas.create_rectangle(0, 370, 110, 450, width=2, fill='black', outline='#4ac9ff')
        self.image_1_cnvs=self.game.main_canvas.create_image(55,230,anchor='center',image=self.image_1)
        self.image_2_cnvs = self.game.main_canvas.create_image(55, 320, anchor='center', image=self.image_2)
        self.image_3_cnvs = self.game.main_canvas.create_image(55, 410, anchor='center', image=self.image_3)
        self.box_4 = self.game.main_canvas.create_rectangle(self.game.geometry[0]+5, 190, self.game.geometry[0]-112, 270, width=2, fill='black',outline='#ffe603')
        self.image_5_cnvs = self.game.main_canvas.create_image(self.game.geometry[0]-55, 230, anchor='center', image=self.image_5)
        self.box_5 = self.game.main_canvas.create_rectangle(self.game.geometry[0] + 5, 280, self.game.geometry[0] - 112,
                                                            360, width=2, fill='black', outline='#fcacac')
        self.image_6_cnvs = self.game.main_canvas.create_image(self.game.geometry[0] - 55, 320, anchor='center',
                                                               image=self.image_7)

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
        if argument=='achievements' and argument in self.Allowed_menus:
            self.curMenu='Achievements'
            self.game.Achievements.place()
        if argument=='Illusory' and argument in self.Allowed_menus:
            self.curMenu='Illusory'
            self.game.Aspects.place()
        if argument=='Stats' and argument in self.Allowed_menus:
            self.curMenu='Stats'
            self.game.Stats.place()
        if argument=='Eternity' and argument in self.Allowed_menus:
            self.curMenu='Eternity'
            self.game.Eternity.place()

    def add(self,argument):
        self.Allowed_menus.append(argument)
        if argument=='doom':
            self.box_3 = self.game.main_canvas.create_rectangle(0, 460, 110, 540, width=2, fill='black', outline='#691913')
            self.image_4_cnvs = self.game.main_canvas.create_image(55, 500, anchor='center', image=self.image_4)
        if argument=='Illusory':
            self.box_6 = self.game.main_canvas.create_rectangle(self.game.geometry[0]+5, 370, self.game.geometry[0]-112, 450, width=2, fill='black', outline='#56dbd2')
            self.image_7_cnvs = self.game.main_canvas.create_image(self.game.geometry[0]-55, 410, anchor='center', image=self.image_6)
        if argument=='Eternity':
            self.box_7 = self.game.main_canvas.create_rectangle(self.game.geometry[0]+5, 460, self.game.geometry[0]-112, 540, width=2, fill='black', outline='#b030ff')
            self.image_8_cnvs = self.game.main_canvas.create_image(self.game.geometry[0]-55, 500, anchor='center', image=self.image_8)


    def close_cur(self):
        if self.curMenu=='Counters':
            self.game.hide_counters()
        elif self.curMenu=='Infinity':
            self.game.Infinity.hide()
        elif self.curMenu=='Automatick':
            self.game.Automatick.hide()
        elif self.curMenu=='Doom':
            self.game.Doom.hide()
        elif self.curMenu=='Achievements':
            self.game.Achievements.hide()
        elif self.curMenu=='Illusory':
            self.game.Aspects.hide()
        elif self.curMenu == 'Stats':
            self.game.Stats.hide()
        elif self.curMenu == 'Eternity':
            self.game.Eternity.hide()
