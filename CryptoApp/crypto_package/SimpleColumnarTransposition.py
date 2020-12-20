__doc__ = """
----------------------------------------------------------------------------
SimpleColumnarTransposition.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

SimpleColumnarTransposition specifications:
------------------------------

* in the cipher text stands for NULL

encrypt(plaintext_utf8, key) where:
- key: specify no. of column to use
- plaintext_utf8: plaintext in UTF8 format
- return: ciphertext in UTF8 format

decrypt(cipher_text_utf8, key) where:
- key: specify no. of column to use
- cipher_text_utf8: ciphertext in UTF8 format
- return: decrypted text in UTF8 format

Use/modify SimpleColumnarTransposition_Test.py to test your implementations.
----------------------------------------------------------------------------
"""

def encrypt(plaintext_utf8, key):
  rows = int(len(plaintext_utf8) / key)
  if (len(plaintext_utf8) % key) != 0:
    rows += 1
  table = [["*" for i in range(key)]
          for j in range(rows)]
  counter = 0
  for row in table:
    for i in range(len(row)):
      try:
        row[i] = plaintext_utf8[counter]
      except IndexError:
        pass
      counter += 1
  cipher_text = ""
  for x in range(key):
    for row in table:
      cipher_text += row[x]
  return cipher_text

def decrypt(cipher_text_utf8, key):
  rows = int(len(cipher_text_utf8) / key)
  if (len(cipher_text_utf8) % key) != 0:
    rows += 1
  table = [["*" for i in range(key)]
           for j in range(rows)]
  counter = 0
  for x in range(key):
    for row in table:
      row[x] = cipher_text_utf8[counter]
      counter += 1
  plain_text = ""
  for row in table:
    for col in row:
      plain_text += col
  plain_text = plain_text.replace("*", "")
  return plain_text