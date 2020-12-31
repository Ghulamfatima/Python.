#NUMBERS
#TYPE
A = 3
S = 4.5
D = "FATIMA"
G = 6J
print(type(A))
print(type(G))
print(type(S))
print(type(S))
b = float(S)
#RANDOM NUMBERS
import random
print(random.randrange(1,4))
#LIST
list1 = [ 1,3,4,45,63,87,98,89,76,56,46,49,490]
list2 = [8,9,10,20,15,25,"pakistan","karachi"]
print(list1)
print(list2)
#length of list
print(len(list1))
print(len(list2))
#access lis items
print(list1[4:8])
print(list2[3:8])
print(list1[:7])
print(list2[6:])
#SORT LIST
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
#ADD ITEMS
list1.append("orange")
print(list1)
list1.insert(2, "orange")
print(list1)
#type
print(type(list1))
#change items of lists
list1[2:7]="16,12,25,27,28"
print(list1)
#copy lists
list1 = list1.copy()
print(list1)
list2 = (list2)
print(list2)
#TUPLES
tuple1 = ("onion","ptato","tomato","bengan","ptato")
tuple2 = ("apple","banana","orange","pear","grapes","peach","mango")
print(len(tuple1))
print(tuple)
print(type(tuple))
print(tuple1[2:5])
print(tuple1[-3])
print(tuple1[1])
#Addition and multiplication of tuple.
a=tuple1+tuple2
b=tuple1*3
#unpacking of tuples
print("ptato")
print("onion")
print("grapes")
print("pear")
#Dictionaries
country = {"Europe":10,"india":20,"USA":30,"54":40,"pakistan":50 ,"coria":60}
print(country["USA"])
#Cheack keys of dictionary
print(country.keys())
#cheak type of dictionary
print(type(country))
#change dictionary
country["USA"] = 30
print(country)
#UP DATE DICTIONARY
country.update({"pakistan":55})
print(country)
#delete dectionary
del(country["coria"])
print(country)
country.pop("india")
print(country)
