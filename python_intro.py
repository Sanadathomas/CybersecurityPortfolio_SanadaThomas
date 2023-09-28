import math
import cmath
import random

print("Sanada Thomas")

Num1 = 15
Num2 = 20
Sum = Num1 + Num2
print('Num1 + Num2 =', Sum)

math.sqrt(49)

from math import sqrt

number = 144
square_root = sqrt(number)
print("The square root is", square_root)

sideA = 80
sideB = 90
sideC = 20

s = (sideA + sideB + sideC) / 2
area = (s * (s - sideA) * (s - sideB) * (s - sideC)) ** 0.5
print('The area of the triangle is %0.5f' % area)

a = 1
b = 5
c = 6

d = (b ** 2) - (4 * a * c)

sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('The solution are {0} and {1}'.format(sol1, sol2))

name1 = "Kaka"
name2 = "Jonny"
name1, name2 = name2, name1
print('your name was', name1)
print("Now it's", name2)

print(random.randint(0, 1000000))

kilometre_1 = 255
conversion_ratio_1 = 0.621371
miles_1 = kilometre_1 * conversion_ratio_1
print("The speed value of car in Miles:", " %.0f" % miles_1, "mph")

celsius_1 = 40
Fahrenheit_1 = (celsius_1 * 1.8) + 32
print("The temperature is", Fahrenheit_1)


def NumberCheck(a):
    if a > 0:
        print("Number given by you is Positive")
    elif a < 0:
        print("Number given by you is Negative")
    else:
        print("Number given by you is zero")


a = float(input("Enter a number to see if it's negative, positive or zero: "))
NumberCheck(a)

num = int(input("Enter a number to see if it's even or odd: "))
if (num % 2) == 0:
    print("{0} is Even a number".format(num))
else:
    print("{0} is Odd a number".format(num))


def CheckLeap(Year):
    if ((Year % 400 == 0) or
            (Year % 100 != 0) and
            (Year % 4 == 0)):
        print("Given Year is a leap Year");
    else:
        print("Given Year is not a leap Year")


Year = int(input("Enter a year: "))
CheckLeap(Year)
