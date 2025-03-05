class Criminal:
    def __init__(self, name, id_number, gender, crime):
        self.name = name
        self.id = id_number
        self.gender = gender
        self.crime = crime
    def show_details(self):
        print(f"Name: {self.name} \nID: {self.id} \nIssue: {self.crime} \nGender: {self.gender}") #\n----new line character

# store data and manipulate data
c1= Criminal("John James","25555333","Male","Stealing computer parts")
c1.show_details()

