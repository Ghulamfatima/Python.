#------------  Classes/Objects------------------

#create class:

class my_class:
  x = 3
print(my_class)

#create object-------

p1 = my_class()
print(p1.x)

#init- Function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("summaira is my friend", 36)

print(p1.name)
print(p1.age)

#Object Methods--

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("fatima", 20)
p1.myfunc()

#self Parameter------

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("fatima", 36)
p1.myfunc()

# modify object properties
class person:
    def __init__(myfriendobject, name, age):
        myfriendobject.name = name
        myfriendobject.age = age
    def my_friend(self):
        print("Her name is " + self.name)
p1 = person("sumaira", 22)
p1.age = 23
print(p1.age)
#

#delete object properties
#del p1.age
#print(p1.22)


#----------------------------->Inheritance<-----------------------
# create parent class
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
p1 = teacher("Rida", "Mariyum")
p1.my_teacher()
# create child cass
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
class Student(teacher):
    pass
p1 = Student("Tasneem", "Abdul Raheem")
p1.my_teacher()
# add __init__function in child class
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
class student(teacher):
    def __init__(self, fname, lname):
        teacher.__init__(self, fname, lname)
p1 = student("Aadila", "Fatima")
p1.my_teacher()
# use super function
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
class student(teacher):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
p1 = student("Mahnoor", "Khan")
p1.my_teacher()
# add properties
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
class student(teacher):
    def __init__(self, fname, lname, year): # add year parameter
        super().__init__(fname, lname)
        self.weddingyear = year
p1 = student("Sumaira", "Fatima", 2020)
print(p1.weddingyear)
# add methods
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
class student(teacher):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.wedding_year = year
    def welcome_family(self):
        print("Welcom", self.firstname, self.lastname, "in your new home in", self.wedding_year)
p1 = student("Sumaira", "Fatima", 2020)
p1.welcome_family()
# if we use the method in child class same as the parent class then parent class method will be overridden.

#methods

class Person:
    def _init__(self, name, age):
        self.name = name
        self.age = age
    def my_friend(self):
        print("Hello my name is " + self.name)
p1 = person("sumaira", 22)
p1.my_friend()
#modify object properties
p1.age = 25
print(p1.age)
# delete object properties
#del p1.age
# print(p1.age) ........it causes error because there' no more p1 value
# delete objects.........it causes error because there' no more p1 value
#del p1
# print(p1)
# pas statement
class Person:
    pass
#--------------------------->Special Functions<---------------------------
# Dunder or magic function __add__()
class my_friend:
    def __init__(self, friend):
     self.friend = friend
    def __add__(self, other):
        return self.friend + " and " + other.friend
Sumaira = my_friend("Sumaira is my friend and she is 22 years old.")
kinat = my_friend("Kinat  is my friend and she is 24 years old.")
print("Sumaira" + "Kinat")
# Dunder or magic function __mul__()
class my_friends:
    def __init__(self, friend):
     self.friend = friend
    def __mul__(self, other):
        return self.friend * other.friend
    def __eq__(self, other):
        return self.friend == other.friend
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.friend < other.friend
    def __len__(self):
        return self.friend
    def __le__(self, other):
        return self.friend <= other.friend
    def __ge__(self, other):
        return self.friend >= other.friend
Sumaira_salary = my_friends(200)
kinat_salary = my_friends(300)
print(Sumaira_salary * kinat_salary)
print(Sumaira_salary == kinat_salary)
print(Sumaira_salary != kinat_salary)
print(Sumaira_salary < kinat_salary)
print(len(Sumaira_salary))
print(Sumaira_salary <= kinat_salary)
print(Sumaira_salary >= kinat_salary)

