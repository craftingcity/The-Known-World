cityTable = {
    "Castle Prosper": "",
    "Gambleum": "",
    "Janesland": "",
    "Magius": "",
    "Moonlight": "",
    "Yerba": "",
    "Amyl Dother": "",
    "Barkryn": "",
    "Beacon": "",
    "Boneborn": "",
    "Darnt Hillkeep": "",
    "Goldfield": "",
    "Lakeview": "",
    "Mossburg": "",
    "New Quillbuck": "",
    "Red Throne": "",
    "Zalfari": "",
    "Groundiki": "",
    "Kickoff": "",
    "Low Hornrock": "",
    "Mountain Hall": "",
    "Golden City": "",
    "Kohnstamm": "",
    "": "",
    "": "",
    "": "",
    "": "",
}

def IntraCityTravelCheck():
    print("Are you heading from one city to another (y/n)?")
    cityCheck = input()
    match cityCheck:
        case "y":
            IntraCityCalculate()
        case "n":
            HexCalculate()
    main()

def IntraCityCalculate():
    print("Where are you travelling from?")
    fromCity = input()

    print("And where to?")
    toCity = input()


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
                    givePrice = True
                case "n":
                    daysOfTravel = numToCalc / 3
                    givePrice = False
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
            givePrice = True
    print(f"Your trip will take {daysOfTravel} days.")
    if givePrice:
        print(f"A vic can be chartared at ~{numCartPrice}sp for the trip.")
        givePrice = False
    main()

def main():
    IntraCityTravelCheck()

if __name__ == "__main__":
    main()