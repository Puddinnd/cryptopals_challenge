cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
cipher_decoded = bytes.fromhex(cipher).decode('utf-8')

alpha = "qwertyuiopasdfghjklzxcvbnm"
alpha += alpha.upper()
alpha += "\'.!"

for i in alpha:
    tmp = ""
    for c in cipher_decoded:
        tmp += chr(ord(i) ^ ord(c))
    if tmp[0] in alpha:
        print(i, tmp)