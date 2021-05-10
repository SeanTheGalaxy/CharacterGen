import random

counter = 1

def num():
    return random.randint(3, 20)==20

while True:
    if num() and num() and num() and num() and num() and num() and num() : break
    counter += 1
    if counter%25000000 == 0:
        print(counter)

print("Done in", counter, "tries!")
