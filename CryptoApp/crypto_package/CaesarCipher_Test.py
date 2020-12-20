__doc__ = """
CaesarCipher_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""

from crypto_package import CaesarCipher


def run_test():
  print(__doc__)
  print(CaesarCipher.__doc__)

  key = 3

  plaintext = "HELLO"     # Q1, Q2
  cipher_text = CaesarCipher.encrypt(key, plaintext)
  decrypted_text = CaesarCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  plaintext = "Hello!"    # Q1, Q2
  cipher_text = CaesarCipher.encrypt(key, plaintext)
  decrypted_text = CaesarCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  plaintext = "Hello123+/="   # Q3
  cipher_text = CaesarCipher.encrypt(key, plaintext)
  decrypted_text = CaesarCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  return


if __name__ == "__main__":
  run_test()
