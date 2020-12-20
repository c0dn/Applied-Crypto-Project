__doc__ = """
----------------------------------------------------------------------------
MonoAlphabetCipher.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

MonoAlphabetCipher specifications:
------------------------------

encrypt(sub_table, plaintext_utf8) where:
- sub_table: Substitution table used for replacing characters in the plaintext to produce the ciphertext
- plaintext_utf8: plaintext in UTF8 format
- return: cipher_text in UTF8 format

decrypt(sub_table, cipher_text_utf8) where:
- sub_table: Substitution table used to produce the ciphertext you are trying to decrypt
- cipher_text_utf8: ciphertext in UTF8 format
- return: decrypted text in UTF8 format

Use/modify MonoAlphabetCipher_Test.py to test your implementations.
----------------------------------------------------------------------------
"""

def encrypt(sub_table: dict, plaintext_utf8: str):
  cipher_text_utf8 = ""
  for char in plaintext_utf8:
    enc: str = sub_table.get(char.lower())
    if enc is None:
      cipher_text_utf8 += char
    elif char.islower():
      cipher_text_utf8 += enc
    else:
      cipher_text_utf8 += enc.upper()
  return cipher_text_utf8

def decrypt(sub_table: dict, cipher_text_utf8: str):
  inv_sub_table = {v: k for k, v in sub_table.items()}
  plaintext_utf8 = ""
  for char in cipher_text_utf8:
    plain: str = inv_sub_table.get(char.lower())
    if plain is None:
      plaintext_utf8 += char
    elif char.islower():
      plaintext_utf8 += plain
    else:
      plaintext_utf8 += plain.upper()
  return plaintext_utf8