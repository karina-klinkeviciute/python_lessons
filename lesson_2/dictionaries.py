person1 = {"ім'я": "Наталля", "місто": "Херсон", "вік": 30}
person2 = {"ім'я": "Дмітро", "місто": "Київ", "вік": 25}

people = [person1, person2]

for person in people:
    print("Name: ", person["ім'я"], "city: ", person["місто"], "age: ", person["вік"]) 
    
    
for person in people:
    name = person["ім'я"]
    city = person["місто"]
    print(f"Name: {name}, city: {city}, age: {person['вік']}")
    

