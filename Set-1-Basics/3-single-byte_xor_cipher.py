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

def main():
	cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

	cipher = bytes.fromhex(cipher)
	print(cipher)
	strings = []
	### XOR  string with single byte and keep in list
	for i in range(256):
		tmp = "".join(list(map(lambda x: chr(x^i), cipher)))
		strings.append(tmp)
	### Scoring all strings and choose the highest one
	high_score = 0
	mostscore_string = ""
	for t in strings:
		tmp_score = scoring(t)
		if tmp_score > high_score:
			high_score = tmp_score
			mostscore_string = t
	print(mostscore_string)
	print(high_score)
main()