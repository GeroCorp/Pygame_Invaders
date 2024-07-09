import pygame
from game import startGame
from options import options
from functions import *
from settings import *


pygame.init()
pygame.display.set_caption("Space Invaders")


startButton = pygame.Rect(SCREEN_X_CENTER- buttonSize[0]//2,SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1])


def main_menu():
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        
        SCREEN.blit(MAIN_MENU_IMG, SCREEN_ORIGIN)
        arrowMouse = False

        if newButton("Start", startButton, COLORES["aqua"], COLORES["green"], startGame):
            arrowMouse = True
        if newButton("Options", pygame.Rect(startButton.left, startButton.y + 60, buttonSize[0], buttonSize[1]), COLORES["aqua"], COLORES["green"], options):
            arrowMouse = True
        if newButton("Exit", pygame.Rect(startButton.left, startButton.y + 120, buttonSize[0], buttonSize[1]), COLORES["aqua"], COLORES["green"], quitGame):
            arrowMouse = True

        pointerChange(arrowMouse)


        pygame.display.flip()



clock = pygame.time.Clock()

main_menu()
    

    
    
   