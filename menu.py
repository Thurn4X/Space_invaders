#Ce fichier est le menu gameover du jeu. L'utilisateur peut choisir de rejouer ou bien de quitter. Son score est affiché.


#imports
from tkinter import *
from tkinter import ttk
import time
import pygame
import importlib



#fonctions qui change le bacground des boutons
def change(keskispasse):
    playimage =  PhotoImage(file = "images/restart1.png")
    restartbutton.config(image = playimage)
    restartbutton.image =  playimage

def change2(keskispasse):
    playimage =  PhotoImage(file = "images/restart.png")
    restartbutton.config(image = playimage)
    restartbutton.image =  playimage

def change3(keskispasse):
    quitimage =  PhotoImage(file = "images/quit1.png")
    quitbutton.config(image = quitimage)
    quitbutton.image =  quitimage

def change4(keskispasse):
    quitimage =  PhotoImage(file = "images/quit.png")
    quitbutton.config(image = quitimage)
    quitbutton.image =  quitimage


#fonction pour relancer le jeu (y'a un petit problème quand on relance le jeu 2 fois)
def startgame():
    quitbutton.destroy()
    restartbutton.destroy()
    window.destroy()
    pygame.mixer.music.stop()
    import spaceinvaderseancetp
    importlib.reload(spaceinvaderseancetp)      #c'est avec cette ligne que je reload le jeu
    quit()




#partie tkinter de la fenêtre

window =  Tk()
window.title("                                                                                                                                                              RESTARTMENU")

window.geometry("1080x720")
window.minsize(1080,720)
window.iconbitmap("images/logo.ico")        #ptite icone






backmenu  =  PhotoImage(file = "images/backmenu.png")


canvas1  =  Canvas( window,width = 1080,height = 720)
canvas1.place(x  = 0, y  =  0)

canvas1.create_image(0,0,anchor = 'nw',image = backmenu)


#partie lecture du score
f  =  open("points.txt", "r")     #j'ouvre le fichier ou sont ecrits les points
score = f.read()                  #je fais pleins de conditions avec un pti commentaire pour chaque score
if int(score) == 0:
    debut = "T'AS FAIT EXPRES"
elif int(score)<= 50:
    debut = "BOF"
elif int(score)<= 150:
    debut = "PAS MAL"
elif int(score)<= 300:
    debut = "BRAVO"
elif int(score)<= 500:
    debut = "INCROYABLE"
else:
    debut = "TU ES UN DIEU !"


label1  =  Label( window,width = 36,text = debut+" ton Score est de: "+score)     #affichage de la partie score
label1.place(x  = 425, y  =  350)

title  =  PhotoImage(file = "images/title.png")     
canvas1.create_image(425,50,anchor = 'nw',image = title)        #affichage du titre de la page




quitimage  =   PhotoImage(file = "images/quit.png")       
quitbutton  = Button(window,image  = quitimage, command = exit, disabledforeground = "#FFFFFF")     #boutton quitter
quitbutton.place(x = 425,y = 500)
quitbutton.bind("<Enter>",change3)      #pour appeler les fonctions en haut
quitbutton.bind("<Leave>", change4)

restart =  PhotoImage(file = "images/restart.png")
restartbutton =  Button(window,image  =  restart, disabledforeground = "#FFFFFF",command = startgame)       #boutton restart
restartbutton.place(x = 425,y = 200)
restartbutton.bind("<Enter>",change)
restartbutton.bind("<Leave>", change2)


pygame.mixer.init(frequency = 44100, size = -16, channels = 3, buffer = 1012)       #la musique ♥
pygame.mixer.music.load("musiques/JOULE.wav")
pygame.mixer.music.play(loops = -1, start = 0.0)


window.mainloop()