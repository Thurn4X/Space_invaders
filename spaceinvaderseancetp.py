#Le jeu space invaders, créé par william, hugo et yannis


#imports
from tkinter import *
import threading
import time
import random
import pygame
import importlib


#VARIABLES
posvx = 550       #valeur position initiale en x vaisseau
posvy = 650       #valeur position initiale en y vaisseau
posax = random.randint(1,1200)        #valeur position initiale en x alien
posay = 100       #valeur position initiale en y alien
ListeTirs = []        #creation d'une liste qui comportera les tirs du vaisseau
ListeAlien = ["images/booba.png","images/JUL.png","images/GIMS.png","images/eminem.png"]      #creation d'une liste qui comportera les apparences des aliens en fonction du niveau
ListeTirsBooba = []       #creation d'une liste qui comportera les tirs des aliens
Listeennemis = []     #creation d'une liste qui comportera les aliens
Listeprotections = []     #creation d'une liste qui comportera les protections
Listeprotx = []       #creation d'une liste qui comportera les composantes en x des protections
vies = 3      #nombre de vies du vaisseau
nbprot = random.randint(1,10)     #nombre de protactions disponibles au debut
niveau = 1        #niveau
vitessetir = 2000     #vitesse du tir de l'alien, il change en fonction du niveau
Score = 0     #score



#création des classes

class Spaceship:                                                                        #classe du vaiseau
    def __del__(self):
        print ("deleted")
    def __init__(self):
        self.x = posvx                                                                    #position du vaisseau
        self.y = posvy
        self.apparence  =  Canevas.create_image(self.x,self.y,anchor = 'nw',image = ImageVaisseau)        #apparence du vaisseau
    def affichage(self):
        Canevas.coords(self.apparence,self.x,self.y)                                    #afficher apparence du vaisseau en fonction des coordonnées 

    def deplacement(self,dir):                                                          #déplacement du vaisseau
        global posvx
        if dir == 1:                                                                      #deplacement a droite
            if self.x<1245:                                                             #condition extreme à droite, sinon on est teleporté de l'autre coté
                self.x+= 10
                posvx = self.x
            else:
                self.x = 0
        elif dir == -1:                                                                   #deplacement du vaisseau a gauche
            if self.x>0:                                                                #condition extreme à gauche, sinon on est teleporté de l'autre coté
                self.x+= -10
                posvx = self.x
            else:
                self.x = 1245
        else:
            pass
        self.affichage()                                                                #appel de la fonction pour afficher le vaisseau





class Alien:                                                                            # Classe de l'alien
    def __del__(self):
        print ("deleted")    
    posay = 100
    def __init__(self,posax,niveau):
        self.boobay = Alien.posay                                                         #position de l'alien lors de sa creation
        self.boobax = posax
        self.boobadx = random.randint(-10,10)                                             #l'alien se deplace un peu a gauche, un peu a droite, cette variable sert a ça
        self.image = PhotoImage(file = ListeAlien[niveau-1])                                #l'image de l'alien dépend du niveau
        self.apparence  =  Canevas.create_image(self.boobax,self.boobay,image = self.image)     #apparence de l'alien

    def affichage(self):
        Canevas.coords(self.apparence,self.boobax,self.boobay)                          #afficher l'apparence de l'alien







class protection:                                                                       #classe pour les protections
    global Listeprotections
    def __del__(self):
        print ("deleted")
    def __init__(self,lavariablex):                                                     #place une protection avec pour coordonnée en x lavariablex
        self.x = lavariablex
        self.y = 600
        self.apparence = Canevas.create_rectangle(self.x,self.y,self.x+50,self.y+20,fill = 'blue')      #apparence de la protection


            
    def checkcollision(self):                                                           #voir si l'alien rentre en collision avec une protection
        global ListeTirsBooba
        for Prot in Listeprotections:
            for booba in Listeennemis:
                if booba.boobax<= Prot.x+50 and booba.boobax+50>Prot.x-50:              #ces deux lignes sont des calculs en fonction des
                    if booba.boobay+50>Prot.y-20 and booba.boobay<Prot.y+20:           #largeurs de l'alien et de protections
                        Canevas.delete(Prot.apparence)
                        gagagou = Listeprotections.index(Prot)
                        del Listeprotections[gagagou]
                        Canevas.delete(booba.apparence)
                        del Listeennemis[0]
                        booba.boobay = 650
                        restartbooba()                                                  #on a supprimé l'alien donc on le restart
                

            


class TirSpaceship:                                                                     #classe pour les tirs du vaisseau
    def __del__(self):
        print ("deleted")
    def __init__(self):
        self.tirx = posvx                                                                 #placer le tir
        self.tiry = posvy
        self.apparence = Canevas.create_image(self.tirx+15, self.tiry, image = ImageTir)    #apparence du tir
        self.tirage = 1                                                                   #tir en cours
        print("letirvamonter")
        self.tirmonte()                                                                 #appel de la fonction pour que le tir monte

    
    def affichage(self):
        Canevas.coords(self.apparence , self.tirx+15 , self.tiry)                       #affichage de l'apparence du tir


    def tirmonte(self):                                                                 #fonction qui fait que le tir monte
        if self.tirage == 1:
            self.tiry-= 10
            self.affichage()                                                            #refresh l'apparence
            self.fintir()                                                               #appel de la fonction qui vérifie que le tir est terminé
            Mafenetre.after(5,self.tirmonte)                                            #on continue jusqu'à ce que le tir soit supprimé

    def fintir(self):                                                                   #fonction qui vérifie que le tir est terminé
        global ListeTirs,Score,Listeennemis,niveau,vitessetir
        if self.tiry<0:                                                                 #si le tir dépasse le haut de la fenetre, il est supprimé
            if ListeTirs!= []:
                self.tirage == 0                                                          # tir plus en cours
                Canevas.delete(self.apparence)
                del ListeTirs[0]                                                        #suppression de l'objet


        for booba in Listeennemis:                                                      #si le tir touche l'alien, il doit aussi etre supprimé

            if self.tirx<= booba.boobax+50 and self.tirx+15>booba.boobax-50:             #les conditions avec les dimensions de l'alien et du tir
                if self.tiry+15>booba.boobay-50 and self.tiry<booba.boobay+50:          #pour qu'il soit considéré comme réussi

                    Score+= 10                                                           #quand on touche l'ennemi, le score augmente
                    affichageautre(vies,Score)                                          #j'appelle la fonction qui affiche le score et les vies en parallèle du jeu

                    if Score  == 100:                                                     #là on gère les niveaux en fonction du score
                        print("next level")
                        niveau+= 1
                        vitessetir = int(vitessetir/2)                                    #la vitesse de tir de l'alien augmente
                        pygame.mixer.music.load("musiques/JOULE.wav")                   #la musique change
                        pygame.mixer.music.play(loops = -1, start = 0.0)
                        del ListeTirsBooba[0]                                           #comme l'alien change, je supprime le dernier tir de l'alien


                    if Score  == 200:
                        print("next level")
                        niveau+= 1
                        vitessetir = int(vitessetir/1.5)
                        pygame.mixer.music.load("musiques/BELLA.wav")                   #meme principe
                        pygame.mixer.music.play(loops = -1, start = 0.0)
                        del ListeTirsBooba[0]

                    if Score  == 300:
                        print("next level")
                        niveau+= 1
                        vitessetir = int(vitessetir/1.5)
                        pygame.mixer.music.load("musiques/ME.wav")                      #meme principe
                        pygame.mixer.music.play(loops = -1, start = 0.0)
                        del ListeTirsBooba[0]                    
                                           
                    Canevas.delete(booba.apparence)                                     # s'il n'y a pas changement de niveau, on supprime l'alien
                    del Listeennemis[0]
                    del booba
                    restartbooba()                                                      #et on le restart

                    Canevas.delete(self.apparence)                                      # et on supprime le tir







class TirBooba:                                                                         #classe pour les tirs de l'alien
    def __del__(self):
        print ("deleted")
    def __init__(self,booba):
        self.tirx = booba.boobax                                                          #placer le tir
        self.tiry = booba.boobay
        self.apparence = Canevas.create_image(self.tirx+15, self.tiry, image = ImageTir)    #apparence du tir
        self.tirdescent()                                                               #appel de la fonction qui fait descendre le tir de l'alien

    
    def affichage(self):
        Canevas.coords(self.apparence , self.tirx+15 , self.tiry)                       #on affiche l'apparence


    def tirdescent(self):                                                               #on fait descendre le tir
        self.tiry+= 10
        self.affichage()                                                                #on l'affiche
        self.fintirbooba()                                                              #on check s'il est terminé
        Mafenetre.after(50,self.tirdescent)                                             #jusqu'à ce qu'il soit supprimé

    def fintirbooba(self):                                                              #on regarde si le tir est fini
        global ListeTirsBooba,Score,Listeennemis,vies

        for booba in Listeennemis:                                                      #si le tir atteint le bas de l'écran, il est supprimé
            for tir in ListeTirsBooba:
                if tir.tiry>700:
                    Canevas.delete(tir.apparence)
                    if len(ListeTirsBooba)>1:
                        del ListeTirsBooba[0]



        for booba in Listeennemis:
            for tir in ListeTirsBooba:                                                  #si le tir touche le vaisseau, il est supprimé
                if tir.tirx<= vaisseau.x+15 and tir.tirx+15>vaisseau.x:                  #conditions de collision avec les coordonnées
                    if tir.tiry+15>vaisseau.y and tir.tiry<vaisseau.y+15:
                        del ListeTirsBooba[0]
                        Canevas.delete(tir.apparence)
                        vies-= 1                                                         #dans ce cas on perd une vie
                        affichageautre(vies,Score)                                      #et on refresh l'affichage parallèle au jeu


            for Prot in Listeprotections:                                               #si le tir touche une protection, il est supprimé
                if self.tirx<= Prot.x+50 and self.tirx+15>Prot.x:                        #conditions de collision avec les coordonnées
                    if self.tiry+15>Prot.y and self.tiry<Prot.y+20:
                        gagagou = Listeprotections.index(Prot)                            #on supprime alors le tir ET la protection
                        del Listeprotections[gagagou]
                        Canevas.delete(Prot.apparence)
                        Canevas.delete(self.apparence)
                        if len(ListeTirsBooba)>1:
                             del ListeTirsBooba[0]
        
        


# création des fonctions


def mouvementAlien():                                                                   #mouvement de l'alien

    global Score,Listeennemis,Listeprotections,vies

    if Listeennemis!= []:
        for booba in Listeennemis:              
            booba.boobay += 2                                                            #l'alien descend
            boobadx = random.randint(-10,10)                                              #il se déplace latéralement au hasard (sinon c'est trop simple)
            booba.boobax +=  boobadx
            if vaisseau.x<= booba.boobax+50 and vaisseau.x+15>booba.boobax-50:           #on vérifie si l'alien touche le vaisseau
                if vaisseau.y+15>booba.boobay-50 and vaisseau.y<booba.boobay+50:
                    Canevas.delete(booba.apparence)                                     #si c'est le cas on supprime l'alien
                    del Listeennemis[0]
                    del booba
                    restartbooba()                                                      #puis on le recrée
                    mouvementAlien()                                                    #et on le fait bouger
                    vies-= 1                                                             #on perd aussi une vie
                    affichageautre(vies,Score)                                          #on refresh l'afichage en parallèle du jeu
            
            if booba.boobax+50>= 1280:                                                   #condition limite à droite pour l'alien
                booba.boobax-= 10

            if booba.boobax-50<= 0:                                                      #condition limite à gauche pour l'alien
                booba.boobax+= 10

            if booba.boobay>650:                                                        #si l'alien atteint le bas de l'écran, 
                Canevas.delete(booba.apparence)                                         #on le supprime
                del Listeennemis[0]
                del booba
                restartbooba()                                                          #on le recrée
                mouvementAlien()                                                        #on le fait bouger

        for Prot in Listeprotections:                                                   #on regarde si l'alien touche lui-même une protection
            if booba.boobax<= Prot.x+50 and booba.boobax+50>Prot.x-50:
                if booba.boobay+50>Prot.y-20 and booba.boobay<Prot.y+20:
                    Canevas.delete(Prot.apparence)                                      #dans ce cas on supprime la protection
                    gagagou = Listeprotections.index(Prot)
                    del Listeprotections[gagagou]
                    Canevas.delete(booba.apparence)                                     #et l'alien
                    del Listeennemis[0]
                    del booba
                    restartbooba()                                                      #on le recrée
                    mouvementAlien()                                                    #et on le met en mouvement

        booba.affichage()                                                               #on refresh l'affichage pour chaque alien


        Mafenetre.after(50,mouvementAlien)                                              # on fait bouger les aliens toutes les 50ms
    else:
        return



def restartbooba():                                                                     # recréer l'alien
    posax = random.randint(50,1230)                                                       #position en x aléatoire
    booba = Alien(posax,niveau)   
    Listeennemis.append(booba)                                                          #on crée l'alien et on l'aoute à la liste des ennemis



def tirbooba():                                                                         #quand l'alien tire           
    for booba in Listeennemis:
        tiralien = TirBooba(booba)   
        ListeTirsBooba.append(tiralien)                                                 #on crée le tir et on l'ajoute à la liste de ses tirs

    Mafenetre.after(vitessetir,tirbooba)                                                #on répète en fonction de la vitesse de tir (le niveau)


#detection clavier


def left(event):
    vaisseau.deplacement(-1)

def right(event):
    vaisseau.deplacement(1)

def Tir(event):
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('musiques/TIRsound.wav'))           #le vaisseau fait un bruit quand il tire
    nouveautir = TirSpaceship()
    ListeTirs.append(nouveautir)                                                        #on ajoute le tir créé à la liste des tirs du vaisseau


def affichageautre(vies,score):                                                         #affichage des infos en parallèle du jeu (score, vies, boutton quitter)

    label2.config(text = 'SCORE:    '+str(score))                                         #affichage du score
    boutton.config(text = ' QUITTER ')                                                    #affichage du boutton quitter
    if vies == 3:                                                                         
        pass
    elif vies == 2:
        boutton3.destroy()                                                              # si on perd une vie, on supprime un coeur
    elif vies == 1:
        boutton2.destroy()                                                              # si on perd deux vies, on supprime deux coeurs
    else:
        gameover()                                                                      #si on n'a plus de vie, c'est fini

def gameover():                                                                         #fonction fin de jeu
    f  =  open("points.txt", "w")                                                         #on écrit le score dans un fichier texte
    f.write(str(Score))
    f.close()

    for booba in Listeennemis:                                                          #on supprime tout    
        for tir in ListeTirsBooba:
            del tir
        del booba

    Canevas.destroy()
    Mafenetre.destroy()
    pygame.quit()
    print("done")
    import menu                                                                         
    importlib.reload(menu)                                                              #on ouvre le menu de fin de jeu



#Création d'une fenêtre
Mafenetre = Tk()
Mafenetre.geometry("1280x720")
Framebase = Frame(Mafenetre, relief  = 'groove', bg = 'green',width = 1280,height = 720)
Framebase.pack(fill = BOTH, expand = True)



#importation liste des images
ImageVaisseau = PhotoImage(file = 'images/kaarisvaisseau.png')
ImageBackground = PhotoImage(file = 'images/backgroundstars.png')
ImageAlien = PhotoImage(file = ListeAlien[niveau-1])                                        #l'image de l'alien dépend du niveau
ImageTir = PhotoImage(file = 'images/cd.png')
ImageCoeur = PhotoImage(file = 'images/heart.png')


#formation des canevas
Canevas =  Canvas(Framebase,width = 1280,height = 720)
Canevas.create_image(600,300,image = ImageBackground)
Canevas.pack(fill = BOTH, expand = True)





label2  =  Label(Canevas, text = "SCORE:   0", fg = "red")                                    #Affichage du score en haut a gauche
label2.place(x = 100)



boutton1  =  Button(Canevas, image = ImageCoeur)                                            #Affichage des trois coeurs
boutton1.place(x = 400)

boutton2  =  Button(Canevas, image = ImageCoeur)
boutton2.place(x = 450)

boutton3  =  Button(Canevas, image = ImageCoeur)
boutton3.place(x = 500)


boutton  =  Button(Canevas, text  = " QUITTER ", command  =  quit)                            #Affichage du boutton quitter
boutton.place(x = 1100)

#attribution des touches
Mafenetre.bind("<Left>",left)
Mafenetre.bind("<Right>",right)
Mafenetre.bind("<space>",Tir)






#création des objets
vaisseau = Spaceship()                                                                    #création du vaisseau
booba = Alien(posax,niveau)                                                               #création du prêmier ennemi
Listeennemis.append(booba)



a = 1280-nbprot*50                                                                        #des maths pour bien placer les protection équitablement
b = a/nbprot                                                                              #(les protections font 50 de large)
lavariablex = b/2


for i in range (nbprot):                                                                #on crée la liste de protections avec leur coordonnée en x respective

    Lignedefront = protection(lavariablex)
    Listeprotections.append(Lignedefront)
    lavariablex+= b+50





mouvementAlien()                                                                        #on fait bouger le premier alien
tirbooba()                                                                              #on fait tirer le premier alien


#lancement de la musique
pygame.mixer.init(frequency = 44100, size = -16, channels = 3, buffer = 1012)
pygame.mixer.music.load("musiques/TCHOUINE.wav")
pygame.mixer.music.play(loops = -1, start = 0.0)

Mafenetre.mainloop()