__doc__ = """
MonoAlphabetCipher_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""
from crypto_package import MonoAlphabetCipher

def run_test():
  print(__doc__)
  print(MonoAlphabetCipher.__doc__)

  mono_alpha_cipher = {
    "a": "m",
    "b": "n",
    "c": "b",
    "d": "v",
    "e": "c",
    "f": "x",
    "g": "z",
    "h": "a",
    "i": "s",
    "j": "d",
    "k": "f",
    "l": "g",
    "m": "h",
    "n": "j",
    "o": "k",
    "p": "l",
    "q": "p",
    "r": "o",
    "s": "i",
    "t": "u",
    "u": "y",
    "v": "t",
    "w": "r",
    "x": "e",
    "y": "w",
    "z": "q",
    " ": " ",
    "1": "5",
    "2": "1",
    "3": "9",
    "4": "2",
    "5": "3",
    "6": "0",
    "7": "4",
    "8": "6",
    "9": "7",
    "0": "8",
  }
  print("Substitution Table")
  for k, v in mono_alpha_cipher.items():
    print(f"Sub {k} with {v}")

  plaintext = "HELLO"
  cipher_text = MonoAlphabetCipher.encrypt(mono_alpha_cipher, plaintext)
  decrypted_text = MonoAlphabetCipher.decrypt(mono_alpha_cipher, cipher_text)
  print("\nplaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  plaintext = "Hello!"
  cipher_text = MonoAlphabetCipher.encrypt(mono_alpha_cipher, plaintext)
  decrypted_text = MonoAlphabetCipher.decrypt(mono_alpha_cipher, cipher_text)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  plaintext = "Hello123+/="
  cipher_text = MonoAlphabetCipher.encrypt(mono_alpha_cipher, plaintext)
  decrypted_text = MonoAlphabetCipher.decrypt(mono_alpha_cipher, cipher_text)
  print("plaintext: " + plaintext)
  print("ciphertext: " + cipher_text)
  print("decryptedtext: " + decrypted_text + "\n")

  return

if __name__ == "__main__":
  run_test()