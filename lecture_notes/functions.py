# EXAMPLE 1
#name = "Reagan"

#print("Hello,", name)

#def say_hello(name):
   # print("Hello,", name)

 #say_hello(name)

# def add(a, b):
#    print(a + b)

# add(7, 8)

# EXAMPLE 2: CONDITIONALS IF/ELIF/ELSE
# def check_num(num):
#    if num > 0:
#        print("Positive")
#    elif num < 0:
#        print("Negative")
#    else: num == 0:
#        print("Zero")

#print(check_num(42))

# EXAMPLE 3: AND STATEMENT
# def can_vote(age, is_citizen):
#    if age >= 18 and is_citizen:
#        return True
#    else:
#        return False

# can_vote(19, True)

# EXAMPLE 4: OR STATEMENT
# def is_weekend(day):
#    if day=="Saturday" or day=="Sunday":
#        return "It is the weekend!"
#    else:
#        return "It is not the weekend :("

# print(is_weekend("Monday"))

# EXAMPLE 5: LOOPS
#for i in range(10):
#    print(i)

#fruit_basket = ["lychee", "mango", "nectarines"]

#for fruit in fruit_basket:
#    print(fruit)

#def countdown(start):
#    while start > 0:
#        print("T-",start)
#        start -=1
#    print("Lift-off")

#countdown(10)

# list = [40,80,10,30,50,20]

# def minimum(list):
#    return min(list)

# print(min(list))

# create a function to determine if a positive integer is a prime number

def isprime(num):
    if num <= 0 or type(num) != int:
        return "try again. choose a new number"
    else:
        if num == 1:
            return "neither"
        elif num == 2:
            return "is a prime number"
        else:
            if num % 2 == 0:
                return "composite number"
            else:
                for i in range(1, num):
                    if num % i == 0:
                        return "composite number"
                    else:
                        return "prime number!!"

print(isprime(34))