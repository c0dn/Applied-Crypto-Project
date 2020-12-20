__doc__ = """
----------------------------------------------------------------------------
Des.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

Des specifications:
------------------------------

get_fixed_key() returns a fixed 8 bytes key

def get_random_key() where:
- return: random 8 bytes key

encrypt(key, plaintext_utf8, cipher_mode) where:
- key: a 64 bits key used for encryption
- plaintext_utf8: plaintext encoded in UTF8 format
- cipher_mode: determine cipher mode, able to choose between ECB, CBC, CFB, OFB cipher mode. default cipher mode is CBC
- return: ciphertext encoded in base64 as a string

decrypt(key, cipher_text_utf8, cipher_mode) where:
- key: a 64 bits key used for decryption
- plaintext_utf8: plaintext encoded in UTF8 format
- cipher_mode: determine cipher mode, able to choose between ECB, CBC, CFB, OFB cipher mode. default cipher mode is CBC
- return: decrypted text in UTF8 format

Use/modify Des_Test.py to test your implementations.
----------------------------------------------------------------------------
"""

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


def get_fixed_key():
  # use fixed DES key, 256 bits
  return b"xcryptox"


def get_random_key():
  return get_random_bytes(8)


# DES encrypt using CBC and IV, with default padding (PKCS7)
def encrypt(key, plaintext_utf8, cipher_mode="cbc"):
  if cipher_mode.lower() == "ecb":
    cipher = DES.new(key, DES.MODE_ECB)
  elif cipher_mode.lower() == "cfb":
    cipher = DES.new(key, DES.MODE_CFB)
  elif cipher_mode.lower() == "ofb":
    cipher = DES.new(key, DES.MODE_OFB)
  else:
    cipher = DES.new(key, DES.MODE_CBC)
  cipher_text = cipher.encrypt(pad(plaintext_utf8, DES.block_size))
  enc_bytes = cipher_text
  if cipher_mode.lower() != "ecb":
    enc_bytes += cipher.iv
  base64_bytes_cipher = base64.b64encode(enc_bytes)
  base64_cipher_text = base64_bytes_cipher.decode("ascii")
  return base64_cipher_text


# DES decrypt using CBC and IV, with default un-padding (PKCS7)
def decrypt(key, cipher_text, cipher_mode="cbc"):
  base64_bytes = cipher_text.encode("ascii")
  enc_bytes = base64.b64decode(base64_bytes)
  if cipher_mode.lower() != "ecb":
    cipher_bytes, iv_bytes = enc_bytes[:len(enc_bytes)-8], enc_bytes[len(enc_bytes)-8:]
  else:
    cipher_bytes = enc_bytes
    iv_bytes = None
  if cipher_mode.lower() == "ecb":
    cipher = DES.new(key, DES.MODE_ECB)
  elif cipher_mode.lower() == "cfb":
    cipher = DES.new(key, DES.MODE_CFB, iv_bytes)
  elif cipher_mode.lower() == "ofb":
    cipher = DES.new(key, DES.MODE_OFB, iv_bytes)
  else:
    cipher = DES.new(key, DES.MODE_CBC, iv_bytes)
  decryptedtext_utf = unpad(cipher.decrypt(cipher_bytes), DES.block_size)
  return decryptedtext_utf.decode("utf-8")