# Constantes para design do texto Mountain Shooter
import pygame

# Constantes para design do texto
COLOR_DARKBLUE = (23, 19, 48)  # Cor AZUL ESCURO
COLOR_BLUE = (63, 72, 204)  # Cor AZUL
BACKGROUND_COLOR = (255, 255, 255)  # Cor de fundo do texto (ajuste conforme necessário)
BORDER_COLOR = (0, 0, 0)  # Cor da borda do fundo (ajuste conforme necessário)
BORDER_PADDING = 5  # Espaço entre o texto e a borda
CORNER_RADIUS = 5  # Raio dos cantos arredondados
CORNER_RADIUS_MAIN = 10  # Raio dos cantos arredondados para os títulos principais
CORNER_RADIUS_OPTION = 5  # Raio dos cantos arredondados para as opções de menu

# ---------------------------------------------
# Constantes para configurações do MENU
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
# Constantes de tamanho da Tela
W_WIDTH = 576
W_HEIGHT = 324
# ---------------------------------------------

# Constantes para entidades
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Player1': 3,
                'Player1Shot': 2,
                'Player2': 3,
                'Player2Shot': 3,
                'Enemy1': 2,
                'Enemy1Shot': 5,
                'Enemy2': 3,
                'Enemy2Shot': 5,
                }
ENTITY_HEALTH = {'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 200,
                 'Enemy1Shot': 1,
                 'Enemy2': 200,
                 'Enemy2Shot': 1,
                 }
ENTITY_SHOT_DELAY = {'Player1': 20,
                     'Player2': 15,
                     'Enemy1': 100,
                     'Enemy2': 200,
                     }

# ---------------------------------------------
# Constantes para mover os Players
PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}

PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}

PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_RCTRL}
