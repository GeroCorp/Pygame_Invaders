import pygame
from settings import *
from functions import *

def options():
    
    isRunning = True
    arrowMouse = False

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        
        backButton = {"rect": pygame.Rect(SCREEN_X_CENTER- buttonSize[0]//2, HEIGHT-100, buttonSize[0], buttonSize[1])}

        SCREEN.blit(OPTION_IMG, SCREEN_ORIGIN)

        if newButton("Back", backButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
            arrowMouse = True
            click = pygame.mouse.get_pressed()
            if click [0] == 1:
                isRunning = False
        
        pointerChange(arrowMouse)

        pygame.display.flip()