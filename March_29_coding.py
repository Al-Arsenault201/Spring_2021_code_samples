# coding for class on Monday, March 29
import os
import json

grand_total_steps = 0
path = "/Users/alfredarsenault/Documents/JSONfiles"

for name in os.listdir(path):
    if ".json" in name:

        filename = path+"/"+name
        with open(filename,"r") as infile:
            d = json.load(infile) #reads in the file
            #now I have a list of dictionaries
            steps = 0
            for i in range(len(d)):
                steps += int(d[i]["value"])
            grand_total_steps += steps
 #           print(steps)

print("THE GRAND TOTAL IS  ", grand_total_steps)

"""
#defining a dictionary

d = {"key1":"value1", "key2":"value2"}
# those keys are strings; keys can be integers or floats, too
new_d = {1:"you win", 2:"nice try", 3:"bronze medal"}

dogs = {"doug":["beagle","bulldog"],"lizzie":"Australian cattle dog",
        "remy":"shepherd", "bonnie":"beagle", "penny":"cocker spaniel"}

if dogs.get('cleo') == None:
    dogs['cleo'] = 'beagle'

dogs['cleo'] = 'dachshund'

if dogs.get('lady') != None:
    del dogs['lady']

"""

# can you get a dictionary entry by its value?
# not directly
# you can only see if any key has that value
