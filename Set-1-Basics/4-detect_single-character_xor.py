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

def main():
	### Read cipher from file
	ciphers = open("./src/4.txt").read()
	ciphers = ciphers.split('\n')

	### Scoring strings after XOR with single byte
	highscore = 0
	highestscore_text = ""
	for cipher in ciphers:
		for i in range(256):
			tmp = "".join(list(map(lambda x: chr(x^i), bytes.fromhex(cipher))))
			score = scoring(tmp)
			if score > highscore:
				highscore = score
				highestscore_text = tmp
	print(highscore)
	print(highestscore_text)

main()