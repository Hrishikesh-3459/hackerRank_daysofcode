class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores
    
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        ave = (sum(self.scores) / len(self.scores))
        # print(ave)
        if (ave >= 90 and ave <=100):
            return 'O'
        if (ave >= 80 and ave <90):
            return 'E'
        if (ave >= 70 and ave <80):
            return 'A'
        if (ave >= 55 and ave <70):
            return 'P'
        if (ave >= 40 and ave <55):
            return 'D'
        if (ave < 40):
            return 'T'



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
