import configparser

configParser = configparser.RawConfigParser()
configFilePath = r'config.txt'
configParser.read(configFilePath)

def encrypt(msg, step):
	outText = []
	cryptText = []

	caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	nocaps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for letter in msg:
		if letter in caps:
			contents = caps.index(letter)
			encrypt = (contents + step) % 26
			cryptText.append(encrypt)
			newLetter = caps[encrypt]
			outText.append(newLetter)
		elif letter in nocaps:
			contents = nocaps.index(letter)
			encrypt = (contents + step) % 26
			cryptText.append(encrypt)
			newLetter = nocaps[encrypt]
			outText.append(newLetter)
	return outText

letters = int(configParser.get('letters', 'l'))
word = configParser.get('letters', 'word')

output = encrypt(word, letters)

print("-------------------------")
print(output)
print("-------------------------")

with open('config.txt', 'r') as file:
    data = file.readlines()

data[6] = 'output = ' + str(output) + '\n'

with open('config.txt', 'w') as file:
    file.writelines( data )