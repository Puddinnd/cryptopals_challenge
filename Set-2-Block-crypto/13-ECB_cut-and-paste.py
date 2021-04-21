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
		'role': 'user'
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
	### Test input							PKCS#7->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	### 0123456789ABCDEF | 0123456789ABCDEF | 01234   5   6   7   8   9   A   B   C   D   E   F
	### email=eiei@test. | com&uid=10&role= | user\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c
	### email=eiei@test.com&uid=10&role=user\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c
	profile = profile_for("eiei@test.com")
	print("Profile:", profile)
	ciphertext = encrypt(profile)
	plaintext = decrypt(ciphertext)
	decoded_profile = decode_profile(plaintext)
	print("Decoded profile:", decoded_profile)
	### Let's attack by rotate information position and change a bit...
	### swap block 2 and 3 then change user to admin(also change padding too)
	### 0123456789ABCDEF | 012345   6   7   8   9   A   B   C   D   E   F    | 0123456789ABCDEF
	### email=eiei@test. | admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b | com&uid=10&role=
	### email=eiei@test.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0bcom&uid=10&role=
	attack_profile = b'email=eiei@test.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0bcom&uid=10&role='
	print("Attack profile:", attack_profile)
	attacker_ciphertext = encrypt(attack_profile)
	modified_ciphertext_profile = ciphertext[0:BLOCK_SIZE*2] + attacker_ciphertext[BLOCK_SIZE:BLOCK_SIZE*2]
	attacker_plaintext = decrypt(modified_ciphertext_profile)
	attacker_decoded_profile = decode_profile(attacker_plaintext)
	print("Decoded profile:", attacker_decoded_profile)

main()


"""
Thanks for the great idea:
https://braincoke.fr/write-up/cryptopals/cryptopals-ecb-cut-and-paste/
"""