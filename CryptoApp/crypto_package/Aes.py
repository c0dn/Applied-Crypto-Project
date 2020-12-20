__doc__ = """
----------------------------------------------------------------------------
Aes.py, william
Tested with PyCharm Professional Edition 2020.1.1 x64, python 3.7

Aes specifications:
------------------------------

get_fixed_key() returns a fixed 32 bytes key

def get_random_key(size) where:
- size: determine key size in bits. able to choose between 128/192/256 key size. default key size generated is 256 bits
- - return: random 16/24/32 bytes key

encrypt(key, plaintext_utf8, cipher_mode) where:
- key: a 128/192/256 bits key used for encryption
- plaintext_utf8: plaintext encoded in UTF8 format
- cipher_mode: determine cipher mode, able to choose between ECB, CBC, CFB, OFB cipher mode. default cipher mode is CBC
- return: ciphertext encoded in base64 as a string

decrypt(key, cipher_text_utf8, cipher_mode) where:
- key: a 128/192/256 bits key used for decryption
- plaintext_utf8: plaintext encoded in UTF8 format
- cipher_mode: determine cipher mode, able to choose between ECB, CBC, CFB, OFB cipher mode. default cipher mode is CBC
- return: decrypted text in UTF8 format

Use/modify Aes_Test.py to test your implementations.
----------------------------------------------------------------------------
"""


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


def get_fixed_key():
  # use fixed AES key, 256 bits
  return b"kshenmvuqowkdjfnchaiqjwkenlpanco"


def get_random_key(size=256):
  if size == 256:
    return get_random_bytes(32)
  elif size == 192:
    return get_random_bytes(24)
  elif size == 128:
    return get_random_bytes(16)
  else:
    return None


# AES encrypt using CBC and IV, with default padding (PKCS7)
def encrypt(key, plaintext_utf8, cipher_mode="cbc"):
  if cipher_mode.lower() == "ecb":
    cipher = AES.new(key, AES.MODE_ECB)
  elif cipher_mode.lower() == "cfb":
    cipher = AES.new(key, AES.MODE_CFB)
  elif cipher_mode.lower() == "ofb":
    cipher = AES.new(key, AES.MODE_OFB)
  else:
    cipher = AES.new(key, AES.MODE_CBC)
  cipher_text = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
  enc_bytes = cipher_text
  if cipher_mode.lower() != "ecb":
    enc_bytes += cipher.iv
  base64_bytes_cipher = base64.b64encode(enc_bytes)
  base64_cipher_text = base64_bytes_cipher.decode("ascii")
  return base64_cipher_text


# AES decrypt using CBC and IV, with default un-padding (PKCS7)
def decrypt(key, cipher_text, cipher_mode="cbc"):
  base64_bytes = cipher_text.encode("ascii")
  enc_bytes = base64.b64decode(base64_bytes)
  if cipher_mode.lower() != "ecb":
    cipher_bytes, iv_bytes = enc_bytes[:len(enc_bytes)-16], enc_bytes[len(enc_bytes)-16:]
  else:
    cipher_bytes = enc_bytes
    iv_bytes = None
  if cipher_mode.lower() == "ecb":
    cipher = AES.new(key, AES.MODE_ECB)
  elif cipher_mode.lower() == "cfb":
    cipher = AES.new(key, AES.MODE_CFB, iv_bytes)
  elif cipher_mode.lower() == "ofb":
    cipher = AES.new(key, AES.MODE_OFB, iv_bytes)
  else:
    cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
  decryptedtext_utf = unpad(cipher.decrypt(cipher_bytes), AES.block_size)
  return decryptedtext_utf.decode("utf-8")