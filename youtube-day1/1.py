# Print Hello World.
print("Hello, World!")
print("\n")

# Print shapes.
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")
print("\n")

# Lists in Python
my_list = ["Darshan", 3, 2.03, "Help", "Nigger"]
# Index:  |    0.   | 1. |  2. |   3. |   4.   |

print(my_list)
print("\n")

print(my_list[3])
print("\n")

print(my_list[1:3])
print("\n")

# List Functions
my_list.append("Noob")
print(my_list)
print("\n")

my_num = [69, 69, 169, 69, 269, 69]
my_list.extend(my_num)
print(my_list)
print("\n")

my_list.insert(2, "Black Man")
print(my_list)
print("\n")

my_list.remove("Darshan")
print(my_list)
print("\n")

my_list.pop()
print(my_list)
print("\n")

print(my_list.index("Black Man"))
print("\n")

print(my_list.count(69))
print("\n")

my_num.sort() #not supported with the combination of String and numbers
print(my_num)
print("\n")

my_num.reverse()
print(my_num)
print("\n")

my_list.clear()
print(my_list)
print("\n")

my_num2 = my_num.copy
print(my_num2)