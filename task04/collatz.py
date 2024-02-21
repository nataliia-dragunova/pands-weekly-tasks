# collatz.py
# a program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation
# if it is even, divide it by two
# if it is odd, multiply it by three and add one
# end if the current value is one
# author : Nataliia Dragunova

# mostly I spent time for to separate numbers :)
num = int(input("Please enter a positive integer:"))
while num != 1: # condition for the end of loop
  print(int(num), end =" ") # printing every new number in line
  if num % 2 == 0: # check the number : even or odd
    num = num /2 # collatz condition for even int
  else:
    num = num * 3 + 1 # collatz condition for odd int
print(int(num)) # end of loop