#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:14:11 2021

@author: pedroPedro
"""
import pygame
import sys
pygame.init()
w = 800
l = 800
game = True
ecran = pygame.display.set_mode((w,l))



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
                    




end_game(w,l, (10,0)) 
print('start')






































