import json
import random
import config
import os

high = config.high
low = config.low
profession = config.profession
quirk1 = config.quirk1
quirk2 = config.quirk2
cantripsoffense = config.cantripsoffense
cantripsdefense = config.cantripsdefense
cantripsutil = config.cantripsutil
weaponsfighter = config.weaponsfighter
weaponsranger = config.weaponsranger
weaponsbarbarian = config.weaponsbarbarian
instrumentsbard = config.instrumentsbard
racial_modifiers = config.racial_modifiers
races = config.races


# Takes a dictionary with a list of characters and saves to storage
def write_characters(data):
    with open('characters.json', 'w') as outfile:
        json.dump(data, outfile)

# Loads characters from storage and returns a dictionary with a list of characters
def load_characters():
    if os.path.exists('characters.json') :
        with open('characters.json') as json_file:
            data = json.load(json_file)
            return data
    else:
        return {"characters":[]}

def load_character(name):
    for c in load_characters()["characters"]:
        if c["name"].lower() == name.lower():
            return c
    return None

def delete_character(name):
    data = load_characters()
    for c in data["characters"]:
        if c["name"].lower() == name.lower():
            data["characters"].remove(c)
            write_characters(data)
            return

def list_characters():
    return [c["name"] for c in load_characters()["characters"]]

# Saves a single character (dictionary)
def save_character(character):
    data = load_characters()
    data["characters"].append(character)
    write_characters(data)

def rollattribute():
    roll0a = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll0a = sorted(roll0a)
    del roll0a[0]
    roll0 = sum(roll0a)
    return roll0


def generate_stats(race):
    stats = dict()
    stats["STR"] = rollattribute()
    stats["DEX"] = rollattribute()
    stats["CON"] = rollattribute()
    stats["INT"] = rollattribute()
    stats["WIS"] = rollattribute()
    stats["CHA"] = rollattribute()

    # apply racial modifiers
    for stat in stats:
        if stat in racial_modifiers[race] :
            stats[stat] = stats[stat]+racial_modifiers[race][stat]

    return stats


def generate_character(name, pronoun, race, pcclass, stats):
    pc = {}

    pc["name"] = name
    pc["race"] = race
    pc["pcclass"] = pcclass
    pc["stats"] = stats
    pc["pronoun"] = pronoun

    # generate quirks
    pc["quirks"] = []
    for i in range(3):
        pc["quirks"].append(random.choice(quirk1)+ " " + random.choice(quirk2))

    # generate spells
    pc["spells"] = []
    if pcclass in ["Wizard", "Cleric", "Bard"]:
        pc["spells"].append(random.choice(cantripsoffense))
        pc["spells"].append(random.choice(cantripsdefense))

    if pcclass in ["Wizard", "Bard"]:
        pc["spells"].append(random.choice(cantripsutil))
    elif pcclass == "Cleric":
        pc["spells"].append("Heal")

    # generate weapons

    pc["weapons"] = []
    if pcclass == "Fighter":
        pc["weapons"].append(random.choice(weaponsfighter))
    elif pcclass == "Ranger":
        pc["weapons"].append(random.choice(weaponsranger))
    elif pcclass == "Barbarian":
        pc["weapons"].append(random.choice(weaponsbarbarian))
    elif pcclass in ["Wizard", "Cleric"]:
        pc["weapons"].append("Staff")
        pc["weapons"].append("Dagger")
    elif pcclass == "Bard":
        pc["weapons"].append("Dagger")

    # generate gear

    pc["gear"]=[]

    if pcclass == "Bard":
        pc["gear"].append(random.choice(instrumentsbard))
    return pc



def console_create_character():
    name = input("What Shall We Name Your Character? ")
    name= name.lower().capitalize()
    pronoun = input("What is their pronoun? ")
    print("Ok", pronoun, "Shall Be Called", name)
    pronoun = pronoun.lower()
    himherthem = pronoun
    if pronoun == "she":
        himherthem = "her"
    elif pronoun == "they":
        himherthem = "them"
    elif pronoun == "he":
        himherthem = "him"
    else:
        himherthem = name
    print("And all shall worship", himherthem + ".", "For", pronoun, "is a...")

    race = random.choice(races)
    print(race)

    stats = generate_stats(race)
    adjectives = []
    suggestions = []
    for stat in stats :
        #print(stat+ ":", pc["stats"][stat])
        if stats[stat] < 9:
            adjectives.append(low[stat])
        elif stats[stat] > 13:
            adjectives.append(high[stat])
            suggestions.append(profession[stat])

    def smartjoin(list, conjunction, nothing):
        if len(list) > 1:
            return ", ".join(list[:-1]) + " " + conjunction + " " + list[-1]
        elif len(list) > 0:
            return list[0]
        else: return nothing

    print(pronoun, "is", smartjoin(adjectives, "and", "boring"))
    #print(pronoun, quirk1[random.randint(0,len(quirk1)-1)], quirk2[random.randint(0,len(quirk2)-1)])
    print("and",pronoun,"would make a good", smartjoin(suggestions, "or", "hostage"))
    pcclass = input("What do you want to be? ")
    pcclass = pcclass.lower().capitalize()


    pc = generate_character(name=name, race=race, pcclass=pcclass, pronoun=pronoun, stats=stats)
    console_print_character(pc)

    if input("Do you want to save " + name + "? (Y/N) ").lower() == "y":
        save_character(pc)
        print("Saved", name+"!")
    else:
        print(name, "is gone forever. Wah Wah Waaaaaaaah. :(")



def console_print_character(pc):
    print("\n\n")
    print("--------------------------------")
    print("Name:", pc["name"])
    print("Class:", pc["pcclass"])
    print("Race:", pc["race"])

    print("")
    for stat in pc["stats"] :
        print(stat+ ":", pc["stats"][stat])

    print("")
    print("Quirks:")
    for q in pc["quirks"] : print("   " + q)

    if len(pc["spells"]) > 0 :
        print("")
        print("Spells:")
        for s in pc["spells"]: print("   " + s)

    if len(pc["weapons"]) > 0 :
        print("")
        print("Weapons:")
        for w in pc["weapons"]: print("   " + w)

    if len(pc["gear"]) > 0 :
        print("")
        print("Gear:")
        for g in pc["gear"]: print("   " + g)
    print("--------------------------------")

def console_print_menu():
    print("")
    print("--------------------------------")
    print("MAIN MENU")
    print("  [C]reate Character")
    print("  [V]iew Character")
    print("  [E]dit Character")
    print("  [D]elete Character")
    print("  [L]ist Characters")
    print("  [Q]uit")
    print("--------------------------------")
# main loop
while True:
    console_print_menu()
    command = input("> ").lower()
    if command == "c":
        console_create_character()
    elif command == "q":
        break
    elif command == "l":
        for c in list_characters() : print(c)
    elif command == "v":
        name = input("Which character? ")
        pc = load_character(name)
        if pc:
            console_print_character(pc)
        else:
            print("Character not found.")
    elif command == "d":
        name = input("Which character? ")
        delete_character(name)
        print(name, "is gone forever. Wah Wah Waaaaaaaah. :(")
    else:
        print("Not implemented yet")
