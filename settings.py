import pygame

pygame.init()

# ==========================================================
# Window
# ==========================================================

TITLE = "Rich Kingdom Alpha 0.20"

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

FPS = 60

# ==========================================================
# Layout
# ==========================================================

MARGIN = 30

RIGHT_PANEL_WIDTH = 340

MESSAGE_HEIGHT = 120

BOARD_WIDTH = SCREEN_WIDTH - RIGHT_PANEL_WIDTH - MARGIN * 3

BOARD_HEIGHT = SCREEN_HEIGHT - MESSAGE_HEIGHT - MARGIN * 3

BOARD_SIZE = min(BOARD_WIDTH, BOARD_HEIGHT)

TILE_SIZE = BOARD_SIZE // 8

BOARD_LEFT = MARGIN

BOARD_TOP = (SCREEN_HEIGHT - MESSAGE_HEIGHT - BOARD_SIZE) // 2

RIGHT_PANEL_X = BOARD_LEFT + BOARD_SIZE + MARGIN

RIGHT_PANEL_Y = MARGIN

RIGHT_PANEL_HEIGHT = SCREEN_HEIGHT - MARGIN * 2

MESSAGE_X = MARGIN

MESSAGE_Y = SCREEN_HEIGHT - MESSAGE_HEIGHT - MARGIN

MESSAGE_WIDTH = BOARD_SIZE

MESSAGE_BOX_HEIGHT = MESSAGE_HEIGHT

# ==========================================================
# Dice
# ==========================================================

DICE_SIZE = 120

DICE_X = RIGHT_PANEL_X + (RIGHT_PANEL_WIDTH - DICE_SIZE) // 2

DICE_Y = SCREEN_HEIGHT - 220

# ==========================================================
# Game
# ==========================================================

START_MONEY = 5000

PASS_START_REWARD = 1000

MOVE_SPEED = 0.15

# ==========================================================
# Colors
# ==========================================================

BACKGROUND = (235, 229, 212)

WHITE = (255, 255, 255)

BLACK = (35, 35, 35)

GRAY = (130, 130, 130)

LIGHT_GRAY = (220, 220, 220)

RED = (235, 90, 90)

BLUE = (70, 150, 255)

GREEN = (90, 200, 120)

YELLOW = (255, 215, 90)

ORANGE = (255, 180, 90)

PURPLE = (205, 155, 255)

CYAN = (170, 240, 255)

BORDER = (70, 70, 70)

# ==========================================================
# Tile Colors
# ==========================================================

TILE_COLORS = {

    "START": (255,220,80),

    "LAND": (215,245,215),

    "SHOP": (170,220,255),

    "BANK": (255,235,180),

    "EVENT": (255,180,180),

    "HOSPITAL": (255,210,255),

    "REST": (220,220,255),

    "FREE": (210,255,255),

    "JAIL": (180,180,180)

}