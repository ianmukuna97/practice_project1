# if statements

entered_value = input("Enter the score: ") # string
if not entered_value.isnumeric():
   print("Please enter a numeric value")
   exit(0)

# print(type(entered_value))
# print(type(52.88)) # float
# print(type(72)) # integer
#
# is_male= True
# print(type(is_male)) # Boolean


score = int(entered_value) # convert the string to a number/integer

if score >= 78:
    print("A")
elif score >= 71 and score <= 77:  # >= upper boundary, <= lower boundary
    print("A-")
elif score >= 64 and score <= 70:
    print("B+")
elif score >= 57 and score <= 63:
    print("B")
elif score >= 50 and score <= 56:
    print("B-")
elif score >= 43 and score <= 49:
    print("C+")
# elif score >= 36 and score <= 42:
#     print("C")
# elif score >= 29 and score <= 35:
#     print("C-")
# elif score >= 22 and score <= 28:
#     print("D+")
# elif score >= 15 and score <= 21:
#     print("D")
# elif score >= 8 and score <= 14:
#     print("D-")
# elif score >= 1 and score <= 7:
#     print("E")
else:
    print("C") # any other value not mentioned above


