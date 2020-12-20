__doc__ = """
----------------------------------------------------------------------------
VernamCipher.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

VernamCipher specifications:
------------------------------
key must be same length as plaintext

encrypt(key, plaintext_utf8) where:
- key: The one time pad used to encrypt the plaintext
- plaintext_utf8: plaintext in UTF8 format
- return: ciphertext in UTF8 format

decrypt(key, cipher_text_utf8) where:
- key: The one time pad used to encrypt the plaintext to produce the cipher text
- cipher_text_utf8: ciphertext in UTF8 format
- return: decrypted text in UTF8 format

Use/modify VernamCipher_Test.py to test your implementations.
----------------------------------------------------------------------------
"""
import string

def encrypt(key, plaintext_utf8):
  characters = string.punctuation + string.ascii_letters + string.digits
  if len(key) != len(plaintext_utf8):
    return None
  else:
    cipher_text = ""
    for i, char in enumerate(plaintext_utf8):
      total = characters.index(char) + (characters.index(key[i]))
      if total > 93:
        total -= 94
      cipher_text += characters[total]
    return cipher_text

def decrypt(key, cipher_text_utf8):
  characters = string.punctuation + string.ascii_letters + string.digits
  if len(key) != len(cipher_text_utf8):
    return None
  else:
    plaintext = ""
    for i, char in enumerate(cipher_text_utf8):
      total =  characters.index(char) - (characters.index(key[i]))
      if total < 0:
        total += 94
      plaintext += characters[total]
    return plaintext
