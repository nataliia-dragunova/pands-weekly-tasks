# accounts.py
# Program reads in a 10 character account number 
# outputs the account number with only the last 4 digits showing
# the first 6 digits replaced with Xs
# author : Nataliia Dragunova

# first attempt - it works but it's clunky because of spaces between numbers :) 
# it's impossible to use this method to endless account number
'''
num = int(input("Please enter an 10 digit account number:"))
acc = str(num)
print("XXXXXX" + " "+ acc[6],acc[7],acc[8],acc[9]);
'''
# second attempt after watching the end of the 2d lecture
# it's impossible to use this method to endless account number
'''
num = int(input("Please enter an 10 digit account number:"))
acc = str(num)
print("XXXXXX" + acc[6:]); 
'''
# third attempt after reading about slicing in W3schools
'''
num = int(input("Please enter an 10 digit account number:"))
acc = str(num)
print("XXXXXX" + acc[-4:]);
'''
# it's possible to use this method to endless account number
# but it can not specify how many Xs before the last 4 numbers
'''
num = int(input("Please enter a digit account number:"))
acc = str(num)
print("∞" + acc[-4:]); 
'''
# EXTRA TASK - Endless account number with the last 4 visible numbers
num = int(input("Please enter a digit account number:"))
acc = str(num)
lnum = len(acc) - 4
print(str(lnum * "X") + acc[-4:]);