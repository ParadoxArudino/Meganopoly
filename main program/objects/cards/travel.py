from os import path
from .card import card

class Travel(card):
    def __init__(self, ID, title, type):
        super().__init__(ID, "station", path.join("assets", "cards", "Travel_cards", "{}.png".format(ID)))
        self.title = title

        if type == "Station":
            self.type = "Station"
        elif type == "Airport":
            self.type = "Airport"
        else:
            raise Exception("Invalid type of travel card")
        
        if self.type == "Station":
            if super.level == 1:
                self.faceValue = 2500
                self.rent = 500
                self.travelCost = 250

            elif super.level == 2:
                self.faceValue = 5000
                self.rent = 1000
                self.travelCost = 500
            
            elif super.level == 3:
                self.faceValue = 7500
                self.rent = 1500
                self.travelCost = 1000
        else:
            self.faceValue = 10000
            self.rent = 1500
            self.travelCost = 2500
