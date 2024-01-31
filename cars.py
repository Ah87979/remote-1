import random

cars = ['BMW', 'Mini', 'Porsche']

def generateModelYear():
	retrun randon.randRange(1970, 2022)

print(random.choice(cars))
print(generateModelYear())
