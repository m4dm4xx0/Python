import math


x = 3.14
y = -4
z = 5
result = round(x)
result1 = abs(y) #absolute value 
resultPower = pow(x,z)
maximum= max(x,y,z)
minimum = min(x,y,z)
print(result)
print(result1)
print(resultPower)
print(maximum)
print(minimum)

print(f"The math pi is: {math.pi}")
print(f"The math expo constant is: {math.e}")
print(f"Square root of 5 is {math.sqrt(5)}")
print(f"ceil of a 5.1 rounds it up : {math.ceil(5.1)}") #6
print(f"floor of a 5.9 rounds it down : {math.floor(5.9)}") #5


#calculate the circumference of a circle
r = float(input("please enter the radius of the circle "))
print(f"the circumference of the circle is {round(r*math.pi*2,2)} cm") # round to two digits
