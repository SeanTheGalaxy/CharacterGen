import random

name = input("What Shall We Name Your Character? ")
name = name.lower().capitalize()
pronoun = input("What is their pronoun? ")
print("Ok", pronoun, "Shall Be Called", name)
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

racelist = ["Dragonborn", "Elf", "Dwarf", "Human", "Halfling", "Half-Orc", "Gnome", "Tiefling"]
race = racelist[random.randint(0,len(racelist)-1)]
print(race)

#def rollstat():
    #return random.randint(3, 20)

def rollattribute():
    roll0a = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll0a = sorted(roll0a)
    del roll0a[0]
    roll0 = sum(roll0a)
    return roll0
#if race == "Dwarf":
#    rbcon=2
#elif race == "Elf":
#    rbdex=2
#elif race == "Halfling":
#    rbdex=2
#elif race == "Human":
#    rbstr=1
#    rbdex=1
#    rbcon=1
#    rbint=1
#    rbwis=1
#    rbcha=1
#elif race == "Dragonborn":
#    rbstr=2
#    rbcha=1
#elif race == "Gnome":
#    rbint=2
#elif race == "Half-Orc":
#    rbstr=2
#    rbcon=1
#elif race == "Tiefling":
#    rbcha=2
#    rbint=1


stats = dict()
stats["STR"] = rollattribute()
stats["DEX"] = rollattribute()
stats["CON"] = rollattribute()
stats["INT"] = rollattribute()
stats["WIS"] = rollattribute()
stats["CHA"] = rollattribute()

high = { "STR" : "strong",
         "DEX" : "agile",
         "CON" : "tough",
         "INT" : "smart",
         "WIS" : "wise",
         "CHA" : "persuasive" }
low = { "STR" : "weak",
         "DEX" : "slooow",
         "CON" : "fragile",
         "INT" : "dumb",
         "WIS" : "foolish",
         "CHA" : "homely" }
profession = { "STR" : "Fighter",
         "DEX" : "Ranger",
         "CON" : "Barbarian",
         "INT" : "Wizard",
         "WIS" : "Cleric",
         "CHA" : "Bard" }
quirk1 = ["is scared of", "loves", "hates", "is allergic to", "has an addiction to", "is a collecter of", "is unfortunately fond of"]
quirk2 = ["pizza", "love", "onions", "the cold", "turkeys", "caves", "baths", "clerics", "fruit bats", "swords", "wood", "paper", "bows", "hostages", "medals", "awards", "rubies", "gods", "phones", "ipads", "ale", "fine wine", "boats", "treehouses"]
cantripsoffense = ["Fireball", "Ice Shard", "Lightning Bolt", "Earth Chunk", "Wind Blade"]
cantripsdefense = ["Fire Wall", "Ice Shield", "Lightning Deflect", "Earth Armor", "Wind Gust"]
cantripsutil = ["Fire Light", "Ice Path", "Lightning Field", "Earth Mold", "Wind Push"]
weaponsfighter = ["Greatsword", "Greataxe"]
weaponsranger = ["Longbow", "Crossbow"]
weaponsbarbarian = ["Warhammer", "Battleaxe"]
instrumentsbard = ["Violin", "Viola", "Cello", "Lute", "Madolin"]

#if stats["STR"] > 16 and stats["DEX"] < 10:
#    print("TREE")
#elif stats["STR"] < 10 and stats["DEX"] > 16:
#    print("WORM")
#elif stats["STR"] < 6 and stats["DEX"] < 6:
#    print("RADISH")
#elif stats["STR"] < 10 and stats["DEX"] < 10:
#    print("WIMP")
#elif stats["STR"] < 15 or stats["DEX"] < 15:
#    print("HUMAN")
#else:
#    print("DEITY")

adjectives = []
suggestions = []
for stat in stats :
    #print(stat+ ":", stats[stat])
    if stats[stat] < 6:
        adjectives.append(low[stat])
    elif stats[stat] > 15:
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

print("\n\n")
print("--------------------------------")
print("Name:", name)
print("Class:", pcclass)
print("Race:", race)
print("")
for stat in stats :
    print(stat+ ":", stats[stat])
print("Quirks:")
for i in range(3):
    print(quirk1[random.randint(0,len(quirk1)-1)], quirk2[random.randint(0,len(quirk2)-1)])
if pcclass == "Wizard" or pcclass == "Cleric" or pcclass == "Bard":
    print("Spells:")
    print(cantripsoffense[random.randint(0,len(cantripsoffense)-1)])
    print(cantripsdefense[random.randint(0,len(cantripsdefense)-1)])
if pcclass == "Wizard" or pcclass == "Bard":
    print(cantripsutil[random.randint(0,len(cantripsutil)-1)])
if pcclass == "Cleric":
    print("Heal")
print("Weapons")
if pcclass == "Fighter":
    print(weaponsfighter[random.randint(0,len(weaponsfighter)-1)])
elif pcclass == "Ranger":
    print(weaponsranger[random.randint(0,len(weaponsranger)-1)])
elif pcclass == "Barbarian":
    print(weaponsbarbarian[random.randint(0,len(weaponsbarbarian)-1)])
elif pcclass == "Wizard" or pcclass == "Cleric":
    print("Staff, Dagger")
elif pcclass == "Bard":
    print(instrumentsbard+", Dagger")
print("--------------------------------")
