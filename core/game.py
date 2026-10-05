import pygame
import random

from settings import *

from core.board import Board
from core.player import Player
from core.dice import Dice
from core.ui import UI
from core.assets import Assets


class Game:

    def __init__(self, screen):

        self.screen = screen

        self.clock = pygame.time.Clock()

        # =============================
        # Assets
        # =============================

        self.assets = Assets()

        self.font = self.assets.font(22)
        self.big_font = self.assets.font(36)

        # =============================
        # Board
        # =============================

        self.board = Board()

        # =============================
        # Dice
        # =============================

        self.dice = Dice()
        self.dice.load_images(self.assets)

        # =============================
        # UI
        # =============================

        self.ui = UI()

        # =============================
        # Players
        # =============================

        self.players = [

            Player(
                0,
                "玩家",
                BLUE
            ),

            Player(
                1,
                "AI",
                RED
            )

        ]

        # 告知玩家棋盤總格數

        total = self.board.tile_count()

        for p in self.players:

            p.total_tiles = total

        # =============================
        # Game State
        # =============================

        self.current_player = 0

        self.message = "按 SPACE 開始遊戲"

        self.waiting_roll = True

        self.running = True

        self.ai_delay = 0

    # =====================================================

    def current(self):

        return self.players[self.current_player]

    # =====================================================

    def next_turn(self):

        self.current_player += 1

        if self.current_player >= len(self.players):

            self.current_player = 0

        self.waiting_roll = True

        self.message = (

            f"{self.current().name} 的回合"

        )

    # =====================================================

    def start_roll(self):

        if self.dice.is_rolling():

            return

        if not self.waiting_roll:

            return

        self.waiting_roll = False

        self.dice.roll()

        self.message = "骰子滾動中..."

    # =====================================================

    def update(self):

        dt = self.clock.tick(FPS) / 1000

        # ------------------------
        # Dice Animation
        # ------------------------

        result = self.dice.update(dt)

        if result is not None:

            self.current().start_move(

                result,

                self.board.tile_count()

            )

            self.message = (

                f"{self.current().name} 擲出了 {result}"

            )

        # ------------------------
        # Player Move
        # ------------------------

        player = self.current()

        arrive = player.update(dt)

        if arrive:

            tile = self.board.get_tile(

                player.position

            )

            self.on_player_arrive(

                player,

                tile

            )

        # ------------------------
        # AI
        # ------------------------

        if (

            self.current_player == 1

            and

            self.waiting_roll

        ):

            self.ai_delay += dt

            if self.ai_delay >= 1.0:

                self.ai_delay = 0

                self.start_roll()

    # =====================================================

    def on_player_arrive(

        self,

        player,

        tile

    ):

        self.message = (

            f"{player.name} 到達 {tile.name}"

        )

        # START

        if tile.type == "START":

            self.next_turn()

            return

        # LAND

        if tile.type == "LAND":

            self.handle_land(

                player,

                tile

            )

            return

        # EVENT

        if tile.type == "EVENT":

            reward = random.randint(

                300,

                1200

            )

            player.earn(reward)

            self.message = (

                f"{player.name} 獲得 ${reward}"

            )

            self.next_turn()

            return

        # BANK

        if tile.type == "BANK":

            reward = 500

            player.earn(reward)

            self.message = (

                f"銀行利息 +${reward}"

            )

            self.next_turn()

            return

        # SHOP

        if tile.type == "SHOP":

            cost = 300

            player.pay(cost)

            self.message = (

                f"商店消費 ${cost}"

            )

            self.next_turn()

            return

        # Others

        self.next_turn()

        # =====================================================

    def handle_land(

        self,

        player,

        tile

    ):

        # ---------- 尚未購買 ----------

        if tile.owner == -1:

            if player.money >= tile.price:

                player.pay(tile.price)

                player.add_land(tile)

                tile.owner = player.id

                self.message = (

                    f"{player.name} 購買了 {tile.name}"

                )

            else:

                self.message = (

                    f"{player.name} 金額不足"

                )

            self.next_turn()

            return

        # ---------- 自己的土地 ----------

        if tile.owner == player.id:

            self.message = (

                f"{player.name} 回到自己的土地"

            )

            self.next_turn()

            return

        # ---------- 收租 ----------

        owner = self.players[tile.owner]

        rent = tile.rent

        player.pay(rent)

        owner.earn(rent)

        self.message = (

            f"{player.name} 支付 ${rent} 給 {owner.name}"

        )

        if player.is_bankrupt():

            self.message = (

                f"{player.name} 破產，遊戲結束"

            )

            self.running = False

            return

        self.next_turn()

    # =====================================================

    def draw(self):

        self.screen.fill(BACKGROUND)

        # ---------------- Board ----------------

        self.board.draw(

            self.screen,

            self.font

        )

        # ---------------- Players ----------------

        for player in self.players:

            player.draw(

                self.screen,

                self.board

            )

        # ---------------- Dice ----------------

        self.dice.draw(

            self.screen,

            self.big_font

        )

        # ---------------- UI ----------------

        self.ui.draw(

            self.screen,

            self.font,

            self.big_font,

            self.players,

            self.current_player,

            self.message

        )

        pygame.display.flip()

    # =====================================================

    def handle_event(

        self,

        event

    ):

        if event.type == pygame.QUIT:

            self.running = False

            return

        if event.type != pygame.KEYDOWN:

            return

        if event.key == pygame.K_ESCAPE:

            self.running = False

            return

        if event.key == pygame.K_SPACE:

            if self.current_player == 0:

                self.start_roll()

    # =====================================================

    def run(self):

        while self.running:

            for event in pygame.event.get():

                self.handle_event(event)

            self.update()

            self.draw()

        pygame.quit()
