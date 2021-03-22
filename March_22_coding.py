# Coding from March 22 - file I/O
# and some notes about HW 5

# Problem 1 from homework
# ask the user for two words
original = input('I need two words')

# split this string to get a list of two words
words = original.split()
first_word = words[0]
#convert first_word into a list
fwl = []
for letter in first_word:
    fwl.append(letter)
second_word = words[1]
# converts second_word into a list
swl = []
for letter in second_word:
    swl.append(letter)

# to compare these words, look at each letter in the
# first word. If it's also in the second word
# delete it from both.
for letter in fwl:
    if letter in swl:
        fwl.remove(letter)
        swl.remove(letter)


# if these are anagrams, both strings will be empty
# when you're done. If one or both strings is not empty
# they're not anagrams
if len(fwl) + len(swl) == 0:
    # it's an anagram
else:
    # return len(fwl) + len(swl) - that's the
    # number of letters that have to be changed

# File I/O

# To use any file, I have to open it. This tells
#Python - and Python tells the OS - what file I want
# to use

with open("/Users/alfredarsenault/PycharmProjects/Spring_2021/integers.txt","r") as f:
    data = f.read() # reads the entire file as a single string
#    data_line = f.readline() # reads one line of the file up to and includin newline
#    data_lines = f.readlines() # reads the entire file into a list with one line per list element


#notice: everything is still a string

    lines = data.split('\n')
    for line in lines:
        numbers = line.split()
#        print(numbers)
        sum = 0
        for number in numbers:
            sum += int(number)
        print('the sum is ',sum)

# when you open a file for writing, it doesn't
# have to exist. Python will create it.
with open("output.txt", "w") as outfile:
    x = "Now is the the time for the ACC"
    y = "to quit losing March Madness games"
    z = "My bracket is so broken"
# The only thing you can write to a file is a string
#    outfile.writelines(x)
#    outfile.writelines(y)
#    outfile.writelines(z)
#    outfile.writelines(x, y, z) - will not work; you can write ONE STRING AT A TIME
    outfile.writelines(x + y + z)


with open('results.txt', 'w') as out:
    out.write('The largest integer in the file is' + largest)

with open("dogs.txt","r") as dogfile:
    text = dogfile.read()
    list_of_text = text.split()
    for i in range(len(list_of_text)):
        if list_of_text[i] == "dogs":
            list_of_text[i] = "cats"
# with open() syntax automatically closes the file
# when you unindent
with open("dogs.txt", "w") as outfile:
    outstring = " ".join(list_of_text)
    outfile.write(outstring)

