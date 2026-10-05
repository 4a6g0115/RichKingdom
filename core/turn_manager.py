class TurnManager:

    def __init__(self, player_count):

        self.player_count = player_count

        self.current = 0

        self.round = 1

    # =====================================================

    def current_player(self):

        return self.current

    # =====================================================

    def next(self):

        self.current += 1

        if self.current >= self.player_count:

            self.current = 0
            self.round += 1

        return self.current

    # =====================================================

    def previous(self):

        self.current -= 1

        if self.current < 0:

            self.current = self.player_count - 1

        return self.current

    # =====================================================

    def reset(self):

        self.current = 0
        self.round = 1

    # =====================================================

    def set_player_count(self, count):

        self.player_count = count

        if self.current >= count:

            self.current = 0

    # =====================================================

    def is_first_player(self):

        return self.current == 0

    # =====================================================

    def is_last_player(self):

        return self.current == self.player_count - 1

    # =====================================================

    def get_round(self):

        return self.round

    # =====================================================

    def __str__(self):

        return (
            f"Round {self.round} | "
            f"Current Player : {self.current}"
        )