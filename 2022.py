import math
import sys

repeat = int(sys.argv[1])
range1 = int(sys.argv[2])
range2 = int(sys.argv[3])

def main():
    binary = ["+", "-", "*", "/", "^"]
    unary = ["!", "!!", "^ 1/2", ""]
    numbers = [[0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 0, 2], [2, 2, 2, 0]]
    expressions = []
    allNumbers = []

    for i in range(range1 - 1, range2):
        for j in range(repeat):
            allNumbers.append(str(i+1))

    generateExpressions(unary, binary, expressions, numbers)
    printAll(expressions, allNumbers)



def generateExpressions(unary, binary, expressions, numbers):
    for number in numbers:
        for operationIndex1 in range(5):
            for operationIndex2 in range(5):
                for operationIndex3 in range(5):
                    for uniaryIndex1 in range(4):
                        for uniaryIndex2 in range(4):
                            for uniaryIndex3 in range(4):
                                for uniaryIndex4 in range(4):
                                    expressions.append({"expression": [number[0], unary[uniaryIndex1], binary[operationIndex1], number[1], unary[uniaryIndex2], binary[operationIndex2], number[2], unary[uniaryIndex3], binary[operationIndex3], number[3], unary[uniaryIndex4]]})

def printAll(expressions, allNumbers):
    for pattern in expressions:
        answer = getAnswer(pattern["expression"])
        pattern.update({"answer": answer})
    sortedPatterns = sorted(expressions, key = lambda i: i["answer"])
    for pattern in sortedPatterns:
        if str(pattern["answer"]) in allNumbers:
            if pattern["answer"] >= 1 and pattern["answer"] <= 100:
                allNumbers.remove(str(pattern["answer"]))
                print("((((((" + str(pattern["expression"][0]) + " " + str(pattern["expression"][1]) + ") " + str(pattern["expression"][2]) + " " + str(pattern["expression"][3]) + ") " + str(pattern["expression"][4]) + ") " + str(pattern["expression"][5]) + " " + str(pattern["expression"][6]) + ") " + str(pattern["expression"][7] + ") " + str(pattern["expression"][8]) + " " + str(pattern["expression"][9]) + ") " + str(pattern["expression"][10]) + ") = " + str(pattern["answer"])))


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
        else:
            return number

    if operator == "!!":
        if number < 11:
            return doubleFact(number)
        else:
            return number

    if number >= 0:
        if operator == "^ 1/2":
            return squareroot(number)
    else:
        return number


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

def squareroot(n):
    return round(math.sqrt(n), 0)

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

main()