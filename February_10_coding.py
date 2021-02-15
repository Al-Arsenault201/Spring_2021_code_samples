# in-class coding from Wednesday, February 10

# = += -= *= /=
# //=  %= are valid
y = 5
y //= 3 # y = y // 3
y = 5
y %= 3

# Lists - my grocery list
"""
Milk
Eggs
Cereal
Coffee 
Apples
Strawberries 
Broccoli
Cucumber
Tomatoes
Green Onions
Half & Half
"""
#declare a list variable, l

l = []
len(l)

# pre-load the list in the declaration
grocery_list = ["Milk", "Eggs", "Cereal", "Coffee", "Apples", "Strawberries", "Broccoli", "Tomatoes", "Cucumbers", "Green Onions", "Half and half"]

# adding a value to a list
# append - adds the value to the end, wherever that is
# insert - adds the value in a specific place in the list
l.append("Milk")
l.append ("Eggs")

# indices in lists always start counting at 0
l[0]

# last element in the list is always index = len(list) - 1
grocery_list[len(grocery_list)-1]

# grocery_list[len(grocery_list)] is ALWAYS an error
l.append()

# if you use a negative integer as the index, Python
# starts counting from the end  - the last
l = ['Milk', 'Eggs', 'Bagels', 'Grapes', 'Strawberries', 'Onions']
l[-1]

# why
# creativity and laziness
# the last item in a list is ALWAYS len(l) - 1
# so - drop the "len(l)"

# multiple ways to get rid of an item from a list
# remove - which gets rid of a value
l.remove("Eggs")
# removes the first instance of the item
# first - with the lowest index
# if it's not there, it's an error

# get rid of an item by its index
# pop
l.pop(3)

#to get rid of multiple entries at the same time
del l[0:3]
# gets rid of the list elements starting at the first
# number - at 0 and deletes everything up to but NOT
# including the second number

#in - return whether or not an item is in a list
# element of the list
if "Soup" in l:
    l.remove("Soup")

#you can put different types in a list
GPA = 3.99
grad_year = 2022
student_list = ["Last_name",GPA, grad_year]

# groceries without a list

first_item = "Milk"
second_item = "Eggs"
third_item = "Bagels"

#now, how do I add another item to my list?  What
# variable name do I use?
#This very quickly will fail and you'll go back to pencil
# and paper
