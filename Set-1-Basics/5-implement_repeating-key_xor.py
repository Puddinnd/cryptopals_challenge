key = "ICE"
text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

cipher = "".join([chr(ord(text[i])^ord(key[i%3])) for i in range(len(text))])
print(cipher.encode().hex())
