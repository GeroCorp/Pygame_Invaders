import pygame
from settings import *
from filesHandler import *

def bestScorePrint(file):
    font = pygame.font.SysFont(None, 32)

    tempList = []
    rankingList = loadBestScores(file)
    width = 100
    height = 20
    for row in range(len(rankingList)):
        if row <5:
            y = row * (height + 30) + 400
            x = BEST_SCORES_X 
            tempList.append({"rect": pygame.Rect(x, y, width, height), "username": rankingList[row]["username"], "score": rankingList[row]["score"]})
        else:
            break


    for score in tempList:
        username = score["username"]
        userScore = score["score"]
        scoreTxt = font.render(f"{username:<10}{userScore:<15}", True, COLORES["white"])
        SCREEN.blit(scoreTxt, score["rect"])
    pygame.display.flip()
    return "printed"


def enemySpawner (row: int, col: int, width: int, height: int, list: list):
    """Create a new list with enemies

    Args:
        row (_type_):Rows quantity
        col (_type_): Col quantity
        width (_type_): Enemy's width
        height (_type_): Enemy's height
        list (_type_): List with enemies' rect
    """
    for thisrow in range(row):
        for thiscol in range(col):
            x = thiscol * (width + 50) + 100
            y = thisrow * (height + 20) + 90
            list.append({"rect": pygame.Rect(x, y, width, height)})
def enemyRetry(list:list):
    """Moves enemies up for a "continue" game

    Args:
        list (list): Enemies list
    """
    for enemy in list:
        if enemy["rect"].top >=90:
            enemy["rect"].y -= 50
def playerDeath(playerRect, playerLifes, deathText: str, screenElements: list):
    """Function for player's death

    Args:
        playerRect (rect): _description_
        playerLifes (var): _description_
        deathText (str): _description_
        screenElements (list): _description_

    Returns:
        newVar: Returns new values for life, lifeText and screenElements
    """
    font = pygame.font.SysFont(None, 36)
    playerRect.x = SCREEN_X_CENTER- playerRect.width//2
    SCREEN.blit(deathText, SCREEN_CENTER)
    screenElements = []
    pygame.display.flip()
    waitUser(pygame.K_SPACE)

    playerLifes -= 1
    playerLifesText = font.render(f"Vidas: {playerLifes}", True, COLORES["white"])

    return playerLifes, playerLifesText, screenElements
