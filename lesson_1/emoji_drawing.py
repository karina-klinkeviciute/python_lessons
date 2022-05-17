# for i in range(3):
#     for j in range(10):
#         print("💙", end="")
#     print("")
# for i in range(3):
#     for j in range(10):
#         print("💛", end="")
#     print(" ")

# print(" ")

# for i in range(2):
#     for j in range(10):
#         print("🟡", end="")
#     print("")
# for i in range(2):
#     for j in range(10):
#         print("🟢", end="")
#     print("")
# for i in range(2):
#     for j in range(10):
#         print("🔴", end="")
#     print("")


# for row in range(10):
#     for symbol in range(row):
#         print("🟢", end="")
#     print("\n")


# for row in range(8):
#     for symbol in range(8 - row):
#         print(" ", end="")
#     for space in range(row):
#         print("🔵", end="")
#     print("\n")
    
    
# for row in range(10):
#     for symbol in range(10-row):
#             print("  ", end="")
#     for space in range(row):
#         print("🟡"*2, end="")
    
#     print("🟡")
    
    
clocks = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]

import time

for clock in clocks:
    print(clock)
    time.sleep(1)