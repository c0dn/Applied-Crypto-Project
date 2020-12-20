__doc__ = """
Aes_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""


from crypto_package import Aes


def run_test():
  print(__doc__)
  print(Aes.__doc__)

  key = Aes.get_fixed_key()
  plaintext_string = "Testing AES encrypt and decrypt."

  print("Using CBC, fixed 256 bits key")
  encrypted = Aes.encrypt(key, plaintext_string.encode("utf8"))
  decryptedtext_string = Aes.decrypt(key, encrypted)
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  print("\nUsing ECB, random 256 bits key")
  key = Aes.get_random_key(256)
  encrypted = Aes.encrypt(key, plaintext_string.encode("utf8"), "ecb")
  decryptedtext_string = Aes.decrypt(key, encrypted, "ecb")
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  print("\nUsing CFB, random 192 bits key")
  key = Aes.get_random_key(192)
  encrypted = Aes.encrypt(key, plaintext_string.encode("utf8"), "cfb")
  decryptedtext_string = Aes.decrypt(key, encrypted, "cfb")
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  print("\nUsing OFB, random 128 bits key")
  key = Aes.get_random_key(128)
  encrypted = Aes.encrypt(key, plaintext_string.encode("utf8"), "ofb")
  decryptedtext_string = Aes.decrypt(key, encrypted, "ofb")
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  return


if __name__ == "__main__":
  run_test()
