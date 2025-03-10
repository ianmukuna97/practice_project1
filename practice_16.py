# Error handling

x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")
z =input("Enter 3rd number: ")

try:
    x_num = int(x) # int --converting string to integer
    y_num = int(y)
    z_num = int(z)

    print(x_num * y_num * z_num)
except:
    print("Please enter valid numbers")