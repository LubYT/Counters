from tkinter import *

#                       'N','N','N','N','N',
#                      'N','N','N','N','N',
#                      'N','N','N','N','N',
#                    'N','N','N','N','N',
#                     'N',

class Achievements:
    def __init__(self,game):
        self.game=game
        self.achieve=self.game.Save.Achieve_data

        self.texts=[['First. Again','Get 1st counter after Infinity','multi to 1st counter 1.1'],['Twice a week','Get 2nd counter after Infinity','multi to 2nd counter 1.1'],
                    ['3^2=9?','Get 3rd counter after Infinity','multi to 3rd counter 1.1'],['True mathematics','Get 4th counter after Infinity','multi to 4th counter 1.1'],
                    ['Time to BOOST!','Get 5th counter after Infinity','multi to 5th counter 1.1'],['VI','Get 6th counter after Infinity','multi to 6th counter 1.1'],
                    ['Lucky number','Get 7th counter after Infinity','multi to 7th counter 1.1'],['Where is 9th?','Get 8th counter after Infinity','multi to 8th counter 1.1'],
                    ['Particle accelerator','Buy Time accelerator','-'],['Infinity*2','Buy Infinity after first Infinity','-'],

                    ["It's A LOT!",'Gain 1e50 multi on 1st counter','-'],['Uh..Oh..Missed up','Buy 4 Time accelerators','Time speed * 1.01'],
                    ['Timeless Infinity','Buy Infinity without Time accelerators','Time speed * 1.1'],['Boostless Infinity','Buy Infinity with 4 or less boosts','All counters * 1.05'],
                    ['Infinity Baron','Have 25 Infinities(not IC)','IC gain *2'],['Doom my mood','Unlock Doom','-'],
                    ['Fully upgraded!','Buy all Infinity upgrades','IC gain *2'],['New currency','Start produce Doomed Destruction','-'],
                    ['Doomed game','Buy 4th Doom Counter','DD gain *1.5'],['Destroy em all','Gain 1e8 DD','Unlock first Illusory Aspect'],

                    ['Speed-runner','Reach Infinity in 10 minutes or less','IC gain *1.25'],['GET RID OUT OF THEORY','Complete 1st Illusory Aspect','IC gain *2'],
                    ['True Timeless Infinity','Reach infinity in 1 minute or less','IC gain *2'],['Hard punch!','Gain 1e15 DD','pain ;-; (lol)'],
                    ['Not a reference','Gain 1000 multi for Doomed Counters from first Illusory Aspect','Time speed * 1.25'],['NO! JUST NO!','Buy Infinity without any counter boosts and time accelerators','uhh.. you are cool!'],
                    ['Get some sleep','Play a game for 3 hours','Time speed * 1.25'],['Who is next??','Complete 2nd Illusory Aspect 16 times','IC gain *2'],]
        self.images=[PhotoImage(file='Data/Files/images/achievements/1.png'),PhotoImage(file='Data/Files/images/achievements/2.png'),
                     PhotoImage(file='Data/Files/images/achievements/3.png'),PhotoImage(file='Data/Files/images/achievements/4.png'),
                     PhotoImage(file='Data/Files/images/achievements/5.png'),PhotoImage(file='Data/Files/images/achievements/6.png'),
                     PhotoImage(file='Data/Files/images/achievements/7.png'),PhotoImage(file='Data/Files/images/achievements/8.png'),
                     PhotoImage(file='Data/Files/images/achievements/9.png'),PhotoImage(file='Data/Files/images/achievements/10.png'),
                     PhotoImage(file='Data/Files/images/achievements/11.png'),PhotoImage(file='Data/Files/images/achievements/12.png'),
                     PhotoImage(file='Data/Files/images/achievements/13.png'),PhotoImage(file='Data/Files/images/achievements/14.png'),
                     PhotoImage(file='Data/Files/images/achievements/15.png'),PhotoImage(file='Data/Files/images/achievements/16.png'),
                     PhotoImage(file='Data/Files/images/achievements/17.png'),PhotoImage(file='Data/Files/images/achievements/18.png'),
                     PhotoImage(file='Data/Files/images/achievements/19.png'),PhotoImage(file='Data/Files/images/achievements/20.png'),
                     PhotoImage(file='Data/Files/images/achievements/21.png'),PhotoImage(file='Data/Files/images/achievements/22.png'),
                     PhotoImage(file='Data/Files/images/achievements/23.png'),PhotoImage(file='Data/Files/images/achievements/24.png'),
                     PhotoImage(file='Data/Files/images/achievements/25.png'),PhotoImage(file='Data/Files/images/achievements/26.png'),
                     PhotoImage(file='Data/Files/images/achievements/27.png'),PhotoImage(file='Data/Files/images/achievements/28.png'),]
        self.placed=[]
        self.created=[]
        self.boxes={}
        self.chosen='N'
        self.first_20=False

    def place(self):
        self.box=self.game.main_canvas.create_rectangle(140, 200,self.game.geometry[0]-140, 700, width=2, fill='black', outline='#736005')
        self.place_achieves()

    def create_box(self,index):
        y=0
        for box in self.boxes:
            coords=self.game.main_canvas.coords(self.boxes[box][0])
            if coords[1]==y+2:
                y+=62
            else:
                break
        list=[]
        list.append(self.game.main_canvas.create_rectangle(self.game.geometry[0]+2, y+2,self.game.geometry[0]+302, y+62, width=2, fill='black', outline='#d6b929'))
        list.append(
            self.game.main_canvas.create_text(self.game.geometry[0]+3,y+32,
                                                                     anchor='w',
                                                                     text=self.texts[index][0],
                                                                     fill='white', justify='center',
                                                                     font=('bahnschrift', 14),width=180))
        list.append(300)
        list.append('plus')

        index=len(self.boxes)
        print(index)
        while True:
            try:
                print(index)
                print(self.box[index])
                index+=1
                print(index)
            except:
                print(index)
                self.boxes[index]=list
                break
        self.game.window.after(250,lambda: self.move(index))

    def move(self,index):
        if self.boxes[index][2]>=3:
            self.boxes[index][2]-=3
            x=3
        elif self.boxes[index][2]==0:
            x=0
            self.boxes[index][2]=0
        elif self.boxes[index][2]<=-3:
            self.boxes[index][2] += 3
            x = -3
        print(index)
        obj=self.boxes[index][0]
        obj1 = self.boxes[index][1]
        if x!=0:
            self.moving_process(obj,obj1,x)
            self.game.window.after(2,lambda: self.move(index))
        else:
            if self.boxes[index][3]=='plus':
                self.boxes[index][2]=-300
                self.boxes[index][3] = 'minus'
                self.game.window.after(4000,lambda: self.move(index))
            else:
                self.game.main_canvas.delete(obj),self.game.main_canvas.delete(obj1)
                self.boxes.pop(index)

    def moving_process(self,*objects):
        for obj in objects[:-1:]:
            coord=self.game.main_canvas.coords(obj)
            if len(coord)==4:
                self.game.main_canvas.coords(obj,coord[0]-objects[2],coord[1],coord[2]--objects[2],coord[3])
            else:
                self.game.main_canvas.coords(obj, coord[0] - objects[2], coord[1])


    def get_achieve(self,num):
        if self.achieve[num-1]=='N':
            self.achieve[num-1]='Y'
            if self.game.Menu.curMenu=='Achievements':
                self.game.main_canvas.itemconfigure(self.placed[num-1][0],fill='#349606')
            ##unlocks##
            if num==20:
                self.game.Aspects.add()

            ##box##
            self.create_box(num-1)

    def achieve_mult(self,*type):
        x=1
        if '1 Counter' in type:
            if self.achieve[0]=='Y':
                x*=1.1
        if '2 Counter' in type:
            if self.achieve[1]=='Y':
                x*=1.1
        if '3 Counter' in type:
            if self.achieve[2]=='Y':
                x*=1.1
        if '4 Counter' in type:
            if self.achieve[3]=='Y':
                x*=1.1
        if '5 Counter' in type:
            if self.achieve[4]=='Y':
                x*=1.1
        if '6 Counter' in type:
            if self.achieve[5]=='Y':
                x*=1.1
        if '7 Counter' in type:
            if self.achieve[6]=='Y':
                x*=1.1
        if '8 Counter' in type:
            if self.achieve[7]=='Y':
                x*=1.1
        if 'Time speed' in type:
            if self.achieve[11]=='Y':
                x*=1.01
            if self.achieve[12]=='Y':
                x*=1.1
            if self.achieve[24]=='Y':
                x*=1.25
            if self.achieve[26]=='Y':
                x*=1.25
        if '1 Counter' in type or '2 Counter' in type or '3 Counter' in type or '4 Counter' in type or '5 Counter' in type or '6 Counter' in type or '7 Counter' in type or '8 Counter' in type:
            if self.achieve[13]=='Y':
                x*=1.05
        if 'IC' in type:
            if self.achieve[14]=='Y':
                x *= 2
            if self.achieve[16]=='Y':
                x *= 2
            if self.achieve[20]=='Y':
                x *= 1.25
            if self.achieve[21]=='Y':
                x *= 2
            if self.achieve[22] == 'Y':
                x *= 2
            if self.achieve[27]=='Y':
                x*=2
        if 'DD' in type:
            if self.achieve[14]=='Y':
                x *= 1.5
        return x



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

    def click(self,event):
        if self.chosen=='Y':
            self.hide_option()
        index=0
        for list in self.placed:
            coords=self.game.main_canvas.coords(list[0])
            if event.x > coords[0] and event.y > coords[1] and event.x < coords[2] and event.y < coords[3]:
                self.chosen = 'Y'
                list=[]
                texts=self.texts[index]
                list.append(self.game.main_canvas.create_rectangle(coords[0]-70,coords[3]+2,coords[2]+70,coords[3]+122, width=1, fill='black', outline='#d6b929'))
                list.append(self.game.main_canvas.create_text((coords[0]+coords[2])//2,coords[3]+4,
                                                                     anchor='n',
                                                                     text=texts[0],
                                                                     fill='white', justify='center',
                                                                     font=('bahnschrift', 12),width=180))
                list.append(self.game.main_canvas.create_text((coords[0] + coords[2]) // 2, coords[3] + 24,
                                                              anchor='n',
                                                              text=texts[1],
                                                              fill='white', justify='center',
                                                              font=('bahnschrift', 10), width=180))
                if texts[2]!='-':
                    list.append(self.game.main_canvas.create_text((coords[0] + coords[2]) // 2, coords[3] + 120,
                                                              anchor='s',
                                                              text=texts[2],
                                                              fill='#ffe603', justify='center',
                                                              font=('bahnschrift', 10), width=180))
                self.created.append(list)

            index+=1




    def hide_option(self):
        if self.chosen=='Y':
            for list in self.created:
                for object in list:
                    self.game.main_canvas.delete(object)

    def hide_ach(self):
        for list in self.placed:
            for object in list:
                self.game.main_canvas.delete(object)

    def hide(self):
        self.game.main_canvas.delete(self.box)
        self.hide_option()
        self.hide_ach()
        self.chosen = 'N'
        self.placed = []
        self.created = []

    def get_save(self):
        print(self.achieve)
        data='['
        for obj in self.achieve:
            data+=str(obj)+','
        data+=']\n'
        return data
