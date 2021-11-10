#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:00:19 2021

@author: pedroPedro
"""
import pygame
import sys
from math import floor
import time
pygame.init()




w = 800
l = 800



taille = 3



length = []
width = []
o_img = pygame.image.load("O.png")
x_img = pygame.image.load("X.png")
o_img = pygame.transform.scale(o_img, ((int(floor(w/taille))), int(l/taille)))
x_img = pygame.transform.scale(x_img, ((int(floor(w/taille))), int(l/taille)))

lignes = []

for i in range(1,taille):
    length.append(l*i/taille)
for i in range(1,taille):
    width.append(w*i/taille)
for i in range(taille-1):
    lignes.append(((length[i],0),(length[i],l)))
    lignes.append(((0,width[i]),(l,width[i])))
#print(lignes)





class Grille:
    def __init__(self, ecran, lignes):
        self.ecran = ecran
        self.lignes = lignes
        self.grille = [[None for x in range(0, taille)] for y in range(0, taille)]
    
    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (0,0,0), ligne[0], ligne[1], 2)
            
    def print_grid(self):
        print(self.grille)
            
    def spot_value(self, x, y, value):
        if self.grille[x][y] == None:
            self.grille[x][y] = value
        else: 
            return False
        
    def centersquare(self, x, y):
        x = x*(w/taille)
        y = y*(l/taille)
        return x,y
        
    
    def placeXO(self, x, y):
        if self.grille[x][y] == 'X':
            x, y = Grille.centersquare(self, x, y)
            self.ecran.blit(x_img, (x, y))
        else:
            x, y = Grille.centersquare(self, x, y)
            self.ecran.blit(o_img, (x, y))
        pygame.display.update()


            
    
class jeu:
    def __init__(self):
        self.ecran = pygame.display.set_mode((w,l))
        pygame.display.set_caption("Tic Tac Toe")
        self.jeu_encours = True
        self.grille = Grille(self.ecran, lignes)
        self.player_X = 'X'
        self.player_O = 'O'
        self.turn = 0
    
    def fonction_principale(self,start):
        stop = False
        self.ecran.fill((240,240,240))
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
                        
                   
                    
                #self.grille.print_grid()
                
                
                lst_X = []
                lst_O = []
                lst_ligne_X = []
                lst_ligne_O = []
                lst_colonne_X = []
                lst_colonne_O = []
                for ligne in range(0, len(self.grille.grille)):
                    for colonne in range(0, len(self.grille.grille)):
        
                        if self.grille.grille[ligne][colonne] == 'X':
                            X_position = (ligne, colonne)
                            lst_X.append(X_position)
        
                        elif self.grille.grille[ligne][colonne] == 'O':
                            O_position = (ligne, colonne)
                            lst_O.append(O_position)
    
                if len(lst_X) >= 3:
                    for (ligne, colonne) in lst_X:
                        lst_ligne_X.append(ligne)
                        lst_colonne_X.append(colonne)
        
                    if lst_ligne_X.count(0) ==3 or lst_ligne_X.count(1) ==3 or lst_ligne_X.count(2) ==3:

                        victoire = True
                        status = 'X'
                    if lst_colonne_X.count(0) ==3 or lst_colonne_X.count(1) ==3 or lst_colonne_X.count(2) ==3:

                        victoire = True
                        status = 'X'
                    if lst_ligne_X == lst_colonne_X or lst_ligne_X == lst_colonne_X[::-1]:

                        victoire = True
                        status = 'X'
                    
                if len(lst_O) >= 3:
                    for (ligne, colonne) in lst_O:
                        lst_ligne_O.append(ligne)
                        lst_colonne_O.append(colonne)
        
                    if lst_ligne_O.count(0) ==3 or lst_ligne_O.count(1) ==3 or lst_ligne_O.count(2) ==3:
          
                        victoire = True
                        status = 'O'
                    if lst_colonne_O.count(0) ==3 or lst_colonne_O.count(1) ==3 or lst_colonne_O.count(2) ==3:

                        victoire = True
                        status = 'O'
                    print(lst_ligne_O)
                    print(lst_colonne_O)
                    if lst_ligne_O == lst_colonne_O or lst_ligne_O == lst_colonne_O[::-1]:
                        self.grille.print_grid()
                        victoire = True
                        status = 'O'
                
            
            self.grille.afficher()
            pygame.display.flip()
            if victoire == True:
                time.sleep(1)
                self.jeu_encours = False
            elif self.turn == taille*taille:
                time.sleep(1)
                self.jeu_encours = False
                status = 'egalite'
        return(status)


def new_game(start):
    if __name__ == "__main__":
        pygame.init()
        status = jeu().fonction_principale(start)
        pygame.quit()
    return status
    
    
    
    
#new_game()
    
    
def inter_game(w,l, turn, status):
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
    if turn == '10':
        text3 = 'Last Round !!!'
    text4 = str('O = '+O)
    text5 = str('X = '+X)


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
        
 
        textRect.center = (w // 2, (l // 8)*(5+(55/100)))
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
                    
                    return new_game(start)

def init_game(w,l):
    game = True
    ecran = pygame.display.set_mode((w,l))
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
        

def end_game(w,l,status):
    pygame.init()
    O, X = status
    if O == X: 
        textpts = 'Fair duel!'
    elif O > X: 
        textpts = 'O wins!'
    else:
        textpts = 'X wins!'
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
    if init_game(w,l) == True:
        status = [0,0]
        for i in range(1,11):
            result = inter_game(w,l, i, status)
            if result == 'O':
                status[0] += 1
            elif result == 'X':
                status[1] += 1
    end_game(w, l, status)
        
    
Startjeu(w,l)
            
    

    
            
















