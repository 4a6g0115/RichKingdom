from settings import *


class Layout:

    def __init__(self):

        # ==========================
        # 棋盤
        # ==========================

        self.board_left = BOARD_LEFT
        self.board_top = BOARD_TOP
        self.board_size = BOARD_SIZE
        self.tile_size = TILE_SIZE

        # ==========================
        # 右側資訊
        # ==========================

        self.panel_x = RIGHT_PANEL_X
        self.panel_y = RIGHT_PANEL_Y

        self.panel_width = RIGHT_PANEL_WIDTH
        self.panel_height = RIGHT_PANEL_HEIGHT

        # ==========================
        # 訊息框
        # ==========================

        self.message_x = MESSAGE_X
        self.message_y = MESSAGE_Y

        self.message_width = MESSAGE_WIDTH
        self.message_height = MESSAGE_BOX_HEIGHT

        # ==========================
        # 骰子
        # ==========================

        self.dice_x = DICE_X
        self.dice_y = DICE_Y
        self.dice_size = DICE_SIZE

    # =====================================================

    @property
    def panel_rect(self):

        return (
            self.panel_x,
            self.panel_y,
            self.panel_width,
            self.panel_height
        )

    # =====================================================

    @property
    def message_rect(self):

        return (
            self.message_x,
            self.message_y,
            self.message_width,
            self.message_height
        )

    # =====================================================

    def tile_center(self, tile):

        return (

            tile.x + self.tile_size // 2,

            tile.y + self.tile_size // 2

        )

    # =====================================================

    def tile_rect(self, tile):

        margin = 4

        return (

            tile.x,

            tile.y,

            self.tile_size - margin,

            self.tile_size - margin

        )

    # =====================================================

    def player_radius(self):

        return max(12, self.tile_size // 4)

    # =====================================================

    def title_position(self):

        return (

            self.panel_x + 25,

            self.panel_y + 20

        )

    # =====================================================

    def player_info_position(self, index):

        base_y = self.panel_y + 90

        return (

            self.panel_x + 25,

            base_y + index * 110

        )

    # =====================================================

    def help_position(self):

        return (

            self.panel_x + 25,

            self.panel_y + 390

        )

    # =====================================================

    def dice_position(self):

        return (

            self.dice_x,

            self.dice_y

        )