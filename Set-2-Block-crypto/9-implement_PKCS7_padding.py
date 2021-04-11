block_size = 20
pad = lambda x : x + (block_size - len(x)%block_size) * chr(block_size - len(x)%block_size)

def main():
	plaintext = "YELLOW SUBMARINE"
	paded_plaintext = pad(plaintext).encode('utf8')
	print(paded_plaintext)

main()