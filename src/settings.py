import pygame
#SCREEN SETTINGS
WIDTH = 1280
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (WIDTH//2, HEIGHT//2)
SCREEN_ORIGIN = (0, 0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_X_CENTER = WIDTH //2
SCREEN_Y_CENTER = HEIGHT //2

#SIZES
buttonSize = (200, 50)
player_width = 70
player_height = 50
enemy_width = 50
enemy_height = 30
PLAYER_SIZE = (player_width, player_height)
ENEMY_SIZE = (enemy_width, enemy_height)
SHELTER_SIZE = (100, 70)
BULLET_SIZE = (10,20)

#ENEMIES ZONE
ENEMIES_X_SQUARE = (100, 1180)
ENEMIES_TOP_SQUARE = 0

#IMAGE LOADS
MAIN_MENU_IMG = pygame.transform.scale(pygame.image.load("./src/assets/img/mainMenu.jpg"), SCREEN_SIZE)
PAUSE_IMG = pygame.transform.scale(pygame.image.load("./src/assets/img/pauseMenu.jpg"), SCREEN_SIZE)
SCOREBOARD_IMG = pygame.transform.scale(pygame.image.load("./src/assets/img/scoreboardScreen.jpg"), SCREEN_SIZE)
GAMEOVER_IMG = pygame.transform.scale(pygame.image.load("./src/assets/img/gameOver.jpg"), SCREEN_SIZE)

PLAYER_SPRITE = pygame.transform.scale(pygame.image.load("./src/assets/sprites/player.png"), PLAYER_SIZE)
SHELTERS_SPRITE = pygame.transform.scale(pygame.image.load("./src/assets/sprites/shelter.png"), SHELTER_SIZE)
SHELTERS_SPRITE2 = pygame.transform.scale(pygame.image.load("./src/assets/sprites/shelter1.png"), SHELTER_SIZE)
SHELTERS_SPRITE3 = pygame.transform.scale(pygame.image.load("./src/assets/sprites/shelter2.png"), SHELTER_SIZE)
SHELTERS_DAMAGE = [SHELTERS_SPRITE,SHELTERS_SPRITE2,SHELTERS_SPRITE3]


ENEMY_SPRITE_1 = pygame.transform.scale(pygame.image.load("./src/assets/sprites/invader_A_1.png"), ENEMY_SIZE)
ENEMY_SPRITE_2 = pygame.transform.scale(pygame.image.load("./src/assets/sprites/invader_A_2.png"), ENEMY_SIZE)

ENEMIES_SPRITES = [ENEMY_SPRITE_1, ENEMY_SPRITE_2]


#Scores display
BEST_SCORES_X = 100
LAST_SCORES_X = 990



#Colors
COLORES = pygame.color.THECOLORS

#File path
RANKING_FILE = "./data/ranking.csv"
LAST_SCORE_FILE = "./data/lastScores.json"
