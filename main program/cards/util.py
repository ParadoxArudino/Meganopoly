from os import path
from .card import card

class Taxi(card):
    def __init__(self, ID):
        super().__init__(ID, "taxi", path.join("Util_cards", "Taxi.png"))
    
class Tax(card):
    def __init__(self, ID, Title, Cost):
        super().__init__(ID, "tax", path.join("Util_cards", "Tax_{}.png".format(Cost)))
        self.Title = Title
        self.Cost = Cost

class Start(card):
    def __init__(self, ID):
        super().__init__(ID, "start", path.join("Util_cards", "{}_start.png".format(super.regionName)))
        
