# in-class coding for Wednesday, March 24

RANK = 0
GOLDS = 1 # change to 2 when country name is inserted
SILVERS = 2 # change to 3
BRONZES = 3 # change to 4
TOTAL = 4 # change to 5

medal_table = [
   [1, 14, 11,4,29],
   [2,5,2,4,11],
   [3,3,5,4,12],
   [4,3,3,3,9],
   [5,2,5,1,8],
   [6,2,3,0,5],
   [7,2,0,4,6],
]
# Print out the 2D list
#print(medal_table)

#print out the first row - the United States results
print(medal_table[0])

#when dealing with a 2D-list, ROW always comes first.
# COLUMN comes second

#what if I want to access a specific element (row, column)
# be careful with syntax
print(medal_table[0][1])

# it is not medal_table[0,1]

#if you want to access a row - just use one index in square brackets
print(medal_table[3])

#what about columns?
# that's harder - you can't do it in a single statement
# you have to use a loop
# I want to print out the number of gold medals won by each
# country
for i in range(len(medal_table)):
    print(medal_table[i][GOLDS], end=" ")
print("\n")

# declare an empty 2D-list
empty_2D_list= []

# len(two_d_list) = the number of ROWS in the list
# if you want to know the number of columns
# use the length of a row
# len(medal_table[0]) = the number of COLUMNS

# you have to be careful. If not all rows have the same
# number of columns, this might not be meaningful.

#Insert a single element into my list
medal_table[1].insert(1, "Kenya")

# Append a whole row - works like you're used to
medal_table.append([8,3,2,3,8])
# To remove a row
medal_table.pop(7)

#Dealing with columns
# insert country names as column 1
# define a list of the country names
countries = ["United States", "Kenya", "Jamaica","China", "Ethiopia", "GB", "Germany"]

for i in range(len(medal_table)):
    medal_table[i].insert(1, countries[i])

# building a table
ROWS = 5
COLUMNS = 10
square_table = []
# first build a row, then append that row to the table
# as a unit
num_to_be_squared = 1
for i in range(ROWS):
    row = []
#build a row - row i
    for j in range(COLUMNS):
        row.append(num_to_be_squared**2)
        num_to_be_squared += 1
# now append the row
    square_table.append(row)
#print(square_table)
for k in range(len(square_table)):
    print(square_table[k])

# read in the data file - one line at a time
with open("medal_table.txt","r") as infile:

    #read in the header line
    header = infile.readline()
    #now throw this line away by ignoring it
    #now read in the rest of the file
    medals = infile.readlines()
    #medals = infile.read()
    # m = medals.split('\n') achieves the same result
    data =[]
    for i in range(len(medals)):
        data.append(medals[i].split())

#reading a .csv file
with open("medal_table.csv","r") as commafile:
    commafile.readline()
    #read rest of file
    medals = commafile.read()
    data = medals.split('\n')
    med_list = []
    for i in range(len(data)):
        med_list.append(data[i].split(','))



