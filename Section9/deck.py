import random
from war_card_game import WarCardGame
from suit import Suit

class Deck:
    SUIT = ("clubs", "diamond", "hearts", "spades")
    def __init__(self, is_empty = False):
        self._cards = []
        if not is_empty:
            self.build()
    @property
    def size(self):
        return len(self._cards)
    def build(self):
        for suit in Deck.SUITS:
            for  value in range(2, 15):
                self._cards.append(Car)