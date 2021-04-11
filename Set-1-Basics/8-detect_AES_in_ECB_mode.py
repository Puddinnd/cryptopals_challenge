from binascii import unhexlify

block_size = 16

def detectAESECB(ciphertext):
	unhex_ciphertext = unhexlify(ciphertext)
	unhex_ciphertext = [unhex_ciphertext[i:i+block_size] for i in range(0, len(unhex_ciphertext), block_size)]
	strings = {}
	for ct in unhex_ciphertext:
		if not ct in strings:
			strings[ct] = 1
		else:
			strings[ct] += 1
			return True
	return False

def main():
	ciphertext = open("./src/8.txt").read().split('\n')[:-1]
	for c in ciphertext:
		tmp = detectAESECB(c)
		if tmp:
			print(c)

main()
