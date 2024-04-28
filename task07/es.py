# es.py
# to create a program reads in a text file and outputs the number of e's it contains
# author : Nataliia Dragunova

import os
filename = input("Please enter a file name:")
with open(filename,'r') as f:
    read_data = f.read()

'''
     # Initialize a counter for 's after apostrophe
    count_apostrophe_s = 0
    
    # Loop through each character in the content
    for i in range(len(read_data)-1):
        # Check if the character is an apostrophe followed by 's'
        if read_data[i] == "'" and read_data[i+1] == 's':
            # Increment the counter
            count_apostrophe_s += 1

# Print the count
print("Number of instances of 's after apostrophe in the file:", count_apostrophe_s)


'''
 # Initialize a counter for "'"
count_s = 0
    # Loop through each character in the content
for char in read_data:
        # Check if the character is '
        if char == "'":
            # Increment the counter
            count_s += 1

# Print the count
print("Number of ' in the file:", count_s)

'''
# Checking If a File Exists

if os.path.exists('example.txt'):
    print('File exists.')
else:
    print('File does not exist.')
'''
