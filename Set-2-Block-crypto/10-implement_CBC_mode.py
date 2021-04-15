from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16
xor = lambda x,y: "".join([chr(i^j) for i,j in zip(x,y)]).encode()

def aes_ecb_encrypt(key, rawtext):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(rawtext)

def aes_ecb_decrypt(key, ciphertext):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(ciphertext)

def aes_cbc_encrypt(key, iv, rawtext):
	prev_block = iv
	ciphertext = b""
	for i in range(0, len(rawtext), BLOCK_SIZE):
		ciphertext += aes_ecb_encrypt(key, xor(prev_block, rawtext[i:i+BLOCK_SIZE]))
		prev_block = ciphertext[i:i+BLOCK_SIZE]
	return ciphertext

def aes_cbc_decrypt(key, iv, ciphertext):
	prev_block = iv
	rawtext = b""
	for i in range(0, len(ciphertext), BLOCK_SIZE):
		tmp = ciphertext[i:i+BLOCK_SIZE]
		rawtext += xor(prev_block, aes_ecb_decrypt(key, ciphertext[i:i+BLOCK_SIZE]))
		prev_block = tmp
	return rawtext

def main():
	ciphertext = base64.b64decode(open('./src/10.txt').read())
	KEY = "YELLOW SUBMARINE".encode('utf8')
	IV = (chr(0) * BLOCK_SIZE).encode('utf8')
	plaintext = aes_cbc_decrypt(KEY, IV, ciphertext)
	print(plaintext.decode())

main()