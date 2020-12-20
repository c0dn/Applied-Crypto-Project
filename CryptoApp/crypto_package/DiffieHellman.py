__doc__ = """
----------------------------------------------------------------------------
DiffieHellman.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

DiffieHellman specifications:
------------------------------

calculate_key(n, g) where:
- n: big prime number 1
- g: big prime number 2
x, y is randomly generated
- return: key, a, b, x, y

Use/modify DiffieHellman_Test.py to test your implementations.
----------------------------------------------------------------------------
"""
import random

def calculate_key(n, g):
  x = random.getrandbits(16)
  y = random.getrandbits(16)
  b = pow(g, y, n)
  a = pow(g, x, n)
  k = pow(b, x, n)
  return k, a, b, x, y
