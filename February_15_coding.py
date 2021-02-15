# in-class coding from Monday, February 15

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# add Washington, DC as a state
# append
# insert

#len
len(states)

# states[len(states)] is always an error
# the last element is always
states[len(states)-1]
#abbreviated
states[-1]

# removing elements from a list
# by value - remove
states.remove("Washington, DC")

# by index - pop
states.pop(23)

# use in to tell you whether something
# is a list element
if "France" in states:
    states.remove("France")
else:
    print("It wasn't there")

#List slicing
# suppose I only want some of the states
# the first 10
first_10_states = states [0:10]

# copies states[0], states [1],... states[9]
# it does not copy states[10]

# syntax of list slicing
# start at the first element listed; stop
# and do not include the second index
# listed

states [0:10]# start at states[0] and copy
# up to states [10] but DO NOT INCLUDE states[10]

# two syntax notes about list slicing
first_10_states = states[0:10]
# same as
first_10_states = states[:10]
# a missing first number before the colong
# means 'start at the beginning'

# a missing second number AFTER the colon
# means go to the end
states[20:len(states)]
# is the same as
states[20:]

# if I want the whole list, I can leave out
# both numbers
states[:]

# Now strings
strvar = "The bank was closed today, much to my unhappiness"

# each character in the string has its index
# start at 0

# can't change the value of a character of the
# string - but you can read it

# in
if "," in strvar:
    print("It has a comma")

# len works - tells you how many characters
# are in the string
len(strvar)

# splitting a string into components
# words
# split - takes a string and returns a list
l = strvar.split()

# if there's nothing in the parentheses
# split breaks up the string on whitespace
# spaces, tabs \t, newlines \n
# split starts a new "word" and deletes the whitespace

# doesn't have to split on whitespace
l1 = strvar.split("s")

# tell Python the maximum number of splits
# or "Words"
l2 = strvar.split("s",2)

# creating words or substrings

# strip - gets rid of whitespace from a string
# returns another string
# but not embedded whitespace - only at the begginning
# and end
new_string = "\t   some number of words \t   "

nns = new_string.strip()

# "strip" gets rid of whitespace at the front
# and the back

# lstrip just gets  rid of whitespace at front
# rstrip just gets rid of whitespace at end

#what I mean by substring
# substring - take the first 10 characters
# of strvar
substring = strvar[0:10]
