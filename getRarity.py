from getValues import ParseAPI

class GetRarity(ParseAPI):
    def __init__(self, id):
        super(GetRarity, self).__init__(id=id)
    
    def calculateRarity(self):
        [res1, res2] = self.formatData()
        rarityPoints = []

        for x in res1:
            rarityPoints.append(1/(x/int(res2)))

        return sum(rarityPoints)

if __name__ == "__main__":
    pass

