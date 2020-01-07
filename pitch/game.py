from pitch.cards import Decks
from pitch.player import Players


class Game(Players, Decks):

    deck = Decks(number_of_decks=1).decks
    players = Players(number_of_players=4)

    def deal(self):
        for player in self.players:
            while len(player.hand) < 9:
                player.hand.append(self.deck.pop(0))
