import math

class Booster:
    def __init__(self, type, tiers, baseBST):
        self.type = type
        BST = int(baseBST)
        self.tierList = []
        for x in range(0, int(tiers)):
            self.tierList.append(BST)
            BST = math.ceil(BST*1.25)