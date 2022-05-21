names = ["Kate", "Jhon", "Lisa"]

names[1] = "John"

print(names)

names.append("Brad")

names2 = ["Jane", "Tom", "Linda", "Ted"]

all_names = names + names2

print(all_names)

length = len(names)

print(length)

if length > 5:
    print names[:5]
    
