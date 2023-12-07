import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @classmethod
    def get_ranks(cls):
        return cls.RANKS


    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
    
    def __len__(self):
        return len(self._cards)
    
    def __str__(self):
        my_type = type(self) # get type of this object
        my_name = my_type.__name__  # name of class
        return f"{my_name}:{len(self)}"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__  # name of class
        return f"{my_name}()"
    
    #  == != gt lt ge le
    def __eq__(self, other):
        return set(self._cards) == set(other.cards)

    #   __gt__  __lt__ 

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"d1: {d1}")
    d1.shuffle()
    print(f"d1.cards: {d1.cards}")
    for _ in range(5):
        print(d1.draw())
    print(len(d1))
    print(d1)
    d3 = CardDeck()
    d2.shuffle()
    d3.shuffle()
    print(d1 == d2)
    print(d2 == d3)
