import random

cars = ['BMW', 'Mini', 'Porsche']

def generateModelYear():
	retrun random.randRange(1970, 2022)

print(random.choice(cars))
print(generateModelYear())
