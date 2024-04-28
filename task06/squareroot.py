# squareroot.py
# to create sqrt function by the newton method at estimating square roots
# author : Nataliia Dragunova

# spent much time on getting the right numbers after decimal

import math
def newton_sq(n):
    sq = math.ceil(n)
    while True:
      new = 0.5*(sq/n + n)
      if (n - new) < 0.00001:
        return new     
      n = new

n = float(input("Please enter a positive number:"))
result = newton_sq(n)
print("The square root of", n, "is approx.", round(result,2))

