import pygame
from settings import *
import sys



def quitGame():
    """Closes the game
    """
    pygame.quit()
    sys.exit()

def point_rect (point, rect) -> bool:
    """Verifies collision betwwen a rect and a point

    Args:
        point (coords): Point in rect
        rect (rect): Rect

    Returns:
        bool: Returns True if collision  
    """
    x, y = point
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def rectCollision (rect_1, rect_2):
    """Verifies collision between rects

    Args:
        rect_1 (rect): First rect
        rect_2 (rect): Second rect

    Returns:
        bool: Returns True if there's a coliision
    """
    if point_rect(rect_1.topleft, rect_2)or \
    point_rect(rect_1.topright, rect_2)or \
    point_rect(rect_1.bottomleft, rect_2)or \
    point_rect(rect_1.bottomright, rect_2):
        return True

def newButton(text, rect, color, hoverColor, action=None):
    """Generates a new button

    Args:
        text (str): Button's text
        rect (rect): Buttons dimentions
        color (ColorValue): Button's default color
        hoverColor (ColorValur): Button's color when hovered
        action (Function, optional): Calls function. Defaults to None.

    Returns:
        bool: Returns True if button's hovered
    """
    font = pygame.font.SysFont(None, 36)
    mousePos= pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hover = point_rect(mousePos, rect)

    if hover:
        pygame.draw.rect(SCREEN, hoverColor, rect)
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(SCREEN, color, rect)

    thisText = font.render(text, True, COLORES["black"])
    SCREEN.blit(thisText, thisText.get_rect(center= rect.center))

    return hover

def pointerChange(hover: bool):
    """Changes mouse pointer

    Args:
        hover (bool): Button's hover
    """
    if hover:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

def bulletCollision(bullet, enemy):
    """Verefies bullets collision with an enemy

    Args:
        bullet (rect): Bullet's rect value
        enemy (rect): Enemy's rect value

    Returns:
        bool: Returns True if collision
    """
    if point_rect(bullet.topleft, enemy) or\
       point_rect(bullet.topright, enemy):
        return True

def waitUser (key):
    """Waits for the user to press 'key' to continue

    Args:
        key (keyValue): Awaited key
    """
    flagStart = True
    while flagStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    flagStart = False

def getActualPath(file: str)-> str:
    """Obtener ruta actual de un archivo

    Returns:
        _type_: Ruta del archivo
    """
    import os
    pwd = os.path.dirname(__file__)

    return os.path.join(pwd, file)

def nameInput(score):
    font = pygame.font.SysFont(None, 36)
    name = ""

    SCREEN.fill(COLORES['black'])
    typingName = True

    endText = font.render("Enter your username: ", True, COLORES['white'])
    endTextRect = pygame.Rect(SCREEN_X_CENTER-50, SCREEN_Y_CENTER, 100, 100)
    SCREEN.blit(endText, endText.get_rect(center= endTextRect.center))
    

    scoreTextRect = pygame.Rect(SCREEN_X_CENTER-50, SCREEN_Y_CENTER-150, 100, 100)
    scoreText = font.render(f"Score: {score}", True, COLORES['white'])
    SCREEN.blit(scoreText, scoreText.get_rect(center= scoreTextRect.center))


    nameRect = pygame.Rect(SCREEN_X_CENTER-50, SCREEN_Y_CENTER+150, 100, 100)
    pygame.display.update()
    while typingName:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return name
                
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else: 
                    name += event.unicode
        
        SCREEN.fill(COLORES['black'])

        endText = font.render("Enter your username: ", True, COLORES['white'])
        SCREEN.blit(endText, endText.get_rect(center= endTextRect.center))

        scoreText = font.render(f"Score: {score}", True, COLORES['white'])
        SCREEN.blit(scoreText, scoreText.get_rect(center= scoreTextRect.center))

        nameText = font.render(name, True, COLORES['white'])
        SCREEN.blit(nameText, nameText.get_rect(center = nameRect.center))
        pygame.display.update()
        
