# ----------------------->class/objects<---------------------------
# create class
class my_friends:
    x = 2
print(my_friends)
# create object
p1 = my_friends()
print(p1.x)
# --init--function
class friend:
    def __init__(self, name, age):
     self.name = name
     self.age = age
p1 = friend("sumaira is my friend and she is", "23 years old")
print(p1.name)
print(p1.age)
# object methods
class friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def her_personality(self):
        print("Her name is " + self.name + " "+"and her age is " + str(23))
p1 = friend("sumaira", 23)
p1.her_personality()
# self parameters
class person:
    def __init__(myfriendobject, name, age):
        myfriendobject.name = name
        myfriendobject.age = age
    def my_friend(self):
        print("Her name is " + self.name + " " + "and her age is " + str(23))
p1 = person("sumaira", 23)
p1.my_friend()
# modify object properties
class person:
    def __init__(myfriendobject, name, age):
        myfriendobject.name = name
        myfriendobject.age = age
    def my_friend(self):
        print("Her name is " + self.name)
p1 = person("sumaira", 22)
p1.age = 24
print(p1.age)
# delete objetc properties
# del p1.age
# print(p1.age)
#pass statement
class person:
    pass
#----------------------------------------->Inheritance<----------------------------
# create parent class
class teacher:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def my_teacher(self):
        print(self.firstname, self.lastname)
p1 = teacher("areeba", "noor")
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
p1 = Student("ghulam", "fatima")
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
p1 = student("sumaira", "bibi")
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
p1 = student("kainat", "komal")
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
p1 = student("sumaira", "bibi", 2020)
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
p1 = student("sumaira", "bibi", 2020)
p1.welcome_family()
# if we use the method in child class same as the parent class then parent class method will be overridden.
#polymorphism----
# Polymorphism with Function and Objects
class my_friends():
    def friend(self):
        print("my_friends")
    def personality(self):
        print("good")
class nida_friends():
    def friend(self):
        print("aqsa_friends")
    def personality(self):
        print("good")
def func(obj):
    obj.friend()
    obj.personality()
obj_my_friends = my_friends()
obj_aqsa_friends = nida_friends()
func(obj_my_friends)
func(obj_aqsa_friends)
# polymorphism with class method.
class my_friends():
    def friend(self):
        print("my_friends")
    def personality(self):
        print("good")
class aqsa_friends():
    def friend(self):
        print("nida_friends")
    def personality(self):
        print("good")
obj_my_frnd = my_friends()
obj_nida_frnd= nida_friends()
for friends in (obj_my_friends, obj_aqsa_friends):friends.friend()
friends.personality()
#Polymorphism with Inheritance
class humans:
     def intro(self):
        print("There are two types of humans")
     def nature(self):
        print("Humans can walk on their feet")
class man(humans):
    def nature(self):
        print("mans work independently")
class women(humans):
    def nature(self):
        print("womens cannot work independently")
obj_humans = humans()
obj_man = man()
obj_women = women()
obj_humans.intro()
obj_humans.nature()
obj_man.intro()
obj_man.nature()
obj_women.intro()
obj_women.nature()
#------------------------------>Encapsulation<------------------------
# encapsulation basically means binding up of data in a single class.
class friend(object):
    def __init__(self):
     self.name = "sumaira"
     self._age = 25
     self.salary = 6000
p1 = friend()
print(p1.name)
print(p1._age)
print(p1.salary)
#
class mobile_phone:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling Price of mobile: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = mobile_phone()
c.sell()
# change the price
c.__maxprice = 1000
c.sell()
# using setter function
c.setMaxPrice(1000)
c.sell()
#----------------------------------->Abstraction<-----------------------
from abc import ABC
class birds(ABC):
   def fly(self):
        pass
class parrots(birds):
    def fly(self):
        print("I can fly in air")
class sparrows(birds):
    def fly(self):
        print("I can fly in air")
class peacock(birds):
    def fly(self):
        print("I can fly in air")
class crow(birds):
    def fly(self):
        print("I can fly in air")
p = parrots()
p.fly()
s = sparrows()
s.fly()
p = peacock()
p.fly()
c = crow()
c.fly()
#----------------------->overloading<--------------------------
# operator overloading
class friend:
    def __init__(self, f):
        self.f = f
# adding two objects
    def __add__(self, other):
        return self.f + other.f
    def __mul__(self, other):
        return self.f * other.f
    def __eq__(self, other):
        return self.f == other.f
    def __lt__(self, other):
        return self.f < other.f
    def __gt__(self, other):
        return self.f > other.f
    def __ge__(self, other):
        return self.f >= other.f
    def __le__(self, other):
        return self.f <= other.f
p1 = friend(3)
p2 = friend(2)
p3 = friend("Geeks")
p4 = friend("For")
print(p1 + p2)
print(p3 + p4)
print(p1 * p2)
print(p1 == p2)
print(p1 < p2)
print(p1 > p2)
print(p3 >= p4)
print(p4 <= p3)
# overloading of built in function
class friend:
    def __init__(self, best_friends, length_friends):
        self.name = list(best_friends)
        self.quantity = length_friends
    def __len__(self):
        return len(self.name)
friend = friend(['sumaira', 'kainat', 'sana', 'zainab'], 'aqsa')
print(len(friend))
# user defined functions
class Teacher:
    def student(self, name=None):
        if name is not None:
            print('Hey ' + name)
        else:
            print('Hey ')
#Creating a class instance
std = Teacher()
# Call the method
std.student()
#call a method and pass a parameter
std.student("Fatima")