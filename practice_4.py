# maths functionality
import math

x = 99
square_root = math.sqrt(x)
print("Root is :", square_root)

rounded = round(square_root, 2) # Rounded to 2 decimal places
print("Rounded to 2 decimal places:" ,rounded)

#functions
# print()

#args
# print( x+y =args)

#call a function
y = round(8.2828282, 3) # Rounded to 3 decimal places
print(y)

print(round(4.444444, 1))

print(math.pow(2, 3))
print("--------")

name = "John, james, Simon"
print(len(name))
print(name[0])
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

post = "This thing is so easy and fluent"
new_post = post.replace("fluent", "flowing")
print(new_post)
