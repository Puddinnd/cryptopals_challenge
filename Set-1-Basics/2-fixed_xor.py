import binascii

a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

a = bytes.fromhex(a)
b = bytes.fromhex(b)

print(a)
print(b)

### First way to xor
ans = ""
for i in range(len(a)):
	ans += chr(a[i]^b[i])
print(ans)

### Second way to xor
ans = "".join(list(map(lambda x,y: chr(x^y), a, b)))
print(ans)

### Convert string to hex
print(ans.encode().hex())
print(binascii.hexlify(ans.encode()))