# in-class coding from Monday, February 8, 2021

# Arithmetic operators
print (5 +9.0)

# real division or floating point division
y = 9/5.0

# integer division
#  9 divided by 5 = 1.8 /
#  9 divided by 5 = 1 remainder 4  // and %
x = 30//7  # 7 goes into 30 4 times with remainder 2

# remainder is called the modulus
# modular arithmetic or modulo

y = 30%7 # 30 modulo 7 or 30 mod 7

#exponentiation
y = 5**3

# assignment - single =
y = 5
# comparison - double == no spaces between
y == 5  # this is true

# not equals !=
y\!= 4 # boolean with value True

# comparison of strings
s = 'Brady won again'

s != 'Mahomes repeated'

# assignment operators
y = 5
#do something
y = y + 1

#you can replace that with
y += 1
y -= 3  # y = y - 3 NOT y = 3 - y
y *= 3
y /= 3  # y = y /3 NOT y = 3/y

# Python does not support "++" to add one
# other languages have y++ to mean y += 1

6 * 5.0 + 2 - 5 / 5
(6 * (5.0 + 2) - 5) / 5
6 < 2 or 5 > 1
6 < (2 or 5) > 1   # let’s talk about this one

#0 or 0.0 equate to False  if you treat them as Boolean
# any other number equates to True
# The empty string '' equates to False if you treat
# as Boolean; any other string equates to True

y = 5
if y == 5:
    print ("Yes")

if y == 5 or y != 3 or y > 0 and y < 1:
    print("yes")
# indentation is important!!!

y = 5
if y >= 0:
    print("y is positive")
    print("y is non-negative", end='#')
    print("that makes sense")
print("we're done with the loop")

#one condition
if (student_major =='Physics'):
    print("What a great choice")
    print("You'll do well")

# two conditions
if (student_major =='Physics'):
    print("What a great choice")
    print("You'll do well")
else:
    print("that's not a bad choice")
print("We're done with the loop")

# three or more cases to cover
age = int(input("enter your age in years"))
if (age < 18):
    print("sorry, you're a minor")
    print("there are lots of things you can't do")
elif ( age < 21):
    print ("you can vote and we hope you did")
    print ("but you still don't have all privileges")
else:
    print("You are now an adult")