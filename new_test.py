DATA_DIRECTORY = "/Users/alfredarsenault/Documents/Spring_21_project_3_data"

import os

# read in one file and put it in a 2D list

first_file = DATA_DIRECTORY+"/04-11-2021.csv"
with open(first_file,"r") as infile:
    infile.readline()   #throws away first line; it's a header
    data = infile.read()  # reads rest of file
    data_list = data.split("\n")  # creates one-D list; one entry per row
    for i in range(len(data_list)) :
        data_list[i] = data_list[i].split(',')
        data_list[i].append(11)
        print(data_list[i])
