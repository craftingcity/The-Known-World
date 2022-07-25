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
        answer = "dimensional rift or gate actived by " + activation_special(random.randint(1, 6))
    if num == 2:
        answer = "hidden space actived by " + activation_special(random.randint(1, 6))
    if num == 3:
        answer = "magical boon actived by " + activation_special(random.randint(1, 6))
    if num == 4:
        answer = "magical curse actived by " + activation_special(random.randint(1, 6))
    if num == 5:
        answer = "teleportation actived by " + activation_special(random.randint(1, 6))
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
    if num == 6:
        answer = "some event, maybe timed"
    return answer

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
        answer = "oddities or resources"
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
        double_trouble = material(random.randint(1, 7)) + "& " + material(random.randint(1, 7))
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
        double_trouble = reason_A(random.randint(1, 7)) + " & " + reason_A(random.randint(1, 7))
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
    return answer

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
    return answer

def erosion(num):
    answer = ""
    if num == 1:
        answer = "ruined, defaced, or otherwise unrecognizable"
    if num == 2:
        answer = "weathered or overgrown"
    if num == 3:
        answer = "fair, restored, or otherwise maintained"
    if num == 4:
        answer = "pristine or well maintained"
    return answer

def main():
    bag_o_dice = reroll()
    final_answer = "This hex is occupied by a "
    if bag_o_dice[0] > 1:
        final_answer += "natural "
        final_answer += item_natural(bag_o_dice[1])
        final_answer += ". The reason this place is significat is because it is/has "
        final_answer += reason_A(bag_o_dice[2])
        final_answer += ". This place is "
        final_answer += age(bag_o_dice[5])
        final_answer += "and "
        final_answer += disposition(bag_o_dice[6]) + "."
    else:
        final_answer += "fabricated "
        final_answer += item_fabricated(bag_o_dice[1])
        final_answer += ". The reason this place is significat is because it is/has "
        final_answer += reason_B(bag_o_dice[2])
        final_answer += ". It is made of some type of " + material(bag_o_dice[3])
        final_answer += " and it is constructed for some " + use_case(bag_o_dice[4])
        final_answer += " purpose. This place is "
        final_answer += age(bag_o_dice[5])
        final_answer += " and "
        final_answer += disposition(bag_o_dice[6]) + "."
    print(final_answer)
    grab = input()
    if grab == "r":
        main()
    else:
        return

if __name__ == "__main__":
    main()