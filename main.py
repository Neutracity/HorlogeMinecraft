from tkinter import *
from time import *
root = Tk()
root.title("Horloge Minecraft")
size=(596,596)
root.geometry(f'{size[0]}x{size[1]}')
cnv=Canvas(root, width=size[0], height=size[1], bg="ivory")
cnv.pack()
lamp_on = PhotoImage(file="redstone_lamp_on.png")
lamp_off = PhotoImage(file="redstone_lamp.png")

class Horloge:
    def __init__(self, heure=00, minutes=00, secondes=00, alarme_heure=00,alarme=False,):
        self.heure=heure
        self.minutes=minutes
        self.secondes=secondes
        self.init_alarme()
    
    def init_alarme(self,alarme_heure=00,alarme_minutes=00,alarme_secondes=00,alarme_activee='activee'):
        self.alarme_heure=alarme_heure
        self.alarme_minutes=alarme_minutes
        self.alarme_secondes=alarme_secondes
        self.alarme = False

    def inc_heure_alarme(self):
        self.alarme_heure+=1
        

    def inc_minute_alarme(self):
        self.alarme_minutes+=1

    def dec_heure_alarme(self):
        self.alarme_heure-=1

    def dec_minute_alarme(self):
        self.alarme_minutes-=1

    def tic(self):
        if self.secondes < 59:
            self.secondes+=1

        elif self.minutes < 59:
            self.minutes+=1
            self.secondes=0

        elif self.heure < 23:
            self.heure+=1
            self.minutes=0
            self.secondes=0
        else:
            self.secondes=0
            self.heure=0
            self.minutes=0

    def activer_alarme(self):
        self.is_alarme_on = True

    def desactiver_alarme(self):
        self.is_alarme_on = False

    def print_time(self):
        return f'{self.heure}:{self.minutes}:{self.secondes}'

    def verifier_alarme(self):
        if self.heure == self.alarme_heure and self.minutes == self.alarme_minutes :
            print("ALARME")

    def __str__(self):
        """Renvoie le temps sous forme string avec des 0 pour les chiffres : 'hhmmss'"""
        stri = ''
        if self.heure < 10:
            stri += f'0{self.heure}'
        else:
            stri += str(self.heure)
        if self.minutes < 10:
            stri += f'0{self.minutes}'
        else:
            stri += str(self.minutes)
        if self.secondes < 10:
            stri += f'0{self.secondes}'
        else:
            stri += str(self.secondes)
        return stri


class Lampe:
    def __init__(self,on=False,coord = (10,10)):
        #faut trouver un nom unique pour l'objet image
        self.coord = coord
        self.on = on
        self.img=cnv.create_image(self.coord, image=lamp_off)
        #self.actu()
    def actu(self):
        #actualise l'image
        if self.on :
            cnv.itemconfig(self.img,image=lamp_on)
        else:
            cnv.itemconfig(self.img,image=lamp_off)
    def up(self):
        cnv.itemconfig(self.img,image=lamp_on)
    def down(self):
        cnv.itemconfig(self.img,image=lamp_off)


class Gridobject:
    def __init__(self,object = Lampe):
        self.grid = [[object(False,(i*16+10,j*16+10)) for i in range(size[0]//16)] for j in range((size[1]//16))]
    
    def light_up(self,coord=(0,0)):
        self.grid[coord[0]][coord[1]].up()

    def light_down(self,coord=(0,0)):
        self.grid[coord[0]][coord[1]].down()

    def to_hour(self,temps="000000"):
        convert = {'0':p0,'1':p1,'2':p2,'3':p3,'4':p4,'5':p5,'6':p6,'7':p7,'8':p8,'9':p9,':':pp}
        self.hauteur = 5

        convert[temps[0]].apply_pattern((self.hauteur,4))
        convert[temps[1]].apply_pattern((self.hauteur,8))
        convert[temps[2]].apply_pattern((self.hauteur,14))
        convert[temps[3]].apply_pattern((self.hauteur,18))
        convert[temps[4]].apply_pattern((self.hauteur,24))
        convert[temps[5]].apply_pattern((self.hauteur,28))
        pp.apply_pattern((self.hauteur,12))
        pp.apply_pattern((self.hauteur,22))
    


class Pattern:
    def __init__(self,pat=[]):
        self.pat = pat

    def apply_pattern(self,coordstart=(0,0)):
        for i in range(len(self.pat)):
            for j in range(len(self.pat[0])):
                if bool(self.pat[i][j]):
                    ecran.light_up((i+coordstart[0],j+coordstart[1]))
                else:
                    ecran.light_down((i+coordstart[0],j+coordstart[1]))

ecran = Gridobject(Lampe)
letemps= Horloge()

pp = Pattern([
    [0,0,0],
    [0,1,0],
    [0,0,0],
    [0,1,0],
    [0,0,0],
])
pr = Pattern([
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
])
p0 = Pattern([
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
])
p1 = Pattern([
    [0,0,0,1,0],
    [0,0,1,1,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
])
p2 = Pattern([
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,1,0],
])
p3 = Pattern([
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
])
p4 = Pattern([
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
])
p5 = Pattern([
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
])
p6 = Pattern([
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
])
p7 = Pattern([
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
])
p8 = Pattern([
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
])
p9 = Pattern([
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
])

for y in range(2,13):
    for x in range(2,len(ecran.grid[0])-2):
        if not 2<x<len(ecran.grid[0])-3 or not 2<y<12:
            ecran.light_up((y,x))

for i in range(8343):
    letemps.tic()
print(letemps.print_time())
ecran.to_hour(str(letemps))
print(str(letemps))
boutton1 = Button(root,text="Quitter",command=root.destroy)
boutton1.place(x=size[0]-100, y=500)
boutton_alarm = Button(root,text="Alarme On",command=letemps.activer_alarme())
boutton_alarm.place(x=50, y=500)
boutton_alarm_h_plus = Button(root,text="Alarme Heure +",command=letemps.inc_heure_alarme())
boutton_alarm_h_plus.place(x=125, y=500)
boutton_alarm_m_plus = Button(root,text="Alarme Min +",command=letemps.inc_minute_alarme())
boutton_alarm_m_plus.place(x=200, y=500)
boutton_alarm_h_moins = Button(root,text="Alarme Heure -",command=letemps.dec_heure_alarme())
boutton_alarm_h_moins.place(x=275, y=500)
boutton_alarm_m_moins = Button(root,text="Alarme Min -",command=letemps.dec_minute_alarme())
boutton_alarm_m_moins.place(x=350, y=500)

def frame():
    letemps.tic()
    letemps.verifier_alarme()
    ecran.to_hour(str(letemps))
    if letemps.secondes%2 ==0:
        pr.apply_pattern((5,22))
        pr.apply_pattern((5,12))
    root.after(1000,frame)
frame()

mainloop()