import random

def reroll():
    rolls = []
    rolls.append(random.randint(1, 3))
    rolls.append(random.randint(1, 8))
    rolls.append(random.randint(1, 8))
    rolls.append(random.randint(1, 8))
    rolls.append(random.randint(1, 8))
    rolls.append(random.randint(1, 4))
    rolls.append(random.randint(1, 4))
    rolls.append(random.randint(1, 4))
    rolls.append(random.randint(1, 4))
    return rolls

def item_natural(num):
    answer = ""
    if num == 1:
        answer = "boulder"
    if num == 2:
        answer = "burrow or cave"
    if num == 3:
        answer = "canyon, ridge, or cliff"
    if num == 4:
        answer = "earth formation"
    if num == 5:
        answer = "floral formation"
    if num == 6:
        answer = "geyser, pond, or spring"
    if num == 7:
        answer = "pit, quicksand, or sinkhole"
    if num == 8:
        double_trouble = item_natural(random.randint(1, 7)) + " " + item_natural(random.randint(1, 7))
        return double_trouble
    else:
        return answer

def item_fabricated(num):
    answer = ""
    if num == 1:
        answer = "alter, shrine, or temple"
    if num == 2:
        answer = "building ro structure"
    if num == 3:
        answer = "carving or relief"
    if num == 4:
        answer = "marking or symbol"
    if num == 5:
        answer = "monument or obelisk"
    if num == 6:
        answer = "statue"
    if num == 7:
        answer = item_natural(random.randint(1, 7)) + " and " + item_fabricated(random.randint(1, 6))
    if num == 8:
        double_trouble = item_natural(random.randint(1, 7)) + " " + item_natural(random.randint(1, 7))
        return double_trouble
    else:
        return answer

def item_special(num):
    answer = ""
    if num == 1:
        answer = "dimensional rift or gate"
    if num == 2:
        answer = "hidden space"
    if num == 3:
        answer = "magical boon"
    if num == 4:
        answer = "magical curse"
    if num == 5:
        answer = "teleportation"
    if num == 6:
        double_trouble = item_special(random.randint(1, 5)) + " " + item_special(random.randint(1, 5))
        return double_trouble
    else:
        return answer

def activation_special(num):
    answer = ""
    if num == 1:
        answer = "anyone"
    if num == 2:
        answer = "those connected"
    if num == 3:
        answer = "thosed othered"
    if num == 4:
        answer = "those samed"
    if num == 5:
        answer = "some sacrificed"
    if num == 4:
        answer = "some event, maybe timed"

def reason_A(num):
    answer = ""
    if num == 1:
        answer = "easy to spot"
    if num == 2:
        answer = "local legend"
    if num == 3:
        answer = "local superstition"
    if num == 4:
        answer = "misinterpreted purpose"
    if num == 5:
        answer = "oddity or resource"
    if num == 6:
        answer = "simple curiosity"
    if num == 7:
        answer = "battle, birth, death, or injury"
    if num == 8:
        double_trouble = reason_A(random.randint(1, 7)) + " " + reason_A(random.randint(1, 7))
        return double_trouble
    else:
        return answer

def reason_B(num):
    answer = ""
    if num == 1:
        answer = "easy to spot"
    if num == 2:
        answer = "local legend"
    if num == 3:
        answer = "local superstition"
    if num == 4:
        answer = "humanoid-esq"
    if num == 5:
        answer = "oddity or resource"
    if num == 6:
        answer = item_special(random.randint(1, 6))
    if num == 7:
        answer = "battle, birth, death, or injury"
    if num == 8:
        double_trouble = reason_A(random.randint(1, 7)) + " " + reason_A(random.randint(1, 7))
        return double_trouble
    else:
        return answer

def material(num):
    answer = ""
    if num == 1:
        answer = "earthwork"
    if num == 2:
        answer = "common metal"
    if num == 3:
        answer = "rare metal"
    if num == 4:
        answer = "petrified organics"
    if num == 5:
        answer = "plain stones"
    if num == 6:
        answer = "fancy stones"
    if num == 7:
        answer = "unidentified / other"
    if num == 8:
        double_trouble = material(random.randint(1, 7)) + " " + material(random.randint(1, 7))
        return double_trouble
    else:
        return answer

def use_case(num):
    answer = ""
    if num == 1:
        answer = "artistic or whimsical"
    if num == 2:
        answer = "commemerative"
    if num == 3:
        answer = "cultural"
    if num == 4:
        answer = "decree or punishment"
    if num == 5:
        answer = "historic"
    if num == 6:
        answer = "religious"
    if num == 7:
        answer = item_special(random.randint(1, 6))
    if num == 8:
        double_trouble = reason_A(random.randint(1, 7)) + " " + reason_A(random.randint(1, 7))
        return double_trouble
    else:
        return answer

def age(num):
    answer = ""
    if num == 1:
        answer = "prehistoric"
    if num == 2:
        answer = "ancient"
    if num == 3:
        answer = "old"
    if num == 4:
        answer = "young"

def disposition(num):
    answer = ""
    if num == 1:
        answer = "feared"
    if num == 2:
        answer = "loved"
    if num == 3:
        answer = "rarely known"
    if num == 4:
        answer = "worshipped"

def age(num):
    answer = ""
    if num == 1:
        answer = "ruined, defaced, or otherwise unrecognizable"
    if num == 2:
        answer = "weathered or overgrown"
    if num == 3:
        answer = "fair, restored, or otherwise maintained"
    if num == 4:
        answer = "pristine or well maintained"