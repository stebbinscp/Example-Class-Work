# Remember to use docstrings in your classes and functions!
from deck import Deck
from hand import Hand
from card import Card
import tkinter as tk
from abc import ABC, abstractmethod

class GameGUI(ABC):

    def __init__(self, window):
        self._window = window
        self._canvas_width = 1024
        self._canvas_height = 400
        self._canvas = tk.Canvas(window, width=self._canvas_width, height=self._canvas_height)
        self._canvas.pack()
        window.bind("<Key>", self._keyboard_event)

    def _keyboard_event(self, event):
        key = str(event.char)

        if key == 'h':
            self.player_hit()
        elif key == 's':
            self.player_stand()
        elif key == 'r':
            self.reset()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def player_hit(self):
        pass

    @abstractmethod
    def player_stand(self):
        pass


class BlackJack(GameGUI):
    """
    Game class which takes in the basic GameGUI class, and 
    runs a blackjack game with the following rules:
    Aces are always 11. 
    The dealer plays after the player.
    If the player is bust, the dealer wins.
    The player can hit (h) until they bust or stand (s).
    If the player stands, the player cannot hit again.
    Ties are awarded to neither the player nor the dealer.

    Reset: clears the board, uses the ssame deck to deal
    Start Game: Initiates a new board
    Player hit: gives the player an additional card. If
    the flag is set to false, continue hitting. If the player
    has busted, set the flag to True and the dealer to win.
    Player Stand: the player indicates they will not take more cards.
    Flag is set to True and the dealer begins the turn.
    Points are calculated and the winner is awarded.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deck = Deck()
        Card.load_images()
        self.player_wins = 0
        self.dealer_wins = 0

    def start_game(self):
        """
        Initiates a player and dealer hand, draws both cards, and
        sets the flag for hit or stand.
        """
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        for _ in range(2):
            self.player_hand.add(self.deck.deal())
            self.dealer_hand.add(self.deck.deal())
        self.status = self._canvas.create_text(800, 200, text = "GAME STATUS: Game in Progress")
        self.dealer_hand.draw(self._canvas, 100, 125, 1024, 600)
        self.player_hand.draw(self._canvas, 100, 325, 1024, 600)
        self.player_total = self._canvas.create_text(100, 220, text = f"Player Hand total: {self.player_hand.total}")
        self.dealer_total = self._canvas.create_text(100, 30, text = f"Dealer Hand total: {self.dealer_hand.total}")
        self.dealer_wins_canvas = self._canvas.create_text(900, 150, text = f"Dealer Wins: {self.dealer_wins}")
        self.player_wins_canvas = self._canvas.create_text(900, 100, text = f"Player Wins: {self.player_wins}")
        self.player_stood = False
        self.bust = False
        if self.player_hand.total > 21:
            self.start_game()
        if self.dealer_hand.total > 21:
            self.start_game()

    def player_hit(self):
        """
        Gives the player an additional card. If
        the flag is set to false, continue hitting. If the player
        has busted, set the flag to True and the dealer to win.
        """
        if self.player_stood is False:
            self.player_hand.add(self.deck.deal())
            self.player_hand.draw(self._canvas, 100, 325, 1024, 600)
            self._canvas.delete(self.player_total)
            self.player_total = self._canvas.create_text(100, 220, text = f"Player Hand total: {self.player_hand.total}")
            if self.player_hand.total > 21:
                self.bust = True
                self.player_stood = True
                self._canvas.delete(self.status)
                self.status = self._canvas.create_text(800, 200, text = "GAME STATUS: PLAYER BUSTED, DEALER WINS, press r to play again")
                self.dealer_wins += 1
                self._canvas.delete(self.dealer_wins_canvas)
                self.dealer_wins_canvas = self._canvas.create_text(900, 150, text = f"Dealer Wins: {self.dealer_wins}")

    def player_stand(self):
        """
        the player indicates they will not take more cards.
        Flag is set to True and the dealer begins the turn.
        Points are calculated and the winner is awarded.
        """
        if self.bust == False:
            self.player_stood = True
            while self.dealer_hand.total < 17:
                self.dealer_hand.add(self.deck.deal())
                self.dealer_hand.draw(self._canvas, 100, 125, 1024, 600)
                self._canvas.delete(self.dealer_total)    
                self.dealer_total = self._canvas.create_text(100, 30, text = f"Dealer Hand total: {self.dealer_hand.total}")
            if self.dealer_hand.total > 21:
                self._canvas.delete(self.status)
                self.status = self._canvas.create_text(800, 200, text = "GAME STATUS: DEALER BUSTED, PLAYER WINS. Press r to play again")
                self.player_wins += 1
                self._canvas.delete(self.player_wins_canvas)
                self.player_wins_canvas = self._canvas.create_text(900, 100, text = f"Player Wins: {self.player_wins}")
                self.bust = True
            else:
                if self.dealer_hand.total > self.player_hand.total:
                    self._canvas.delete(self.status)
                    self.status = self._canvas.create_text(800, 200, text = "GAME STATUS: Dealer wins. Press r to play again")
                    self.dealer_wins += 1
                    self._canvas.delete(self.dealer_wins_canvas)
                    self.dealer_wins_canvas = self._canvas.create_text(900, 150, text = f"Dealer Wins: {self.dealer_wins}")
                    self.bust = True
                elif self.dealer_hand.total == self.player_hand.total:
                    self._canvas.delete(self.status)
                    self.status = self._canvas.create_text(800, 200, text = "GAME STATUS: Tie game. Press r to play again")
                    self.bust = True
                else:
                    self._canvas.delete(self.status)
                    self.status = self._canvas.create_text(800, 200, text = "GAME STATUS: Player wins. Press r to play again")
                    self.player_wins += 1
                    self._canvas.delete(self.player_wins_canvas)
                    self.player_wins_canvas = self._canvas.create_text(900, 100, text = f"Player Wins: {self.player_wins}")
                    self.bust = True
    
    def reset(self):
        """
        Resets the board but not the score.
        """
        self._canvas.delete(tk.ALL)
        self.bust = False
        self.player_stood = False
        self.start_game()


def main():
    window = tk.Tk()
    window.title("Blackjack")
    game = BlackJack(window)
    game.start_game()
    window.mainloop()

if __name__ == "__main__":
    main()
