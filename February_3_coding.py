# Coding done in class Wednesday 2/3/21

first_integer = 8
second_integer = 42
first_float = 3.14159
second_float = 32.4
first_string = "Purdue football is terrible"
second_string = "sad but true"

print("here's an example")

print(first_integer)
print(second_integer)

# What if we don't want a newline between these two
# We want both values on the same line?

# Combine in a single print statement

print (first_integer, second_integer)
# That comma caused one blank space to be printed
# between the two values

print (first_string, second_string)
# + only works with strings
print (first_string+second_string)

#convert to strings by using str()
print(str(first_integer)+str(second_integer))

# Newline at the end of print by default

# use end= ' ' argument
print(first_integer, end='stopping here')
print (second_integer)

print(first_integer, end = ' ')
print(second_integer)

print("The answers are ", first_integer, " and ", second_integer, end = 'done')

# Python defines special characters


# newline = \n
# tab = \t

print (first_integer, '\n', second_integer)
print (first_integer, '\t', second_integer)

# you want to print \n
# you have escape it - inserting another \
print ('\\n')

#f strings
f"hello there {first_integer:5}"
f"hello there {second_integer:5}"

n = 1/3
f"{n:5.2}"

# the input statement

data = input("Please enter your name")

#everything is a string
number = input("enter a number between 1 and 10 inclusive")
print(number + 5)

# if you don't want a string you have to cast
number = int(input("Enter a number between 1 and 10 inclusive"))
print (number + 5)

# the prompt has to be a single string
number = input("enter", "a", "number")

prompt = "enter a number"
number = input(prompt)
