### GLOBAL
selectedItem = 0
selectedMaterial = 0
isCompatable = False

### CLASS

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
    print("Textile, Mettalic, ")
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