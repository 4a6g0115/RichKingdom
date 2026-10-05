import json
import pygame

from settings import *
from core.tile import Tile
from core.layout import Layout


class Board:

    def __init__(self):

        self.layout = Layout()

        self.tiles = []

        self.path = []

        self.load_map()

    # =========================================================

    def load_map(self):

        with open(
            "data/map.json",
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        self.tiles.clear()

        for item in data:

            tile = Tile(

                id=item["id"],

                name=item["name"],

                type=item["type"],

                price=item.get("price", 0),

                rent=item.get("rent", 0)

            )

            self.tiles.append(tile)

        self.build_positions()

    # =========================================================

    def build_positions(self):

        self.path.clear()

        LEFT = self.layout.board_left
        TOP = self.layout.board_top
        SIZE = self.layout.tile_size

        # 上方
        for i in range(8):

            self.path.append(

                (

                    LEFT + i * SIZE,

                    TOP

                )

            )

        # 右方
        for i in range(1, 7):

            self.path.append(

                (

                    LEFT + 7 * SIZE,

                    TOP + i * SIZE

                )

            )

        # 下方
        for i in range(7, -1, -1):

            self.path.append(

                (

                    LEFT + i * SIZE,

                    TOP + 7 * SIZE

                )

            )

        # 左方
        for i in range(6, 0, -1):

            self.path.append(

                (

                    LEFT,

                    TOP + i * SIZE

                )

            )

        for tile, pos in zip(self.tiles, self.path):

            tile.x = pos[0]

            tile.y = pos[1]

    # =========================================================

    def draw(self, screen, font):

        for tile in self.tiles:

            rect = pygame.Rect(

                tile.x,

                tile.y,

                self.layout.tile_size - 4,

                self.layout.tile_size - 4

            )

            color = TILE_COLORS.get(

                tile.type,

                WHITE

            )

            pygame.draw.rect(

                screen,

                color,

                rect,

                border_radius=8

            )

            pygame.draw.rect(

                screen,

                BORDER,

                rect,

                2,

                border_radius=8

            )

            # -------- 土地名稱 --------

            text = font.render(

                tile.name,

                True,

                BLACK

            )

            text_rect = text.get_rect(

                center=(

                    tile.x + self.layout.tile_size // 2 - 2,

                    tile.y + self.layout.tile_size // 2 - 10

                )

            )

            screen.blit(

                text,

                text_rect

            )

            # -------- 價格 --------

            if tile.price > 0:

                price = font.render(

                    f"${tile.price}",

                    True,

                    GRAY

                )

                price_rect = price.get_rect(

                    center=(

                        tile.x + self.layout.tile_size // 2 - 2,

                        tile.y + self.layout.tile_size - 18

                    )

                )

                screen.blit(

                    price,

                    price_rect

                )

            # -------- 地主 --------

            if tile.owner != -1:

                owner_color = BLUE if tile.owner == 0 else RED

                pygame.draw.circle(

                    screen,

                    owner_color,

                    (

                        tile.x +

                        self.layout.tile_size - 14,

                        tile.y + 14

                    ),

                    6

                )

    # =========================================================

    def get_tile(self, index):

        return self.tiles[index]

    # =========================================================

    def tile_count(self):

        return len(self.tiles)

    # =========================================================

    def draw_path(self, screen):

        for x, y in self.path:

            pygame.draw.circle(

                screen,

                (180, 180, 180),

                (

                    x +

                    self.layout.tile_size // 2,

                    y +

                    self.layout.tile_size // 2

                ),

                2

            )