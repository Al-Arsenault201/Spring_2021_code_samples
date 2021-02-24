# in-class coding from Wednesday, February 24

# the join statement
l = ["Red","Yellow","Blue"]
s = "sep".join(l)
print(s)

#what happens if you have a list whose elements are not strings?
l2 = [1,2,3]
s = ".".join(l2)
print(s)

l2 = [1,2,3]
str_list  =[]
for num in l2:
    str_list.append(str(num))

#nested loops

# nested for i loops
for i in range(10):
    print("i = ", i, end=": ")
    for j in range(5):
#        print( i, " * ", j, " is ", i*j )
#        input ("hit Enter to continue")

        print (i*j, end=" ")
    print("\n")




i = 0
while i < 10:
    j = 0
    while j < 5:
      print( i, " * ", j, " is ", i*j)
      input ("hit Enter to continue")
      j += 1
    i += 1

i = 0
while i < 10:
    j = 0
    while j < 5:
      print( i, " * ", j, " is ", i*j, end = " ")
      input ("hit Enter to continue")
      j += 1
    print("\n")
    i += 1

#nesting for inside while
i = 0
while i < 10:
    print("i = ", i, end=": ")
    for j in range (5):
        print (i*j, end=" ")
    print ("\n")
    i += 1

for a in range('a','e'):
    print (a)

# floating point roundoff error
n = 0
for i in range(20):
    n += 0.1
    print(n)
# imagine if n was being used as the iterator in a
# for i loop
