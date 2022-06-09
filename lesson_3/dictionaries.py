person1 = {"ім'я": "Наталія", "місто": ["Херсон", "Kaunas", "Київ"], "вік": 30}
person2 = {"ім'я": "Дмитро", "місто": "Київ", "вік": 25}

person3 = dict()

person4 = {}

cities = ["Kaunas", "Vilnius", "London"]

people2 = []

people3 = list()

people = [person1, person2]

# for person in people:
#     print("Name: ", person["ім'я"], "cities: ", person["місто"], "age: ", person["вік"]) 
    
    
# for person in people:
#     name = person["ім'я"]
#     city = person["місто"]
#     print(f"Name: {name}, city: {city}, age: {person['вік']}")
    

# print(person1.keys())
# print(person1.values())

ages = {"Jane": 32, "Tom": 25, "Linda": 74, "Ted": 65}

# for name, age in ages.items():
#     print(f"{name} is {age} years old")


# # добовления

person1["робота"] = "manager"
person2["робота"] = "teacher"
# print(person1)
# print(person2)

ages["Tom"] = 26

ages2 = {"Наталія": 20, "Дмитро": 45}

ages3 = {"John": 21, "Jane": 22}

ages.update(ages2)

# ages4 = ages2 | ages3

print(ages)
print(ages2)
# print(ages4)

print(len(ages))
