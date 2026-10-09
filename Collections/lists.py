# collection = single "variable" used to store multiple values
#   List    =[] ordered and changeable. Duplicates OK
#   Set     ={} unordered and immutable, but add/Remove OK. NO Duplicates
#   Tuple   =() ordered and unchangeable. Duplicates OK. FASTER

fruits = ["Apple","Orange","Banana","Coconut"]
print(fruits[:3]) #from 0 to 3 or 0:3
print(fruits[::2]) #every second element starting from index 0
print(fruits[::-1]) # fruits backwards
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("Apple" in fruits)
#for fruit in fruits:
 #   print(fruit)
fruits[0] = "pineapple"
print(fruits)
#helpful functions: append, remove, insert, sort, reverse, clear, index, count
