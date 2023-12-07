# from functools import total_ordering

# @total_ordering
class Card:  # inherits from 'object'
    VALID_SUITS = 'Clubs Diamonds Hearts Spades JOKER'.split()

    # NO member list here!
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):  # getter method
        return self._rank
    
    @property
    def rank(self):    # getter property
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if value in self.VALID_SUITS:
            self._suit = value
        else:
            raise ValueError("Invalid suit name")

    def __str__(self):
        return f"Card: {self.rank}-{self.suit}"

    def __repr__(self):  # representation of the code for the object
        return f"Card('{self.rank}', '{self.suit}')"

    # def __eq__(self, other):
    #     return (self.rank == other.rank) and (self.suit == other.suit)
    
    # def __gt__(self, other):
    #     return True

    def __hash__(self):
        return 4

if __name__ == "__main__":
    c1 = Card('3', 'Diamonds')
    print(c1.get_rank())
    print(c1.rank)  # 
    print(c1.suit) 
    c1.suit = 'Hearts'
    print(c1.suit)
    print(c1)
    c2 = Card('A', 'Spades')
    print(c2)
    print(repr(c1))
    print(repr(c2))