#-------------------------------     Basic operators  ----------------
a = 4
b = 3
print(a+b)

#---------------------       Python Arithmetic Operators  -------------------

a = 4
b = 4
print(a+b)
print(a/b)
print(a-b)
print(a*b)
print(a%b)
print(a**b)
print(a//b)
#----------------------------------------    Assignment Operators    ------------
a = 4
print(a)
# a = a+3 same for all
a +=3
print(a)
a -=3
print(a)
a *=3
print(a)
a /=3
print(a)
a %=3
print(a)
a //=3
print(a)
a **=3
print(a)

print("bitwise operator")#------------------------------------------      Bitewise operators       -----------------------------------------
print("hy")
i = 7
i &= 3
print(i)
i = 10
i |= 2
print(i)
i = 5
i ^= 2
print(i)
i = 7
i >>= 4
print(i)
i = 13
i <<= 4
print(i)

#---------------------        identity  operators         -------------------------------------------

i = ["apple", "banana"]
j = ["apple", "banana"]
k = i
print(i is k)
# returns True because k is the same object as i
print(i is k)
# returns False because i is not the same object as j, even if they have the same content
print(i == j)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to j

#--------------------------------------------   Membership operators  --------------------------------------------------

i = ["apple", "banana","grapes"]
print("banana" in i)       # returns True because a sequence with the value "banana" is in the list.
i = ["apple", "banana","grapes"]
print("pear" in i)       # returns True because a sequence with the value "banana" is in the list.

#------------------------------------------  comparison operators     --------------------------------------------------

x = 3
y = 2
print(x == y)   # returns False because 3 is not equal to 2.
print(x>=y)     # returns true because 3 is greater than 3
print(x<=y)     # returns false because 3 is greater than  2.
print(x>y)      #returns  true   because 3 is greater than  2.
print(x<y)      #returns  false because 3 is less  than  2.
print(x!=y)     #returns  true  because 3 is greater than  2. and 3 is greater  than 2.

#----------------------------->Chained Operators<-------------------------------
i = 7
j = 8
k = 20
print(i<j<k)
print(i<=j<=k)
print(i<j*k/i%j//k)

# ---------------------------->Conditional Expressions<---------------------------
i = 8
j = 4
if i>=j:
    print("i is greater than j")
else:
    print("j is greater than i")
