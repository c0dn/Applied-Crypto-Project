__doc__ = """
SimpleColumnarTransposition_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""

from crypto_package import SimpleColumnarTransposition


def run_test():
  print(__doc__)
  print(SimpleColumnarTransposition.__doc__)

  plaintext = "HELLO"     # Q1, Q2
  cipher_text = SimpleColumnarTransposition.encrypt(plaintext, 2)
  decrypted_text = SimpleColumnarTransposition.decrypt(cipher_text, 2)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("Key: 2")
  print("decryptedtext: " + decrypted_text + "\n")

  plaintext = "Hello!"    # Q1, Q2
  cipher_text = SimpleColumnarTransposition.encrypt(plaintext, 3)
  decrypted_text = SimpleColumnarTransposition.decrypt(cipher_text, 3)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("Key: 3")
  print("decryptedtext: " + decrypted_text + "\n")

  plaintext = "Hello123+/="   # Q3
  cipher_text = SimpleColumnarTransposition.encrypt(plaintext, 5)
  decrypted_text = SimpleColumnarTransposition.decrypt(cipher_text, 5)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("Key: 5")
  print("decryptedtext: " + decrypted_text + "\n")

  return


if __name__ == "__main__":
  run_test()