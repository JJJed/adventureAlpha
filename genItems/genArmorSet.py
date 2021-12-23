import math

class ArmorSet:
    def __init__(self, type, tiers, basePRT):
        self.type = type
        PRT = int(basePRT)
        self.tierList = []
        for x in range(0, int(tiers)):
            self.tierList.append(PRT)
            PRT = math.ceil(PRT*1.25)