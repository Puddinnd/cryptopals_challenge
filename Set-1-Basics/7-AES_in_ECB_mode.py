from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import base64

key = "YELLOW SUBMARINE"

def decrypt(ciphertext):
	cipher = AES.new(key.encode(), AES.MODE_ECB)
	return cipher.decrypt(ciphertext)

def main():
	ciphertext = base64.b64decode(open('./src/7.txt').read())
	plaintext = unpad(decrypt(ciphertext), 16).decode()
	print(plaintext)

main()
