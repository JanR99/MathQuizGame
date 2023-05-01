import random
import time

#TODO timer soll Program immer stoppen können

def getSign(x: int):
    if x == 0:
        return "+"
    elif x == 1:
        return "-"
    elif x == 2:
        return "*"
    else:
        return "/"


def newEquation():
    number1 = random.randrange(1, 10)
    number2 = random.randrange(1, 10)
    sign = getSign(random.randrange(4))
    return str(number1) + sign + str(number2)


def printEquation(equation: str):
    print(equation)


def getSolution(equation: str):
    x = int(equation[0])
    y = int(equation[2])
    sign = equation[1]
    if sign == "+":
        return int(x + y)
    if sign == "-":
        return int(x - y)
    if sign == "*":
        return int(x * y)
    if sign == "/":
        return int(x / y)
    return -1


class MathQuizGame:
    correct = 0

    def start(self):
        print("Press enter to start the game")
        input()
        begin = time.time()
        while time.time() - begin < 10:
            equation = newEquation()
            solution = getSolution(equation)
            print(solution)
            printEquation(equation)
            answer = 1000
            while answer != solution:
                if time.time() - begin > 10:
                    break
                try:
                    answer = int(input())
                except ValueError:
                    print("Answer should be a number")
            if answer == solution:
                self.correct += 1
        self.end()

    def end(self):
        print("You answered " + str(self.correct) + " equations correct")
