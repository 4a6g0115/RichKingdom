import random
import pygame

from settings import *
from core.layout import Layout


class Dice:

    def __init__(self):

        self.layout = Layout()

        self.value = 1

        self.rolling = False

        self.timer = 0.0

        self.roll_time = 0.8

        self.interval = 0.06

        self.frame_timer = 0.0

        self.result = None

        self.images = {}

    # =====================================================

    def load_images(self, assets):

        for i in range(1, 7):

            img = assets.image(f"dice{i}")

            if img:

                img = pygame.transform.smoothscale(

                    img,

                    (

                        self.layout.dice_size,

                        self.layout.dice_size

                    )

                )

            self.images[i] = img

    # =====================================================

    def roll(self):

        if self.rolling:

            return

        self.rolling = True

        self.timer = 0

        self.frame_timer = 0

        self.result = None

    # =====================================================

    def update(self, dt):

        if not self.rolling:

            return None

        self.timer += dt

        self.frame_timer += dt

        if self.frame_timer >= self.interval:

            self.frame_timer = 0

            self.value = random.randint(1, 6)

        if self.timer >= self.roll_time:

            self.rolling = False

            self.result = random.randint(1, 6)

            self.value = self.result

            return self.result

        return None

    # =====================================================

    def draw(self, screen, font):

        x = self.layout.dice_x
        y = self.layout.dice_y
        s = self.layout.dice_size

        pygame.draw.rect(

            screen,

            WHITE,

            (

                x,

                y,

                s,

                s

            ),

            border_radius=12

        )

        pygame.draw.rect(

            screen,

            BORDER,

            (

                x,

                y,

                s,

                s

            ),

            2,

            border_radius=12

        )

        # ---------- PNG ----------

        img = self.images.get(self.value)

        if img:

            screen.blit(img, (x, y))

            return

        # ---------- 沒圖片時 ----------

        text = font.render(

            str(self.value),

            True,

            BLACK

        )

        rect = text.get_rect(

            center=(

                x + s // 2,

                y + s // 2

            )

        )

        screen.blit(text, rect)

    # =====================================================

    def get_value(self):

        return self.value

    # =====================================================

    def is_rolling(self):

        return self.rolling

    # =====================================================

    def reset(self):

        self.value = 1

        self.rolling = False

        self.timer = 0

        self.frame_timer = 0

        self.result = None