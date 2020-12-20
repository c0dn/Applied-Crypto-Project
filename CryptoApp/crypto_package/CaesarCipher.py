__doc__ = """
----------------------------------------------------------------------------
CaesarCipher.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

CaesarCipher specifications:
------------------------------

encrypt(key, plaintext_utf8) where:
- key: Caesar key, e.g. 3 denotes shifting 3 character positions
- plaintext_utf8: plaintext in UTF8 format
- return: ciphertext in UTF8 format

decrypt(key, cipher_text_utf8) where:
- key: Caesar key, e.g. 3 denotes shifting 3 character positions
- cipher_text_utf8: ciphertext in UTF8 format
- return: decrypted text in UTF8 format

Use/modify CaesarCipher_Test.py to test your implementations.
----------------------------------------------------------------------------
"""


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/="    # Q1, Q2, Q3

def encrypt(key, plaintext_utf8):
  cipher_text_utf8 = ""

  for character in plaintext_utf8:
    if character.upper() in LETTERS:
      # get the character position
      if character.isupper():
        position = LETTERS.find(character) # hint: use find()
        position = position + key

        # wrap-around if position >= length of LETTERS
        if position >= len(LETTERS):
          position = position - 39

        # append encrypted character
        cipher_text_utf8 += LETTERS[position]

      else:
        position = LETTERS.find(character.upper()) # hint: use find()
        position = position + key

        # wrap-around if position >= length of LETTERS
        if position >= len(LETTERS):
          position = position - 39

        # append encrypted character
        cipher_text_utf8 = cipher_text_utf8 + LETTERS[position].lower()

    else:
      # append character without encrypting
      cipher_text_utf8 = cipher_text_utf8 + character

  return cipher_text_utf8


def decrypt(key, cipher_text_utf8):
  decrypted_text_utf = ""

  for character in cipher_text_utf8:
    if character.upper() in LETTERS:
      # get the character position
      if character.isupper():
        position = LETTERS.find(character) # hint: use find()
        position = position - key
        # wrap-around if position >= length of LETTERS
        if position < 0 :
          position = position + 39

        # append encrypted character
        decrypted_text_utf = decrypted_text_utf + LETTERS[position]

      else:
        position = LETTERS.find(character.upper()) # hint: use find()
        position = position - key

        # wrap-around if position >= length of LETTERS
        if position < 0:
          position = position + 39

        # append encrypted character
        decrypted_text_utf = decrypted_text_utf + LETTERS[position].lower()


    else:
      # append character without encrypting
      decrypted_text_utf = decrypted_text_utf + character

  return decrypted_text_utf


