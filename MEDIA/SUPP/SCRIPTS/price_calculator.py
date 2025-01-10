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
    def __init__(self, name, cost):
        self.name = name                #   name of specific item
        self.cost = cost                #   silver per lb of material
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

##### MATERIALS
class TypeTextile(BaseMaterial):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class TypeMetalic(BaseMaterial):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class TypeGem(BaseMaterial):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class TypeFlora(BaseMaterial):
    def __init__(self, name, cost):
        super().__init__(name, cost)

class TypeFauna(BaseMaterial):
    def __init__(self, name, cost):
        super().__init__(name, cost)


### LOCAL DEF

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

def MakeBaseItems():
    pass

def MakeBaseMaterial():
    pass

def GenerateBases():
    MakeBaseItems()
    MakeBaseMaterial()

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
    GenerateBases()
    Start()
    pass

if __name__ == "__main__":
    main()