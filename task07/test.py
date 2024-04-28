
import os
import sys

def main():
    # Check if filename is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python program.py <filename>")
        return

    filename = sys.argv[1]

def file_name():
    filename = input("Please enter a file name:")
    return check(filename)

def check(filename):
    match os.path.exists(filename), filename.endswith('.txt'):
        case (True, True):
                with open(filename, 'r') as f:
                    read_data = f.read()
                 # Initialize a counter for 's after apostrophe
                count_apostrophe_s = 0
                # Loop through each character in the content
                for r in range(len(read_data)-1):
                # Check if the character is an apostrophe followed by 's'
                    if read_data[r] == "'" and read_data[r+1] == 's':
                        # Increment the counter
                        count_apostrophe_s += 1
                    # Print the count
                print("Number of e's in the file:", count_apostrophe_s)
        case (False, _):
            print('File does not exist.')
            file_name()
        case (_, False):
            print('Wrong extension')
            file_name()



file_name()
if __name__ == "__main__":
    main()