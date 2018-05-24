'''
Problem: Design the data structures for a generic deck of cards. Describe how you would subclass
    them to implement blackjack
'''
from setup import Singleton
from enum import IntEnum


@Singleton
class Game:
    _DEFAULT_HAND_SIZE = 5

    def initialize(self, players=None, deck=None, hand_size=None):
        self.deck = deck
        self.deck.initialize()
        self.hand_size = hand_size or self._DEFAULT_HAND_SIZE
        self.players = []
        for player in players:
            p = Player(player)
            p.hand = self.deck.get_hand()
            self.players.append(p)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None
        self.score = None
        self.rank = None


class Card:
    def __init__(self, val, suite):
        self.val = val
        self.suite = suite


@Singleton
class Deck:
    def initialize(self, size=52, ace_high=True):
        if size % len(Suites):
            raise Exception('deck size must be divisible by the number of suites, %d' % len(Suites))
        self.size = size
        self.ace_high = ace_high
        self.cards = self.generate_cards()
        self.shuffle()

    def generate_cards(self):
        cards = []
        # generates all the cards that should be in the deck
        for suite in Suites:
            for i in xrange(self.size/len(Suites)):
                cards.append(Card(i, suite))

    def shuffle(self):
        # shuffles the deck
        pass


class Suites(IntEnum):
    hearts = 1
    diamonds = 2
    clubs = 3
    spaces = 4

    def __len__(self):
        return 4

game = Game.instance()
game.initialize(['joe'], Deck.instance())
