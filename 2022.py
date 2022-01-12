import math
import sys


def main():
    maximum = 100
    minimum = 1

    syslength = len(sys.argv) - 1
    if syslength == 1:
        maximum = sys.argv[1]
        minimum = sys.argv[1]
        
    if syslength == 2:
        minimum = sys.argv[1]
        maximum = sys.argv[2]
    
    if syslength > 2:
        print("Usage: p3 2022.py [solution] | [solution-max] [solution-min]")
        sys.exit(2)


    binary = ["+", "-", "*", "/", "^"]
    unary = ["!", "!!", "^ 1/2", ""]
    numbers = [[0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 0, 2], [2, 2, 2, 0]]
    expressions = []
    allNumbers = []


    for i in range(int(minimum) - 1, int(maximum)):
        for j in range(1):
            allNumbers.append(str(i+1))

    expressions = generateExpressions(unary, binary, numbers)
    sortedPatterns = getResult(expressions)
    printAll(allNumbers, sortedPatterns)


def generateExpressions(unary, binary, numbers):
    expressions = []
    for number in numbers:
        for operationIndex1 in range(5):
            for operationIndex2 in range(5):
                for operationIndex3 in range(5):
                    for uniaryIndex1 in range(4):
                        for uniaryIndex2 in range(4):
                            for uniaryIndex3 in range(4):
                                for uniaryIndex4 in range(4):
                                    expressions.append({"expression": [number[0], unary[uniaryIndex1], binary[operationIndex1], number[1], unary[uniaryIndex2], binary[operationIndex2], number[2], unary[uniaryIndex3], binary[operationIndex3], number[3], unary[uniaryIndex4]]})
    return expressions


def getResult(expressions):
    for expression in expressions:
        answer = getAnswer(expression["expression"])
        expression.update({"answer": answer})
    sortedPatterns = sorted(expressions, key = lambda i: i["answer"])
    return sortedPatterns


def printAll(allNumbers, sortedPatterns):
    for expression in sortedPatterns:
        if str(expression["answer"]) in allNumbers:
            if expression["answer"] >= 1 and expression["answer"] <= 100:
                allNumbers.remove(str(expression["answer"]))
                print("((((((" + str(expression["expression"][0]) + " " + str(expression["expression"][1]) + ") " + str(expression["expression"][2]) + " " + str(expression["expression"][3]) + ") " + str(expression["expression"][4]) + ") " + str(expression["expression"][5]) + " " + str(expression["expression"][6]) + ") " + str(expression["expression"][7] + ") " + str(expression["expression"][8]) + " " + str(expression["expression"][9]) + ") " + str(expression["expression"][10]) + ") = " + str(expression["answer"])))


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


def specialCalculate(number, operator):
    if operator == "":
        return number

    if operator == "!":
        if number < 101:
            return factorial(number)
        else:
            return number

    if operator == "!!":
        if number < 101:
            return doubleFactorial(number)
        else:
            return number

    if number >= 0:
        if operator == "^ 1/2":
            return squareroot(number)
    else:
        return number


def getAnswer(expression):
    # [0, '!', '+', 2, '!', '+', 2, '', '*', 2, '!'] = 8
    answer = specialCalculate(expression[0], expression[1])
    answer = calculate(answer, expression[2], expression[3])
    answer = specialCalculate(answer, expression[4])
    answer = calculate(answer, expression[5], expression[6])
    answer = specialCalculate(answer, expression[7])
    answer = calculate(answer, expression[8], expression[9])
    answer = specialCalculate(answer, str(expression[10]))
    return answer


def squareroot(n):
    return round(math.sqrt(n), 0)


def factorial(number):
    total = 1
    if number == 0:
        return 0
    for i in range(int(number) - 1):
        total = recursiveFactorial(number - i, total)
    return total


def recursiveFactorial(number, total):
    return number * total


def doubleFactorial(x):
    if x == 0:
        return 0
    total = 1
    if x % 2 == 1:
        for i in range(1, int(x), 2):
            total = doubleFactorialRecursive(x - i + 1, total)

    if x % 2 == 0:
        for i in range(0, int(x), 2):
            total = doubleFactorialRecursive(x - i, total)

    return total


def doubleFactorialRecursive(x, total):
    return x * total


main()