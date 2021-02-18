# In-class coding from Wednesday, February 17

# for loops

# define a constant list to use
STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# print each state in STATES on a separate line
for state in STATES:
    print(state)
    print("next state", end=": ")

# now we're out of the loop
print("we're done")

# do same as above using for i loop
for i in range(0, len(STATES),1):
    print(STATES[i])
    print("next state", end=": ")

# now we're out of the loop
print("we're done")

for i in range(0, len(STATES), 2):
    print(STATES[i])

for i in range(0, len(STATES), -1):
    print(STATES[i])

for i in range(len(STATES)-1, -1, -1):
    print(STATES[i])

# in the range statement - you can use 3 values
# you can use 2 values or you can use 1 value

# 2 values
for i in range(0, len(STATES)):
    print(STATES[i])
# if you use two values, python interprets the
# first as the starting value and the second
# as the stopping value. The hop count defaults to 1.

for i in range(len(STATES)):
    print(STATES[i])

# if you provide only one value in range
# python interprets as the stopping value
# the starting value is 0 and the hop count is 1

# print the states in indices 10 through 19
for i in range(10,20):
    print(i, STATES[i])

# list of the first 7 squares
numbers = [1, 4, 9, 25, 36, 49]
# want to replace each list element with the cube
for i in range(len(numbers)):
#    numbers[i] = numbers[i] * numbers[i]**0.5
    numbers[i] = (i+1) * numbers[i]

# the point is - with a for i loop, I can
# change the list within the loop

# how about with a for each loop?
for num in numbers:
    num = num * 2

# you can't change list values with a
# for each loop

# print out each state that ends in a
for state in STATES:
    if state[-1] == 'a':
        print(state)

# the same with a for i loop:
for i in range(len(STATES)):
    if STATES[i][-1] == "a":
        print(STATES[i])

#print out the state name if it ends in a vowel
# vowels are 'a', 'e', 'i', 'o', 'u', 'y'

for state in STATES:
    if state[-1]=='a'  or state[-1] == 'e' or state[-1] == 'i' or state[-1]=='o' or state[-1]== 'u' or state[-1]=='y':
        print (state)

# an easier way that uses lists

vowels = ['a','e','i','o','u','y']

for state in STATES:
    if state[-1] in vowels:
        print(state)

# could have done:
for state in STATES:
    if state[-1] in ['a','e','i','o','u','y']: #not good programming practice
        print (state)

#print every state that begins with a consonant
vowels = ['A','a','E','e','I','i','O', 'o', 'U','u','y']
for state in STATES:
    if not(state[0] in vowels):
        print (state)

#strings and loops
word = 'supercalifragilisticexpialidocious'
#print each letter in the string on a line
# for each loop
for char in word:
    print(char)

# for i thing
for i in range(len(word)):
    print(word[i])
