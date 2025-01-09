### CLASS

### LOCAL DEF

def TellItemCategories():
    pass

def TellMaterialCategories():
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