from tkinter import *


class Achievements:
    def __init__(self,game):
        self.game=game
        self.achieve=['N','N','N','N','N',
                      'N','N','N','N','N',
                      'N','N','N','N','N',
                      'N','N','N','N','N',
                      'N',]

        self.texts=[['First. Again','Get 1st counter after Infinity','multi to 1st counter 1.1'],['Twice a week','Get 2nd counter after Infinity','multi to 2nd counter 1.1'],
                    ['3^2=9?','Get 3rd counter after Infinity','multi to 3rd counter 1.1'],['True mathematics','Get 4th counter after Infinity','multi to 4th counter 1.1'],
                    ['Time to BOOST!','Get 5th counter after Infinity','multi to 5th counter 1.1'],['VI','Get 6th counter after Infinity','multi to 6th counter 1.1'],
                    ['Lucky number','Get 7th counter after Infinity','multi to 7th counter 1.1'],['Where is 9th?','Get 8th counter after Infinity','multi to 8th counter 1.1'],
                    ['Particle accelerator','Buy Time accelerator','-'],['Infinity*2','Buy Infinity after first Infinity','-'],

                    ["It's A LOT!",'Gain 1e60 multi on 1st counter','-'],['Uh..Oh..','Buy 4 Time accelerators','Time speed * 1.01'],
                    ['Timeless Infinity','Buy Infinity without Time accelerators','Time speed * 1.01'],['Boostless Infinity','Buy Infinity without Counter boosts','All counters * 1.01'],
                    ['Infinity Baron','Have 25 Infinities(not IC)','IC gain *2'],['Doom my mood','Unlock Doom','-'],
                    ['Fully upgraded!','Buy all Infinity upgrades','IC gain *2'],['New currency','Start produce Doomed Destruction','-'],
                    ['Doomed game','Buy 4th Doom Counter','DD gain *1.5'],['Theory of math','Gain 1e8 DD','Unlock first Illusory Aspect'],

                    ['GET RID OUT OF THEORY','Complete 1st Aspect','IC gain *2'],]
        self.images=[PhotoImage(file='Data/Files/images/achievements/1.png'),PhotoImage(file='Data/Files/images/achievements/2.png'),
                     PhotoImage(file='Data/Files/images/achievements/3.png'),PhotoImage(file='Data/Files/images/achievements/4.png'),
                     PhotoImage(file='Data/Files/images/achievements/5.png'),PhotoImage(file='Data/Files/images/achievements/6.png'),
                     PhotoImage(file='Data/Files/images/achievements/7.png'),PhotoImage(file='Data/Files/images/achievements/8.png'),
                     PhotoImage(file='Data/Files/images/achievements/9.png'),PhotoImage(file='Data/Files/images/achievements/10.png'),
                     PhotoImage(file='Data/Files/images/achievements/11.png'),PhotoImage(file='Data/Files/images/achievements/12.png'),
                     PhotoImage(file='Data/Files/images/achievements/13.png'),PhotoImage(file='Data/Files/images/achievements/14.png'),
                     PhotoImage(file='Data/Files/images/achievements/15.png'),PhotoImage(file='Data/Files/images/achievements/16.png'),
                     PhotoImage(file='Data/Files/images/achievements/17.png'),PhotoImage(file='Data/Files/images/achievements/18.png'),
                     PhotoImage(file='Data/Files/images/achievements/19.png'),PhotoImage(file='Data/Files/images/achievements/20.png'),]
        self.placed=[]

    def place(self):
        self.box=self.game.main_canvas.create_rectangle(140, 200,self.game.geometry[0]-140, 700, width=2, fill='black', outline='#736005')
        self.place_achieves()


    def place_achieves(self):
        x_2=0
        index=0
        while x_2<=self.game.geometry[0]-140:
            x_2+=63
        x_2-=self.game.geometry[0]-140
        x_2=x_2//2
        x,y=x_2,0
        for achieve in self.achieve:
            list=[]
            if achieve=='N':
                list.append(self.game.main_canvas.create_rectangle(142+x, 202+y,203+x, 263+y, width=1, fill='black', outline='#d6b929'))
            if achieve=='Y':
                list.append(self.game.main_canvas.create_rectangle(142+x, 202+y,203+x, 263+y, width=1, fill='#349606', outline='#d6b929'))
            list.append(
                self.game.main_canvas.create_image(143 + x, 203 + y,anchor='nw',image=self.images[index]))
            self.placed.append(list)
            x+=63
            index+=1
            while x>=self.game.geometry[0]-344:
                y+=63
                x=x_2


    def hide(self):
        self.game.main_canvas.delete(self.box)