### GLOBAL
selectedItem = 0
selectedMaterial = 0
isCompatable = False

### CLASS
##### BASE
class BaseItem:
    def __init__(self, name, weight, craftTime, complexity):
        self.name = name                #   name of specific item
        self.weight = weight            #   weight in lbs per item
        self.craftTime = craftTime      #   time in hours per item
        self.complexity = complexity    #   complexity in silver paid per hour
        pass

class BaseMaterial:
    def __init__(self, name, cost, materialbonus, note):
        self.name = name                #   name of specific item
        self.cost = cost                #   silver per lb of material
        self.materialbonus = materialbonus  #   int
        self.note = note                #   str
        pass

##### ITEMS
class TypeArmor(BaseItem):
    def __init__(self, name, weight, craftTime, complexity, armorclass, armortype, strengthreq, stealthbonus):
        super().__init__(name, weight, craftTime, complexity)
        self.armorclass = armorclass    # str
        self.armortype = armortype      # str
        self.strengthreq = strengthreq  # int
        self.stealthbonus = stealthbonus    # str
        pass

class TypeMelee(BaseItem):
    def __init__(self, name, weight, craftTime, complexity, wepdamage, wepstat):
        super().__init__(name, weight, craftTime, complexity)
        self.wepdamage = wepdamage      # "xdy"
        self.wepstat = wepstat          # STR/DEX
        pass

class TypeRange(BaseItem):
    def __init__(self, name, weight, craftTime, complexity, wepdamage, ammunition, firearm=False):
        super().__init__(name, weight, craftTime, complexity)
        self.wepdamage = wepdamage      # "xdy"
        self.ammunition = ammunition    # str
        self.firearm = firearm          # bol
        pass

class TypeCasting(BaseItem):
    def __init__(self, name, weight, craftTime, complexity, knownspells, charges=0):
        super().__init__(name, weight, craftTime, complexity)
        self.knownspells = knownspells  # str
        self.charges = charges          # int
        pass

class TypeTools(BaseItem):
    def __init__(self, name, weight, craftTime, complexity, charges=0):
        super().__init__(name, weight, craftTime, complexity)
        self.charges = charges          # int
        pass

class TypeProduct(BaseItem):
    def __init__(self, name, weight, craftTime, complexity, use, charges=0):
        super().__init__(name, weight, craftTime, complexity)
        self.use = use                  # str
        self.charges = charges          # int
        pass


### LOCAL DEF
##### HARDWRITE BASE ITEMS
## ARMOR
light = "LIGHT"
medium = "MEDIUM"
heavy = "HEAVY"
LeatherArmor = TypeArmor("Underarmor", 10, 12, 11, "11+DEX", light, 2, "0")
StuddedLeather = TypeArmor("Studded", 13, 18, 11, "12+DEX", light, 5, "0")
HideArmor = TypeArmor("Hide Armor", 12, 16, 11, "12+DEX(2)", medium, 5, "0")
ChainShirt = TypeArmor("Chain Shirt", 20, 16, 14, "13+DEX(2)", medium, 8, "-2")
ScaleArmor = TypeArmor("Scalemail", 45, 24, 14, "14+DEX(2)", medium, 11, "D")
PlateShirt = TypeArmor("Breastplate", 20, 16, 14, "14+DEX(2)", medium, 11, "0")
HalfPlateArmor = TypeArmor("Halfplate", 40, 24, 14, "15+DEX(2)", medium, 13, "D")
RingArmor = TypeArmor("Ringmail", 40, 36, 14, "14", heavy, 11, "D")
ChainArmor = TypeArmor("Chain Armor", 55, 24, 14, "16", heavy, 13, "D")
SplintArmor = TypeArmor("Splintmail", 60, 40, 14, "17", heavy, 15, "D")
PlateArmor = TypeArmor("Platemail", 65, 48, 14, "18", heavy, 15, "D")
Shield = TypeArmor("Shield", 6, 8, 14, "+2", medium, 11, "D")
ScoutSuit = TypeArmor("Scout Armor", 16, 12, 20, "16+DEX", light, 8, "+2")
CombatSuit = TypeArmor("Combat Armor", 24, 18, 20, "18+DEX", light, 11, "0")
TankPlate = TypeArmor("Tank Plate", 100, 48, 26, "19, DR1")
PowerPlate = TypeArmor("Power Plate", 120, 60, 26, "21 DR3", "POWER", 15, "D")
HazSuit = TypeArmor("PSUPI", 16, 36, 14, "9+DEX(2)", medium, 11, "D")
## MELEE
SimpleClub = TypeMelee("Club", 2, 4, 11, "1d4", "+S/D")
BigClub = TypeMelee("Greatclub", 11, 6, 11, "1d8", "+STR")
Maul = TypeMelee("Maul", 18, 8, 11, "2d6", "+STR")
Dagger = TypeMelee("Dagger", 1, 8, 11, "1d4", "+S/D")
SmallAxe = TypeMelee("Handaxe", 2, 8, 11, "1d6", "+S/D")
BattleAxe = TypeMelee("Battle Axe", 6, 12, 14, "1d8", "+STR")
GreatAxe = TypeMelee("Great Axe", 12, 12, 14, "+STR")
Mace = TypeMelee("Mace", 4, 6, 11, "1d6", "+STR")
Staff = TypeMelee("Quarterstaff", 2, 4, 14, "1d6", "+STR")
Flail = TypeMelee("Flail", 3, 8, 14, "1d8", "+STR")
Spear = TypeMelee("Spear", 3, 6, 11, "1d6", "+STR")
Glaive = TypeMelee("Glaive", 10, 8, 14, "1d10", "+STR")
Halberd = TypeMelee("Halberd", 7, 12, 14, "1d10", "+STR")
Lance = TypeMelee("Lance", 12, 12, 11, "1d12", "+STR")
Pike = TypeMelee("Pike", 18, 16, 16, "1d10", "+STR")
Greatsword = TypeMelee("Greatsword", 8, 12, 11, "2d6", "+STR")
Longsword = TypeMelee("Longsword", 4, 8, 11, "1d8", "+STR")
Rapier = TypeMelee("Rapier", 2, 8, 14, "1d8", "+S/D")
Scimitar = TypeMelee("Scimitar", 3, 6, 11, "1d6", "+S/D")
Shortsword = TypeMelee("Shortsword", 2, 6, 11, "1d6", "+S/D")
Warhammer = TypeMelee("Warhammer", 6, 16, 14, "1d8", "+STR")
WarPick = TypeMelee("Warpick", 3, 8, 11, "1d8", "+STR")
## RANGED & FIREARM
LightCrossbow = TypeRange()
Shortbow = TypeRange()
Longbow = TypeRange()
HeavyCrossbow = TypeRange()
HandCrossbow = TypeRange()
LightSling = TypeRange()
FPHandgun = TypeRange()
FPScatter = TypeRange()
FPLonggun = TypeRange()
FPRotator = TypeRange()
FPCarbine = TypeRange()
DRMHandgun = TypeRange()
DRMScatter = TypeRange()
DRMLonggun = TypeRange()
DRMRotator = TypeRange()
DRMCarbine = TypeRange()
## CASTING
Wand = TypeCasting()
Rod = TypeCasting()
Orb = TypeCasting()
Icon = TypeCasting()
Charm = TypeCasting()
## TOOL
RopeOrChain = TypeTools()
Hook = TypeTools()
HandHammer = TypeTools()
Lock = TypeTools()
Handcuff = TypeTools()
PickTool = TypeTools()
Pole = TypeTools()
HandRam = TypeTools()
Shovel = TypeTools()
Hook = TypeTools()
SledgeHammer = TypeTools()
Caltrops = TypeTools()
ClimberKit = TypeTools()
Crowbar = TypeTools()
BearTrap = TypeTools()
Backpack = TypeTools()
## PRODUCT
##### HARDWRITE BASE MATERIALS
## TEXTILE
## METAL
## GEM
## FLORA
## FAUNA
    

def TellItemCategories():
    print("(A)rmors, (M)elee, (R)ange, (C)asting, (F)irearms, (T)ools, Alchemical (P)roducts")
    answer = input()
    match answer:
        case "a":
            pass
        case "m":
            pass
        case "r":
            pass
        case "c":
            pass
        case "f":
            pass
        case "t":
            pass
        case "p":
            pass
        case _:
            pass
    
    pass

def TellMaterialCategories():
    print("(T)extiles, (M)etalics, (G)emstones, Fl(o)ra, Fa(u)na")
    answer = input()
    match answer:
        case "t":
            pass
        case "m":
            pass
        case "g":
            pass
        case "o":
            pass
        case "u":
            pass
        case _:
            pass
    pass

def Start():
    print("Looking at (I)tems or (M)aterials?")
    answer = input()
    match answer:
        case "i":
            TellItemCategories()
            pass
        case "m":
            TellMaterialCategories()
            pass

### MAIN

def main():
    Start()
    pass

if __name__ == "__main__":
    main()