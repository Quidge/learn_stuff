# Formula Used: 1 - [ t! / ((t-n)! * (t^n)) ]
# where t is the table size and n is the number of records inserted. 

from math import factorial
import decimal 

def calc(t, n):
  return 1 - (
    decimal.Decimal(factorial(t)) / decimal.Decimal(factorial(t-n) * t**n))

if __name__ == "__main__":
  print(calc(1000, 40))
