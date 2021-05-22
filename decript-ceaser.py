import configparser

configParser = configparser.RawConfigParser()
configFilePath = r'C:\Users\isaac\encrypt\config.txt'
configParser.read(configFilePath)

def decrypt(msg, step):
	outText = []
	cryptText = []
	
	caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	nocaps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for letter in msg:
		if letter in caps:
			contents = caps.index(letter)
			decrypt = (contents - step) % 26
			cryptText.append(decrypt)
			newLetter = caps[decrypt]
			outText.append(newLetter)
		elif letter in nocaps:
			contents = nocaps.index(letter)
			decrypt = (contents - step) % 26
			cryptText.append(decrypt)
			newLetter = nocaps[decrypt]
			outText.append(newLetter)
	return outText

letters = int(configParser.get('letters', 'l'))
word = configParser.get('letters', 'output')

output = decrypt(word, letters)
print("-------------------------")
print(output)
print("-------------------------")