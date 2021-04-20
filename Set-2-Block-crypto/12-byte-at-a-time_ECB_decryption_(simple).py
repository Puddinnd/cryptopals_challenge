from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from base64 import b64decode
import os


### Create global variable random key
BLOCK_SIZE = 16
KEY = os.urandom(BLOCK_SIZE)
extension_string = b64decode("""
Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK
""")

### aes_128_ecb
def oracle_encrypt(plaintext):
	cipher = AES.new(KEY, AES.MODE_ECB)
	return cipher.encrypt(pad(plaintext + extension_string, 16))

def oracle_decrypt():
	### unknow string len =SS 144 - 6 = 138
	### 144 / 6 = 9 blocks
	unknown_text_len = 144
	known_string = b""
	nblock = (unknown_text_len - 1) // BLOCK_SIZE
	start = nblock * BLOCK_SIZE
	stop = start + BLOCK_SIZE
	while unknown_text_len > (144 - 138):
		unknown_text_len -= 1
		rawtext = b'A' * unknown_text_len
		ciphertext = oracle_encrypt(rawtext + extension_string)
		ciphertext = ciphertext[start:stop]
		for i in range(256):
			current_chr = chr(i).encode('utf8')
			guess_plaintext = rawtext + known_string + current_chr
			guess_ciphertext = oracle_encrypt(guess_plaintext)[start:stop]
			if ciphertext == guess_ciphertext:
				known_string += current_chr
				break
	print(known_string.decode('utf8'))


def main():
	oracle_decrypt()

main()

