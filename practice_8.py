# Dictionary --mutable (can be changed)
# dictionary --{}  , tuple--(),  list--[]


student = {"name": "John James", "id":4567, "age":25, "gender": "M"}

print(student["name"]) # key value (prints only the name)
print(student)

# adding value to a dictionary
student["weight"] = 70
print(student)

# set -- only one existence per item , also unordered (used in organizing emails --removing duplicates if are any)
people = {"Jane", "John", "James", "Natasha", "Zoe", "Zoe"} #(omits the duplicate value)
print(people)

# to discard/remove
people.discard("John")
print(people)

#to add a set
people.add("Hank")
print(people)
print(len(people)) # count

# git init
# git add.
# git commit -m "practice_project
# git remote add origin https:link
# git push -u origin master