global speedOnHorse
global speedOnBoat
global speedOnFoot


def calculate():
    pass

def IntraCityCheck():
    print("Are you heading from one city to another (y/n)?")
    keypress = input()
    match keypress:
        case "y":
            pass
        case "n":
            pass
    pass

def IntraCityCalculate():
    pass

def HexCalculate():
    print("How many Hexes to calculate?")
    numToCalc = input()
    if numToCalc is str:
        numToCalc = int(numToCalc)
    else:
        HexCalculate()
    print("What is your method of travel?")
    print("(f - Foot/Cart, h - Horse, b - Boat)")
    methodOfTravel = input()
    match methodOfTravel:
        case "f":
            print("Are you travelling the Highways (y/n)?")
            highwayCheck = input()
            match highwayCheck:
                case "y":
                    daysOfTravel = numToCalc / 4
                    numCartPrice = daysOfTravel * 12
                    giveCartPrice = True
                case "n":
                    daysOfTravel = numToCalc / 3
                    giveCartPrice = False
        case "h":
            print("Are you travelling the Highways (y/n)?")
            highwayCheck = input()
            match highwayCheck:
                case "y":
                    daysOfTravel = numToCalc / 5
                case "n":
                    daysOfTravel = numToCalc / 4
        case "b":
            print("Are you heading downstream (y/n)?")
            downstreamCheck = input()
            match downstreamCheck:
                case "y":
                    daysOfTravel = numToCalc / 5
                case "n":
                    daysOfTravel = numToCalc / 3
            numBoatPrice = daysOfTravel * 20
    print(f"Your trip will take {daysOfTravel} days.")
    if giveCartPrice:
        print(f"A vic can be chartared at ~{numCartPrice}sp for the trip.")
        giveCartPrice = False
    main()

def main():
    IntraCityCheck()

if __name__ == "__main__":
    main()