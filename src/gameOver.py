from functions import *
from settings import *
from pygame import *
from gameFunctions import *


def gameOver(game):
    running = True
    while running:
        click = None
        mouse_arrow = False
        SCREEN.blit(GAMEOVER_IMG, SCREEN_ORIGIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONUP:
                click = event.button


        retryButton = {"rect": pygame.Rect(340 ,SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Retry"}
        mainMenuButton = {"rect": pygame.Rect(740 , SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Main menu"}
        
        if newButton(retryButton["text"], retryButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
            mouse_arrow = True
            

            if click == 1:
                game()
                return
            
        if newButton(mainMenuButton["text"], mainMenuButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
            mouse_arrow = True
            
            if click == 1:
                running = False
                return running

        bestScorePrint(RANKING_FILE)
        lastScorePrint(LAST_SCORE_FILE)

        pointerChange(mouse_arrow)

        pygame.display.flip()




