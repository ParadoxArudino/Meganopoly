from .card import card

class Station(card):
    def __init__(self, ID, title):
        super().__init__(ID, "station")
        self.title = title
    
class Airport(card):
    def __init__(self, ID, title):
        super().__init__(ID, "airport")
        self.title = title