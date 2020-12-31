#SETS
set1 = {"banana","apple","mango","orange","grapes","1"}
print(set1)
#length
print(len(set1))
#data type
set2 = {1,2,76,87,65,44,3,3,222,2,2,2,22,33,44,}
print(type(set1))
print(type(set2))
print("HY")
#find this item are present in set or not
set3 = {"name",435,"apple","abc","banana"}
print("pear" in set3)
set2 = {1,2,76,87,65,44,3,3,222,2,2,2,22,33,44,}
print( 5  in set2)
print("HY")
#add new item
set1.add("pear")
print(set1)
#add sets
set1.update(set3)
print(set1)
#delete sets items
set2.remove(44)
print(set2)
set1.discard("mango")
print(set1)
#delete by pop method
print("HY")
set = set1.pop()
print(set)
print(set1)
#join two sets by union method
set1 = {"a","b","d"}
set2 = {5, 6, 7, 8, 9, 19, 45,6}
set3 = set1.union(set2)
print(set3)
#join two sets by update method
set1.update(set2)
#show duplication items
set1.intersection_update(set2)
print(set1)
#keep all items except repeted items
set1.symmetric_difference_update(set2)
print(set1)

#TUPLES -------------------

tuple1 = ("onion","ptato","tomato","bengan","ptato")
tuple2 = ("apple","banana","orange","pear","grapes","peach","mango")
print(tuple1)
print(len(tuple1))
print(type(tuple2))
print(tuple1[2:5])
print(tuple1[-3])
print(tuple1[1])

#Addition and multiplication of tuple.
a=tuple1+tuple2
b=tuple1*3
print(a)
print(b)
#unpacking of tuples
print("ptato")
print("onion")
print("grapes")
print("pear")
#BOOLEAN
print(set2>set3)
print(set2==set3)