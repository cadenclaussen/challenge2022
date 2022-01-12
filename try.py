import math

def squareroot(n):
	#print(str(math.sqrt(n)) + "is math.sqrt(n)")
	return round(math.sqrt(n), 1)

def specialCalc(number, operator):
	if operator == "":
		return number

	if operator == "!":
		if number < 11:
			return fact(number)
		return number

	if operator == "!!":
		if number < 11:
			return doubleFact(number)
		return number

	if operator == "^ 1/2":
		return squareroot(number)

print(specialCalc(64, "^ 1/2"))