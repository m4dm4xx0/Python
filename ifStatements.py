# if = Do some code only if some condition is True
#      Else do something else

age = int(input('Enter your age: '))

if age >= 18:
    print("You are now signed up")
elif age<0:
    print("You haven't been born yet:")

else:
    print("You must be an adult to sign up")
