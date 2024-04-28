# bank.py
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
# out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# author : Nataliia Dragunova

# first attempt with exact amounts after reading "Python String Formatting (w3schools.com)"
'''
amount1 = 65
amount2 = 180
sum = (amount1 + amount2)/100
txt = "The sum of these is €{}"
print (txt.format(sum));

'''
# the last version

amount1 = int(input("please enter first amount in cents:"))
amount2 = int(input("please enter second amount in cents:"))
sum = (amount1 + amount2)/100
txt = "The sum of these is € {}"
print (txt.format(sum));
