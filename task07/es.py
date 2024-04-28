# es.py
# to create a program reads in a text file and outputs the number of e's it contains
# author : Nataliia Dragunova + chat Gpt


import os
import sys

def main():
    # Check if filename is provided as an argument
    if len(sys.argv) != 2:
        print("Print: python program.py <filename>")
        return

    filename = sys.argv[1]

    def check(filename):
        # if file exists
        if os.path.exists(filename):
            # if file .txt file
            if filename.endswith('.txt'):
                with open(filename, 'r') as f:
                    read_data = f.read()
                    # a counter for 's 
                    count_apostrophe_s = 0
                    # Loop through each character in the content
                    for r in range(len(read_data)-1):
                        # Check if the character is an apostrophe followed by 's'
                        if read_data[r] == "'" and read_data[r+1] == 's':
                            # Increment the counter
                            count_apostrophe_s += 1
                    # Print the count
                    print("Number of 's in the file:", count_apostrophe_s)
            else:
                print('Wrong extension')
        else:
            print('File does not exist.')

    check(filename)

if __name__ == "__main__":
    main()
