import pygame
from settings import *
from functions import *

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

def startGame():

    pygame.mouse.set_visible(False)

    font = pygame.font.SysFont(None, 36)

    
    keyK = False
    

    #Buttons
    resumeButton = {"rect": pygame.Rect(SCREEN_X_CENTER- buttonSize[0]//2,SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Resume"}
    mainMenuButton = {"rect": pygame.Rect(SCREEN_X_CENTER- buttonSize[0]//2,HEIGHT-100,buttonSize[0], buttonSize[1]),"text":"Main menu"}
    retryMain = {"rect": pygame.Rect(resumeButton["rect"].x - buttonSize[0] , SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Main menu"}
    retryButton = {"rect": pygame.Rect(resumeButton["rect"].x + buttonSize[0] ,SCREEN_Y_CENTER ,buttonSize[0], buttonSize[1]),"text":"Retry"}

    #-------------------- PLAYER ------------------------
    player = {"rect": pygame.Rect(SCREEN_X_CENTER- player_width//2, HEIGHT-100, player_width, player_height)}
    player_speed = 5
    bullet_speed = 4
    bullets = []
    #                   HEALTH AND SCORE
    player_lifes = 3

    lifesText = font.render(f"Vidas: {player_lifes}", True, COLORES["white"])
    continueText = font.render("Press 'Space' to continue",True, COLORES["white"])

    player_score = 0
    scoreText = font.render(f"Score: {player_score}", True, COLORES["white"])
    #                   MOVEMENT
    kLeft = False
    kRight = False
    

    #-------------------------------ENEMIES------------------------------------------------------
    enemy = {"rect": pygame.Rect(SCREEN_X_CENTER, SCREEN_Y_CENTER, player_width, player_height)}
    laser_speed = 6
    num_enemies_x = 10
    num_enemies_y = 5
    MAX = 15
    HARD = 10
    NORMAL = 5
    enemies = []
    lasers = []
    enemyRespawn = False
    maxRight = False

    enemySpawner(num_enemies_y, num_enemies_x, enemy_width, enemy_height, enemies)


   

    mouse_arrow= False
    gamePaused = False 
    isRunning = True



    #----------------------------TIMERS------------------------------
    #enemy movement timer
    segs = 0.4
    startTime= pygame.time.get_ticks()
    intervalo = segs * 1000 #segs SEGUNDOS
    
    #sprite timer
    sprite = 0
    spriteChange = 0.3 #Cambia el sprite cada X segundos
    timeLastFrame = 0

    #lasers timer
    lastLaser = 0
    laserCd = 3500 #MS

    #bullet cooldown
    lastShot = 0
    coolDown = 1000 #MS

    while isRunning:
        pygame.time.Clock().tick(60)

        lastTick = pygame.time.Clock().tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:

                #MOVEMENT KEYS
                if event.key == pygame.K_LEFT:
                    kLeft = True
                if event.key == pygame.K_RIGHT:
                    kRight = True

                #PAUSE KEY
                if event.key == pygame.K_ESCAPE:
                    if gamePaused:
                        gamePaused = not gamePaused
                    else:
                        gamePaused = not gamePaused
                    
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    currentTime = pygame.time.get_ticks()
                    #Si pasó un segundo desde el ultimo disparo
                    if currentTime - lastShot > coolDown:
                        playerBullet = pygame.Rect(player["rect"].centerx - 2, player["rect"].top - 10, 5, 10)
                        bullets.append(playerBullet)
                        lastShot = currentTime

                if event.key == pygame.K_DOWN:
                    kDown = False
                #MOVEMENT KEYS
                if event.key == pygame.K_LEFT:
                    kLeft = False
                if event.key == pygame.K_RIGHT:
                    kRight = False

                #TEST delete later------------------
                if event.key == pygame.K_k:
                    keyK = True
                #TEST--------------------------------
        
    
            if event.type == pygame.WINDOWFOCUSLOST:
                gamePaused = True



        if not gamePaused:
            SCREEN.fill(COLORES["grey"])
            pygame.mouse.set_visible(False)

            #PLAYER MOVEMENT
            if kLeft:
                player["rect"].x -= player_speed
            elif kRight:
                player["rect"].x += player_speed

            if player["rect"].right>= WIDTH:
                player["rect"].right = WIDTH
            if player["rect"].left<= 0:
                player["rect"].left = 0
                
            #-------------------------BULLET AND LASER-------------------------
            for bullet in bullets:
                bullet.y -= bullet_speed
                if bullet.bottom <0:
                    bullets.remove(bullet)
            #                         BULLETS COLLISION
            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if bulletCollision(bullet, enemy["rect"]):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        if not enemyRespawn:
                            if len(enemies) < 35:
                                player_score +=10
                                scoreText = font.render(f"Score: {player_score}", True, COLORES["white"])
                            else: 
                                player_score +=5
                                scoreText = font.render(f"Score: {player_score}", True, COLORES["white"])
                        else:
                            player_score +=20
                            scoreText = font.render(f"Score: {player_score}", True, COLORES["white"])

            #                           LASER SPAWN
            currentTime = pygame.time.get_ticks()
            if currentTime - lastLaser > laserCd:
                from random import randint
                for enemy in enemies:
                    rng = randint(1,12)
                    if rng >10:
                        enemyLaser = pygame.Rect(enemy["rect"].centerx - 2, enemy["rect"].bottom + 10, 5, 10)
                        lasers.append(enemyLaser)
                        lastLaser = currentTime
            #                         LASER MOVEMENT
            for laser in lasers:
                laser.y+= laser_speed
                if laser.top > HEIGHT:
                    lasers.remove(laser)
            


            

            #PLAYER KILL
            for enemy in enemies:
                if rectCollision(player["rect"], enemy["rect"]):
                    player["rect"].x = SCREEN_X_CENTER- player_width//2
                    SCREEN.blit(continueText,SCREEN_CENTER)
                    bullets = []
                    pygame.display.flip()
                    waitUser(pygame.K_SPACE)

                    player_lifes -=1
                    lifesText = font.render(f"Vidas: {player_lifes}", True, COLORES["white"])

                    enemyRetry(enemies)
            for laser in lasers:
                if rectCollision(laser, player["rect"]):
                    player_lifes, lifesText, lasers =playerDeath(player["rect"], player_lifes, continueText, lasers)
                    enemyRetry(enemies)
                    bullets= []

            #TEST delete later---------------------------------------
            if keyK:
                player["rect"].x = SCREEN_X_CENTER- player_width//2
                SCREEN.blit(continueText,SCREEN_CENTER)
                bullets = []
                lasers = []
                pygame.display.flip()
                waitUser(pygame.K_SPACE)

                player_lifes -=1
                lifesText = font.render(f"Vidas: {player_lifes}", True, COLORES["white"])

                enemyRetry(enemies)

                keyK = False
            #TEST-----------------------------------------------------


            #ENEMIES DRAW N MOVEMENT
            timeLastFrame += lastTick
            if timeLastFrame >= spriteChange:
                timeLastFrame= 0
                sprite = (sprite + 1) % len(ENEMIES_SPRITES)
                #Le asigna el resto de la division a "sprite"
        
            #           Enemy speed
            if not enemyRespawn:
                enemy_speed = NORMAL if len(enemies) > 35 else HARD
            else:
                enemy_speed = MAX

            currentTime = pygame.time.get_ticks()
            #Cada 0.4 segundos actualiza posición
            if currentTime - startTime >= intervalo:
                #
                lastRowEnemy = max(enemies, key=lambda enemy: enemy["rect"].right)

                firstRowEnemy = min(enemies, key=lambda enemy: enemy["rect"].left)
                
                if lastRowEnemy["rect"].right >= ENEMIES_X_SQUARE[1]:
                    maxRight = True

                
                if firstRowEnemy["rect"].left <= ENEMIES_X_SQUARE[0]:
                    maxRight = False

                for enemy in enemies:
                    if enemy["rect"].right <= ENEMIES_X_SQUARE[1] and not maxRight:
                        enemy["rect"].x += enemy_speed

                    if enemy["rect"].left >= ENEMIES_X_SQUARE[0] and maxRight:
                        enemy["rect"].x -= enemy_speed

                startTime = currentTime



            #IF EVERY ENEMY IS KILLED
            if len(enemies) == 0:
                    enemySpawner(num_enemies_y, num_enemies_x, enemy_width, enemy_height, enemies)
                    enemyRespawn = True
            for enemy in enemies:
                SCREEN.blit(ENEMIES_SPRITES[sprite], enemy["rect"])

            SCREEN.blit(PLAYER_SPRITE, player["rect"])

            #TEXT DRAW
            SCREEN.blit(lifesText, SCREEN_ORIGIN)
            SCREEN.blit(scoreText, (WIDTH-scoreText.get_width(), 0))

            for bullet in bullets:
                pygame.draw.rect(SCREEN, COLORES["white"],bullet)

            for laser in lasers:
                pygame.draw.rect(SCREEN, COLORES["red2"],laser)
            

            #GAME OVER SCREEN
            if player_lifes == 0:
                pygame.mouse.set_visible(True)
                enemies = []
                SCREEN.blit(GAMEOVER_IMG, SCREEN_ORIGIN)
                
                #RETRY BUTTON
                if newButton(retryButton["text"], retryButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
                    mouse_arrow = True
                    click = pygame.mouse.get_pressed()
                    if click [0] == 1:
                        player_lifes = 3
                        lifesText = font.render(f"Vidas: {player_lifes}", True, COLORES["white"])
                        enemySpawner(num_enemies_y, num_enemies_x, enemy_width, enemy_height, enemies)

                        player_score = 0
                        scoreText = font.render(f"Score: {player_score}", True, COLORES["white"])
                        lasers= []
                        bullets= []
                        enemyRespawn = False

                #MAIN MENU BUTTON
                if newButton(retryMain["text"], retryMain["rect"], COLORES["yellow2"], COLORES["orange2"]):
                    mouse_arrow = True
                    click = pygame.mouse.get_pressed()
                    if click [0] == 1:
                        isRunning = False
                    
                    pygame.display.flip()

            pygame.display.flip()

        else:
            pygame.mouse.set_visible(True)
            
            SCREEN.blit(PAUSE_IMG, SCREEN_ORIGIN)
                
            if newButton(resumeButton["text"], resumeButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
                mouse_arrow = True
                click = pygame.mouse.get_pressed()
                if click [0] == 1:
                    gamePaused = False
            if newButton(mainMenuButton["text"], mainMenuButton["rect"], COLORES["yellow2"], COLORES["orange2"]):
                mouse_arrow = True
                click = pygame.mouse.get_pressed()
                if click [0] == 1:
                    isRunning = False

            pointerChange(mouse_arrow)
            pygame.display.flip()

        pass