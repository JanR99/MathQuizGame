import random
import threading
import time


# TODO Division sollte ohne Rest sein

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
    def __init__(self):
        self.correct = 0
        self.lock = threading.Lock()
        self.running = True

    def start(self):
        print("Press enter to start the game")
        input()
        self.work()
        self.end()

    def end(self):
        self.running = False
        print("You answered " + str(self.correct) + " equations correct")

    def work(self):
        begin = time.time()
        while time.time() - begin <= 10:
            equation = newEquation()
            solution = getSolution(equation)
            print(solution)
            print(equation)
            answer = 1000
            while answer != solution:
                try:
                    answer = int(input())
                    if answer == solution and time.time() - begin <= 10:
                        self.correct += 1
                except ValueError:
                    print("Answer should be a number")


if __name__ == '__main__':
    MathQuizGame().start()
