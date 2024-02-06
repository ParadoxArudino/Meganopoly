from os import path
from .card import card


class Property(card):
    def __init__(self, ID, title, propertyBand, faceValue, baseRent):
        super().__init__(ID, "property", path.join("assets", "cards", "Property_cards", "{}.png".format(ID)))

        self.title = title
        self.propertyBand = propertyBand
        self.faceValue = faceValue
        self.buildingLevel = 0

        self.rents = [baseRent, baseRent * 2, baseRent * 3.5, baseRent * 5, baseRent * 7.5, baseRent * 10]

        if self.propertyBand == 1 or 2:
            self.housePrice = 500
        elif self.propertyBand == 3 or 4:
            self.housePrice = 1000
        elif self.propertyBand == 5 or 6:
            self.housePrice = 1500
        elif self.propertyBand == 7 or 8:
            self.housePrice = 2000
        elif self.propertyBand == 9 or 10:
            self.housePrice = 4000
        elif self.propertyBand == 11 or 12:
            self.housePrice = 7500

        
