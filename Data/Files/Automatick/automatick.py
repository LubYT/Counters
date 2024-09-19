from tkinter import *

play=PhotoImage(file='Data/Files/images/auto_other/play.png')
pause=PhotoImage(file='Data/Files/images/auto_other/pause.png')
delete=PhotoImage(file='Data/Files/images/auto_other/delete.png')
reset=PhotoImage(file='Data/Files/images/auto_other/reset.png')

class Automatick:
    def __init__(self,game):
        self.game=game
        self.time_cycle=int(self.game.Save.Auto_data[0][3])
        self.time_cycle_cur=2000
        self.cycle_active=bool(self.game.Save.Auto_data[0][4])
        self.allowed=self.game.Save.Auto_data[0][2]
        self.commands=self.game.Save.Auto_data[0][0]
        self.first_open=False
        self.blocks=[]
        self.buttons=[]
        self.main_list=[]
        self.saved_nums_for_bars={1:self.game.Save.Auto_data[0][1][0],2:self.game.Save.Auto_data[0][1][1]}
        print(self.cycle_active,self.allowed,self.commands,self.saved_nums_for_bars)
        self.current_bar='N'
        self.type_command_add ='N'
        self.chosen_block='N'
        self.cycle()

    def place(self):

        self.chosen_block = 'N'

        self.rect=self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 500, 200,
                                                              self.game.geometry[0] // 2 + 100, 610, width=1,
                                                              fill='#062b3b', outline='#4c9ec2')
        self.rect_1_2 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 490, 210,
                                                           self.game.geometry[0] // 2 + 90, 550, width=1,
                                                           fill='#00031f', outline='#070e47')
        self.rect_2 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +103, 200,
                                                           self.game.geometry[0] // 2 + 320, 280, width=1,
                                                           fill='#515859', outline='#4c9ec2')

        self.buttons.append([[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 490, 555,
                                                               self.game.geometry[0] // 2 - 450, 595, width=1,
                                                               fill='#012e00', outline='#40ff3d'),
            self.game.main_canvas.create_image(self.game.geometry[0] // 2 - 468, 575,image=play,anchor='center')
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 400, 555,
                                                                        self.game.geometry[0] // 2 - 440, 595, width=1,
                                                                        fill='#141002', outline='#ffd53d'),
            self.game.main_canvas.create_image(self.game.geometry[0] // 2 - 419, 575, image=pause,
                                                                     anchor='center')]
            , [
                self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 390, 555,
                                                       self.game.geometry[0] // 2 - 350, 595, width=1,
                                                       fill='#121212', outline='#b3b3b3'),
                self.game.main_canvas.create_image(self.game.geometry[0] // 2 - 369, 575, image=delete,
                                                   anchor='center')]
            , [
                self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 340, 555,
                                                       self.game.geometry[0] // 2 - 300, 595, width=1,
                                                       fill='#330a0a', outline='#ff3d3d'),
                self.game.main_canvas.create_image(self.game.geometry[0] // 2 - 319, 575, image=reset,
                                                   anchor='center')]
        ])


        self.text=self.game.main_canvas.create_text(self.game.geometry[0] // 2 +105, 240,anchor='w',
                                                      text='Automatick programm.\nMake full cycle every '+str(round(self.time_cycle/1000,2))+' seconds.\n'
                                                            'You can add blocks in programm.\nYou can choose and delete any block.\nYou can put max 32 blocks.',
                                                      fill='#bef1f7', justify='left',font=('bahnschrift', 10))
        self.timer=self.game.main_canvas.create_text(self.game.geometry[0] // 2 +95, 575, anchor='e',
                                              text=str(round(self.time_cycle_cur/1000,5)),
                                              fill='#00cad9', justify='right', font=('bahnschrift', 24))
        self.blocks.append([[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +110, 290,
                                                              self.game.geometry[0] // 2 + 150, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 130, 310, anchor='center',
                                              text='Count 1\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_1_BUY',
            'Counter 1\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +160, 290,
                                                              self.game.geometry[0] // 2 + 200, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 180, 310, anchor='center',
                                              text='Count 2\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_2_BUY',
            'Counter 2\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +210, 290,
                                                              self.game.geometry[0] // 2 + 250, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 230, 310, anchor='center',
                                              text='Count 3\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_3_BUY',
            'Counter 3\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +260, 290,
                                                              self.game.geometry[0] // 2 + 300, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 280, 310, anchor='center',
                                              text='Count 4\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_4_BUY',
            'Counter 4\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +310, 290,
                                                              self.game.geometry[0] // 2 + 350, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 330, 310, anchor='center',
                                              text='Count 5\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_5_BUY',
            'Counter 5\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +360, 290,
                                                              self.game.geometry[0] // 2 + 400, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 380, 310, anchor='center',
                                              text='Count 6\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_6_BUY',
            'Counter 6\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +410, 290,
                                                              self.game.geometry[0] // 2 + 450, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 430, 310, anchor='center',
                                              text='Count 7\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_7_BUY',
            'Counter 7\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +460, 290,
                                                              self.game.geometry[0] // 2 + 500, 330, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 480, 310, anchor='center',
                                              text='Count 8\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'COUNT_8_BUY',
            'Counter 8\nsingle',
            'n'
        ],[
            self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 +110, 340,
                                                              self.game.geometry[0] // 2 + 180, 380, width=1,
                                                              fill='#04093b', outline='#484e8a'),
            self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 145, 360, anchor='center',
                                              text='Game speed\nBuy',
                                              fill='#263cff', justify='center', font=('bahnschrift', 8)),
            'GAME_SPEED_BUY',
            'Game speed\nsingle',
            'n'
        ]])
        self.place_temp()
        self.place_blocks()
        if self.first_open!=True:
            self.first_open=True
            self.save_data_get()

    def add_temp(self):
        pass

    def save_data_get(self):
        for command in self.commands:
            x = len(self.main_list) * 70
            y = 30
            while x >= 560:
                x -= 560
                y += 50
            if 'COUNT_1_BUY' == command:
                block=self.blocks[0][0]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_2_BUY' == command:
                block = self.blocks[0][1]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_3_BUY' == command:
                block = self.blocks[0][2]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_4_BUY' == command:
                block = self.blocks[0][3]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_5_BUY' == command:
                block = self.blocks[0][4]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_6_BUY' == command:
                block = self.blocks[0][5]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_7_BUY' == command:
                block = self.blocks[0][6]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'COUNT_8_BUY' == command:
                block = self.blocks[0][7]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'GAME_SPEED_BUY' == command:
                block = self.blocks[0][8]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y, width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'C_BOOST_BUY_' == command[:12:]:
                block=self.blocks[0][9]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y,
                                                               width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3] + command[12::],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])
            elif 'T_ACCEL_BUY_' == command[:12:]:
                block = self.blocks[0][10]
                one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                               self.game.geometry[0] // 2 - 413 + x, 230 + y,
                                                               width=1,
                                                               fill='#04093b', outline='#b2d9db'),
                one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                          anchor='center',
                                                          text=block[3] + command[12::],
                                                          fill='#263cff', justify='center', font=('bahnschrift', 9))
                index = self.commands.index(command)
                self.main_list.append([one_1, one_2, command, index])

    def place_temp(self):
        if self.allowed[0]=='Y':
            self.blocks[0].append([
                self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 430, 340,
                                                       self.game.geometry[0] // 2 + 500, 410, width=1,
                                                       fill='#04093b', outline='#484e8a'),
                self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 465, 360, anchor='center',
                                                  text='CNTR boost\nLimit:',
                                                  fill='#263cff', justify='center', font=('bahnschrift', 8)),
                'C_BOOST_BUY_',
                'CNTR boost\n',
                'limited',
                self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 435, 385,
                                                       self.game.geometry[0] // 2 + 495, 405, width=1,
                                                       fill='#000', outline='#484e8a'),
                self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 465, 395, anchor='center',
                                                  text='input',
                                                  fill='#263cff', justify='center', font=('bahnschrift', 8)),
                self.saved_nums_for_bars[1],
                1,
            ])
        if self.allowed[1]=='Y':
            self.blocks[0].append([
                self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 350, 340,
                                                       self.game.geometry[0] // 2 + 420, 410, width=1,
                                                       fill='#04093b', outline='#484e8a'),
                self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 385, 360, anchor='center',
                                                  text='Time accel\nLimit:',
                                                  fill='#263cff', justify='center', font=('bahnschrift', 8)),
                'T_ACCEL_BUY_',
                'Time accel\n',
                'limited',
                self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 + 355, 385,
                                                       self.game.geometry[0] // 2 + 415, 405, width=1,
                                                       fill='#000', outline='#484e8a'),
                self.game.main_canvas.create_text(self.game.geometry[0] // 2 + 385, 395, anchor='center',
                                                  text='input',
                                                  fill='#263cff', justify='center', font=('bahnschrift', 8)),
                self.saved_nums_for_bars[2],
                2,
            ])
        print(self.blocks)
        for block in self.blocks[0]:
            if block[4]=='limited':
                self.game.main_canvas.itemconfigure(block[6],text=block[7])



    def hide(self):
        self.game.main_canvas.delete(self.rect),self.game.main_canvas.delete(self.rect_1_2),self.game.main_canvas.delete(self.rect_2)
        self.game.main_canvas.delete(self.text),self.game.main_canvas.delete(self.timer)
        for block in self.blocks[0]:
            if block[4] == 'n':
                self.game.main_canvas.delete(block[0]),self.game.main_canvas.delete(block[1])
            elif block[4] == 'limited':
                self.game.main_canvas.delete(block[0]), self.game.main_canvas.delete(block[1])
                self.game.main_canvas.delete(block[5]), self.game.main_canvas.delete(block[6])
        for list in self.main_list:
            self.game.main_canvas.coords(list[0],-1000,-1000,-1000,-1000)
            self.game.main_canvas.coords(list[1], -1000, -1000)
        for btt in self.buttons[0]:
            self.game.main_canvas.delete(btt[0]), self.game.main_canvas.delete(btt[1])
        self.game.window.unbind('<KeyPress>')
        self.buttons=[]
        self.blocks=[]

    def play(self):
        self.cycle_active = True

    def stop(self):
        self.cycle_active = False

    def reset_blocks(self):
        self.stop()
        for list in self.main_list:
            self.game.main_canvas.delete(list[0])
            self.game.main_canvas.delete(list[1])
        self.main_list=[]
        self.commands=[]
        self.chosen_block='N'

    def delete_block(self):
        self.stop()
        if self.chosen_block != 'N':
            print(self.commands)
            self.game.main_canvas.delete(self.main_list[self.chosen_block][0])
            self.game.main_canvas.delete(self.main_list[self.chosen_block][1])
            self.commands.pop(self.main_list[self.chosen_block][3])
            self.main_list.pop(self.chosen_block)
            for list in self.main_list:
                if list[3]>0:
                    list[3]-=1
            self.chosen_block = 'N'
            self.place_blocks()

    def add_symbol(self,event):
        if self.current_bar!='N':
            try:
                if int(event.keysym)<10 and int(event.keysym)>-1:
                    if self.blocks[0][self.current_bar][7]=='input':
                        self.blocks[0][self.current_bar][7]=''
                    elif self.blocks[0][self.current_bar][7]=='0':
                        self.blocks[0][self.current_bar][7]=''
                    self.blocks[0][self.current_bar][7]+=str(event.keysym)
                    self.game.main_canvas.itemconfigure(self.blocks[0][self.current_bar][6],text=self.blocks[0][self.current_bar][7])
            except:
                if event.keysym=='BackSpace' and self.blocks[0][self.current_bar][7]!='':
                    if self.blocks[0][self.current_bar][7] != 'input':
                        self.blocks[0][self.current_bar][7] = self.blocks[0][self.current_bar][7][:-1:]
                        if self.blocks[0][self.current_bar][7] == '':
                            self.blocks[0][self.current_bar][7]='0'
                        self.game.main_canvas.itemconfigure(self.blocks[0][self.current_bar][6],
                                                            text=self.blocks[0][self.current_bar][7])
            self.saved_nums_for_bars[self.blocks[0][self.current_bar][8]] = self.blocks[0][self.current_bar][7]


    def click(self,coords):

        self.current_bar = 'N'

        ###

        play_coords=self.game.main_canvas.coords(self.buttons[0][0][0])
        if coords.x > play_coords[0] and coords.y>play_coords[1] and coords.x < play_coords[2] and coords.y<play_coords[3]:
            self.play()
        play_coords = self.game.main_canvas.coords(self.buttons[0][1][0])
        if coords.x > play_coords[0] and coords.y > play_coords[1] and coords.x < play_coords[2] and coords.y < \
                play_coords[3]:
            self.stop()
        delete_coords = self.game.main_canvas.coords(self.buttons[0][2][0])
        if coords.x > delete_coords[0] and coords.y > delete_coords[1] and coords.x < delete_coords[2] and coords.y < \
                delete_coords[3]:
            self.delete_block()
        reset_coords = self.game.main_canvas.coords(self.buttons[0][3][0])
        if coords.x > reset_coords[0] and coords.y > reset_coords[1] and coords.x < reset_coords[2] and coords.y < \
                reset_coords[3]:
            self.reset_blocks()

            ###

        for block in self.blocks[0]:
            coord = self.game.main_canvas.coords(block[0])
            if block[4]=='n':
                if coords.x > coord[0] and coords.y>coord[1] and coords.x < coord[2] and coords.y<coord[3] and len(self.commands) < 32:
                    self.type_command_add=block[2]
                    x=len(self.main_list)*70
                    y=30
                    while x>=560:
                        x-=560
                        y+=50
                    one_1=self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 -478+x, 190+y,
                                                                  self.game.geometry[0] // 2 - 413+x, 230+y, width=1,
                                                                  fill='#04093b', outline='#b2d9db'),
                    one_2=self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445+x, 210+y, anchor='center',
                                                  text=block[3],
                                                  fill='#263cff', justify='center', font=('bahnschrift', 9))
                    index=self.add_command(self.type_command_add)
                    self.main_list.append([one_1,one_2,self.type_command_add,index])
                    break

            elif block[4]=='limited':
                coord_1 = self.game.main_canvas.coords(block[5])
                if coords.x > coord_1[0] and coords.y > coord_1[1] and coords.x < coord_1[2] and coords.y < coord_1[3]:
                    self.current_bar = self.blocks[0].index(block)
                    self.game.window.bind("<KeyPress>",self.add_symbol)
                elif coords.x > coord[0] and coords.y>coord[1] and coords.x < coord[2] and coords.y<coord[3] and len(self.commands) < 32:
                    if block[7]=='input' or block[7]=='0':
                        use='unlimited'
                    else:
                        use=str(block[7])
                    self.type_command_add = block[2]+use
                    x = len(self.main_list) * 70
                    y = 30
                    while x >= 560:
                        x -= 560
                        y += 50
                    one_1 = self.game.main_canvas.create_rectangle(self.game.geometry[0] // 2 - 478 + x, 190 + y,
                                                                   self.game.geometry[0] // 2 - 413 + x, 230 + y,
                                                                   width=1,
                                                                   fill='#04093b', outline='#b2d9db'),
                    one_2 = self.game.main_canvas.create_text(self.game.geometry[0] // 2 - 445 + x, 210 + y,
                                                              anchor='center',
                                                              text=block[3] + use,
                                                              fill='#263cff', justify='center', font=('bahnschrift', 9))
                    index = self.add_command(self.type_command_add)
                    self.main_list.append([one_1, one_2, self.type_command_add, index])
                    break

            self.type_command_add ='N'


        ###

        for list in self.main_list:
            xy=self.game.main_canvas.coords(list[0])
            if coords.x > xy[0] and coords.y>xy[1] and coords.x < xy[2] and coords.y<xy[3]:
                if self.chosen_block != 'N':
                    self.game.main_canvas.itemconfigure(self.main_list[self.chosen_block][0], outline='#b2d9db')
                self.chosen_block=self.main_list.index(list)
                self.game.main_canvas.itemconfigure(self.main_list[self.chosen_block][0], outline='#6eff6b')

    def place_blocks(self):
        x=0
        y=30
        for list in self.main_list:
            if x>=560:
                x-=560
                y+=50
            self.game.main_canvas.tag_raise(list[0]),self.game.main_canvas.tag_raise(list[1])
            self.game.main_canvas.coords(list[0],self.game.geometry[0] // 2 -478+x, 190+y,
                                                              self.game.geometry[0] // 2 - 413+x, 230+y)
            self.game.main_canvas.coords(list[1],self.game.geometry[0] // 2 - 445+x, 210+y)
            x += 70


    def add_command(self,command):
        if command!='N':
            self.commands.append(command)
            index=self.commands.index(command)
            return index

    def auto_counter(self,command):
        if 'COUNT_1_BUY' == command:
            self.game.Counter_1.buy()
        elif 'COUNT_2_BUY' == command and self.game.Counter_1.first:
            self.game.Counter_2.buy()
        elif 'COUNT_3_BUY' == command and self.game.Counter_2.first:
            self.game.Counter_3.buy()
        elif 'COUNT_4_BUY' == command and self.game.Counter_3.first:
            self.game.Counter_4.buy()
        elif 'COUNT_5_BUY' == command and self.game.CB.amount>=1 and self.game.Counter_4.first:
            self.game.Counter_5.buy()
        elif 'COUNT_6_BUY' == command and self.game.CB.amount>=2 and self.game.Counter_5.first:
            self.game.Counter_6.buy()
        elif 'COUNT_7_BUY' == command and self.game.CB.amount>=3 and self.game.Counter_6.first:
            self.game.Counter_7.buy()
        elif 'COUNT_8_BUY' == command and self.game.CB.amount>=4 and self.game.Counter_7.first:
            self.game.Counter_8.buy()
        elif 'GAME_SPEED_BUY' == command:
            self.game.Tickspeed.buy()
        elif 'C_BOOST_BUY_' == command[:12:]:
            if command[12::]!='unlimited':
                if self.game.CB.amount<int(command[12::]):
                    self.game.CB.buy()
            else:
                self.game.CB.buy()
        elif 'T_ACCEL_BUY_' == command[:12:]:
            if command[12::] != 'unlimited':
                if self.game.TA.amount<int(command[12::]):
                    self.game.TA.buy()
            else:
                self.game.TA.buy()


    def iter_commands(self):
        for command in self.commands:
            self.auto_counter(command)
        print(self.commands)
        print(self.main_list)
    def cycle(self):
        if self.cycle_active:
            self.time_cycle_cur-=100
            if self.time_cycle_cur<=0:
                self.time_cycle_cur=self.time_cycle
                self.iter_commands()
            if self.game.Menu.curMenu=='Automatick':
                self.game.main_canvas.itemconfigure(self.timer,text=str(round(self.time_cycle_cur/1000,5)))
        else:
            self.time_cycle_cur=self.time_cycle
            if self.game.Menu.curMenu=='Automatick':
                self.game.main_canvas.itemconfigure(self.timer,text=str(round(self.time_cycle_cur/1000,5)))
        self.game.window.after(95,self.cycle)

    def get_save(self):
        data = ''
        data+='['
        for command in self.commands:
            data+=str(command)+','
        data+='],['
        for neznayu in self.saved_nums_for_bars:
            add=self.saved_nums_for_bars[neznayu]
            print(add)
            data+=str(add)+','
        data += '],['
        for allow in self.allowed:
            data+=str(allow)+','
        data += '],'
        data+=str(self.time_cycle)+','
        if self.cycle_active==True:
            data+=str(self.cycle_active)
        else:
            data+=''
        data+='\n'
        return data