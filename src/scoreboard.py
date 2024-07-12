import pygame
from settings import *
from functions import *
from gameFunctions import bestScorePrint,lastScorePrint

def scoreScreen():
    
    isRunning = True
    while isRunning:
        click = None
        arrowMouse = True
        SCREEN.blit(SCOREBOARD_IMG, SCREEN_ORIGIN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONUP:
                click = event.button
        
        backButton = {"rect": pygame.Rect(SCREEN_X_CENTER- buttonSize[0]//2, SCREEN_Y_CENTER- buttonSize[1]//2, buttonSize[0], buttonSize[1])}

        if newButton("Back", backButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
            arrowMouse = True
            if click == 1:
                isRunning = False
        
        pointerChange(arrowMouse)
        lastScorePrint(LAST_SCORE_FILE)
        bestScorePrint(RANKING_FILE)
        pygame.display.flip()