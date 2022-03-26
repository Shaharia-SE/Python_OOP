class WarCardGame:

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._player)
        self.make_deck(self._player)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)
