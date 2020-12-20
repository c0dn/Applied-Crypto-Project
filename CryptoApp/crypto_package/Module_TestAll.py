__doc__ = """
Module_TestAll.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""

from crypto_package import CaesarCipher_Test
from crypto_package import MonoAlphabetCipher_Test
from crypto_package import RailFence_Test
from crypto_package import VernamCipher_Test
from crypto_package import Aes_Test
from crypto_package import DiffieHellman_Test
from crypto_package import SimpleColumnarTransposition_Test
from crypto_package import Des_Test


def run_test():
  print(__doc__)
  CaesarCipher_Test.run_test()
  MonoAlphabetCipher_Test.run_test()
  RailFence_Test.run_test()
  VernamCipher_Test.run_test()
  Aes_Test.run_test()
  DiffieHellman_Test.run_test()
  SimpleColumnarTransposition_Test.run_test()
  Des_Test.run_test()

  return

if __name__ == "__main__":
  run_test()
