import pygame

from settings import *
from core.layout import Layout


class Player:

    def __init__(self, player_id, name, color):

        self.layout = Layout()

        self.id = player_id

        self.name = name

        self.color = color

        self.money = START_MONEY

        self.position = 0

        self.lands = []

        # ========= 動畫 =========

        self.moving = False

        self.steps_left = 0

        self.timer = 0

        self.total_tiles = 0

        # ========= Sprite(預留) =========

        self.image = None

    # ==================================================

    def start_move(

        self,

        steps,

        total_tiles

    ):

        if self.moving:

            return

        self.steps_left = steps

        self.total_tiles = total_tiles

        self.timer = 0

        self.moving = True

    # ==================================================

    def update(self, dt):

        if not self.moving:

            return False

        self.timer += dt

        if self.timer >= MOVE_SPEED:

            self.timer = 0

            old = self.position

            self.position = (

                self.position + 1

            ) % self.total_tiles

            # 經過起點

            if self.position < old:

                self.money += PASS_START_REWARD

            self.steps_left -= 1

            if self.steps_left <= 0:

                self.moving = False

                return True

        return False

    # ==================================================

    def draw(

        self,

        screen,

        board

    ):

        tile = board.tiles[self.position]

        cx = tile.x + self.layout.tile_size // 2

        cy = tile.y + self.layout.tile_size // 2

        radius = max(12, self.layout.tile_size // 4)

        # ===== 若之後有 PNG =====

        if self.image:

            rect = self.image.get_rect(center=(cx, cy))
            screen.blit(self.image, rect)
            return

        # ===== 暫時使用圓形 =====

        pygame.draw.circle(

            screen,

            self.color,

            (cx, cy),

            radius

        )

        pygame.draw.circle(

            screen,

            WHITE,

            (cx, cy),

            radius,

            2

        )

        font = pygame.font.SysFont(

            "Microsoft JhengHei",

            16,

            bold=True

        )

        text = font.render(

            self.name[0],

            True,

            WHITE

        )

        rect = text.get_rect(

            center=(cx, cy)

        )

        screen.blit(text, rect)

    # ==================================================

    def add_land(self, tile):

        if tile not in self.lands:

            self.lands.append(tile)

    # ==================================================

    def pay(self, amount):

        self.money -= amount

        return self.money >= 0

    # ==================================================

    def earn(self, amount):

        self.money += amount

    # ==================================================

    def is_bankrupt(self):

        return self.money < 0

    # ==================================================

    def reset(self):

        self.money = START_MONEY

        self.position = 0

        self.lands.clear()

        self.steps_left = 0

        self.timer = 0

        self.moving = False