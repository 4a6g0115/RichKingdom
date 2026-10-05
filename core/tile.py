from dataclasses import dataclass, field


@dataclass
class Tile:

    id: int
    name: str
    type: str

    price: int = 0
    rent: int = 0

    owner: int = -1

    level: int = 0

    x: int = 0
    y: int = 0

    houses: int = 0

    max_level: int = 5

    mortgage: bool = False

    # =====================================================

    def is_buyable(self):

        return (

            self.type == "LAND"

            and

            self.owner == -1

        )

    # =====================================================

    def buy(self, player_id):

        self.owner = player_id

        self.level = 1

    # =====================================================

    def can_upgrade(self):

        return (

            self.owner != -1

            and

            self.level < self.max_level

        )

    # =====================================================

    def upgrade(self):

        if self.can_upgrade():

            self.level += 1

            self.houses += 1

            self.rent = int(self.rent * 1.5)

    # =====================================================

    def reset(self):

        self.owner = -1

        self.level = 0

        self.houses = 0

        self.mortgage = False

    # =====================================================

    def owner_name(self, players):

        if self.owner == -1:

            return "無"

        return players[self.owner].name

    # =====================================================

    def __str__(self):

        return (

            f"{self.name} "

            f"({self.type}) "

            f"Price={self.price} "

            f"Rent={self.rent} "

            f"Owner={self.owner}"

        )