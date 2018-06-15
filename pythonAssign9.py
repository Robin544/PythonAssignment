# Create a circle class and initialize it with radius
# Make two methods getArea and getCircumference inside this class

class Circle():                   # Creating a circle
    radius = 0
    def __init__(self, radius):         # Initializing radius of circle
        self.radius = radius
    def getArea(self):          # Calculating area of circle
        print(("\n Area of given circle : %02f")%(3.14*self.radius*self.radius))
    def getCircumference(self): # Calculating circumference
        print(" Circumference of given circle : ", 2*3.14*self.radius)
ob = Circle(6)        # Creating object of circle class
ob.getArea()         # Calling getArea()
ob.getCircumference() # Calling getCircumference



# Create a Student class and initialize it with name and roll number
# Make methods to display all information of the student

class Student():
    stream = "CSE"
    year = "3Srd"
    def __init__(self, name, roll):
        self.name = name
        self.rollNumber = roll
    def display(self):
        print("\n Name : ",self.name, "\nRoll-Number : ",self.rollNumber,
              "\n", "Stream : ", self.stream, "\nYear : ", self.year)
print("\n")
ob1 = Student("Pooja",11)
ob1.display()
ob2 = Student("Robin", 12)
ob2.display()



# Create a Temprature class. Make two methods:
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius

class Temprature():
    def convertFahrenheit(self, c):         # It will take celsius and will convert it into Fahrenheit
        print("\n\n", c,"Degree Celsius in Fahrenheit: ", (c*(9/5))+32)
    def convertCelsius(self, f):            # It will take Fahrenheit and will convert it into Celsius
        print("", f, "Fahrenheit  in Celsius: ", (f-32)*(5/9))
ob3 = Temprature()
ob3.convertFahrenheit(12)
ob3.convertCelsius(12)



# Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings
# Make methods to
# 1. Display-Display the details
# 2. Update- Update the movie details

class MovieDetail():
    def __init__(self, mName, aName, YOR, mRating):     # Print the movie details
        self.mName = mName
        self.aName = aName
        self.yor = YOR
        self.rating = mRating
    def display(self):          # Display Function
        print("\n\nMovie name : ", self.mName)
        print("Artist name : ", self.aName)
        print("Year of release : ", self.yor)
        print("Ratings : ", self.rating)
    def update(self):           # Update function to update the movie detail
        self.mName = input("\nEnter the new movie name : ")
        self.aName = input("Enter the artist name : ")
        self.yor = int(input("Enter the new year of release : "))
        self.rating = float(input("Enter the new ratings : "))
ob4 = MovieDetail("Rustam", "Akshay Kumar", 2017, 9.5)
ob4.display()
ob4.update()
ob4.display()



# Create a class Expenditure and initialize it with expenditure, savings. Make the following methods:
# 1. Display expenditure and savings
# 2. Calculate total salary
# 3. Display salary

class Expenditure():
    def __init__(self, exp, save):
        self.expend = exp
        self.saving = save
        self.salary = 0
    def display(self):
        print("\n\nExpenditure : ", self.expend)
        print("Savings : ", self.saving)
    def cal_total(self):
        self.salary = self.expend + self.saving
    def dis_salary(self):
        print("Salary is : ", self.salary)
obj = Expenditure(70000, 80000)
obj.display()
obj.cal_total()
obj.dis_salary()



# Finally done

print("\n\nDone")