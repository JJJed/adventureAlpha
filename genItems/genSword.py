import math

class Sword:
    def __init__(self, type, tiers, baseDMG):
        self.type = type
        DMG = int(baseDMG)
        self.tierList = []
        for x in range(0, int(tiers)):
            self.tierList.append(DMG)
            DMG = math.ceil(DMG*1.25)