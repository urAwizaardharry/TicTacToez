#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:55:44 2021

@author: pedroPedro
"""


import pygame

jeu = {}
jeu["1"] = "0"
jeu["2"] = "0"
jeu["3"] = "0"
jeu["4"] = "0"
jeu["5"] = "0"
jeu["6"] = "0"
jeu["7"] = "0"
jeu["8"] = "0"
jeu["9"] = "0"





def test(liste):
    if liste[0] == liste[1] == liste[2]:
        if int(liste[0]) == 0:
            return False
        return True
    return False

def victoire(jeu):
    """
    

    Parameters
    ----------
    jeu : dictionnaire
        dictionnaire avec neuf clefs (les 9 cases du jeu) et qui on en valeur 
        0, 1 et 2. l'équipe 0 si il n'y a pas d'équipe, 1 c'est l'équipe 1 et 
        2 c'est paareil.

    Returns
    -------
    TYPE str + int / bool
        si victoire: str qui donne la victoire et int--> nombre de l'équipe
        pas victoire: 
        bool == False --> jeu pas fini
        bool == True --> jeu fini
        .

    """
    listeh = []
    listev1 = []
    listev2 = []
    listev3 = []
    listeT = []

    for j in range (3):
        for i in range(1,4):
            h = str(i + 3 * j)
            listeh.append(jeu[h])
            print()
            
        if test(listeh) == True:
            return "victoire de l'équipe1",listeh[0]
        
        v1 = str(3 * j + 1)
        listev1.append(jeu[v1])
    
        v2 = str(3 * j + 2)
        listev2.append(jeu[v2])
    
        v3 = str(3 * j + 2)
        listev3.append(jeu[v3])
        
    
    if test(listev1) == True:
        return "victoire de l'équipe2",listev1[0]
    
    if test(listev2) == True:
        return "victoire de l'équipe3",listev2[0]
    
    if test(listev3) == True:
        return "victoire de l'équipe4",listev3[0]
    
    
    if jeu["1"] == jeu["5"] == jeu["9"] != '0':
        
        return "victoire de l'équipe5", jeu["1"] 
        
    if jeu["3"] == jeu["5"] == jeu["7"] != '0':
        return "victoire de l'équipe6", jeu["3"] 
    
    for n in range(1,10):
        n = str(n)
        listeT.append(jeu[n])
    for el in listeT:
        if int(el) == 0:
            return False
    return True
    



def position(w,l,taille):
    """
    positions du centre du cercle
    t: equipe (1 ou 2)
    """
    x = int(input("choisis x "))
    y = int(input("choisis y "))
    x = int(x*w/taille + w/(taille*2))
    y = int(y*l/taille + l/(taille*2))
    t = input("Quelle est ton équipe?")
    return x, y, t


def pose(jeu, equipe, position):
    """
    
    Parameters
    ----------
    jeu : dict
        dictionnaire du jeu.
    equipe : int
        equipe du joueur.
    position : int
        on suppose que position est un chiffre de 1 à 9 qui represente les 
        cases du morpion.

    Returns
    -------
    jeu : dict
        dictionnaire du jeu.

    """
    position = str(position)
    while jeu[position] != '0':
        print('cette position est déjà prise')
        position = int(input("choisis une position pas prise de 1 à 9 inclus"))
        position = str(position)
    equipe = str(equipe)
    jeu[position] = equipe
    return jeu


def pose_map(w,l,taille, jeu):
    """
    positions du centre du cercle (x, y)
    equipe: equipe (1 ou 2)
    """
    position = int(input("choisis une position pas prise de 1 à 9 inclus "))
    equipe = int(input('Quelle est ton équipe?'))
    x = 0
    jeu = pose(jeu, equipe, position)
    position = position - 1
    while position >= 3:
        position = position - 3
        x += 1
    
    y = position
    x = (x*l) / taille + l/(taille * 2)
    y = (y*w) / taille + w/(taille * 2)

    return x, y, equipe


#print(pose_map(w, l, taille))


#x, y, t = pose_map(w,l,taille, jeu)
w = 900
l = 900
taille = 3
length = []
width = []
surf = pygame.display.set_mode((w,l))
run = True
lst = []
coups = 0
for i in range(1,taille):
    length.append(l*i/taille)
for i in range(1,taille):
    width.append(w*i/taille)
for i in range(taille-1):
    print(length[i])
    pygame.draw.line(surf,(255,0,0),(length[i],0),(length[i],l),10)
    pygame.draw.line(surf,(255,0,0),(0,width[i]),(l,width[i]),10)
        
pygame.display.flip()
while run :
    

    
    coups += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if coups == 9:
        run = False
    print("coups:", coups)
    x, y, t = pose_map(w,l,taille, jeu)
    for el in lst:
        if el == (x, y):
            print("cette case est déjà prise")
            x, y = pose_map(w,l,taille, jeu)
    lst.append((x,y,t))
    if t == 1:
        pygame.draw.circle(surf, (0,0,255), (x, y), 30, 2)
    
    else : 
        pygame.draw.circle(surf, (255,0,0), (x, y), 30, 2)
    pygame.display.flip()
    print(run)
    if victoire(jeu) == True:
        run = False
        print('le jeu est finis et le résultat est égalité')
        

    elif not(victoire(jeu) == False):
        run = False
        print(victoire(jeu))



empty = pygame.Color(0,0,0,0)
surf.fill(empty)
pygame.quit()











