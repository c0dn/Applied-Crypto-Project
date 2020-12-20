__doc__ = """
----------------------------------------------------------------------------
RailFence.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

RailFence specifications:
------------------------------

no. of rows = 2

encrypt(plaintext_utf8, key) where:
- plaintext_utf8: plaintext in UTF8 format
- key: specify no. of rows to use
- return: cipher_text in UTF8 format

decrypt(cipher_text_utf8, key) where:
- cipher_text_utf8: ciphertext in UTF8 format
- key: specify no. of rows used
- return: decrypted text in UTF8 format

Use/modify RailFence_Test.py to test your implementations.
----------------------------------------------------------------------------
"""

def encrypt(plaintext_utf8, key):
  rail = [["\n" for i in range(len(plaintext_utf8))]
          for j in range(key)]
  dir_down = False
  row, col = 0, 0

  for i in range(len(plaintext_utf8)):
    if row == 0 or row == key - 1:
      dir_down = not dir_down
    rail[row][col] = plaintext_utf8[i]
    col += 1
    if dir_down:
      row += 1
    else:
      row -= 1
  result = []
  for i in range(key):
    for j in range(len(plaintext_utf8)):
      if rail[i][j] != "\n":
        result.append(rail[i][j])
  return "".join(result)


def decrypt(cipher_text_utf8, key):
  rail = [["\n" for i in range(len(cipher_text_utf8))]
          for j in range(key)]
  dir_down = None
  row, col = 0, 0
  for i in range(len(cipher_text_utf8)):
    if row == 0:
      dir_down = True
    if row == key - 1:
      dir_down = False
    rail[row][col] = "*"
    col += 1
    if dir_down:
      row += 1
    else:
      row -= 1
  index = 0
  for i in range(key):
    for j in range(len(cipher_text_utf8)):
      if rail[i][j] == "*" and index < len(cipher_text_utf8):
        rail[i][j] = cipher_text_utf8[index]
        index += 1
  result = []
  row, col = 0, 0
  for i in range(len(cipher_text_utf8)):
    if row == 0:
      dir_down = True
    if row == key - 1:
      dir_down = False
    if rail[row][col] != "*":
      result.append(rail[row][col])
      col += 1
    if dir_down:
      row += 1
    else:
      row -= 1
  return "".join(result)