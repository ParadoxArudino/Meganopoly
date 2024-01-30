from os import path
from .card import Card

class ActionSpace(Card):
    def __init__(self, ID):
        super().__init__(ID, "actionSpace", path.join("Action_cards", "{}.png".format(ID)))