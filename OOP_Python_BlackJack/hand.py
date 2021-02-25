# Remember to use docstrings in your classes and functions!
import tkinter as tk
from card import Card


class Hand:
    """
    Object which holds a collection of card objects.
    reset: resets the hand to empty
    add: adds a card object
    draw: puts the card object on the tkinter canvas
    total: sums the value of the hand
    """
    def __init__(self):
        self.hand = []

    def reset(self):
        """Clears the collection of cards"""
        self.hand = []

    def add(self, card):
        """Takes in a card object and returns the deck with the
        added card."""
        self.hand.append(card)

    def draw(self, canvas, start_x, start_y, canvas_width, canvas_height):
        """Draws a hand of cards to the canvas at the specified x and y"""
        for card in self.hand:
            image = card.image
            canvas.create_image(start_x, start_y, image=image)
            start_x += 110

    @property
    def total(self):
        """Sum the hand object"""
        total = 0
        for card in self.hand:
            if card.value in ["K","Q","J"]:
                # print(card.value)
                total += 10
            elif card.value in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                total += int(card.value)
            else: total += 11
        return total
