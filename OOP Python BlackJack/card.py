# Remember to use docstrings in your classes and functions!

import tkinter as tk
from PIL import Image, ImageTk

class Card:
    """
    Object class which stors the suit and value of the given
    card, loads the images as a class method, and has two properties:
    size, and image.
    """
 
    CLUBS = "C"
    DIAMONDS = "D"
    HEARTS = "H"
    SPADES =  "S" 

    def __init__(self, suit, card):
        """Initiate the card class with a suit and value."""
        # self.suit = self.set_suit(suit)
        # self.value = self.set_value(value)
        self.suit = suit
        self.card = card

    @classmethod
    def load_images(self):
        """
        Load in images for every card into a class attribute self.card_images
        in tuples of (card name, tkinter photo object)
        """
        suits = ['H', 'C', 'D', 'S']
        face_cards = ['J', 'K', 'Q', "A", "10"]
        self.card_images = [] 
        # list with every card in a tuple (name, tkinker object)
        pre_file = r"/Users/Xtina/Documents/GitHub/homework-5-stebbinscp/blackjack/images"

        for suit in suits:
            for value in range(2, 10):
                card = '{}{}'.format(str(value), suit)
                card_name = "/"+card+".jpg"
                img = Image.open(pre_file+card_name)
                img = img.resize((100,150), Image.ANTIALIAS)
                image = ImageTk.PhotoImage(img)
                self.card_images.append((card, image))
            for card in face_cards:
                card = '{}{}'.format(str(card), suit)
                card_name = "/"+card+".jpg"
                img = Image.open(pre_file+card_name)
                img = img.resize((100,150), Image.ANTIALIAS)
                image = ImageTk.PhotoImage(img)
                self.card_images.append((card, image))

    @property
    def value(self):
        if self.card in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]:
            # print(self.card)
            return self.card
        else:
            # print(self.card) 
            raise ValueError("The inputted card value is not within specifications.")
        
    @property
    def image(self):
        if self.card == "10":
            key = str(self.card[0:2])+str(self.suit[0:1].upper())
        else:
            key = str(self.card[0:1])+str(self.suit[0:1].upper())
        for i in range(52):
            if self.card_images[i][0] == key:
                return self.card_images[i][1] # should return the object
