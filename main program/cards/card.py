class Card:
    def __init__(self, ID, card_type, imageFile):

        if len(ID) != 5:
            raise ValueError("ID must be 5 characters long")

        self.ID = ID
        self.space = int(ID[3:5])
        self.card_type = card_type

        if ID[:3] == "EDL":
            self.region = 1
            self.regionName = "Edinburgh"
            self.level = 1

        elif ID[:3] == "GLL":
            self.region = 2
            self.regionName = "Glasgow"
            self.level = 1

        elif ID[:3] == "LEM":
            self.region = 3
            self.regionName = "Leeds"
            self.level = 2

        elif ID[:3] == "MAM":
            self.region = 4
            self.regionName = "Manchester"
            self.level = 2

        elif ID[:3] == "LIM":
            self.region = 5
            self.regionName = "Liverpool"
            self.level = 2

        elif ID[:3] == "BIM":
            self.region = 6
            self.regionName = "Birmingham"
            self.level = 2

        elif ID[:3] == "LOL":
            self.region = 7
            self.regionName = "London"
            self.level = 3

        elif ID[:3] == "SCL":
            self.region = 8
            self.regionName = "South Coast"
            self.level = 3

        self.imageFile = imageFile

        @property
        def get_region_name(self):
            return self.regionName

        @property    
        def getCardImg(self) -> str:
            return self.imageFile
            
    
            