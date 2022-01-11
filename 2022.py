import math

def main():
	operators = ["+", "-", "*", "/"]
	uniary = ["!", "!!"]
	numbers = [[0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 0, 2], [2, 2, 2, 0]]
	allPatternList = []

	for number in numbers:
		for operationIndex1 in range(4):
			for operationIndex2 in range(4):
				for operationIndex3 in range(4):
					# for uniaryIndex1 in range(2):
					# 	for uniaryIndex2 in range(2):
					# 		for uniaryIndex3 in range(2):
					# 			for uniaryIndex4 in range(2):
					allPatternList.append({"expression": [number[0], operators[operationIndex1], number[1], operators[operationIndex2], number[2], operators[operationIndex3], number[3]]})
	for pattern in allPatternList:
		answer = getAnswer(pattern)
		pattern.update({"answer": int(answer)})
	sortedPatterns = sorted(allPatternList, key = lambda i: i["answer"])
	for pattern in sortedPatterns:
		if pattern["answer"] >= 1:
			print("(((" + str(pattern["expression"][0]) + " " + pattern["expression"][1] + " " + str(pattern["expression"][2]) + ") " + pattern["expression"][3] + " " + str(pattern["expression"][4]) + ") " + pattern["expression"][5] + " " + str(pattern["expression"][6]) + ") = " + str(pattern["answer"]))



def calculate(number, operator, number2):
	operator = str(operator)
	if operator == "+":
		return number + number2
	if operator == "-":
		return number - number2
	if operator == "*":
		return number * number2
	if operator == "/":
		if number2 != 0:
			return number / number2
		return False	

	if operator == "!":
		return factorial(number)
	if operator == "!!":
		return doubleFact(number)
	if operator == "^":
		return power(number)
	if operator == "√":
		return sqrt(number)

def getAnswer(expression):
	answer = calculate(expression["expression"][0], expression["expression"][1], expression["expression"][2])
	answer = calculate(answer, expression["expression"][3], expression["expression"][4])
	answer = calculate(answer, expression["expression"][5], expression["expression"][6])

	return answer

def factorial(number):
	total = 1
	if number > 0:
		total *= number
		factorial(number - 1)
	else: 
		return number

def doubleFact(number):
	if number > 0:
		total *= number
		doubleFact(number - 2)
	else: 
		return total

def sqrt(number):
	if number > 0:
		answer = math.sqrt(number)
	else:
		return number

	if answer // 1 == answer:
		return answer
	else: 
		return number

def power(number):
	return number ** 2



main()