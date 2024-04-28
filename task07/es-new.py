import sys

def main():
    # Check if filename is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python program.py <filename>")
        return

    filename = sys.argv[1]

    # Now you can use the filename variable to perform operations on the file
    print("Filename:", filename)
    # Example: open and read the file
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found:", filename)

if __name__ == "__main__":
    main()