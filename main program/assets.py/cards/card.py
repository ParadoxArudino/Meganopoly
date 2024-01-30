

class Card:
    def __init__(self, ID, card_type):

        if len(ID) != 5:
            raise ValueError("ID must be 5 characters long")

        self.ID = ID
        self.space = int(ID[3:5])
        self.card_type = card_type

        if ID[:3] == "EDL":
            self.region = 1
            self.level = 1

        elif ID[:3] == "GLL":
            self.region = 2
            self.level = 1

        elif ID[:3] == "LEM":
            self.region = 3
            self.level = 2
        elif ID[:3] == "MAM":
            self.region = 4
            self.level = 2
        elif ID[:3] == "LIM":
            self.region = 5
            self.level = 2
        elif ID[:3] == "BIM":
            self.region = 6
            self.level = 2

        elif ID[:3] == "LOL":
            self.region = 7
            self.level = 3
        elif ID[:3] == "SCL":
            self.region = 8
            self.level = 3

        def get_region_name(self):
            if self.region == 1:
                return "Edinburgh"
            elif self.region == 2:
                return "Glasgow"
            elif self.region == 3:
                return "Leeds"
            elif self.region == 4:
                return "Manchester"
            elif self.region == 5:
                return "Liverpool"
            elif self.region == 6:
                return "Birmingham"
            elif self.region == 7:
                return "London"
            elif self.region == 8:
                return "South Coast"
            
    
            