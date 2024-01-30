from .card import card

class Taxi(card):
    def __init__(self, ID):
        super().__init__(ID, "taxi")
    
class Tax(card):
    def __init__(self, ID, Title, Cost):
        super().__init__(ID, "tax")
        self.Title = Title
        self.Cost = Cost

class Start(card):
    def __init__(self, ID):
        super().__init__(ID, "start")
        
