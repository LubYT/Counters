import random
from tkinter import *
import pygame
import os
pygame.mixer.init()
from mutagen.mp3 import MP3
# from PIL import Image
# import stagger
# import io




class Music:
    def __init__(self,game):
        self.play=False
        self.paused = False
        self.placed=False
        self.cur_music="-"
        self.game=game
        self.mode='Basic'
        self.time_music = 0
        self.song_len=0
        self.switch=False
        self.arrow_left = PhotoImage(file='Data/Files/images/auto_other/arrow_left.png').zoom(2,2)
        self.arrow_right = PhotoImage(file='Data/Files/images/auto_other/arrow_right.png').zoom(2,2)
        self.pause_img = PhotoImage(file='Data/Files/images/mp/pause.png')
        self.play_img = PhotoImage(file='Data/Files/images/mp/resume.png')
        self.sound_img = PhotoImage(file='Data/Files/images/mp/sound.png')
        self.left_img =PhotoImage(file='Data/Files/images/mp/left.png')
        self.right_img = PhotoImage(file='Data/Files/images/mp/right.png')
        self.volume_img = PhotoImage(file='Data/Files/images/mp/volume.png')
        self.basic = PhotoImage(file='Data/Files/images/mp/basic.png')
        self.repeat = PhotoImage(file='Data/Files/images/mp/repeat.png')
        self.random = PhotoImage(file='Data/Files/images/mp/random.png')
        list=os.listdir('Data/Music')
        list.remove('__pycache__')
        list.remove('Musicplayer.py')
        list.remove('README.txt')
        list.remove('settings')
        self.playlists=list
        self.page=1
        with open('Data/Music/settings','r') as file:
            data=[]
            if file.readline()[:-1:]=='True':
                data.append(True)
            else: data.append(False)
            data.append(int(file.readline()[:-1:]))
            data.append(file.readline()[:-1:])
            data.append(file.readline())
            self.settings=data
        self.mode = self.settings[2]

    def open_canvas(self):
        if self.placed==False:
            self.placed=True
            self.canvas=Canvas(width=self.game.geometry[0]-self.game.geometry[0]/8,height=self.game.geometry[1]-self.game.geometry[1]/8,borderwidth=0, highlightthickness=0,bg='white')
            self.canvas.place(x=self.game.geometry[0]/16,y=self.game.geometry[1]/16)
            self.size=[self.game.geometry[0]-self.game.geometry[0]/8,self.game.geometry[1]-self.game.geometry[1]/8]
            self.canvas.create_rectangle(0,0,self.size[0],self.size[1],width=6,fill='black',outline='#ad0000')
            self.canvas.create_rectangle(self.size[0]-self.size[0]/4, self.size[1],self.size[0],0, width=4, fill='black', outline='#ad0000')
            self.canvas.create_rectangle(self.size[0] / 4, self.size[1], 0, 0, width=4,
                                         fill='black', outline='#ad0000')
            self.canvas.bind('<Button-1>',self.click)
            self.game.window.bind('<space>',self.play_pause)
            self.game.window.bind('<MouseWheel>', self.wheel)
            self.place_playlists()
            self.place_musiclist()
            self.place_music()
        else:
            self.placed=False
            self.close_canvas()

    def wheel(self,event):
        if event.x>0 and event.x<self.size[0]/4:
            if event.delta==-120:
                if self.page <= int(len(self.music_list) / 15):
                    self.page += 1
                    self.musiclist_del()
                    self.place_musiclist()
            if event.delta == 120:
                if self.page > 1:
                    self.page -= 1
                    self.musiclist_del()
                    self.place_musiclist()


    def place_playlists(self):
        self.play_widgets=[]
        for playlist in self.playlists:
            list=[]
            boost_y=len(self.play_widgets)*65
            list.append(self.canvas.create_rectangle(self.size[0] - self.size[0] / 4+10, 70+boost_y, self.size[0]-10, 10+boost_y, width=2,
                                         fill='black', outline='#ad0000'))
            list.append(self.canvas.create_text(self.size[0] - self.size[0] / 4 + 15, 40 + boost_y, text=playlist,
                                    anchor='w', justify='center', fill='#61c449',
                                    font=('bahnschrift', 14), width=self.size[0] / 4 - 25))
            self.play_widgets.append(list)

    def place_musiclist(self):
        try:
            self.music_list=os.listdir('Data/Music/'+self.settings[3])
        except:
            self.music_list = os.listdir('Data/Music/'+self.playlists[0])
        self.list_music_w=[]
        crack=self.music_list[(self.page-1)*15:self.page*15:]
        x=0
        for music in crack:
            list = []
            boost_y = x * ((self.size[1] -self.size[1] / 4)/16)
            if music==self.cur_music:
                list.append(
                    self.canvas.create_rectangle(10, 10 + boost_y, self.size[0] / 4 - 10,
                                                 10 + ((self.size[1] - self.size[1] / 4) / 15) + boost_y - 7, width=2,
                                                 fill='black', outline='#6ff763'))
                list.append(
                    self.canvas.create_text(15, 10 + ((self.size[1] - self.size[1] / 4) / 30) + boost_y - 3, text=music,
                                            anchor='w', justify='center', fill='#61c449',
                                            font=('bahnschrift', 14), width=self.size[0] / 4 - 25))
                list.append(music)
            else:
                list.append(
                    self.canvas.create_rectangle(10, 10+boost_y, self.size[0] / 4 - 10,
                                                 10 +((self.size[1] -self.size[1] / 4)/15)+ boost_y-7, width=2,
                                                 fill='black', outline='#ad0000'))
                list.append(self.canvas.create_text(15, 10 +((self.size[1] -self.size[1] / 4)/30)+ boost_y-3, text=music,
                                                    anchor='w', justify='center', fill='#61c449',
                                                    font=('bahnschrift', 14), width=self.size[0] / 4 - 25))
                list.append(music)
            self.list_music_w.append(list)
            x+=1
        self.left_box=self.canvas.create_rectangle(9,self.size[1]-9, 73, self.size[1]-73,width=2,
                                         fill='black', outline='#ad0000')
        self.left=self.canvas.create_image(40,self.size[1]-40,image=self.arrow_left,anchor='center')
        self.right_box = self.canvas.create_rectangle(self.size[0] / 4-9, self.size[1] - 9, self.size[0] / 4-73, self.size[1] - 73, width=2,
                                                     fill='black', outline='#ad0000')
        self.right = self.canvas.create_image(self.size[0] / 4-40, self.size[1] - 40, image=self.arrow_right, anchor='center')
        self.cur_page_text=self.canvas.create_text(self.size[0] / 4-self.size[0] / 8, self.size[1] - 40, text='Page\n'+str(self.page),
                                                    anchor='center', justify='center', fill='white',
                                                    font=('bahnschrift', 20))

    def choose_playlist(self,playlist):
        self.settings[3]=playlist
        self.paused=False
        self.play = False
        self.switch=True
        pygame.mixer.music.unload()
        self.time_music=0
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        self.page=1
        self.musiclist_del()
        self.place_musiclist()
        self.conf_play_pause()

    def choose_music(self,music):
        self.time_music = 0
        self.cur_music=music
        self.conf_musiclist()
        audio = MP3('Data/Music/' + self.settings[3] + '/' + self.cur_music)
        self.song_len=audio.info.length
        self.conf_name()
        self.conf_timers()
        if self.paused:
            self.play_pause()
        if self.play:
            self.play_music()



    def musiclist_del(self):
        for playlist in self.list_music_w:
            for x in playlist:
                self.canvas.delete(x)
        self.list_music_w=[]
        self.canvas.delete(self.left),self.canvas.delete(self.left_box)
        self.canvas.delete(self.right), self.canvas.delete(self.right_box)
        self.canvas.delete(self.cur_page_text)

    def play_music(self,*args):
        self.switch=False
        if 'scale' in args:
            pygame.mixer.music.load('Data/Music/' + self.settings[3] + '/' + self.cur_music)
            pygame.mixer.music.set_volume(self.settings[1] / 100)
            if self.paused==False and self.play:
                pygame.mixer.music.play(start=self.time_music)
        else:
            if self.paused==False:
                pygame.mixer.music.load('Data/Music/'+self.settings[3]+'/'+self.cur_music)
                pygame.mixer.music.set_volume(self.settings[1] / 100)
                pygame.mixer.music.play(start=self.time_music)
                # mp3 = stagger.read_tag('song.mp3')
                # by_data = mp3[stagger.id3.APIC][0].data
                # im = io.BytesIO(by_data)
                # imageFile = Image.open(im)
                # self.conf_img(imageFile)
                # self.conf_img(self.sound_img)
            else:
                pygame.mixer.music.unpause()


    def get_next(self):
        if self.play:
            if pygame.mixer.music.get_busy()==False and self.paused==False:
                self.time_pause=0
                self.next_process()
            self.conf_musiclist()
            self.conf_timers()
            self.game.main_canvas.after(50,self.get_next)

    def next_process(self):
        if self.play:
            self.time_music = 0
            if self.mode == 'Basic':
                index = self.music_list.index(self.cur_music)
                try:
                    self.cur_music = self.music_list[index + 1]
                except:
                    self.cur_music = self.music_list[0]
            elif self.mode == 'Repeat':
                pass
            elif self.mode=='Random':
                name=str(self.cur_music)
                max_num=len(self.music_list)
                min_num=0
                self.cur_music=self.music_list[random.randint(min_num,max_num)]
                if name==self.cur_music:
                    index = self.music_list.index(self.cur_music)
                    try:
                        self.cur_music = self.music_list[index + 1]
                    except:
                        self.cur_music = self.music_list[0]
            self.play_music()
            self.conf_name()

    def back_process(self):
        if self.play:
            self.time_music = 0
            if self.mode == 'Basic':
                index = self.music_list.index(self.cur_music)
                if index>0:
                    self.cur_music = self.music_list[index - 1]
                else:
                    index=len(self.music_list)
                    self.cur_music = self.music_list[index-1]
            elif self.mode == 'Repeat':
                pass
            elif self.mode=='Random':
                name=str(self.cur_music)
                max_num=len(self.music_list)
                min_num=0
                self.cur_music=self.music_list[random.randint(min_num,max_num)]
                if name==self.cur_music:
                    index = self.music_list.index(self.cur_music)
                    try:
                        self.cur_music = self.music_list[index + 1]
                    except:
                        self.cur_music = self.music_list[0]
            self.play_music()
            self.conf_name()



    def play_pause(self,*arg):
        if self.play:
            self.play=False
            self.paused=True
            pygame.mixer.music.pause()
        else:
            self.play=True
            self.play_music()
            self.get_next()
            self.paused = False
        self.conf_play_pause()


    def conf_musiclist(self):
        if self.placed:
            for box in self.list_music_w:
                if self.cur_music==box[2]:
                    self.canvas.itemconfigure(box[0], outline='#6ff763')
                else:
                    self.canvas.itemconfigure(box[0], outline='#ad0000')

    def conf_play_pause(self):
        if self.paused or self.play==False:
            self.canvas.itemconfigure(self.play_box, outline='#ad0000')
            self.canvas.itemconfigure(self.play_box_img, image=self.play_img)
        else:
            self.canvas.itemconfigure(self.play_box, outline='#faa019')
            self.canvas.itemconfigure(self.play_box_img, image=self.pause_img)

    def click_line(self,event,coo):
        if event.x<=coo[0]:
            self.time_music=0
            self.play_music('scale')
        elif event.x>=coo[2]:
            self.time_music = 0
            if self.play:
                self.next_process()
        else:
            self.time_music=((event.x-coo[0])/(coo[2]-coo[0]))*self.song_len
            self.play_music('scale')
        self.conf_timers()

    def click_volume(self,event,coo):
        if event.x<=coo[0]:
            self.settings[1]=0
        elif event.x>=coo[2]:
            self.settings[1]=100
        else:
            self.settings[1]= int(round(((event.x - coo[0]) / (coo[2] - coo[0]))*100,0))
        pygame.mixer.music.set_volume(self.settings[1] / 100)
        self.conf_volume()

    def next_music(self):
        if self.paused:
            self.play_pause()
        self.next_process()

    def back_music(self):
        if self.paused:
            self.play_pause()
        self.back_process()


    def click(self,event):
        for widget in self.play_widgets:
            coords_1 = self.canvas.coords(widget[0])
            if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
                playlist=self.playlists[self.play_widgets.index(widget)]
                self.choose_playlist(playlist)
        for widget in self.list_music_w:
            coords_1 = self.canvas.coords(widget[0])
            if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
                music=self.music_list[self.list_music_w.index(widget)+15*(self.page-1)]
                print('choose')
                self.choose_music(music)
        coords_1 = self.canvas.coords(self.right_m_box)
        if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
            self.next_music()
        coords_1 = self.canvas.coords(self.left_m_box)
        if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
            self.back_music()
        coords_1 = self.canvas.coords(self.box_mode)
        if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
            self.change_mode()
        coords_1 = self.canvas.coords(self.left_box)
        if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
            if self.page>1:
                self.page-=1
                self.musiclist_del()
                self.place_musiclist()
        coords_1 = self.canvas.coords(self.line)
        if event.x > coords_1[0]-20 and event.y > coords_1[1]-15 and event.x < coords_1[2]+20 and event.y < coords_1[3]+15:
            self.click_line(event,coords_1)
        coords_1 = self.canvas.coords(self.volume_line)
        if event.x > coords_1[0] - 20 and event.y > coords_1[1] - 15 and event.x < coords_1[2] + 20 and event.y < \
                coords_1[3] + 15:
            self.click_volume(event, coords_1)
        coords_1 = self.canvas.coords(self.play_box)
        if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
            self.play_pause()
        coords_1 = self.canvas.coords(self.right_box)
        if event.x > coords_1[0] and event.y > coords_1[1] and event.x < coords_1[2] and event.y < coords_1[3]:
            if self.page <= int(len(self.music_list)/15):
                self.page += 1
                self.musiclist_del()
                self.place_musiclist()


    def conf_name(self):
        if self.placed:
            self.canvas.itemconfigure(self.text_name,text=self.cur_music)

    def conf_timers(self):
        if self.placed:
            self.conf_circle()
            self.canvas.itemconfigure(self.text_timer, text=self.notation('timer'))
            self.canvas.itemconfigure(self.text_len,text=self.notation('len'))

    def notation(self,arg):
        if arg=='timer':
            if self.switch:
                time=0
            else:
                time=(pygame.mixer.music.get_pos()+self.time_music)/1000+self.time_music

            min=0
            while time>60:
                min+=1
                time-=60
            bx1=str(min)
            bx2=str(int(time))
            x=0
            while len(bx2)<2:
                x+=1
                bx2=(str(0)*x)+str(int(time))
            return bx1+':'+bx2
        if arg=='len':
            time=self.song_len
            min = 0
            while time > 60:
                min += 1
                time -= 60
            bx1 = str(min)
            bx2 = str(int(time))
            if len(bx2) < 2 and min > 0:
                bx2 = str(0) + str(int(time))
            return bx1 + ':' + bx2

    def conf_circle(self):
        if self.placed:
            if self.switch:
                x=0
            else:
                if ((pygame.mixer.music.get_pos()/1000+self.time_music)/self.song_len)<0:
                    x=0
                elif ((pygame.mixer.music.get_pos()/1000+self.time_music)/self.song_len)>1:
                    x=1
                else:
                    x=((pygame.mixer.music.get_pos()/1000+self.time_music)/self.song_len)
            self.canvas.coords(self.cicrle,
                               self.size[0] / 2-self.size[0]/8-8  +x*self.size[0] / 4,
                               self.size[1] / 2 + 80-8,
                               self.size[0] / 2 - self.size[0] / 8+8  +x*self.size[0] / 4,
                               self.size[1] / 2 + 80+8)

    def conf_volume(self):
        if self.placed:
            self.canvas.coords(self.volume_circle,self.size[0] / 2-self.size[0]/24-8+(self.size[0]/12*self.settings[1]/100), self.size[1] / 2 +262,
                                                 self.size[0] / 2-self.size[0]/24+8+(self.size[0]/12*self.settings[1]/100),self.size[1] / 2 +278)

    def conf_mode_box(self):
        if self.mode=='Basic':
            self.canvas.itemconfigure(self.box_mode_img,image=self.basic)
        elif self.mode=='Repeat':
            self.canvas.itemconfigure(self.box_mode_img,image=self.repeat)
        elif self.mode=='Random':
            self.canvas.itemconfigure(self.box_mode_img,image=self.random)

    def change_mode(self):
        if self.mode == 'Basic':
            self.mode='Repeat'
        elif self.mode == 'Repeat':
            self.mode='Random'
        elif self.mode == 'Random':
            self.mode='Basic'
        self.conf_mode_box()


    def place_music(self):
        self.canvas.create_rectangle(self.size[0]/2-100, self.size[1]/2-200,self.size[0]/2+100, self.size[1]/2, width=3, fill='black', outline='#ad0000')
        self.img_music = self.canvas.create_image(self.size[0] / 2, self.size[1] / 2-100, anchor='center',
                                                     image=self.sound_img)
        self.play_box=self.canvas.create_rectangle(self.size[0] / 2 - 40, self.size[1] / 2 +210, self.size[0] / 2 + 40,
                                     self.size[1] / 2+130, width=2, fill='black', outline='#faa019')
        self.play_box_img=self.canvas.create_image(self.size[0] / 2,self.size[1] / 2+170,anchor='center',image=self.pause_img)
        self.left_m_box = self.canvas.create_rectangle(self.size[0] / 2 - 80, self.size[1] / 2 + 210,
                                                     self.size[0] / 2 -160,
                                                     self.size[1] / 2 + 130, width=2, fill='black', outline='#ad0000')
        self.left_m_box_img = self.canvas.create_image(self.size[0] / 2-120, self.size[1] / 2 + 170, anchor='center',
                                                     image=self.left_img)
        self.right_m_box = self.canvas.create_rectangle(self.size[0] / 2 + 80, self.size[1] / 2 + 210,
                                                       self.size[0] / 2 + 160,
                                                       self.size[1] / 2 + 130, width=2, fill='black', outline='#ad0000')
        self.right_m_box_img = self.canvas.create_image(self.size[0] / 2 + 120, self.size[1] / 2 + 170, anchor='center',
                                                       image=self.right_img)
        self.line=self.canvas.create_rectangle(self.size[0] / 2-self.size[0]/8, self.size[1] / 2 +80, self.size[0] / 2+self.size[0]/8,
                                     self.size[1] / 2+80, width=2, fill='black', outline='#ad0000')
        self.cicrle = self.canvas.create_oval(self.size[0] / 2 - self.size[0] / 8-8, self.size[1] / 2 + 80-8,
                                                 self.size[0] / 2 - self.size[0] / 8+8,
                                                 self.size[1] / 2 + 80+8, width=3, fill='black', outline='#ad0000')
        self.text_name = self.canvas.create_text(self.size[0] / 2, self.size[1] / 2+25, text=self.cur_music,
                                                    anchor='center', justify='center', fill='#ffcfcf',
                                                    font=('bahnschrift', 20))
        self.text_timer = self.canvas.create_text(self.size[0] / 2-self.size[0]/8, self.size[1] / 2 +100, text='',
                                                 anchor='center', justify='center', fill='#ffcfcf',
                                                 font=('bahnschrift', 16))
        self.text_len = self.canvas.create_text(self.size[0] / 2+self.size[0]/8, self.size[1] / 2 +100, text='',
                                                 anchor='center', justify='center', fill='#ffcfcf',
                                                 font=('bahnschrift', 16))
        self.box_mode = self.canvas.create_rectangle(self.size[0] / 2+self.size[0]/24+33, self.size[1] / 2 + 243,
                                                        self.size[0] / 2+self.size[0]/24+85,
                                                        self.size[1] / 2 + 295, width=2, fill='black',
                                                        outline='#ad0000')
        self.box_mode_img = self.canvas.create_image(self.size[0] / 2+self.size[0]/24+59, self.size[1] / 2 +269, anchor='center',
                                                       image=self.volume_img)
        self.volume_line=self.canvas.create_rectangle(self.size[0] / 2-self.size[0]/24, self.size[1] / 2 +270, self.size[0] / 2+self.size[0]/24,
                                     self.size[1] / 2+270, width=2, fill='black', outline='#ad0000')
        self.volume_box_img = self.canvas.create_image(self.size[0] / 2-self.size[0]/24-60, self.size[1] / 2 +270, anchor='center',
                                                       image=self.volume_img)
        self.volume_circle =self.canvas.create_oval(self.size[0] / 2-self.size[0]/24-8+(self.size[0]/12*self.settings[1]/100), self.size[1] / 2 +262,
                                                 self.size[0] / 2-self.size[0]/24+8+(self.size[0]/12*self.settings[1]/100),
                                                 self.size[1] / 2 +278, width=3, fill='black', outline='#ad0000')
        self.conf_play_pause()
        self.conf_mode_box()
        self.conf_timers()

    def close_canvas(self):
        self.canvas.destroy()

    def save(self):
        with open('Data/Music/settings', 'w') as file:
            file.write('placeholder lol\n'+str(self.settings[1])+'\n'+self.mode+'\n'+self.settings[3])


