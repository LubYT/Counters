import math
import time
from tkinter import *


class Decimal_counters:
    def __init__(self,total,e):
        self.num=total
        self.e=e
        self.inf_lock=False

    def get(self,roundn):
        if (self.e>=309 or (self.e==308 and self.num>=1.8)) and self.inf_lock==True:
            return 'inf'
        else:
            if self.num<1/10**roundn:
                return str(0)+'e+'+str(self.e)
            return str(round(self.num,roundn))+'e+'+str(self.e)

    def __add__(self, other):
        if type(other)==type(self):
            if other.e>self.e:
                e_dif=other.e-self.e
                self.e=other.e
                if e_dif<100:
                    self.num=other.num+self.num/10**(e_dif)
            elif other.e<self.e:
                e_dif = self.e - other.e
                self.e = self.e
                if e_dif < 100:
                    self.num = other.num/ 10 ** (e_dif) + self.num
            else:
                self.num = other.num + self.num
            if self.num>=10:
                log=math.log10(self.num)
                log=int(round(log,0))
                self.num=self.num/10**log
                self.e+=log
        else:
            e=int(math.log10(other))
            print(e)
            e_dif=self.e-e
            if e_dif>=1:
                self.num+=other/10**int(math.log10(other))/10**e_dif
            elif e_dif==0:
                self.num += other/10**int(math.log10(other))
            else:
                self.e=e
                if e_dif>-100:
                    self.num += other * 10 ** e_dif
            if self.num>=10:
                log=math.log10(self.num)
                log=int(round(log,0))
                self.num=self.num/10**log
                self.e+=log
        return self

    def __sub__(self, other):
        if type(other) == type(self):
            if other.e > self.e:
                self.e = 0
                self.num = 0
            elif other.e < self.e:
                e_dif = self.e - other.e
                self.e = self.e
                if e_dif < 100:
                    self.num = self.num - other.num / 10 ** (e_dif)
            else:
                self.num = self.num - other.num
                if self.num<=0:
                    self.e=0
            if self.num < 1 and not self.num==0:
                log = math.log10(self.num)
                log = int(round(log, 0)-1)
                self.num = self.num / 10 ** log
                self.e += log
        else:
            e = int(math.log10(other))
            e_dif = self.e - e
            print(e_dif)
            if e_dif >= 1:
                self.num -= other/ 10 ** int(math.log10(other)) / 10 ** (e_dif)
            elif e_dif == 0:
                self.num -= other / 10 ** int(math.log10(other))
                if self.num<=0:
                    self.num=0
                    self.e=0
            else:
                self.e = 0
                self.num = 0
            if self.num < 1 and not self.num == 0:
                log = math.log10(self.num)
                log = int(round(log, 0) - 1)
                self.num = self.num / 10 ** log
                self.e += log
        return self

    def __mul__(self, other):
        if type(other) == type(self):
            self.e=self.e+other.e
            self.num*=other.num
            if self.num>=10:
                log=math.log10(self.num)
                log=int(round(log,0))
                self.num=self.num/10**log
                self.e+=log
        else:
            e = int(math.log10(other))
            self.e = self.e + e
            self.num *= other/ 10 ** int(math.log10(other))
            if self.num>=10:
                log=math.log10(self.num)
                log=int(round(log,0))
                self.num=self.num/10**log
                self.e+=log
        return self

    def __truediv__(self,other):
        if type(other) == type(self):
            self.e = self.e - other.e
            if self.e>-100 and self.e<=0:
                self.num /= other.num/10**self.e
            elif self.e>0:
                self.num/= other.num
            if self.e<0:
                self.e=0
            if self.num < 1 and not self.num == 0:
                log = math.log10(self.num)
                log = int(math.floor(log))
                if self.e!=0:
                    self.num = self.num / 10 ** log
                    self.e += log
        return self

    def __pow__(self, power, modulo=None):
        self.e*=power
        self.num=self.num**power
        if self.num >= 10:
            log = math.log10(self.num)
            log = int(log)
            self.num = self.num / 10 ** log
            self.e += log
        return self



# num1=Decimal_counters(2.55,1)
# num2=5
# num3=Decimal_counters(4.5,9)
# num4=Decimal_counters(2.3,9)
# num5=Decimal_counters(7,16)
# num6=Decimal_counters(5,14)
# num1=(num1**5*(num3+num4)-num5)/num6
# print(num1.get(3))

# window=Tk()
#
# num1=Decimal_counters(1,0)
# num2=Decimal_counters(1,0)
# num3=Decimal_counters(1,0)
# num4=Decimal_counters(1,0)
# num5=Decimal_counters(1,0)
# num6=Decimal_counters(1,0)
# num7=Decimal_counters(1,0)
# def get():
#     global num1,num2,num3,num4,num5,num6,num7
#     num1+=num2
#     num2 += num3
#     num3 += num4
#     num4 += num5
#     num5 += num6
#     num6 += num7
#     print(num1.get(15))
#     window.after(0,get)
#
# get()
# window.mainloop()

#print(2.48e-324)
#print(1.79e308)
