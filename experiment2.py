import random
roll0a = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
roll0a = sorted(roll0a)
del roll0a[0]
roll0 = sum(roll0a)
print(roll0)
