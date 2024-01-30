from .card import Card
from random import randint
from os import path

class Luck(Card):
    def __init__(self, ID, type):

        if type == "Chance":
            self.type = "Chance"
            super().__init__(ID, "luck", path.join("Luck_cards", "Chance.png"))
            
        elif type == "Community Chest":
            self.type = "Community Chest"
            super().__init__(ID, "luck", path.join("Luck_cards", "Community.png"))

        else:
            raise Exception("Invalid type of luck card")

            