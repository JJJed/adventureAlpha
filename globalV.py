import numpy as np
import mysql.connector

global db
db = mysql.connector.connect(
    host="localhost",
    user="jeddevne_jed",
    passwd="josh",
    database="jeddevne_advGameSQL"
)

from genItems.genSword import Sword
from genItems.genBow import Bow
from genItems.genPickaxe import Pickaxe
from genItems.genAxe import Axe
from genItems.genShovel import Shovel
from genItems.genArmorSet import ArmorSet
from genItems.genHeal import Heal
from genItems.genBooster import Booster

global users
users = []

global topScores
topScores = []

global swords
global bows
global pickaxes
global axes
global shovels
global armorSets
global heals
global boosters

swords = np.array([
    ["Wooden Sword", 3, 5],
    ["Stone Sword", 3, 10],
    ["Iron Sword", 5, 20],
    ["Diamond Sword", 10, 50],
    ["Magical Sword", 4, 80]
])

bows = np.array([
    ["Basic Bow", 3, 5],
    ["Advanced Bow", 3, 15],
    ["Expert's Bow", 5, 30],
    ["Master's Bow", 5, 50],
    ["Mythical Bow", 2, 150]
])

pickaxes = np.array([
    ["Wooden Pickaxe", 1, 1],
    ["Stone Pickaxe", 2, 2],
    ["Iron Pickaxe", 3, 3],
    ["Diamond Pickaxe", 5, 5],
    ["Legendary Pickaxe", 2, 10]
])

axes = np.array([
    ["Wooden Axe", 1, 1],
    ["Stone Axe", 2, 2],
    ["Iron Axe", 3, 3],
    ["Diamond Axe", 5, 5],
    ["Legendary Axe", 2, 10]
])

shovels = np.array([
    ["Wooden Shovel", 1, 1],
    ["Stone Shovel", 2, 2],
    ["Iron Shovel", 3, 3],
    ["Diamond Shovel", 5, 5],
    ["Legendary Shovel", 2, 10]
])

armorSets = np.array([
    ["Basic Armor", 3, 1],
    ["Advanced Armor", 3, 3],
    ["Iron Armor", 5, 5],
    ["Diamond Armor", 5, 10],
    ["Expert’s Armor", 4, 15],
    ["Master’s Armor", 4, 25],
    ["Legend’s Armor", 6, 50]
])

heals = np.array([
    ["Bandage", 1, 25],
    ["First Aid Kit", 1, 75],
    ["First Aid Kit+", 1, 100]
])

boosters = np.array([
    ["HP Boost", 5, 10]
])

swords0 = []
for x in range(0, len(swords)):
    sword = swords[x]
    swords0.append(Sword(sword[0], sword[1], sword[2]))

bows0 = []
for x in range(0, len(bows)):
    bow = bows[x]
    bows0.append(Bow(bow[0], bow[1], bow[2]))

pickaxes0 = []
for x in range(0, len(pickaxes)):
    pickaxe = pickaxes[x]
    pickaxes0.append(Pickaxe(pickaxe[0], pickaxe[1], pickaxe[2]))

axes0 = []
for x in range(0, len(axes)):
    axe = axes[x]
    axes0.append(Axe(axe[0], axe[1], axe[2]))

shovels0 = []
for x in range(0, len(shovels)):
    shovel = shovels[x]
    shovels0.append(Shovel(shovel[0], shovel[1], shovel[2]))

armorSets0 = []
for x in range(0, len(armorSets)):
    armorSet = armorSets[x]
    armorSets0.append(ArmorSet(armorSet[0], armorSet[1], armorSet[2]))

heals0 = []
for x in range(0, len(heals)):
    heal = heals[x]
    heals0.append(Heal(heal[0], heal[1], heal[2]))

boosters0 = []
for x in range(0, len(boosters)):
    booster = boosters[x]
    boosters0.append(Booster(booster[0], booster[1], booster[2]))

global items
items = [swords0, bows0, pickaxes0, axes0, shovels0, armorSets0, heals0, boosters0]

# for itemType in items:
#     for itemMat in itemType:
#         print(itemMat)

global treeSize
treeSize = 0;