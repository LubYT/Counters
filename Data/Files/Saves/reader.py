
class Save:
    def __init__(self,game):
        self.game=game
        self.counters_data=[]
        self.CB_data=[]
        self.TA_data=[]
        self.TS_data=[]
        self.Auto_data=[]
        self.Doom_data=[]
        self.Infinity_data=[]
        self.Achieve_data=[]
        with (open('Data/Files/Saves/SAVE.txt','r') as file):
            self.total_count=float(file.readline()[:-1:])
            for i in range(8):
                list=[]
                data=file.readline()
                while data.find(',')!=-1:
                    index=data.find(',')
                    list.append(data[:index:])
                    data=data[index+1::]
                else:
                    list.append(data[:-1:])
                self.counters_data.append(list)
            data=file.readline()
            list = []
            while data.find(',')!=-1:
                if data.find('[')==0:
                    list_2=[]
                    data=data[1:-2:]
                    print(data)
                    while data.find(',')!=-1:
                        index=data.find(',')
                        list_2.append(int(data[:index:]))
                        data=data[index+1::]
                        print(data)
                    list.append(list_2)
                else:
                    index=data.find(',')
                    list.append(data[:index:])
                    data=data[index+1::]
            self.CB_data.append(list)
            data=file.readline()
            list=[]
            while data.find(',') != -1:
                index = data.find(',')
                list.append(data[:index:])
                data = data[index + 1::]
            else:
                list.append(data[:-1:])
            self.TA_data.append(list)
            data = file.readline()
            list = []
            while data.find(',') != -1:
                index = data.find(',')
                list.append(data[:index:])
                data = data[index + 1::]
            else:
                list.append(data[:-1:])
            self.TS_data.append(list)

            data=file.readline()
            list=[]
            for i in range(6):
                if i<3:
                    index=data.find(',')
                    list.append(data[:index:])
                    data=data[index+1::]
                elif i==3:
                    list_2=[]
                    while data.find(',')!=-1 and data.find(']')!=0:
                        if data.find('[')==0:
                            data=data[1::]
                        index=data.find(',')
                        list_2.append(data[:index:])
                        data=data[index+1::]
                    list.append(list_2)
                    data=data[2::]
                elif i == 4:
                    index = data.find(',')
                    list.append(data[:index:])
                    data = data[index + 1::]
                elif i == 5:
                    list.append(data[:-1:])
                self.Infinity_data.append(list)

            data = file.readline()
            data=data[:-1:]
            list = []
            for i in range(3):
                data=data[1::]
                list_2=[]
                while data.find(']')!=0:
                    index=data.find(',')
                    if i==1:
                        list_2.append(data[:index:])
                    else:
                        list_2.append(data[:index:])
                    data = data[index + 1::]
                list.append(list_2)
                data=data[2::]
            index = data.find(',')
            list.append(data[:index:])
            data=data[index+1::]
            list.append(data)
            self.Auto_data.append(list)


            data=file.readline()
            data = data[:-1:]
            list=[]
            index=data.find(',')
            list.append(data[:index:])
            data=data[index+1::]
            index = data.find(',')
            list.append(data[:index:])
            data = data[index + 1::]
            for i in range(4):
                data = data[1::]
                list_2 = []
                while data.find(']') != 0:
                    index = data.find(',')
                    if i==0 or i==1 or i==2:
                        list_2.append(float(data[:index:]))
                    else:
                        list_2.append(int(data[:index:]))
                    data = data[index + 1::]
                list.append(list_2)
                data = data[2::]
            list.append(data)
            self.Doom_data.append(list)
            print(self.Doom_data)

            data = file.readline()
            data = data[1:-2:]
            list=[]
            while data.find(',') != -1:
                index = data.find(',')
                list.append(data[:index:])
                data = data[index + 1::]
            self.Achieve_data=list

            data=file.readline()
            data = data[:-1:]
            self.Aspect_data =data

            data = file.readline()
            data = data[1:-1:]
            list=[]
            list_2=[]
            i=0
            while data.find(']') != 0:
                i+=1
                print(data)
                index = data.find(',')
                if i<4:
                    list.append(int(data[:index:]))
                else:
                    list.append(float(data[:index:]))
                data = data[index + 1::]
            list_2.append(list)
            data = data[3::]
            list = []
            i = 0
            while data.find(']') != 0:
                i += 1
                print(data)
                index = data.find(',')
                if i < 4:
                    list.append(int(data[:index:]))
                else:
                    list.append(float(data[:index:]))
                data = data[index + 1::]
            list_2.append(list)
            data = data[3::]
            list = []
            i = 0
            while data.find(']') != 0:
                i += 1
                print(data)
                index = data.find(',')
                if i < 4:
                    list.append(int(data[:index:]))
                else:
                    list.append(float(data[:index:]))
                data = data[index + 1::]
            list_2.append(list)
            self.Stats_data = list_2





            print(self.CB_data)
            print(self.counters_data)





    def save(self):
        with open('Data/Files/Saves/SAVE.txt','w') as file:
            full_save_data=''
            full_save_data+=str(self.game.Value.value)+'\n'
            full_save_data+=self.game.Counter_1.get_save()
            full_save_data += self.game.Counter_2.get_save()
            full_save_data+=self.game.Counter_3.get_save()
            full_save_data += self.game.Counter_4.get_save()
            full_save_data+=self.game.Counter_5.get_save()
            full_save_data += self.game.Counter_6.get_save()
            full_save_data+=self.game.Counter_7.get_save()
            full_save_data += self.game.Counter_8.get_save()
            full_save_data+=self.game.CB.get_save()
            full_save_data+=self.game.TA.get_save()
            full_save_data+=self.game.Tickspeed.get_save()
            full_save_data+=self.game.Infinity.get_save()
            full_save_data+=self.game.Automatick.get_save()
            full_save_data+=self.game.Doom.get_save()
            full_save_data += self.game.Achievements.get_save()
            full_save_data+=self.game.Aspects.get_save()
            full_save_data += self.game.Stats.get_save()
            file.write(full_save_data)
