# in-class coding for Monday, Feb. 22

# our list of states as a constant, to use in
# a number of examples
STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# run until the user enters an appropriate age
age = 0;
while (age < 18):
    age = int(input("enter your age in years: "))
    print ("If you’re 18 or older you should vote")
print ("that’s the end of our story")

# a priming read - get an initial value to "prime" the loop
# THE Loop may never be executed

age = int(input("enter your age in years: "))
while (age < 18):
    age = int(input("enter your age in years: "))
    print ("If you’re 18 or older you should vote")
print ("that’s the end of our story")


# factorial - for loop and while loop
# compute 10! Using a while loop
product = 1
factor = 1
while factor <= 10:
    product *= factor   #or product = product * factor
    factor += 1

# a loop that never executes
age = int(input("please enter your age in years: "))
while (age < 0) and (age > 100):
	print("Age must be between 0 and 100 inclusive ")
	age = int(input("please enter your age in years: "))

# an infinite loop

#print all the positive odd numbers
#less than 100

num = 1
while num != 100:
    print(num)
    num = num + 2

# Sentinel loop
# Ask user to input classes taken this semester
# Tell user to enter "q" or "Q" to quit
courses = []
next_course = input("Enter the next course; enter q or Q to quit")
while next_course != 'q' and next_course != 'Q':
    # not(next_course == 'q' or next_course == "Q")
    courses.append(next_course)
    next_course = input("Enter the next course; enter q or Q to quit")

# done with loop
print("The classes you're taking this semseter are: ", courses)

