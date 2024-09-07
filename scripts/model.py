from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from queue import Queue
import random

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"

@dataclass
class RegularCard:
    color: Color
    number: int

class Deck:
    def __init__(self):
        self.cards: Queue[RegularCard] = self.generate_deck()
    
    def generate_deck(self) -> Queue[RegularCard]:
        cards_list = []
        deck = Queue()
        for color in Color:
            cards_list.append(RegularCard(color=color, number=0))
            for i in range(1,10):
                for _ in range(2):  # forgive me for the forception
                    cards_list.append(RegularCard(color=color, number=i))
        random.shuffle(cards_list)
        for el in cards_list:
            deck.put(el)
    
    def get_card(self) -> RegularCard:
        return self.cards.get()
    
    def put_card(self, card: RegularCard) -> None:
        self.cards.put(card)

class DiscardPile:
    def __init__(self):
        self.last_card: RegularCard = None
    
    def check_legal(self, new_card: RegularCard) -> bool:
        return (
            self.last_card.color == new_card.color or
            self.last_card.number == new_card.number
        )
    
    def place_card(self, new_card: RegularCard) -> None:
        if self.check_legal(new_card=new_card):
            self.last_card = new_card
        else:
            print("Illegal play")

    def place_init_card(self, card: RegularCard) -> None:
        self.last_card = card