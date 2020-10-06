def xor(a, b):
    c = ""
    for i in range(len(a)):
        c += chr(ord(a[i])^ord(b[i]))
    return c.encode()

a = bytes.fromhex("1c0111001f010100061a024b53535009181c").decode('utf-8')
b = bytes.fromhex("686974207468652062756c6c277320657965").decode('utf-8')
print( xor(a, b).hex() )