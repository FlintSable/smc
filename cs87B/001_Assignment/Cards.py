#!/usr/bin/env python3
import random

class Card:
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Heats', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    # def __lt__(self, other):
    #     if self.suit < other.suit:
    #         return True
    #     if self.suit > other.suit:
    #         return False
    #     # suits are the same.. Check ranks
    #     return self.rank < other.rank

    # written more concisely
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(Card)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


def main():
    NewCard = Card()
    NewCard2 = Card(2, 11)
    NewDeck = Deck()
    print(NewCard)
    print(str(NewCard2))
    print(NewDeck)

if __name__ == "__main__":
    main()