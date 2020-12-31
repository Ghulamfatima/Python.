#-------------------------------- pythan LOOPs --------------------------

#while loop

a = 2
while a < 4:
     print(a)
     a += 1

#-------- using break statemen  ---------

a = 2
while a < 5:
    print(a)
    if a == 3:
      break
    a += 1

#-------  continue statement  ------------

a = 2
while a < 5:
   a += 1
   if a == 3:
     continue      #by using continue statement all numbers are continued but we stop the current  statement
   print(a)

#---------- by using else statement -------------

a = 1
while a < 5:
    print(a)
    a += 1


else:
    print("a is not loger less than 9")

# ----------   FOR LOOP  -------------



fruits = ["apple", "banana", "mango","orange"]
for y in fruits:
    if y == "mango":
        break
    print(y)





#-------------------------  PYTHANS CONDITIONS AND IF STATEMENTS  ----------------------

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b


#Using if statement:-------------
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif

a = 23
b = 23
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

#else statement ------------

a = 43
b = 28
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than  b")
#Short Hand If-------

if a > b:
    print("a is greater than b")

#Short Hand If Else:

a = 43
b = 35
print("A") if a > b else  print("B")

#IF WITH AND   ---------

a = 50
b = 30
c = 990
if a > b and c > a:

     print("both conditions are true")

#IF OR statement---------

a = 50
b = 30
c = 70
if a > b or a > c:
    print("one condition are true")

# Nested if statement

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above  20.")

# The pass statement---------

a = 33
b = 200

if b > a:
  pass


# ------ List Comprehension --------------------
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#------------ ----------------------------------



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

