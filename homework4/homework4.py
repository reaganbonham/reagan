# 3 LISTS

#3.1 LIST OPERATIONS

favorite_foods = ["strawberry", "chocolate", "noodles", "chicken nuggets", "pizza"]
print(favorite_foods[1])

favorite_foods.append("sushi")
print(favorite_foods)

favorite_foods.insert(0, "apple")
print(favorite_foods)

favorite_foods.remove("noodles")
print(favorite_foods)

print(len(favorite_foods))

favorite_foods = [food.upper() for food in favorite_foods]
print(favorite_foods)

new_foods = favorite_foods[0] + favorite_foods[-1]
print(new_foods)


#error in code #1
#def potato(str(favorite_foods)):
#    if "potato" in str(favorite_foods):
#        return "a potato!!"
#    else:
#        return "no potato!!"

#print(potato(favorite_foods))
"""
my error said:
SyntaxError: invalid syntax
I didn't write the function correctly; i didn't write the inside of the function as an input and i wrote it as a list.
"""

def check(str):
    if str == "potato":
        return "a potato!!"
    else:
        return "no potato!!"

print(check("potato"))
print(check("apple"))

# 3.2 SLICING & STRIDING

numbers = list(range(0, 20))

def get_first_15(lst):
    return lst[:15]

def get_every_fifth(lst):
    return lst[::5] #start at 0, end at 20, go every 5th

def reverse_and_stride(lst):
    reversed_lst = lst[::-1]
    return reversed_lst[::3]

print(get_first_15(numbers))
print(get_every_fifth(numbers))
print(reverse_and_stride(numbers))

# 3.3 NESTED LISTS
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(numbers[3][0])

# error in code #2:
"""
My error was as follows:
IndexError: list index out of range
I didn't use the proper matrix notation to access the elements in the third row
"""
print(numbers[2])

print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    for row in numbers:
        sum(row)
    return sum(sum(row) for row in numbers)

print(sum_nested(numbers))

# 3.4 CREATE A 5X5 LIST
#def create_5x5_list():

#__

# 4 DICTIONARIES

# 4.1 DICTIONARY OPERATIONS
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])

#ages["Mira" = 100]
#print(ages)

# error in code #3:
"""
I received the error message:
SyntaxError: invalid syntax
I wrote the change in Mira's age wrong; it should be ages["Mira"] = 100; here the brackets are in the correct place
"""

ages["Mira"] = 100
print(ages)

ages["Milana"] = 52
print(ages)

del ages["Mariam"]
print(ages)

for name, age in ages.items():
    print(f"{name} is {age} years old")

