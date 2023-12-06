from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for _ in range(2):
            card = Card('JOKER', 'JOKER')
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    print(f"len(j): {len(j)}")
    
    for _ in range(5):
        print(j.draw())
    print(j)
    print(len(j))
