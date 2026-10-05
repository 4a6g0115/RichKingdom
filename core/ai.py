import random


class AI:

    def __init__(self):

        self.buy_rate = 0.85

        self.upgrade_rate = 0.70

        self.safe_money = 1000

    # =====================================================

    def should_buy(

        self,

        player,

        tile

    ):

        if tile.owner != -1:

            return False

        if tile.price <= 0:

            return False

        if player.money - tile.price < self.safe_money:

            return False

        return random.random() <= self.buy_rate

    # =====================================================

    def should_upgrade(

        self,

        player,

        tile

    ):

        if tile.owner != player.id:

            return False

        if tile.level >= tile.max_level:

            return False

        cost = tile.price // 2

        if player.money - cost < self.safe_money:

            return False

        return random.random() <= self.upgrade_rate

    # =====================================================

    def buy(

        self,

        player,

        tile

    ):

        if not self.should_buy(player, tile):

            return False

        player.pay(tile.price)

        player.add_land(tile)

        tile.buy(player.id)

        return True

    # =====================================================

    def upgrade(

        self,

        player,

        tile

    ):

        if not self.should_upgrade(player, tile):

            return False

        cost = tile.price // 2

        player.pay(cost)

        tile.upgrade()

        return True

    # =====================================================

    def take_turn(

        self,

        player,

        tile

    ):

        result = {

            "buy": False,

            "upgrade": False

        }

        if tile.owner == -1:

            result["buy"] = self.buy(

                player,

                tile

            )

            return result

        if tile.owner == player.id:

            result["upgrade"] = self.upgrade(

                player,

                tile

            )

            return result

        return result

    # =====================================================

    def choose_card(

        self,

        cards

    ):

        if not cards:

            return None

        return random.choice(cards)

    # =====================================================

    def choose_target(

        self,

        players

    ):

        alive = [

            p

            for p in players

            if not p.is_bankrupt()

        ]

        if not alive:

            return None

        return random.choice(alive)

    # =====================================================

    def reset(self):

        pass