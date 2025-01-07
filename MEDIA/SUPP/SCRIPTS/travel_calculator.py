cityTable = {
    "Castle Prosper": "0L24",
    "Gambleum": "0E23",
    "Janesland": "0G28",
    "Magius": "0J26",
    "Moonlight": "0I19",
    "Yerba": "0N18",
    "Amyl Dother": "AK17",
    "Barkryn": "AG32",
    "Beacon": "AN30",
    "Boneborn": "AG26",
    "Darnt Hillkeep": "0Z20",
    "Goldfield": "AB16",
    "Lakeview": "0Y29",
    "Mossburg": "AC24",
    "New Quillbuck": "AN17",
    "Red Throne": "AE28",
    "Zalfari": "AI16",
    "Groundiki": "AA16",
    "Kickoff": "0Y10",
    "Low Hornrock": "0T07",
    "Mountain Hall": "0R10",
    "Golden City": "AD07",
    "Kohnstamm": "0K04",
    "Odaya": "0F06",
    "Kanielkiln": "0I10",
    "Wychway": "0N12",
    "Yagil": "0D10",
    "default": "FAIL"
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
    if fromCity in cityTable.keys():
        fromCityCoords = cityTable.get(fromCity)

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