__doc__ = """
Des_Test.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7
"""


from crypto_package import Des


def run_test():
  print(__doc__)
  print(Des.__doc__)

  key = Des.get_fixed_key()
  plaintext_string = "Testing DES encrypt and decrypt."

  print("Using CBC, fixed 64 bits key")
  encrypted = Des.encrypt(key, plaintext_string.encode("utf8"))
  decryptedtext_string = Des.decrypt(key, encrypted)
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  print("\nUsing ECB, random 64 bits key")
  key = Des.get_random_key()
  encrypted = Des.encrypt(key, plaintext_string.encode("utf8"), "ecb")
  decryptedtext_string = Des.decrypt(key, encrypted, "ecb")
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  print("\nUsing CFB, random 64 bits key")
  key = Des.get_random_key()
  encrypted = Des.encrypt(key, plaintext_string.encode("utf8"), "cfb")
  decryptedtext_string = Des.decrypt(key, encrypted, "cfb")
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  print("\nUsing OFB, random 64 bits key")
  key = Des.get_random_key()
  encrypted = Des.encrypt(key, plaintext_string.encode("utf8"), "ofb")
  decryptedtext_string = Des.decrypt(key, encrypted, "ofb")
  print("plaintext: " + plaintext_string)
  print(f"key: {key}")
  print(f"Cipher text (encoded base64): {encrypted}")
  print("decryptedtext: " + decryptedtext_string)

  return


if __name__ == "__main__":
  run_test()
