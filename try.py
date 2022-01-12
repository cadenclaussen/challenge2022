import math

def squareroot(n):
	#print(str(math.sqrt(n)) + "is math.sqrt(n)")
	return round(math.sqrt(n), 1)

def calculate(number, operator, number2):
    operator = str(operator)
    if operator == "+":
        return number + number2
    if operator == "-":
        return number - number2
    if operator == "*":
        return number * number2
    if operator == "^":
        return number ** number2
    if operator == "/":
        if number2 != 0:
            return number / number2
        return False 

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
    if x == 0:
        return 0
    total = 1
    if x % 2 == 1:
        for i in range(1, int(x), 2):
            total = doubleFactRec(x - i + 1, total)

    if x % 2 == 0:
        for i in range(0, int(x), 2):
            total = doubleFactRec(x - i, total)

    return total

def doubleFactRec(x, total):
    return x * total

def getAnswer(expression):
    # [0, '!', '+', 2, '!', '+', 2, '', '*', 2, '!'] = 8
    answer = specialCalc(expression[0], expression[1])
    answer = calculate(answer, expression[2], expression[3])
    answer = specialCalc(answer, expression[4])
    answer = calculate(answer, expression[5], expression[6])
    answer = specialCalc(answer, expression[7])
    answer = calculate(answer, expression[8], expression[9])
    answer = specialCalc(answer, str(expression[10]))
    return answer

# print("[0, '!', '+', 2, '!', '+', 2, '!!', '*', 2, '!!']")
# print(getAnswer([0, '!', '+', 2, '!', '+', 2, '!!', '*', 2, '!!']))
print(doubleFact(100))





