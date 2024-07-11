from functions import *
from settings import *
from pygame import *
from gameFunctions import *


def gameOver(game):
    mouse_arrow = False
    running = True
    while running:
        SCREEN.blit(GAMEOVER_IMG, SCREEN_ORIGIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()


        retryButton = {"rect": pygame.Rect(340 ,SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Retry"}
        mainMenuButton = {"rect": pygame.Rect(740 , SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Main menu"}
        
        if newButton(retryButton["text"], retryButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
            mouse_arrow = True
            click = pygame.mouse.get_pressed()

            if click[0] == 1:
                game()
                return
            
        if newButton(mainMenuButton["text"], mainMenuButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
            mouse_arrow = True
            click = pygame.mouse.get_pressed()
            if click [0] == 1:
                running = False
                return running

        bestScorePrint(RANKING_FILE)
        pointerChange(mouse_arrow)

        pygame.display.flip()




