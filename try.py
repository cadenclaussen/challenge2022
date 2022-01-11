expression = [ 2, "+", 4, "-", 2, "*", 4]

def calculate(number, operator, number2):
	if operator == "+":
		return number + number2
	if operator == "-":
		return number - number2
	if operator == "*":
		return number * number
	if operator == "/":
		if number2 != 0:
			return number / number2
		print("Error, cannot divide by zero")
		return False

def getAnswer(expression):
	answer = calculate(expression[0], expression[1], expression[2])
	answer = calculate(answer, expression[3], expression[4])
	answer = calculate(answer, expression[5], expression[6])
	return answer

print(getAnswer(expression))
