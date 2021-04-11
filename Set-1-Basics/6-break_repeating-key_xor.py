import binascii
import base64
from pprint import pprint

### Calculate edit distance/Hamming distance between 2 strings
def calHammingDistance(a, b):
    bin_a = bin(int(binascii.hexlify(a), 16))
    bin_b = bin(int(binascii.hexlify(b), 16))
    h_sum = 0
    for x, y in zip(bin_a, bin_b):  
        if x != y:
            h_sum += 1
    return h_sum

### Transpose text
def getTransposeFromText(text, size):
    transpose_chunks = []
    for i in range(size):
        transpose_chunks.append("".join([chr(text[c]) for c in range(i, len(text), size)]))
    # print(transpose_chunks)
    return transpose_chunks

### Function from challenge 3
score = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253,
    "e": 0.12702, "f": 0.02228, "g": 0.02015, "h": 0.06094,
    "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929,
    "q": 0.00095, "r": 0.05987, "s": 0.06327, "t": 0.09056,
    "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00074, " ": 0.13000
}
def scoring(text):
    return sum([score.get(b, 0) for b in text.lower()])

### Break repeating-key XOR
def breakRepeatingKeyXOR(ciphertext):
    all_distance = []
    ### Find smallest normailzed distance
    for ks in range(2,40):
        chunks = [ciphertext[i:i+ks] for i in range(0, len(ciphertext), ks)]
        distance = []
        for i in range(0, len(chunks), 2):
            try:
                ### Calculate hamming distance of pair
                pair_distance = calHammingDistance(chunks[i], chunks[i+1])
                ### Nomalize by dividing by ks(KEYSIZE)
                distance.append(pair_distance/ks)
            except:
                ### Not have any pair left
                break
        all_distance.append({
            "keysize": ks,
            "distance": sum(distance)/len(distance)
            })
    all_distance.sort(key=lambda x:x['distance'])
    # pprint(all_distance)
    possible_ks = all_distance[:5]

    highest_plaintext_score = 0
    plaintext = ""
    real_key = ""
    ### Find keys from possible keysize
    for pks in possible_ks:
        ks = pks['keysize']
        chunks = getTransposeFromText(ciphertext, ks)
        key = ""
        for chunk in chunks:
            highest_chunk_score = 0
            k = ""
            for i in range(256):
                tmp = "".join([chr(ord(c)^i) for c in chunk])
                chunk_score = scoring(tmp)
                if chunk_score > highest_chunk_score:
                    highest_chunk_score = chunk_score
                    k = chr(i)
            key += k
        # print("possible key:", key)

        tmp_plaintext = "".join([chr(ciphertext[i]^ord(key[i%ks])) for i in range(len(ciphertext))])
        plaintext_score = scoring(tmp_plaintext)
        if plaintext_score > highest_plaintext_score:
            highest_plaintext_score = plaintext_score
            plaintext = tmp_plaintext
            real_key = key

    print("Key: ", real_key)
    print("Plaintext:", plaintext, sep="\n")


def main():
    ## Test calHammingDistance function
    # d1 = b"this is a test"
    # d2 = b"wokka wokka!!!"
    # dis = calHammingDistance(d1, d2)
    # print("Distance:", dis)

    ciphertext = base64.b64decode(open("./src/6.txt").read())
    # print(ciphertext)
    breakRepeatingKeyXOR(ciphertext)

main()