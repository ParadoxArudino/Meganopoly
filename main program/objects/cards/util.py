from os import path
from .card import card

class Taxi(card):
    def __init__(self, ID):
        super().__init__(ID, "taxi", path.join("assets", "cards", "Util_cards", "Taxi.png"))
    
class Tax(card):
    def __init__(self, ID, Title):
        super().__init__(ID, "tax", path.join("assets", "cards", "Util_cards", "Tax.png"))
        self.Title = Title
        self.flippedPath = path.join("Util_cards", "Tax_{}.png".format(ID))

class Start(card):
    def __init__(self, ID):
        super().__init__(ID, "start", path.join("assets", "cards", "Util_cards", "{}_start.png".format(super.regionName)))
        self.wage = 5000
        

