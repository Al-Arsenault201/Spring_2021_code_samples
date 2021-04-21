# some information about Project 2
LAST_NAME = 0
FIRST_NAME = 1
ID = 2
P1 = 3
P2 = 4
P3 = 5
T1 =6
T2 = 7
T3 = 8
# open one of the data files, convert it to a 2D list and start working with it
with open("/Users/alfredarsenault/PycharmProjects/Spring_2023.csv") as infile:
    d = infile.readline()
    d = infile.readline()  #read in the header lines and throw them away
    data = infile.read()   #split this into a 2D list

    # first, create a 1-D list with each student's record as one element
    spring_list = data.split('\n')
    for i in range(len(spring_list)):  # covers all rows
        spring_list[i] = spring_list[i].split(",")  #creates a 2-D list


    for i in range(len(spring_list)):
        for j in range(P1,T3+1):
            spring_list[i][j] = int(spring_list[i][j])
#        print(spring_list[i])

# insert a new column 6 in each row
    for i in range(len(spring_list)):
        spring_list[i].insert(6,spring_list[i][P1] + spring_list[i][P2]+ spring_list[i][P3])
        print(spring_list[i])

def read_file(filename):
    with open (filename,"r") as infile:


if __name__ == "__main__":
    files = ["Fall_2022.csv", "Spring_2023.csv","Fall_2023.csv"]
    with file in files:
        read_file(file)
