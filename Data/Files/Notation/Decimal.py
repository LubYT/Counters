import math
import time
from tkinter import *


class Decimal_counters:
    def __init__(self,total,e,game='n',value='counters'):
        self.num=total
        self.e=e
        self.value_type=value
        self.game=game
        self.inf_lock=False

    def get_save(self):
        return str(self.num)+'e'+str(self.e)

    def get(self,roundn=2,eobj=4):
        if self.value_type=='counters':
            if (self.e>=309 or (self.e==308 and self.num>=1.8)) and ((self.game.Eternity.upgrades[2]=='N')):
                return 'Infinity'
            else:
                if self.e<eobj:
                    if type(roundn)==str:
                        return str(int(self.num * 10 ** self.e))
                    return str(round(self.num*10**self.e,roundn))
                else:
                    if type(roundn) == str:
                        return str(round(self.num,int(roundn)))+'e'+str(self.e)
                    else:
                        if self.num<1/10**roundn:
                            return str(0)+'e'+str(self.e)
                        str_t=str(round(self.num,roundn))
                        index=str_t.find('.')
                        if len(str_t[index+1::])!=roundn and index!=-1:
                            dif=roundn-len(str_t[index+1::])
                            str_t+='0'*dif
                        return str_t+'e'+str(int(self.e))
        elif self.value_type=='IC':
            if (self.e>=309 or (self.e==308 and self.num>=1.8)) and ((self.game.Eternity.upgrades[3]=='N')):
                return 'Infinity'
            else:
                if self.e<eobj:
                    if type(roundn)==str:
                        return str(int(self.num * 10 ** self.e))
                    return str(round(self.num*10**self.e,roundn))
                else:
                    if type(roundn) == str:
                        return str(round(self.num,int(roundn)))+'e'+str(self.e)
                    else:
                        if self.num<1/10**roundn:
                            return str(0)+'e'+str(self.e)
                        str_t = str(round(self.num, roundn))
                        index = str_t.find('.')
                        if len(str_t[index + 1::]) != roundn and index!=-1:
                            dif = roundn - len(str_t[index + 1::])
                            str_t += '0' * dif
                        return str_t + 'e' + str(int(self.e))
        else:
            if self.e < eobj:
                if type(roundn) == str:
                    return str(int(self.num * 10 ** self.e))
                return str(round(self.num * 10 ** self.e, roundn))
            else:
                if type(roundn) == str:
                    return str(round(self.num, int(roundn))) + 'e' + str(self.e)
                else:
                    if self.num < 1 / 10 ** roundn:
                        return str(0) + 'e' + str(self.e)
                    str_t = str(round(self.num, roundn))
                    index = str_t.find('.')
                    if len(str_t[index + 1::]) != roundn and index!=-1:
                        dif = roundn - len(str_t[index + 1::])
                        str_t += '0' * dif
                    return str_t + 'e' + str(int(self.e))

    def maker_from_float(self,other):
        log=int(math.log10(other))
        self.e=log
        self.num=other/10**log

    def log(self,base=10):
        if base==10:
            if self.num>0:
                return self.e+math.log10(self.num)
            else:
                return self.e

    def __int__(self):
        if self.e==0:
            add=1
        else:
            add=0
        return int((self.num)+(10**self.e)-add)

    def alt(self,type):
        if type=='e':
            return -self.e
        if type == 'num':
            return -self.num

    def __round__(self, n=None):
        self.num=round(self.num,n)


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
                log=int(log)
                self.num=self.num/10**log
                self.e+=log
            if self.num < 1 and not self.num == 0:
                log = math.log10(self.num)
                log = int(round(log, 0) - 1)
                self.num = self.num / 10 ** log
                self.e += log

        else:
            if other!=0:
                e=int(math.log10(other))
                e_dif=int(self.e)-e
                if e_dif < 100:
                    if e_dif>=1:
                        self.num+=other/10**int(math.log10(other))/10**e_dif
                    elif e_dif==0:
                        self.num += other/10**int(math.log10(other))
                    else:
                        self.e=e
                        if e_dif>-100:
                            self.num = other* 10 ** e_dif + self.num* 10 ** e_dif
                    if self.num>=10:
                        log=math.log10(self.num)
                        log=int(round(log,0))
                        self.num=self.num/10**log
                        self.e+=log
                    if self.num < 1 and not self.num == 0:
                        log = math.log10(self.num)
                        log = int(round(log, 0) - 1)
                        self.num = self.num / 10 ** log
                        self.e += log
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
            if other != 0:
                e = int(math.log10(other))
                e_dif = self.e - e
                if e_dif < 100:
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
            if self.num < 1 and not self.num == 0:
                log = math.log10(self.num)
                log = int(round(log, 0) - 1)
                self.num = self.num / 10 ** log
                self.e += log
            elif self.num==0:
                self.e=0
        else:
            if other != 0:
                e = int(math.log10(other))
                self.e = self.e + e
                self.num *= other/ 10 ** int(math.log10(other))
                if self.num>=10:
                    log=math.log10(self.num)
                    log=int(round(log,0))
                    self.num=self.num/10**log
                    self.e+=log
                if self.num < 1 and not self.num == 0:
                    log = math.log10(self.num)
                    log = int(round(log, 0) - 1)
                    self.num = self.num / 10 ** log
                    self.e += log
            else:
                self.e=0
                self.num=0
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
            if self.num >= 10:
                log = math.log10(self.num)
                log = int(round(log, 0))
                self.num = self.num / 10 ** log
                self.e += log
        else:
            if other != 0:
                e = int(math.log10(other))
                self.e = self.e - e
                self.num /= other/ 10 ** int(math.log10(other))
                if self.num < 1 and not self.num == 0:
                    log = math.log10(self.num)
                    log = int(math.floor(log))
                    if self.e != 0:
                        self.num = self.num / 10 ** log
                        self.e += log
                if self.num>=10:
                    log=math.log10(self.num)
                    log=int(round(log,0))
                    self.num=self.num/10**log
                    self.e+=log
        return self

    def __pow__(self, power, modulo=None):
        self.e*=power
        self.num=self.num**power
        if self.num>1.8e308:
            self.num=1.8
            self.e+=308
        if type(self.e)!=int:
            inte=int(self.e)
            dif=self.e-inte
            res=10**dif
            self.e=int(self.e)
            self.num=self.num*res
        if self.num >= 10:
            log = math.log10(self.num)
            log = int(log)
            self.num = self.num / 10 ** log
            self.e += log
        if self.num < 1 and not self.num == 0:
            log = math.log10(self.num)
            log = int(math.floor(log))
            if self.e != 0:
                self.num = self.num / 10 ** log
                self.e += log
        return self

    def __lt__(self, other):
        if type(other) == type(self):
            if other.e>self.e:
                return True
            elif other.e==self.e and other.num>self.num:
                return True
            else:
                return False
        else:
            if other==1.8e308:
                if self.e>308:
                    return False
                elif self.e==308 and self.num>= 1.79:
                    return False
                else:
                    return True

            else:
                if other!=0:
                    e = int(math.log10(other))
                    if e>self.e:
                        return True
                    elif e == self.e and other/ 10 ** int(math.log10(other)) > self.num:
                        return True
                    else: return False
                if self.e > 0 or self.num > 0:
                    return False
                else:
                    return True

    def __le__(self, other):
        if type(other) == type(self):
            if other.e>self.e:
                return True
            elif other.e==self.e and other.num>=self.num:
                return True
            else:
                return False
        else:
            if other==1.8e308:
                if self.e>308:
                    return False
                elif self.e==308 and self.num>1.79:
                    return False
                else:
                    return True

            else:
                if other!=0:
                    e = int(math.log10(other))
                    if e>self.e:
                        return True
                    elif e == self.e and other/ 10 ** int(math.log10(other)) >= self.num:
                        return True
                    else: return False
                else:
                    if self.e > 0 or self.num >= 0:
                        return False
                    else:
                        return True

    def __eq__(self, other):
        if type(other) == type(self):
            if other.e==self.e and round(self.num,1) == round(other.num,1):
                return True
            else:
                return False
        elif type(other) == type(int):
            if other == 1.8e308:
                if self.e > 308:
                    return True
                elif self.e == 308 and self.num > 1.79:
                    return True
                else:
                    return False
            else:
                if other!=0:
                    e = int(math.log10(other))
                    if e==self.e  and round(other / 10 ** int(math.log10(other)),1) == round(self.num,1):
                        return True
                    return False
                else:
                    if self.e == 0 and self.num == 0:
                        return True
                    else: return False
        else:
            return False

    def __ne__(self, other):
        if type(other) == type(self):
            if other.e!=self.e or (other.e==self.e and round(self.num,1) != round(other.num,1)):
                return True
            else:
                return False
        elif type(other)==type(int):
            if other == 1.8e308:
                if self.e > 308:
                    return False
                elif self.e == 308 and self.num > 1.79:
                    return False
                else:
                    return True
            else:
                if other!=0:
                    e = int(math.log10(other))
                    if e!=self.e or (e==self.e  and round(other / 10 ** int(math.log10(other)),1) != round(self.num,1)):
                        return True
                    return False
                else:
                    if self.e==0 and self.num==0:
                        return False
                    else: return True
        else:
            return True

    def __gt__(self, other):
        if type(other) == type(self):
            if other.e<self.e:
                return True
            elif other.e==self.e and other.num<self.num:
                return True
            else:
                return False
        else:
            if other==1.8e308:
                if self.e<308:
                    return False
                elif self.e==308 and self.num<= 1.79:
                    return False
                else:
                    return True

            else:
                if other!=0:
                    e = int(math.log10(other))
                    if e<self.e:
                        return True
                    elif e == self.e and other/ 10 ** int(math.log10(other)) < self.num:
                        return True
                    else: return False
                else:
                    if self.e>0 or self.num>0:
                        return True
                    else: return False


    def __ge__(self, other):
        if type(other) == type(self):
            if other.e<self.e:
                return True
            elif other.e==self.e and other.num<=self.num:
                return True
            else:
                return False
        else:
            if other==1.8e308:
                if self.e<308:
                    return False
                elif self.e==308 and self.num<1.79:
                    return False
                else:
                    return True

            else:
                if other!=0:
                    e = int(math.log10(other))
                    if e<self.e:
                        return True
                    elif e == self.e and other/ 10 ** int(math.log10(other)) <= self.num:
                        return True
                    else: return False
                else:
                    if self.e>0 or self.num>=0:
                        return True
                    else: return False

# num1=Decimal_counters(7,5,game='n')
# num2=100000
# num1/=num2
# num3=Decimal_counters(4.5,9)
# num4=Decimal_counters(2.3,9)
# num5=Decimal_counters(7,16)
# num6=Decimal_counters(5,14)
# num1=(num1**5*(num3+num4)-num5)/num6
# print(num1.get(3))