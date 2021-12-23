import math

class Shovel:
    def __init__(self, type, tiers, baseSPD):
        self.type = type
        SPD = int(baseSPD)
        self.tierList = []
        for x in range(0, int(tiers)):
            self.tierList.append(SPD)
            SPD = math.ceil(SPD*1.25)