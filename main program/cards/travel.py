from os import path
from .card import card

class Transport(card):
    def __init__(self, ID, title):
        super().__init__(ID, "station", path.join("Travel_cards", "{}.png".format(ID)))
        self.title = title