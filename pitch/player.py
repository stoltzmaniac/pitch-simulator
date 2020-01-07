

class PlayerBase:

    def __init__(self, position=None, team=None):
        self.position = position
        self.team = team
        self.hand = []


class Players(PlayerBase):

    def __init__(self, number_of_players=4):
        if number_of_players % 2:
            raise Exception('Error: number of players must be even')
        super().__init__()
        self.players = [PlayerBase(position=i, team=i % 2) for i in range(0, number_of_players)]
