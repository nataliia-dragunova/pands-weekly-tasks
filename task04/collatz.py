# collatz.py
# a program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation
# if it is even, divide it by two
# if it is odd, multiply it by three and add one
# end if the current value is one
# author : Nataliia Dragunova

# mostly I spent time for to separate numbers :)
num = int(input("Please enter a positive integer:"))
while num != 1:
  print(int(num), end =" ")
  if num % 2 == 0:
    num = num /2
  else:
    num = num * 3 + 1
print(int(num))