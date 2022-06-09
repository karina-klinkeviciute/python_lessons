numbers = [2, 5, 8, 3, 4, 10]

# squares = []
# for number in numbers:
#     squares.append(number**2)
    
squares = [number**2 for number in numbers]

ages = {"Jane": 32, "Tom": 25, "Linda": 74, "Ted": 65}

# for name, age in ages.items():
#     print(name, age)

names = [age for age in ages.values()]

print(names)
