import itertools
import random


class DeckBase:

    def __init__(self):
        self.basic_deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))


class Decks(DeckBase):

    def __init__(self, number_of_decks=1, is_shuffled=True):
        super().__init__()
        decks_list = [self.basic_deck for _ in range(0, number_of_decks)]
        self.decks = list(itertools.chain(*decks_list))
        if is_shuffled:
            random.shuffle(self.decks)
