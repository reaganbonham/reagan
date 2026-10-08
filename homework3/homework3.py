# 3.1 SAY GOODBYE
import time


name = "reagan"

def say_goodbye(name):
    print("goodbye,", name) # prints "goodbye, reagan"

say_goodbye(name)

# 3.2 AREA OF A CIRCLE
def circle_area(radius):
    print(3.14 * radius**2)

circle_area(7) # calculates 3.14 * 7^2, which is 153.86

# 4.1 SUBTRACT, MULTIPLY, DIVIDE
a = 5
b = 2

def subtract(a, b):
    return a - b

print(subtract(a, b)) # subtracts 2 from 5

def multiply(a, b):
    return a * b

print(multiply(a, b)) # multiplies 5 and 2

def divide(a, b):
    return a / b

print(divide(a, b)) # divides 5 by 2

# 5.1 WHAT SHOULD I WEAR?
list = [15, 14, 17, 20, 23, 28, 20]

def what_to_wear(min, max):
    return("the temperature extremes today are:", (min(list), max(list)))

print(what_to_wear(min, max)) # returns "the temperature extremes today are (14, 28)"

# 5.2 CHECK IF IT'S THE WEEKEND
def is_weekend(num):
    if num == 7 or num == 6:
        return "True!!"
    else:
        return "False :("

print(is_weekend(2)) # returns False

print(is_weekend(6)) # returns True

# 5.3 FUEL EFFICIENCY CALCULATOR
d = 25
f = 2
def fuel_efficiency(d, f):
    return((d / f), "miles per gallon")

print(fuel_efficiency(d, f)) # calculates 25 divided by 2, which is 12.5

# 5.4 SECRET CODE
def encrypt_astro(num):
    n = len(str(num))
    a = num % 10
    b = num // 10
    return a*(10**(n-1)) + b

print(encrypt_astro(12345))


# 6.1 OSKI STOLE POWER
def inyourface_oski(x, y):
    result = 1
    if y == 0: # because anything to the power of 0 is 1
        return(1)
    for _ in range(abs(y)): # multiplies the result by itself however many times
        result *= x
    if y < 0: # deals with the negative exponents
        return (1 / result)
    return(result)

print(inyourface_oski(2, 5)) # takes 2 to the fifth power, which is 32

print(inyourface_oski(2, -5)) # takes 2 the negative fifth power, which is 0.03125

# 6.2 MIN & MAX WITH LOOPS
list1 = [5, 8, 2, 9, 3]

# 6.2.1 for loops
def new_min_for(list1):
    if not list1:
        return None
    minim = list1[0]
    for num in list1:
        if num < minim:
            minim = num
    return minim

print(new_min_for(list1))

def new_max_for(list1):
    if not list1:
        return None
    maxim = list1[0]
    for num in list1:
        if num > maxim:
            maxim = num
    return maxim

print(new_max_for(list1))

# 6.2.2 while loops
def new_min_while(list1):
    if not list1:
        return None
    mini = list1[0]
    index = 1
    while index < len(list1):
        if list1[index] < mini:
            mini = list1[index]
        index += 1
    return mini

print(new_min_while(list1))

def new_max_while(list1):
    if not list1:
        return None
    maxi = list1[0]
    index = 1
    while index < len(list1):
        if list1[index] > maxi:
            maxi = list1[index]
        index += 1
    return maxi

print(new_max_while(list1))

# 6.3 CALCULATE THE SUM
def sum_calculation(integer):
    return(sum(int(digit) for digit in str(integer)))

print(sum_calculation(1234))


