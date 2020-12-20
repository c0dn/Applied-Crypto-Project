__doc__ = """
DiffieHellman_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""
from crypto_package import DiffieHellman


def run_test():
  print(__doc__)
  print(DiffieHellman.__doc__)

  n = 11
  g = 7
  key, a, b, x, y = DiffieHellman.calculate_key(n, g)
  print(f"Alice and Bob agreed on {n} and {g}.")
  print(f"Alice choose another large random number x ({x}) and calculates A ({a}).")
  print(f"A = {g}^{x} mod {n}")
  print(f"Alice sent the number (A) calculated to Bob.")
  print(f"Bob independently choose another large random number y ({y}) and calculates B ({b}).")
  print(f"B = {g}^{y} mod {n}")
  print(f"Bob sent the number (B) calculated to Alice")
  print("Bob and Alice now calculate the key.")
  print(f"Key = {key}")
  return


if __name__ == "__main__":
  run_test()
