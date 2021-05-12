import random
import config

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

race = races[random.randint(0,len(racelist)-1)]
print(race)

#def rollstat():
    #return random.randint(3, 20)

def rollattribute():
    roll0a = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    roll0a = sorted(roll0a)
    del roll0a[0]
    roll0 = sum(roll0a)
    return roll0


# roll stats
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

adjectives = []
suggestions = []
for stat in stats :
    #print(stat+ ":", stats[stat])
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
    print(instrumentsbard[random.randint(0,len(instrumentsbard)-1)]+", Dagger")
print("--------------------------------")
