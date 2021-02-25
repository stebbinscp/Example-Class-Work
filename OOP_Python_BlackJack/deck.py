# Remember to use docstrings in your classes and functions!
import tkinter as tk
# suggested to use 1canvas.create_image(...)1
import random
from card import Card


class Deck:
    """
    Deck object with the following attributes: deck, used, cards.
    The cards attribute stores all 52 cards in a standard deck which are then shuffled
    Methods:
    The deal method pops the top card and adds it to the specified hand
    object, while adding that card to the used card pile. When 
    the size of the deck is 13 or lower, the used cards are 
    reshuffled back into the deck.
    Shuffle: method which randomly shuffles the given list
    Size: property which returns the size of the deck
    """
    def __init__(self):
        """ Build a deck of 52 cards """
        cards = ["2C", "2H", "2D", "2S", "3C", "3H", "3D", "3S", 
        "4C", "4H", "4D", "4S", "5C", "5H", "5D", "5S", 
        "6C", "6H", "6D", "6S", "7C", "7H", "7D", "7S",
        "8C", "8H", "8D", "8S", "9C", "9H", "9D", "9S",
        "10C", "10H", "10D", "10S", "AC", "AH", "AD", "AS",
        "KC", "KH", "KD", "KS", "QC", "QH", "QD", "QS", 
        "JC", "JH", "JD", "JS"]
        random.shuffle(cards)
        self.deck = cards
        self.used = []
        
    def deal(self):
        """Removes the top card on the deck and returns it. 
        If no more cards, shuffle"""
        top_card = self.deck.pop()
        self.used.append(top_card)
        if top_card in ["10S", "10H", "10D", "10C"]:
            if self.size == 13:
                self.shuffle()
            return Card(top_card[2], top_card[0:2])
        else:
            if self.size == 13:
                self.shuffle()
            return Card(top_card[1], top_card[0])

    @property
    def size(self):
        return len(self.deck)-1

    def shuffle(self):
        """Shuffle the used cards and add them to self.deck. """
        random.shuffle(self.used)
        for item in self.used:
            self.deck.append(item)
        self.used = []


# x = Deck()
# print(x.deal())
# x.deal()
# x.deal()
# print(x.deck)
# print(x.size)