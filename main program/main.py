class card:
    def __init__(self,ID) -> None:
        self.ID = ID
    
    def getID(self):
        return self.ID

class property(card):
    def __init__(self, ID, value) -> None:
        super().__init__(ID)
        self.value = value
 
    def getValue(self):
        return self.value

card1 = property(input(),100)

print(card1.getID())
print(card1.getValue())

print("HI")