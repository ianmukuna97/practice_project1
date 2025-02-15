# loops

# while loop
while True:
    print("Hello, world")
    break # stops the loop


scores= [50, 45, 60, 70, 65, 37, 42, 56, 80, 75, 82]

# for loop
for score in scores:
    if score >= 50 and score <=70 and score % 2 == 0: # Values btwn 50 and 70 which are divisible by 2-- % -- modulus
      print(score)
