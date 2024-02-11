# accounts.py
# Program reads in a 10 character account number 
# outputs the account number with only the last 4 digits showing
# the first 6 digits replaced with Xs
# author : Nataliia Dragunova

# first attempt - it works but it's clunky :)
num = int(input("Please enter an 10 digit account number:"))
acc = str(num)
print("XXXXXX" + " "+ acc[6],acc[7],acc[8],acc[9]);