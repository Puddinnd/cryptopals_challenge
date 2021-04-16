from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from random import randint
import os

block_size = 16

def xor(x,y):
	return bytes(map(lambda x: x[0]^x[1] , zip(x,y)))

def isECB(ciphertext):
	chunks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
	strings = {}
	for chunk in chunks:
		if not chunk in strings:
			strings[chunk] = 1
		else:
			strings[chunk] += 1
			return True
	return False

def aes_ecb_encrypt(key, rawtext):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(rawtext)

def aes_cbc_encrypt(key, iv, rawtext):
	ciphertext = b""
	prev_block = iv
	for i in range(0, len(rawtext), block_size):
		ciphertext += aes_ecb_encrypt(key, xor(prev_block, rawtext[i:i+block_size]))
		prev_block = ciphertext[i:i+block_size]
	return ciphertext

def encryption_oracle(rawtext):
	key = os.urandom(block_size)
	br = os.urandom(randint(5,10)) ### add random 5-10 bytes before rawtext
	ar = os.urandom(randint(5,10)) ### add random 5-10 bytes after rawtext
	rawtext_extended = pad(br+rawtext+ar, block_size)
	if randint(0,1):
		### Encrypt by ECB mode
		print("encrypted by mode: ECB")
		return aes_ecb_encrypt(key, rawtext_extended)
	else:
		### Encrypt by CBC mode
		print("encrypted by mode: CBC")	
		iv = os.urandom(block_size)
		return aes_cbc_encrypt(key, iv, rawtext_extended)
		

def main():
	rawtext = b"A" * block_size * 5
	ciphertext = encryption_oracle(rawtext)
	if isECB(ciphertext):
		print("Guess: ECB")
	else:
		print("Guess: CBC?")

main()
