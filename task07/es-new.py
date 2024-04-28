import sys
import os

filename = input("Please enter a file name:")

def count_s(filename):
    try:
        # Check if the file exists
        if not os.path.exists(filename):
            print("File not found:", filename)
            return -1

        # Check if the file is a text file
        if not filename.lower().endswith('.txt'):
            print("File is not a text file:", filename)
            return -1

        # Open the file and count 's'
        with open(filename, 'r') as file:
            content = file.read()
            s_count = content.count('s')
            return s_count
    except Exception as e:
        print("An error occurred:", str(e))
        return -1

def main():
    # Check if the filename argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script_name.py filename")
        sys.exit(1)  # Exit the script with a non-zero status code

    # Get the filename from the command line argument
    filename = sys.argv[1]

    # Count the occurrences of 's' in the file
    s_count = count_s(filename)
    if s_count != -1:
        print("Number of 's' in the file:", s_count)

if __name__ == "__main__":
    main()

