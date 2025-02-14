# creating a list  --[] --mutable (can be changed) (allows duplicates)

scores = [92, 65, 45, 50, 37, 32, 75, 85]

print(scores[0]) # 1st
print(scores[3]) #4th

# adding values in a list
scores.append(71)
print(scores)

# removing values from a list
scores.pop(2) # 45
print(scores)

# Sorting values in a list
scores.sort(reverse=True) # Sorts from lowest to highest (default) (if put reverse=true --from highest to lowest)
print(scores)