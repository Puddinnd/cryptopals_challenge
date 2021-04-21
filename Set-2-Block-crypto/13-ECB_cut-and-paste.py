from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os

BLOCK_SIZE = 16
KEY = os.urandom(BLOCK_SIZE)
cipher = AES.new(KEY, AES.MODE_ECB)

def profile_for(user):
	if '=' in user or '&' in user:
		return "character '&' and '=' are not allowed."
	p = {
		'user': user,
		'uid': 10,
		'role': 'admin'
	}
	return ("email=%s&uid=%d&role=%s" % (p['user'], p['uid'], p['role'])).encode('utf8')

def decode_profile(user_profile):
	profile = {}
	for data in user_profile.decode('utf8').split('&'):
		data = data.split('=')
		profile[data[0]] = data[1]
	return profile

def encrypt(plaintext):
	return cipher.encrypt(pad(plaintext, BLOCK_SIZE))

def decrypt(ciphertext):
	return unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)

def main():
	profile = profile_for("eiei")
	ciphertext = encrypt(profile)
	plaintext = decrypt(ciphertext)
	decoded_profile = decode_profile(plaintext)
	print(decoded_profile)

main()
