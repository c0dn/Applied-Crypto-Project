__doc__ = """
VernamCipher_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""
from crypto_package import VernamCipher

def run_test():
  print(__doc__)
  print(VernamCipher.__doc__)

  key = "Stamp"
  plaintext = "HELLO"
  cipher_text = VernamCipher.encrypt(key, plaintext)
  decrypted_text = VernamCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print(f"Key used: {key}")
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  key = "APPLE"
  plaintext = "HELLO"
  cipher_text = VernamCipher.encrypt(key, plaintext)
  decrypted_text = VernamCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print(f"Key used: {key}")
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  key = "Stamp?"
  plaintext = "Hello!"
  cipher_text = VernamCipher.encrypt(key, plaintext)
  decrypted_text = VernamCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print(f"Key used: {key}")
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  key = "Stamp900?/-"
  plaintext = "Hello123+/="
  cipher_text = VernamCipher.encrypt(key, plaintext)
  decrypted_text = VernamCipher.decrypt(key, cipher_text)
  print("plaintext: " + plaintext)
  print(f"Key used: {key}")
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  return

if __name__ == "__main__":
  run_test()