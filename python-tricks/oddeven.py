'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
'''
import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input().strip())
  odd = lambda x:True if x%2!=0 else False
  if odd(n):
    print("Weird")
    exit()
  if (n in range(2,5)) or (n>20):
    print("Not Weird")
  if (n in range(6,21)):
    print("Weird")