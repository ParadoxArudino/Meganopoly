from .card import Card
from random import randint

class Luck(Card):
    def __init__(self, ID, type):
        super().__init__(ID, "luck")
        self.type = type