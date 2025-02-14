entered_value = input("Enter your value: ")
if not entered_value.isnumeric():
    print("Enter a number")
    exit(0)

score = int(entered_value)
if score >=80:
    print("A")
elif score >=71 and score <= 79:
    print("B")
elif score >=61 and score <= 69:
    print("C")
else:
    print("C+")