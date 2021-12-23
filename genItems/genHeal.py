import math

class Heal:
    def __init__(self, type, tiers, baseHP):
        self.type = type
        HP = int(baseHP)
        self.tierList = []
        for x in range(0, int(tiers)):
            self.tierList.append(HP)
            HP = math.ceil(HP*1.25)