#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:47:33 2021

@author: pedroPedro
"""
# Import les modules necessaires pour le code
import pygame
import sys
from math import floor
import time

# pygame.init() initialise tous les modules de pygame
pygame.init()
# initialisation de variables nécessaires au fonctionnement du jeu. peuvent etre modifié
w = 900 # largeur de la fenetre pygame
l = 900 # hauteur de la fenetre pygame
taille = 3 # n pour un jeux avec n par n cases peut etre utilisé pour faire un quadrier plus grand
# import d'images pour le jeu
o_img = pygame.image.load("O.png")
x_img = pygame.image.load("X.png")
# scale des images pour les mettres de la bonne taille
o_img = pygame.transform.scale(o_img, ((int(floor(w/taille))), int(l/taille))) 
x_img = pygame.transform.scale(x_img, ((int(floor(w/taille))), int(l/taille)))

lignes = []# liste qui réunit les coordonnées x,y des lignes nécéssaires pour le quadrillé du jeu
length = []
width = []
for i in range(1,taille):
    length.append(l*i/taille)
for i in range(1,taille):
    width.append(w*i/taille)
for i in range(taille-1):
    lignes.append(((length[i],0),(length[i],l)))
    lignes.append(((0,width[i]),(l,width[i])))

class Grille: 
    def __init__(self, ecran, lignes): #initialisation de la classe grille
        self.ecran = ecran # ecran: fenetre pygame
        self.lignes = lignes
        self.grille = [[None for x in range(0, taille)] for y in range(0, taille)]
   
    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (0,0,0), ligne[0], ligne[1], 2)
           
    def print_grille(self):
        # print dans le terminale la grille (non utilisé)
        print(self.grille)
           
    def spot_value(self, x, y, value):
        if self.grille[x][y] == None:
            self.grille[x][y] = value
        else:
            return False
       
    def centersquare(self, x, y):
        """
        Parameters
        ----------
        x : int
            position x de la zone.
        y : int
            position y de la zone.

        Returns
        -------
        x : int
            position x exacte pour poser l'image.
        y : int
            position y exacte pour poser l'image.

        """
        x = x*(w/taille)
        y = y*(l/taille)
        return x,y
       
   
    def placeXO(self, x, y):
        """
        Parameters
        ----------
        x : int
            position x.
        y : int
            position y.
        permet de placer les symboles sur la fenetre pygame
        """
        if self.grille[x][y] == 'X':
            x, y = Grille.centersquare(self, x, y)
            self.ecran.blit(x_img, (x, y))
        else:
            x, y = Grille.centersquare(self, x, y)
            self.ecran.blit(o_img, (x, y))
        pygame.display.update()


def result(w,l, ecran, status):
    """
    

    Parameters
    ----------
    w ,l : variable globales
        
    ecran : fenetre pygame
    status : str
        savoir qui à gagné.
    affiche les stats du jeu


    """
    game = True
    if status == 'O':
        text = 'Victoire de O'
    elif status == 'X':
        text = 'Victoire de X'
    else:
        text = 'Égalité'
    
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render(text, True, (255, 255, 0))
    while game == True: #lance une boucle non bornée qui se finit seulement si necéssaire ce qui permet d'évité des bugs
        pygame.display.update() #update la fenetre pygame
        textRect = text.get_rect() #necessaire pour la création du text su la fenetre pygame
        textRect.center = (w // 2, (l // 2)) #centre le texte au milieu de la fenetre
        ecran.blit(text, textRect) #pose le texte sur la fenetre
        for event in pygame.event.get(): #si il y a interaction de l'utilisateur avec la fenetre
            if event.type == pygame.QUIT:
                sys.exit() #ferme la fenetre
                
                
class jeu: #claasse principale
    def __init__(self):
        self.ecran = pygame.display.set_mode((w,l))
        pygame.display.set_caption("Tic Tac Toe")
        self.jeu_encours = True
        self.grille = Grille(self.ecran, lignes)
        self.player_X = 'X'
        self.player_O = 'O'
        self.turn = 0
   
    def fonction_principale(self,start, name):
        if start == 'o':
            self.player_O == 'O'
            self.player_X == 'X'
        elif start == 'o':
            self.player_O == 'X'
            self.player_X == 'O'
        stop = False
        self.ecran.fill((240,240,240)) #met le fond de la fenetre en blanc
        pygame.display.set_caption('Morpion')
        victoire = False
        while self.jeu_encours:
            
                
            for event in pygame.event.get():
                if stop == True:
                    pygame.quit()
                    sys.exit()
                   
                if event.type == pygame.QUIT:
                    sys.exit()
               
                if event.type == pygame.QUIT:
                    pygame.quit()
               
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                   
                    position_x , position_y = int(position[0] // (w/taille)), int(position[1] // (l/taille))
                    #print(position_x , position_y)
                   
                    if self.turn % 2 == 0:
                        if not(self.grille.spot_value(position_x, position_y, self.player_O) == False):
                            self.turn += 1
                        self.grille.spot_value(position_x, position_y, self.player_O)
                        self.grille.placeXO(position_x, position_y)
                    else:
                        if not(self.grille.spot_value(position_x, position_y, self.player_X) == False):
                            self.turn += 1
                        self.grille.spot_value(position_x, position_y, self.player_X)
                        self.grille.placeXO(position_x, position_y)
                    pygame.display.flip()
                       
                   
                   
                
               
               # Tests de victoires debuts
                lst_X = [] #liste qui rassemble les differentes position des elements de x
                lst_O = [] #liste qui rassemble les differentes position des elements de o
                lst_ligne_X = [] #liste qui rassemble les differentes position des elements de X d'une meme ligne
                lst_ligne_O = [] #liste qui rassemble les differentes position des elements de O d'une meme ligne
                lst_colonne_X = [] #liste qui rassemble les differentes position des elements de X d'une meme colonne
                lst_colonne_O = [] #liste qui rassemble les differentes position des elements de O d'une meme colonne
                for ligne in range(0, len(self.grille.grille)):
                    for colonne in range(0, len(self.grille.grille)):
       
                        if self.grille.grille[ligne][colonne] == 'X':
                            X_position = (ligne, colonne)
                            lst_X.append(X_position)
       
                        elif self.grille.grille[ligne][colonne] == 'O':
                            O_position = (ligne, colonne)
                            lst_O.append(O_position)
                  
                    # Tests de victoires de X
                if len(lst_X) >= taille:
                    
                    for (ligne, colonne) in lst_X:
                       
                        lst_ligne_X.append(ligne)
                        lst_colonne_X.append(colonne)
       
                    if lst_ligne_X.count(0) ==3 or lst_ligne_X.count(1) ==3 or lst_ligne_X.count(2) ==3:

                        victoire = True
                        status = 'X'
                        #test en ligne
                    if lst_colonne_X.count(0) ==3 or lst_colonne_X.count(1) ==3 or lst_colonne_X.count(2) ==3:

                        victoire = True
                        status = 'X'
                        #test en colone
                    
                    #tests en diagonales
                    if (0, 2) in lst_X:
                        if  (1, 1) in lst_X:
                            if (2, 0) in lst_X:

                                victoire = True
                                status = 'X'
                                
                    if (0, 0) in lst_X:
                        if  (1, 1) in lst_X:
                            if (2, 2) in lst_X:
                                victoire = True
                                status = 'X'
                    
                   # Tests de victoires de O
                if len(lst_O) >= taille:

                    for (ligne, colonne) in lst_O:

                        lst_ligne_O.append(ligne)
                        lst_colonne_O.append(colonne)
       
                    if lst_ligne_O.count(0) ==3 or lst_ligne_O.count(1) ==3 or lst_ligne_O.count(2) ==3:
         
                        victoire = True
                        status = 'O'
                        #test en ligne
                        
                    if lst_colonne_O.count(0) ==3 or lst_colonne_O.count(1) ==3 or lst_colonne_O.count(2) ==3:

                        victoire = True
                        status = 'O'
                        #test en colonne
                        
                        
                    #test en diagonales
                    if (0, 2) in lst_O:
                        if  (1, 1) in lst_O:
                            if (2, 0) in lst_O:
                               
                                victoire = True
                                status = 'O'
                    if (0, 0) in lst_O:
                        if  (1, 1) in lst_O:
                            if (2, 2) in lst_O:
                                
                                victoire = True
                                status = 'O'
                
               
            pygame.init()
            self.grille.afficher()
            pygame.display.flip()
            if victoire == True:
                if status == 'O':
                    text = 'Victoire de '+ name[0]
                elif status == 'X':
                    text = 'Victoire de '+ name[1]
                time.sleep(1) # attend une seconnde pour permettre à l'utilisateur de voir le résultat
                font = pygame.font.Font('freesansbold.ttf', 50)# les lignes suivantes permettent d'ecrire du texte sur la fenetre
                text = font.render(text, True, (0,255,0))
                textRect = text.get_rect()
                textRect.center = (w // 2, (l // 2))
                self.ecran.blit(text, textRect)
                pygame.display.update() #update la fenetre avec le bilt ci dessus
                time.sleep(1)
                self.jeu_encours = False #met fin a la boucle non bornée
            elif self.turn == taille*taille: #met fin au jeu si toutes les cases sont occupés mais pas de victoires
                time.sleep(1)
                self.jeu_encours = False 
                status = 'egalite'
                text = 'Égalité'
                font = pygame.font.Font('freesansbold.ttf', 50)
                text = font.render(text, True, (0,255,0))
                textRect = text.get_rect()
                textRect.center = (w // 2, (l // 2))
                self.ecran.blit(text, textRect)
                pygame.display.update()
                time.sleep(1)
            
        return(status)





def new_game(start, names): #Lance une partie
    if __name__ == "__main__":
        pygame.init()
        status = jeu().fonction_principale(start, names)
        if start == 'x': # permet de joué chacun son tours
            if status == 'X':
                status = 'O'
            elif status == 'O':
                status = 'X'
       
           
        pygame.quit()
    return status   
#new_game()
#activer pour tester juste le morpion


def settings(w,l):
    
    pygame.init()




    screen = pygame.display.set_mode([w, l])


    base_font = pygame.font.Font('freesansbold.ttf', 30)
    user_text = ''


    input_rect = pygame.Rect(w/3, (l/4)*1, 100, 50)
    #permet d'avoir une case input qui prend la couleur noir quand elle est selectionnee
    color_active = pygame.Color((0,0,0))

    
    color_passive = pygame.Color((255,255,0))# Permet que la case input sait jaune quand elle est pas selectionner
    color = color_passive
    
    active = False 
    user_text_test = 0 # pour savoir poser les bonnes questions
    screen.fill((19,19,70)) 
    while True:
        #Permet de faire les contours de la fenetre
        w=w-1
        l=l-1
        pygame.draw.line(screen, (255, 255, 0), (0,0), (w, 0), 5)
        pygame.draw.line(screen, (255, 255, 0), (0,0), (0, l), 5)
        pygame.draw.line(screen, (255, 255, 0), (w,0), (w, l), 5)
        pygame.draw.line(screen, (255, 255, 0), (0,l), (w, l), 5)
        w=w+1
        l=l+1
        font = pygame.font.Font('freesansbold.ttf', 50)
        #pose les questions pour connaitre 
        if user_text_test == 0:
            text = font.render('Name P1: ', True, (255, 255, 0),(19,19,70))
        elif user_text_test == 1:
            text = font.render('Name P2: ', True, (255, 255, 0),(19,19,70))
        elif user_text_test == 2:
            text = font.render('Number of rounds: ', True, (255, 255, 0),(19,19,70))
        textRect = text.get_rect()
        textRect.center = (w // 2, (l // 8)*(75/100))
        screen.blit(text, textRect)
            
            
        for event in pygame.event.get():

	# if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
    
                # Unicode standard is used for string formation
                elif event.key == pygame.K_RETURN:
                    
                    user_text = str(user_text)
                    
                    if user_text_test == 0:
                        
                        if len(user_text) < 1:
                            user_text = 'trop court'
                        else:
                            user_text_test +=1
                            user_textp1 = user_text
                            user_text = ''
                    elif user_text_test == 1:
                        if len(user_text) < 1:
                            user_text = 'trop court'
                        else:
                            user_text_test +=1
                            user_textp2 = user_text
                            user_text = ''
                    elif user_text_test == 2:
                        user_text = int(user_text)
                        if type(user_text) != int:
                            user_text = 'Pas entier'
                        else:
                            user_text_test +=1
                            user_textTurn = int(user_text)
                            user_text = ''
                            pygame.quit()
                            return((user_textp1, user_textp2), user_textTurn)
                    
                    
                    
                else:
                    user_text += event.unicode
                    
    
    
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect)
    
        text_surface = base_font.render(user_text, True, (255,255,0))
    
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    
        input_rect.w = max(100, text_surface.get_width()+10)

    
        pygame.display.flip() # met a jour la fenetre

   
def inter_game(w,l, turn, status, names, maxtours):
    """
    Parameters
    ----------
    w, l : int
        variable globale.
    turn : int
        nombre du tour actuel.
    status : str
        gagnant: 'O' si O a gagné et 'X' si X à gagné.
    names : str, str
        noms des joueurs.
    maxtours : int
        nombre de tours max.

    Returns:
    -------
        lance une nouvelle partie.
cette fonction permet de donner les stats du jeu entre deux parties et au début de la partie
    """
    game = True
    ecran = pygame.display.set_mode((w,l))
    if turn %2 ==0:
        start = 'x'
    else:
        start = 'o'
    turn = str(turn)
    O, X = status
    O = str(O)
    X = str(X)
    text3 = str("Let's go for round "+ turn)
    if turn == maxtours:
        text3 = 'Last Round !!!'
    text4 = str(names[0]+' = '+O)
    text5 = str(names[1]+' = '+X)
    if int(turn) %2 == 0:
        
        name = (names[1],names[0]) 
    else:
        name = (names[0],names[1]) 



    while game == True:
        pygame.display.update()
        pygame.display.set_caption('Morpion')
        ecran.fill((19,19,70))
        w=w-1
        l=l-1
        pygame.draw.line(ecran, (255, 255, 0), ((w/9)*3,(l/8)*5), ((w/9)*6,(l/8)*5), 3)
        pygame.draw.line(ecran, (255, 255, 0), ((w/9)*3,(l/8)*6), ((w/9)*6,(l/8)*6), 3)
        pygame.draw.line(ecran, (255, 255, 0), (0,0), (w, 0), 5)
        pygame.draw.line(ecran, (255, 255, 0), (0,0), (0, l), 5)
        pygame.draw.line(ecran, (255, 255, 0), (w,0), (w, l), 5)
        pygame.draw.line(ecran, (255, 255, 0), (0,l), (w, l), 5)
        w=w+1
        l=l+1
   
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 40)
        font2 = pygame.font.Font('freesansbold.ttf', 170)
        fontstatus = pygame.font.Font('freesansbold.ttf', 35)
 
        text = font.render(text3, True, (255, 255, 0))
        text2 = font2.render('Morpion', True, (255, 255, 0))
        textO = fontstatus.render(text4, True, (255, 255, 0))
        textX = fontstatus.render(text5, True, (255, 255, 0))
       
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRectO = textO.get_rect()
        textRectX = textX.get_rect()
       
 
        textRect.center = (w // 2, (l // 8)*(5+(55/100))) #centre les differends textes
        textRect2.center = (w // 2, (l // 8)*(2+(7/10)))
        textRectO.center = ((w // 8)*(1+(7/10)), (l // 8)*(7+(0/10)))
        textRectX.center = ((w // 8)*(6+(3/10)), (l // 8)*(7+(0/10)))
   
   
   
        ecran.blit(text, textRect)
        ecran.blit(text2, textRect2)
        ecran.blit(textO, textRectO)
        ecran.blit(textX, textRectX)
   
        for event in pygame.event.get():
       
       
            if event.type == pygame.QUIT:
                sys.exit()
                   
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                posX, posY = position[0]//(w/9), position[1]//(l/8)
           
                if posX >= 3 and posX <= 5 and posY == 5:
                   
                    return new_game(start, name)

def init_game(w,l):
    """
    Parameters
    ----------
    w , l : int
        variable globale.

    permet de creer une fenetre qui montre le bouton start et le titre du jeu
    en honeur au celebre Pac-man, je me suis inspiré pour le choix des couleurs :-) 

    """
    game = True
    ecran = pygame.display.set_mode((w,l))
    pygame.init()
    while game == True:
       
       
       
       
        pygame.display.update()
        pygame.display.set_caption('Morpion')
        ecran.fill((19,19,70))
        w=w-1
        l=l-1
        pygame.draw.line(ecran, (255, 255, 0), ((w/9)*3,(l/8)*5), ((w/9)*6,(l/8)*5), 3)
        pygame.draw.line(ecran, (255, 255, 0), ((w/9)*3,(l/8)*6), ((w/9)*6,(l/8)*6), 3)
        pygame.draw.line(ecran, (255, 255, 0), (0,0), (w, 0), 5)
        pygame.draw.line(ecran, (255, 255, 0), (0,0), (0, l), 5)
        pygame.draw.line(ecran, (255, 255, 0), (w,0), (w, l), 5)
        pygame.draw.line(ecran, (255, 255, 0), (0,l), (w, l), 5)
        w=w+1
        l=l+1
   
   
        font = pygame.font.Font('freesansbold.ttf', 50)
        font2 = pygame.font.Font('freesansbold.ttf', 170)
 
        text = font.render('START', True, (255, 255, 0))
        text2 = font2.render('Morpion', True, (255, 255, 0))
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
 
        textRect.center = (w // 2, (l // 8)*(555/100))
        textRect2.center = (w // 2, (l // 8)*(2+(7/10)))
   
   
   
        ecran.blit(text, textRect)
        ecran.blit(text2, textRect2)
   
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
               
            if event.type == pygame.QUIT:
                pygame.quit()
                   
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                posX, posY = position[0]//(w/9), position[1]//(l/8)
           
                if posX >= 3 and posX <= 5 and posY == 5:
                    pygame.quit()
                    return(True)
       

def end_game(w,l,status, names, maxtours):
    """
    Parameters
    ----------
    w, l : int
        variable globale.
    status : str
        vainqueur.
    names : str, str
        noms des joueurs.
    maxtours : int
        nombre de manches max.
permet une page finale pour clore le jeu
    """
    pygame.init()
    
    
    O, X = status

    if O == X:
        textpts = 'Fair duel!'
    elif O > X:
        textpts = names[0]+' wins!'
    else:
        textpts = names[1]+' wins!'
    game = True
    ecran = pygame.display.set_mode((w,l))
   
    while game == True:
       
       
       
       
       
        pygame.display.set_caption('Morpion')
        ecran.fill((19,19,70))
        w=w-1
        l=l-1
        pygame.draw.line(ecran, (255, 255, 0), ((w/9)*3,(l/8)*5), ((w/9)*6,(l/8)*5), 3)
        pygame.draw.line(ecran, (255, 255, 0), ((w/9)*3,(l/8)*6), ((w/9)*6,(l/8)*6), 3)
        pygame.draw.line(ecran, (255, 255, 0), (0,0), (w, 0), 5)
        pygame.draw.line(ecran, (255, 255, 0), (0,0), (0, l), 5)
        pygame.draw.line(ecran, (255, 255, 0), (w,0), (w, l), 5)
        pygame.draw.line(ecran, (255, 255, 0), (0,l), (w, l), 5)
        w=w+1
        l=l+1
   
   
        font = pygame.font.Font('freesansbold.ttf', 50)
        font2 = pygame.font.Font('freesansbold.ttf', 140)
 
        text = font.render('Finish', True, (255, 255, 0))
        text2 = font2.render(textpts, True, (255, 255, 0))
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
 
        textRect.center = (w // 2, (l // 8)*(555/100))
        textRect2.center = (w // 2, (l // 8)*(2+(7/10)))
   
   
   
        ecran.blit(text, textRect)
        ecran.blit(text2, textRect2)
   
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
               
            if event.type == pygame.QUIT:
                pygame.quit()
                   
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                posX, posY = position[0]//(w/9), position[1]//(l/8)
           
                if posX >= 3 and posX <= 5 and posY == 5:
                    pygame.quit()
                    sys.exit(0)
        pygame.display.update()
       
       
    return

def Startjeu(w,l):
    """
    

    Parameters
    ----------
    w , l : int
        variable globale.
permet de lancer et gérer le jeu au fur et a mesure des manches

    """
    if init_game(w,l) == True:
        names, maxtours = settings(w,l)
        status = [0,0]
        for i in range(1,maxtours+1):
            result = inter_game(w,l, i, status, names, maxtours)
            if result == 'O':
                status[0] += 1
            elif result == 'X':
                status[1] += 1
    end_game(w, l, status,names, maxtours)
    
    

Startjeu(w,l)









