#Exception Handling.
try:
  print(x)
except:
  print("An exception occurred")
#Many Exceptions.
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#Else.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#Finally.-----------
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#Raise an exception.
# raise keyword is used to raised an exception
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")