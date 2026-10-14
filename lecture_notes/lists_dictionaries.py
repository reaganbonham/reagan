#numbers = [1, 2, 3, 4]

# print(numbers)

#fruits = ["apple", "cherries", "bananas"]

# print(fruits)

#mixed = ["hello", 5, True, None]

# print(mixed)

# ACCESS ITEMS IN A LIST

# print(numbers[-1])

#fruits[0] = "grape"

# prints(fruits)

# ADDING ITEMS

#numbers.append(6)

# print(numbers)

#print(mixed)

#print(mixed.insert(1, False))

#print(mixed)

# REMOVING ITEMS

#fruits.remove("bananas")

#print(fruits)

#fruits.pop(0)

#print(fruits)

#for num in numbers:
 #   print(num)

#nums = [10, 20, 30, 40, 50, 60]
#print(nums[1:4])
#print(nums[:3])

#STRIDES

#nums = [20, 40, 60, 80, 100, 120]
#print(nums[1::2])

#NEGATIVE INDEXING
nums = [2, 4, 6, 8, 10, 12]

#print(nums[-1]) # prints 12

#print(nums[1::3]) #prints [4, 10]

# DICTIONARIES

#bugs = {
#    "ants": ["black", "fire"],
#    "spiders": ["black widow", "tarantula"],
 #   "flies": ["horse", "house"]
#}

#bugs.items() huh

#Nested listtttt
#nested_list = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

#print(nested_list[2][1])

stars_data = {
    "name": ["Sirius", "Vega", "Altair"],
    "magnitude": [-1.46, 0.03, 0.77],
    "distance_ly": [8.6, 25.0, 16.7],
    "constellation": ["Canis Major", "Lyra", "Aquila"]
}

for name in stars_data.values():
    print(name)

def count_close_stars(data):
    count = 0
    for distance in data["distance_ly"]:
        if distance < 20:
            count += 1
    return count