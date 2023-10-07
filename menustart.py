#Ce fichier est le menu de départ du jeu. L'utilisateur peut choisir de jouer ou bien de quitter.

#imports

from tkinter import *
from tkinter import ttk
import pygame            #celui ci n'est pas obligatoire mais si vous ne le voulez pas il faudra enlever tout ce qui concerne pygame(plus de musique)




#Les fonctions suivantes permettent lorsque l'utilisateur passe sa souris dessus, de changer le background du boutton.

def change(keskispasse):
    playimage =  PhotoImage(file = "images/start1.png")
    startbutton.config(image = playimage)
    startbutton.image =  playimage

def change2(keskispasse):
    playimage =  PhotoImage(file = "images/start.png")
    startbutton.config(image = playimage)
    startbutton.image =  playimage

def change3(keskispasse):
    quitimage =  PhotoImage(file = "images/quit1.png")
    quitbutton.config(image = quitimage)
    quitbutton.image =  quitimage

def change4(keskispasse):
    quitimage =  PhotoImage(file = "images/quit.png")
    quitbutton.config(image = quitimage)
    quitbutton.image =  quitimage


#Voici la fonction qui démarre le jeu. En fait j'importe juste le fichier pour le lancer.

def startgame():
    quitbutton.destroy()
    startbutton.destroy()
    randomtrucquisertarien = 100
    window.destroy()
    pygame.mixer.music.stop()
    import spaceinvaderseancetp
    quit()


#Le tkinter lié à la fenêtre du menu

window =  Tk()
window.title("                                                                                                                                                                     MENU")

window.geometry("1080x720")
window.minsize(1080,720)
window.iconbitmap("images/logo.ico")      #une petite icone de fenêtre créée par mes soins






backmenu  =  PhotoImage(file = "images/backmenu.png")   

canvas1  =  Canvas( window,width = 1080,height = 720)
canvas1.place(x  = 0, y  =  0)

canvas1.create_image(0,0,anchor = 'nw',image = backmenu)        #background

title  =  PhotoImage(file = "images/title.png")            
canvas1.create_image(425,50,anchor = 'nw',image = title)        #image titre




quitimage =  PhotoImage(file = "images/quit.png")
quitbutton  = Button(window,image  = quitimage, command = exit, disabledforeground = "#FFFFFF")     #boutton quitter
quitbutton.place(x = 425,y = 500)
quitbutton.bind("<Enter>",change3)      #c'est grâce a ça que j'appele les fonctions qui change le background
quitbutton.bind("<Leave>", change4)

start =  PhotoImage(file = "images/start.png")
startbutton =  Button(window,image  =  start, disabledforeground = "#FFFFFF",command = startgame)   #boutton start
startbutton.place(x = 425,y = 200)
startbutton.bind("<Enter>",change)
startbutton.bind("<Leave>", change2)


pygame.mixer.init(frequency = 44100, size = -16, channels = 3, buffer = 1012)       # La musique 
pygame.mixer.music.load("musiques/slim.wav")
pygame.mixer.music.play(loops = -1, start = 0.0)


window.mainloop()