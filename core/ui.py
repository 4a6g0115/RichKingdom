import pygame

from settings import *
from core.layout import Layout


class UI:

    def __init__(self):

        self.layout = Layout()

        self.right_panel = pygame.Rect(

            self.layout.panel_x,

            self.layout.panel_y,

            self.layout.panel_width,

            self.layout.panel_height

        )

        self.message_panel = pygame.Rect(

            self.layout.message_x,

            self.layout.message_y,

            self.layout.message_width,

            self.layout.message_height

        )

    # =========================================================

    def draw(

        self,

        screen,

        font,

        big_font,

        players,

        current,

        message

    ):

        self.draw_right_panel(

            screen,

            font,

            big_font,

            players,

            current

        )

        self.draw_message(

            screen,

            font,

            message

        )

    # =========================================================

    def draw_right_panel(

        self,

        screen,

        font,

        big_font,

        players,

        current

    ):

        pygame.draw.rect(

            screen,

            (245, 241, 226),

            self.right_panel,

            border_radius=12

        )

        pygame.draw.rect(

            screen,

            BORDER,

            self.right_panel,

            2,

            border_radius=12

        )

        title = big_font.render(

            "Rich Kingdom",

            True,

            BLACK

        )

        screen.blit(

            title,

            (

                self.layout.panel_x + 20,

                self.layout.panel_y + 20

            )

        )

        pygame.draw.line(

            screen,

            LIGHT_GRAY,

            (

                self.layout.panel_x + 15,

                self.layout.panel_y + 70

            ),

            (

                self.layout.panel_x +

                self.layout.panel_width - 15,

                self.layout.panel_y + 70

            ),

            2

        )

        y = self.layout.panel_y + 95

        for index, player in enumerate(players):

            pygame.draw.circle(

                screen,

                player.color,

                (

                    self.layout.panel_x + 28,

                    y + 15

                ),

                10

            )

            name = font.render(

                player.name,

                True,

                BLACK

            )

            money = font.render(

                f"金錢：${player.money}",

                True,

                BLACK

            )

            land = font.render(

                f"土地：{len(player.lands)}",

                True,

                BLACK

            )

            screen.blit(

                name,

                (

                    self.layout.panel_x + 50,

                    y

                )

            )

            screen.blit(

                money,

                (

                    self.layout.panel_x + 50,

                    y + 28

                )

            )

            screen.blit(

                land,

                (

                    self.layout.panel_x + 50,

                    y + 56

                )

            )

            if current == index:

                turn = font.render(

                    "◀ 目前回合",

                    True,

                    RED

                )

                screen.blit(

                    turn,

                    (

                        self.layout.panel_x + 180,

                        y

                    )

                )

            y += 110

        pygame.draw.line(

            screen,

            LIGHT_GRAY,

            (

                self.layout.panel_x + 15,

                self.layout.panel_y + 350

            ),

            (

                self.layout.panel_x +

                self.layout.panel_width - 15,

                self.layout.panel_y + 350

            ),

            2

        )

        op_title = font.render(

            "操作方式",

            True,

            BLACK

        )

        screen.blit(

            op_title,

            (

                self.layout.panel_x + 20,

                self.layout.panel_y + 365

            )

        )

        tips = [

            "SPACE  擲骰",

            "ESC      離開"

        ]

        yy = self.layout.panel_y + 405

        for tip in tips:

            img = font.render(

                tip,

                True,

                BLACK

            )

            screen.blit(

                img,

                (

                    self.layout.panel_x + 20,

                    yy

                )

            )

            yy += 35

    # =========================================================

    def draw_message(

        self,

        screen,

        font,

        message

    ):

        pygame.draw.rect(

            screen,

            (245, 241, 226),

            self.message_panel,

            border_radius=12

        )

        pygame.draw.rect(

            screen,

            BORDER,

            self.message_panel,

            2,

            border_radius=12

        )

        title = font.render(

            "遊戲訊息",

            True,

            BLACK

        )

        screen.blit(

            title,

            (

                self.layout.message_x + 20,

                self.layout.message_y + 12

            )

        )

        pygame.draw.line(

            screen,

            LIGHT_GRAY,

            (

                self.layout.message_x + 15,

                self.layout.message_y + 42

            ),

            (

                self.layout.message_x +

                self.layout.message_width - 15,

                self.layout.message_y + 42

            ),

            2

        )

        text = font.render(

            message,

            True,

            BLUE

        )

        screen.blit(

            text,

            (

                self.layout.message_x + 20,

                self.layout.message_y + 60

            )

        )