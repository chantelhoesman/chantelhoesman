# import file
import csv

# take in input to call file for read
with open(input(), 'r') as csvfile:
    csvfile_info = csv.reader(csvfile, delimiter=',')

    # create empty list
    empty = {}

    for line in csvfile_info:
        ''' this loop iterates over the file for each line'''
        for i in line:
            ''' this loops iterates over each item in the list and determines it the item was already read'''
            if i in empty:
                empty[i] += 1
            else:
                empty[i] = 1
        for k, v in empty.items():
            ''' this loop takes the key value pairs and prints them for the new list that was created'''
            print(k, v)