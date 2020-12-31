
#------------------------------------------------------Methods-----------------------------------------------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties

p1.age = 40
print(p1.age)


#-------------------------------------------------------Functions-------------------------------------------------------------------------------------------


#Create a function:
def my_fellows():
     print("Hello")
     print("How are you")
     my_fellows()
#Call a function:
def my_fellows():
     print("Hello")
     print("How are you")
my_fellows()

#Arguments in functions:
def my_fellows(fname):
    print(fname + " " + "is my fellow")
my_fellows("komal")
my_fellows("ayesha")
my_fellows("sumaira")
#Number of Arguments:
def my_fellows(fname,lname):
    print(fname+"  "+lname)
my_fellows("Ayesha","shocket")
my_fellows("Kinat","komal")
my_fellows("Sumaira","bibi")
#pass two arguments and get 1 argument:
def my_fellows(fname,lname):
    print(fname+"  "+lname)
my_fellows("ayesha", "shokat")# if we get 1or3 arguments in function . then error will be occure.
#Arbitrary Arguments, *args:
def my_fellows(*fellows):
      print("my class fellows is="+ " "+ fellows[1])
my_fellows("ayesha", "komal", "sumaira")
#Keyword Arguments:
def my_fellows( fellow1,fellow2,fellow3 ):
    print("my best fellow is"+fellows[3])
    my_fellows(fellow1= "ayesha", fellow2=  "komal" , fellow3= "sumaira")
#By passing the Arbitrary Keyword Arguments, **kwargs:
def my_friends(**friends):
  print("Hes last name is " + friends["lname"])
my_friends(fname = "sumaira", lname ="bibi")
#By passing Default Parameter Value:
def my_function(country = "USA"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("india")
my_function("pakistan")
#By Passing a List as an Argument:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "grapes","orange"]

my_function(fruits)


#Return Values:
def my_function(x):
  return 4 * x

print(my_function(56))
print(my_function(76))
print(my_function(9))
#The pass Statement:
def  my_function():
    pass
# having an empty function definition like this, would raise an error without the pass statement


#-------------------------------------     LAMBDA expression    -----------------------

# single statement

j = lambda i : i+ 20
print(j(10))

j = lambda i : i/ 20
print(j(5))


#Using lambda in function to make a value double.

def myfunc(n):
  return lambda i : i * n
mydoubler = myfunc(2)

print(mydoubler(22))

#Using lambda in function to make a value triple.

def myfunc(n):
  return lambda i : i * n

mydoubler = myfunc(7)
mytripler = myfunc(8)

print(mydoubler(34))
print(mytripler(43))

#---------------------------------------------------------     Nested statements    -----------------
#Loops Inside Loops--

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#if inside if statement
i = 50

if i > 34:
  print("Above twenty,")
  if i > 25:
    print("and also above 34!")
  else:
    print("but not above 34.")

