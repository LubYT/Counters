from tkinter import *
import importlib
import sys
import Data.Files.Menu as menu_import
import Data.Files.Counters.value as value_import
import Data.Files.Counters.value_per_sec as value_per_sec_import
import Data.Files.Counters.Counter_boost as CB_import
import Data.Files.Saves.reader as save_import
import Data.Files.Layers.Infinity as I_import
import Data.Files.other.stats as Stats_import
import Data.Files.Doom.Doom as Doom_import
import Data.Files.Counters.Time_accelerator as TA_import
Aspects_import=importlib.import_module('Data.Files.Illusory aspects.Illusory aspects')
import Data.Files.Achievements.Achievements as achieve_import
import Data.Files.Counters.counter1 as counter1_import
import Data.Files.Counters.counter2 as counter2_import
import Data.Files.Counters.counter3 as counter3_import
import Data.Files.Counters.counter4 as counter4_import
import Data.Files.Counters.counter5 as counter5_import
import Data.Files.Counters.counter6 as counter6_import
import Data.Files.Counters.counter7 as counter7_import
import Data.Files.Counters.counter8 as counter8_import
import Data.Files.Counters.game_time as game_time_import

window=Tk()
window.title('Counters')
width=window.winfo_screenwidth()
window.iconbitmap("Data/Files/images/icon.ico")
height=window.winfo_screenheight()
window.attributes("-fullscreen", True)
window.geometry(str(width)+'x'+str(height))

import Data.Files.Automatick.automatick as import_automatick
class Game:
    def __init__(self,window,geometry):
        self.geometry=geometry
        self.window=window
        self.main_canvas=Canvas(width=geometry[0],height=geometry[1],bg='black')
        self.main_canvas.place(x=-2,y=-2)
        self.Save = save_import.Save(self)
        self.Menu=menu_import.Menu(self)
        self.Automatick=import_automatick.Automatick(self)
        self.Infinity=I_import.Infinity(self)
        self.TA=TA_import.Time_accelerator(self)
        self.CB=CB_import.Counter_boost(self)
        self.Value=value_import.Value(self)
        self.Doom=Doom_import.Doom(self)
        self.Value_PS = value_per_sec_import.Value_per_second(self)
        self.Aspects=Aspects_import.Illusory_aspects(self)
        self.Achievements=achieve_import.Achievements(self)
        self.Stats = Stats_import.Stats(self)
        self.Tickspeed = game_time_import.Tickspeed(self)
        self.Counter_1=counter1_import.Counter1(self)
        self.Counter_2 = counter2_import.Counter2(self)
        self.Counter_3 = counter3_import.Counter3(self)
        self.Counter_4 = counter4_import.Counter4(self)
        self.Counter_5 = counter5_import.Counter5(self)
        self.Counter_6 = counter6_import.Counter6(self)
        self.Counter_7 = counter7_import.Counter7(self)
        self.Counter_8 = counter8_import.Counter8(self)
        self.boost_cheat=False
        self.box=self.main_canvas.create_rectangle(geometry[0]-45,190,geometry[0]-(geometry[0]-45),geometry[1]+10,width=2,fill='black',outline='#ad0000')
        self.Value.place()
        self.Value_PS.place()
        self.Tickspeed.place()
        self.Counter_1.place()
        if self.Infinity.first:
            self.Infinity.post_save()
            self.menu_place()
    def tick(self):
        self.Counter_8.produce()
        self.Counter_7.produce()
        self.Counter_6.produce()
        self.Counter_5.produce()
        self.Counter_4.produce()
        self.Counter_3.produce()
        self.Counter_2.produce()
        self.Counter_1.produce()
        self.Infinity.other_funcs()
        self.Doom.produce()
        self.Stats.time()
        window.after(40, self.tick)
    def counters_reset(self):
        self.Counter_8.reset(),self.Counter_7.reset(),self.Counter_6.reset(),self.Counter_5.reset(),self.Counter_4.reset(), self.Counter_3.reset(),self.Counter_2.reset(),self.Counter_1.reset()
    def CB_reset(self):
        self.Value.reset(),self.Value_PS.reset(),self.Tickspeed.reset()
        self.Counter_8.reset(),self.Counter_7.reset(),self.Counter_6.reset(),self.Counter_5.reset(),self.Counter_4.reset(), self.Counter_3.reset(),self.Counter_2.reset(),self.Counter_1.reset()

    def TA_reset(self):
        self.CB.reset()
        self.Value.reset(), self.Value_PS.reset(), self.Tickspeed.reset()
        self.Counter_8.reset(), self.Counter_7.reset(), self.Counter_6.reset(), self.Counter_5.reset(), self.Counter_4.reset(), self.Counter_3.reset(), self.Counter_2.reset(), self.Counter_1.reset()

    def I_reset(self):
        self.Doom.reset(), self.Infinity.reset()
        self.TA.reset(),self.CB.reset()
        self.Value.reset(), self.Value_PS.reset(), self.Tickspeed.reset()
        self.Counter_8.reset(), self.Counter_7.reset(), self.Counter_6.reset(), self.Counter_5.reset(), self.Counter_4.reset(), self.Counter_3.reset(), self.Counter_2.reset(), self.Counter_1.reset()

    def menu_place(self):
        self.Menu.place_menus()
        self.Counter_1.return_place()
        self.main_canvas.coords(self.box, self.geometry[0]-125,190,self.geometry[0]-(self.geometry[0]-125),self.geometry[1]+10)

    def max(self,event):
        self.Counter_1.buy_max()
        if self.Counter_1.first:
            self.Counter_2.buy_max()
        if self.Counter_2.first:
            self.Counter_3.buy_max()
        if self.Counter_3.first:
            self.Counter_4.buy_max()
        if self.Counter_4.first and self.CB.amount>=1:
            self.Counter_5.buy_max()
        if self.Counter_5.first and self.CB.amount>=2:
            self.Counter_6.buy_max()
        if self.Counter_6.first and self.CB.amount>=3:
            self.Counter_7.buy_max()
        if self.Counter_7.first and self.CB.amount>=4:
            self.Counter_8.buy_max()
        self.Tickspeed.max_buy()

    def hide_counters(self):
        self.Counter_8.hide(), self.Counter_7.hide(), self.Counter_6.hide(), self.Counter_5.hide(), self.Counter_4.hide(), self.Counter_3.hide(), self.Counter_2.hide(), self.Counter_1.hide()

    def return_counters(self):
        self.Counter_8.return_place(), self.Counter_7.return_place(), self.Counter_6.return_place(), self.Counter_5.return_place(), self.Counter_4.return_place(), self.Counter_3.return_place(), self.Counter_2.return_place(), self.Counter_1.return_place()
    def click(self,event):
        if self.Menu.active:
            coords_menu_1 = self.main_canvas.coords(self.Menu.box)
            if event.x > coords_menu_1[0] and event.y > coords_menu_1[1] and event.x < coords_menu_1[2] and event.y < coords_menu_1[3]:
                self.Menu.open_new_cur('counters')
            coords_menu_2 = self.main_canvas.coords(self.Menu.box_1)
            if event.x > coords_menu_2[0] and event.y > coords_menu_2[1] and event.x < coords_menu_2[2] and event.y < coords_menu_2[3]:
                self.Menu.open_new_cur('infinity')
            coords_menu_3 = self.main_canvas.coords(self.Menu.box_2)
            if event.x > coords_menu_3[0] and event.y > coords_menu_3[1] and event.x < coords_menu_3[2] and event.y < \
                    coords_menu_3[3]:
                self.Menu.open_new_cur('automatick')
            coords_menu_5 = self.main_canvas.coords(self.Menu.box_4)
            if event.x > coords_menu_5[0] and event.y > coords_menu_5[1] and event.x < coords_menu_5[2] and event.y < \
                    coords_menu_5[3]:
                self.Menu.open_new_cur('achievements')
            if 'Illusory' in self.Menu.Allowed_menus:
                coords_menu_6 = self.main_canvas.coords(self.Menu.box_6)
                if event.x > coords_menu_6[0] and event.y > coords_menu_6[1] and event.x < coords_menu_6[2] and event.y < \
                        coords_menu_6[3]:
                    self.Menu.open_new_cur('Illusory')

            coords_menu_7 = self.main_canvas.coords(self.Menu.box_5)
            if event.x > coords_menu_7[0] and event.y > coords_menu_7[1] and event.x < coords_menu_7[2] and event.y < \
                    coords_menu_7[3]:
                self.Menu.open_new_cur('Stats')
            if 'doom' in self.Menu.Allowed_menus:
                coords_menu_4 = self.main_canvas.coords(self.Menu.box_3)
                if event.x > coords_menu_4[0] and event.y > coords_menu_4[1] and event.x < coords_menu_4[2] and event.y < \
                        coords_menu_4[3]:
                    self.Menu.open_new_cur('doom')
        if self.Value.first_e10:
            coords_cb = self.main_canvas.coords(self.CB.box_buy)
            if event.x > coords_cb[0] and event.y > coords_cb[1] and event.x < coords_cb[2] and event.y < coords_cb[3]:
                self.CB.buy()
        if self.Value.first_e50:
            coords_ta = self.main_canvas.coords(self.TA.box_buy)
            if event.x > coords_ta[0] and event.y > coords_ta[1] and event.x < coords_ta[2] and event.y < coords_ta[3]:
                self.TA.buy()
        if self.Value.first_inf:
            coords_I = self.main_canvas.coords(self.Infinity.box_buy)
            if event.x > coords_I[0] and event.y > coords_I[1] and event.x < coords_I[2] and event.y < coords_I[3]:
                self.Infinity.buy()
        coords_0 = self.main_canvas.coords(self.Tickspeed.box_buy)
        if event.x > coords_0[0] and event.y > coords_0[1] and event.x < coords_0[2] and event.y < coords_0[3]:
            self.Tickspeed.buy()
        coords_0_max = self.main_canvas.coords(self.Tickspeed.box_buy_max)
        if event.x > coords_0_max[0] and event.y > coords_0_max[1] and event.x < coords_0_max[2] and event.y < coords_0_max[3]:
            self.Tickspeed.max_buy()

        if self.Menu.curMenu == 'Automatick':
            self.Automatick.click(event)

        if self.Menu.curMenu == 'Doom':
            self.Doom.click(event)

        if self.Menu.curMenu == 'Achievements':
            self.Achievements.click(event)


        if self.Menu.curMenu == 'Infinity':
            coords_upgr_1 = self.main_canvas.coords(self.Infinity.upgr_1_box)
            if event.x > coords_upgr_1[0] and event.y > coords_upgr_1[1] and event.x < coords_upgr_1[2] and event.y < coords_upgr_1[3]:
                self.Infinity.buy_upgrade(1)
            coords_upgr_2 = self.main_canvas.coords(self.Infinity.upgr_2_box)
            if event.x > coords_upgr_2[0] and event.y > coords_upgr_2[1] and event.x < coords_upgr_2[2] and event.y < \
                    coords_upgr_2[3]:
                self.Infinity.buy_upgrade(2)
            coords_upgr_3 = self.main_canvas.coords(self.Infinity.upgr_3_box)
            if event.x > coords_upgr_3[0] and event.y > coords_upgr_3[1] and event.x < coords_upgr_3[2] and event.y < \
                    coords_upgr_3[3]:
                self.Infinity.buy_upgrade(3)
            coords_upgr_4 = self.main_canvas.coords(self.Infinity.upgr_4_box)
            if event.x > coords_upgr_4[0] and event.y > coords_upgr_4[1] and event.x < coords_upgr_4[2] and event.y < \
                    coords_upgr_4[3]:
                self.Infinity.buy_upgrade(4)
            coords_upgr_5 = self.main_canvas.coords(self.Infinity.upgr_5_box)
            if event.x > coords_upgr_5[0] and event.y > coords_upgr_5[1] and event.x < coords_upgr_5[2] and event.y < \
                    coords_upgr_5[3]:
                self.Infinity.buy_upgrade(5)
            coords_upgr_6 = self.main_canvas.coords(self.Infinity.upgr_6_box)
            if event.x > coords_upgr_6[0] and event.y > coords_upgr_6[1] and event.x < coords_upgr_6[2] and event.y < \
                    coords_upgr_6[3]:
                self.Infinity.buy_upgrade(6)
            coords_upgr_7 = self.main_canvas.coords(self.Infinity.upgr_7_box)
            if event.x > coords_upgr_7[0] and event.y > coords_upgr_7[1] and event.x < coords_upgr_7[2] and event.y < \
                    coords_upgr_7[3]:
                self.Infinity.buy_upgrade(7)

        if self.Menu.curMenu=='Counters':
            coords_1=self.main_canvas.coords(self.Counter_1.box_buy)
            if event.x>coords_1[0] and event.y>coords_1[1] and event.x<coords_1[2] and event.y<coords_1[3]:
                self.Counter_1.buy()
            coords_1_max = self.main_canvas.coords(self.Counter_1.box_buy_max)
            if event.x > coords_1_max[0] and event.y > coords_1_max[1] and event.x < coords_1_max[2] and event.y < coords_1_max[3]:
                self.Counter_1.buy_max()
            if self.Counter_1.first:
                coords_2 = self.main_canvas.coords(self.Counter_2.box_buy)
                if event.x > coords_2[0] and event.y > coords_2[1] and event.x < coords_2[2] and event.y < coords_2[3]:
                    self.Counter_2.buy()
                coords_2_max = self.main_canvas.coords(self.Counter_2.box_buy_max)
                if event.x > coords_2_max[0] and event.y > coords_2_max[1] and event.x < coords_2_max[2] and event.y < coords_2_max[3]:
                    self.Counter_2.buy_max()
            if self.Counter_2.first:
                coords_3 = self.main_canvas.coords(self.Counter_3.box_buy)
                if event.x > coords_3[0] and event.y > coords_3[1] and event.x < coords_3[2] and event.y < coords_3[3]:
                    self.Counter_3.buy()
                coords_3_max = self.main_canvas.coords(self.Counter_3.box_buy_max)
                if event.x > coords_3_max[0] and event.y > coords_3_max[1] and event.x < coords_3_max[2] and event.y < coords_3_max[3]:
                    self.Counter_3.buy_max()
            if self.Counter_3.first:
                coords_4 = self.main_canvas.coords(self.Counter_4.box_buy)
                if event.x > coords_4[0] and event.y > coords_4[1] and event.x < coords_4[2] and event.y < coords_4[3]:
                    self.Counter_4.buy()
                coords_4_max = self.main_canvas.coords(self.Counter_4.box_buy_max)
                if event.x > coords_4_max[0] and event.y > coords_4_max[1] and event.x < coords_4_max[2] and event.y < coords_4_max[3]:
                    self.Counter_4.buy_max()
            if self.Counter_4.first and self.CB.amount>=1:
                coords_5 = self.main_canvas.coords(self.Counter_5.box_buy)
                if event.x > coords_5[0] and event.y > coords_5[1] and event.x < coords_5[2] and event.y < coords_5[3]:
                    self.Counter_5.buy()
                coords_5_max = self.main_canvas.coords(self.Counter_5.box_buy_max)
                if event.x > coords_5_max[0] and event.y > coords_5_max[1] and event.x < coords_5_max[2] and event.y < coords_5_max[3]:
                    self.Counter_5.buy_max()
            if self.Counter_5.first and self.CB.amount>=2:
                coords_6 = self.main_canvas.coords(self.Counter_6.box_buy)
                if event.x > coords_6[0] and event.y > coords_6[1] and event.x < coords_6[2] and event.y < coords_6[3]:
                    self.Counter_6.buy()
                coords_6_max = self.main_canvas.coords(self.Counter_6.box_buy_max)
                if event.x > coords_6_max[0] and event.y > coords_6_max[1] and event.x < coords_6_max[2] and event.y < coords_6_max[3]:
                    self.Counter_6.buy_max()
            if self.Counter_6.first and self.CB.amount>=3:
                coords_7 = self.main_canvas.coords(self.Counter_7.box_buy)
                if event.x > coords_7[0] and event.y > coords_7[1] and event.x < coords_7[2] and event.y < coords_7[3]:
                    self.Counter_7.buy()
                coords_7_max = self.main_canvas.coords(self.Counter_7.box_buy_max)
                if event.x > coords_7_max[0] and event.y > coords_7_max[1] and event.x < coords_7_max[2] and event.y < coords_7_max[3]:
                    self.Counter_7.buy_max()
            if self.Counter_7.first and self.CB.amount>=4:
                coords_8 = self.main_canvas.coords(self.Counter_8.box_buy)
                if event.x > coords_8[0] and event.y > coords_8[1] and event.x < coords_8[2] and event.y < coords_8[3]:
                    self.Counter_8.buy()
                coords_8_max = self.main_canvas.coords(self.Counter_8.box_buy_max)
                if event.x > coords_8_max[0] and event.y > coords_8_max[1] and event.x < coords_8_max[2] and event.y < coords_8_max[3]:
                    self.Counter_8.buy_max()

    def cheat(self,event):
        if self.boost_cheat==False:
            self.boost_cheat=True
        else:
            self.boost_cheat=False
    def ass_to_much(self,event):
        self.Value.get_count(self.Value.value*2)
    def ass_to_much_2(self,event):
        self.Infinity.get_points(1)

    def ass_to_much_2_1(self,event):
        self.Infinity.get_points(self.Infinity.infinity_counter)
    def ass_to_much_3(self,event):
        self.Value.get_count(self.Value.value*1e10)
Game=Game(window,[width,height])
window.bind('<Button-1>',Game.click)
window.bind('<m>',Game.max)
window.bind('<X>',Game.cheat)
window.bind('<o>',Game.ass_to_much)
window.bind('<l>',Game.ass_to_much_2)
window.bind('<Control-l>',Game.ass_to_much_2_1)
window.bind('<Control-o>',Game.ass_to_much_3)
window.after(50,Game.tick)
def close(event):
    Game.Save.save()
    window.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

window.bind('<Escape>', close)
window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()


#"{:.2E}".format(Decimal('408304611030.00000000000000'))