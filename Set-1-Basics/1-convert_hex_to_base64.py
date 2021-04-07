import base64
import binascii
hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

### Hex to Ascii in 2 ways 
print(binascii.unhexlify(hex_str))
print(bytes.fromhex(hex_str))

### Bytes to String
text = bytes.fromhex(hex_str)
text = text
print(text)

### Ascii to base64
print(binascii.b2a_base64(text))
print(base64.b64encode(text))