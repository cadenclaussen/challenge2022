def fact(number):
	total = 1
	if number == 0:
		return 0
	for i in range(int(number) - 1):
		total = recFact(number - i, total)
	return total

def recFact(number, total):
	return number * total

def doubleFact(x):
	total = 1
	if x == 0:
		return 0
	if x % 2 == 1:
		for i in range(1, int(x), 2):
			total = doubleFactRec(x - i + 1, total)

	if x % 2 == 0:
		for i in range(0, int(x), 2):
			total = doubleFactRec(x - i, total)

	return total

def doubleFactRec(x, total):
	return x * total

print(fact(4))
print(doubleFact(0))