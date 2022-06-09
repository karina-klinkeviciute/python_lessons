a = [1, 1, 2, 3, 5, 8, 13, 21, 4, 55, 89]
numbers = [3, 5, 4]

c = int(input("enter a number "))

b = []

for number in a:
    if number < c:
        b.append(number)

# b = [number for number in a if number < c]

print(b)
