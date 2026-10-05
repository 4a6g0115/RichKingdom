import os
import pygame


class Assets:

    def __init__(self):

        self.images = {}

        self.fonts = {}

        self.load_fonts()

        self.load_images()

    # =======================================================
    # Fonts
    # =======================================================

    def load_fonts(self):

        font_path = "assets/fonts/NotoSansTC-Regular.ttf"

        if os.path.exists(font_path):

            self.fonts[18] = pygame.font.Font(font_path, 18)
            self.fonts[22] = pygame.font.Font(font_path, 22)
            self.fonts[28] = pygame.font.Font(font_path, 28)
            self.fonts[36] = pygame.font.Font(font_path, 36)
            self.fonts[48] = pygame.font.Font(font_path, 48)

        else:

            self.fonts[18] = pygame.font.SysFont(
                "Microsoft JhengHei",
                18
            )

            self.fonts[22] = pygame.font.SysFont(
                "Microsoft JhengHei",
                22
            )

            self.fonts[28] = pygame.font.SysFont(
                "Microsoft JhengHei",
                28
            )

            self.fonts[36] = pygame.font.SysFont(
                "Microsoft JhengHei",
                36
            )

            self.fonts[48] = pygame.font.SysFont(
                "Microsoft JhengHei",
                48
            )

    # =======================================================
    # Images
    # =======================================================

    def load_images(self):

        folders = [

            "assets/images/board",

            "assets/images/ui",

            "assets/images/players",

            "assets/images/dice",

            "assets/images/icons",

            "assets/images/effects"

        ]

        for folder in folders:

            if not os.path.exists(folder):

                continue

            for file in os.listdir(folder):

                if not file.lower().endswith(".png"):

                    continue

                path = os.path.join(folder, file)

                key = os.path.splitext(file)[0]

                image = pygame.image.load(path).convert_alpha()

                self.images[key] = image

    # =======================================================
    # Font
    # =======================================================

    def font(self, size):

        return self.fonts[size]

    # =======================================================
    # Image
    # =======================================================

    def image(self, name):

        if name in self.images:

            return self.images[name]

        return None

    # =======================================================
    # Scale Image
    # =======================================================

    def image_scaled(

        self,

        name,

        width,

        height

    ):

        img = self.image(name)

        if img is None:

            return None

        return pygame.transform.smoothscale(

            img,

            (width, height)

        )

    # =======================================================
    # Draw Image
    # =======================================================

    def draw(

        self,

        screen,

        name,

        x,

        y

    ):

        img = self.image(name)

        if img:

            screen.blit(img, (x, y))

    # =======================================================
    # Draw Scale
    # =======================================================

    def draw_scaled(

        self,

        screen,

        name,

        x,

        y,

        w,

        h

    ):

        img = self.image_scaled(

            name,

            w,

            h

        )

        if img:

            screen.blit(img, (x, y))