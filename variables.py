#variable is a container for a value (string, integer, float, boolean)
#            a variable behavves as if it was the vale it contains

# Strings
first_name = "Lyds"
food = "pizza"
email = "lyds@example.com"
#printing using the f string
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} km")

# Boolean
is_student = True
for_sale = False
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("You are offline")
