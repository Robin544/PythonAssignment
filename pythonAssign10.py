# Let’s dig the python OOPs concept deeper.


# Create a class Animal as a base class and define method animal_attribute.
# Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    """
    This is the Animal class to show some characteristics of animals.
    """
    legs = 0
    eyes = 0

    def animal_attribute(self, legs, eyes):
        """
        This is the function to define the legs and eyes of animal.
        """
        self.legs = legs
        self.eyes = eyes
        print(" It has ", self.legs,  "legs")
        print(" It has ", self.eyes, "eyes")


class Tiger(Animal):
    """
    This is the derived class of Animal class i.e. it inherits the feature of the base class.
    """
    def __init__(self, speed: str):
        """
        This is the constructor of this class.
        speed parameter defines the speed of tiger.
        """
        self.speed = speed
        print("\n Tiger is %s than others" % self.speed)


"""
Creating object of derived class.
"""
obj1 = Tiger("very fast")

"""
Accessing base class method using derived class object.
"""
obj1.animal_attribute(4, 2)


# What will be the output of following code.


class A:
    """
    This is the base class
    """
    def f(self):
        """
        This function will return calling of the other function named as g().
        """
        return self.g()

    def g(self):
        """
        This function will return "A"
        """
        return 'A'


class B(A):
    """
    This is derived class of class A
    """
    def g(self):
        """
        This function will return "B"
        """
        return 'B'


"""
creating object of class A
"""
a = A()
"""
creating object of class B
"""
b = B()
"""
a.f() will call f() of class A which will call its own g()
b.f() will call f() of its base class A which will call g() of class B
"""
print("\n\nFirst output : ", a.f(), b.f())
"""
a.g() will call g() of class A
b.gg() will call g() of class B 
"""
print("Second output : ", a.g(), b.g() + "\n")


# Create a class Cop Initialize its name, age , work experience and designation.
# Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a particular cop
# and make it available for mission.

class Cop:
    """
    This is Cop class (Base Class).
    """
    def __init__(self):
        """
        This is the constructor of the class to initialize name,
        age, work experience and designation of the cop.
        """
        self.cop_name = "Robin Singh"
        self.cop_age = 22
        self.work_exp = 1
        self.designation = "SSP"

    def add_details(self, cop_name, cop_age, work_exp, designation):
        """
        This is add function to add details of Cops.
        """
        self.cop_name = cop_name
        self.cop_age = cop_age
        self.work_exp = work_exp
        self.designation = designation

    def display(self):
        """
        This  function display all details of Cop.
        """
        print("\nCop name : ", self.cop_name)
        print("Cop age : ", self.cop_age)
        print("Cop work experience : ", self.work_exp)
        print("Cop designation : ", self.designation)

    def update(self):
        """
        This function used to update the details of Cop.
        """
        self.cop_name = input("\nEnter the new Cop name : ")
        self.cop_age = int(input("Enter the Cop age in years : "))
        self.work_exp = int(input("Enter the Cop work experience in years : "))
        self.designation = input("Enter the Cop designation : ")


class Mission(Cop):
    """
    This is derived class and inherits the Base class Cop.
    """
    mission = ""

    def add_mission_details(self):
        """
        This function add mission details of the Cop.
        """
        self.mission = input("Enter the mission : ")

    def display1(self):
        """
        This function display mission of the Cop
        """
        print("The mission of the Cop : ", self.mission)


""" 
Creating object of class Cop.
"""
ob1 = Cop()
"""
Calling of base class functions.
"""
ob1.add_details("Pooja", 23, 3, "SP")
ob1.display()
ob1.update()
""" 
Creating object of class Mission.
"""
ob2 = Mission()
"""
Calling of derived class functions.
"""
ob2.add_mission_details()
ob2.display()       # This is the base class(Cop) function.
ob2.display1()


# Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area.

class Shape:
    """
    This is base class Shape.
    """
    def __init__(self):
        """
        This is constructor of base class.
        Here length is the length of shape.
        and breadth is the breadth of shape
        """
        self.length = float(input("Enter Length : "))
        self.breadth = float(input("Enter Breadth : "))

    def area(self):
        """
        This function return the area of shape.
        """
        return self.length*self.breadth


class Rectangle(Shape):
    """
    This is derived class which inherits class Shape.
    """
    def rect(self):
        """
        This function print area of rectangle by calling function area() of parent class Shape.
        """
        print("Area of rectangle : ", self.area())


class Square(Shape):
    """
    This is derived class which also inherits class Shape.
    """
    def sqr(self):
        """
        This function print area of square by calling function area() of parent class Shape
        only when length and breadth of shape are equal.
        """
        if self.length == self.breadth:
            print("Area of square : ", self.area())
        else:
            print("Sides are not equal \nPlease enter same side")


print("\n\nRectangle -->")
"""
Creating object of Rectangle class which implicitly call base class Constructor.
"""
object2 = Rectangle()
"""
Calling rect() of Rectangle class using Rectangle class object.
"""
object2.rect()
print("\nSquare -->")
"""
Creating object of Square class which implicitly call base class Constructor.
"""
object3 = Square()
"""
Calling sqr() of Square class using Square class object.
"""
object3.sqr()


# Finally done

print("\n\nDone")
