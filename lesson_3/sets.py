fruits = {"apple", "orange", "pear", "plum", "cherry"}
berries = set(["cherry", "blueberry", "strawberry", "tomatoe"])
vegetables = {"potato", "tomatoe", "eggplant", "cabbage"}

food = input("enter fruit or berry ")
if food in fruits:
    print("it's fruit")
elif food in berries:
    print("it's a berry")
elif food in vegetables:
    print("it's a vegetable")

print(fruits)
fruits.add("banana")
print(fruits)

foods = {"bread", "salad"}

foods.update(fruits)

print(foods)


# remove and discard

