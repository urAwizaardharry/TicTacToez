#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:00:19 2021

@author: pedroPedro
"""
import pygame
import sys
from math import floor




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
        x = x*(w/taille)+w/(2*taille)
        y = y*(l/taille)+l/(2*taille)
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
    
    def fonction_principale(self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
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
                        
                   
                    
                self.grille.print_grid()
                
                
                    
                    
            
            self.ecran.fill((240,240,240))
            self.grille.afficher()
            pygame.display.flip()
            


if __name__ == "__main__":
    pygame.init()
    jeu().fonction_principale()
    pygame.quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    