DATA_DIRECTORY = "/Users/alfredarsenault/Documents/Spring_21_project_3_data"
import os
master_list = []
os.chdir("/Users/alfredarsenault/Documents/Spring_21_project_3_data")
for file in os.listdir("/Users/alfredarsenault/Documents/Spring_21_project_3_data"):
    print(file)
    if ".csv" in file:
        with open (file, "r") as infile:
            infile.readline()
            d = infile.read()
            d_list = d.split('\n')
            for i in range(len(d_list)):
                master_list.append(d_list[i].split(','))

print(master_list)