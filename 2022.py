def main():
	operators = ["+", "-", "*", "/"]
	numbers = [[0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 0, 2], [2, 2, 2, 0]]
	allPatternList = []

	for number in numbers:
		for operationIndex1 in range(4):
			for operationIndex2 in range(4):
				for operationIndex3 in range(4):
					allPatternList.append([number[0], operators[operationIndex1], number[1], operators[operationIndex2], number[2], operators[operationIndex3], number[3]])
	
	for pattern in allPatternList:
		answer = getAnswer(pattern)
		if answer != 0:
			print("(((" + str(pattern[0]) + " " + pattern[1] + " " + str(pattern[2]) + ") " + pattern[3] + " " + str(pattern[4]) + ") " + pattern[5] + " " + str(pattern[6]) + ") = " + str(answer))


def calculate(number, operator, number2):
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

def getAnswer(expression):
	answer = calculate(expression[0], expression[1], expression[2])
	answer = calculate(answer, expression[3], expression[4])
	answer = calculate(answer, expression[5], expression[6])
	return answer




main()