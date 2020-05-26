from random import randint
import matplotlib.pylab as plt

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, key):

	#convert the letters to uppercase
	plain_text = plain_text.upper()
	cipher_text = ''
	#consider all the plain_text letters: enumerate returns the item + it's index
	for index, char in enumerate(plain_text):
		#the value with which we shift the given letter
		key_index = key[index]
		#the given letter in the plain_text
		char_index = ALPHABET.find(char)
		#encrypted letter = char's value in the plain_text + random value (+using mod26)
		cipher_text += ALPHABET[(char_index+key_index)%len(ALPHABET)]	
		
	return cipher_text	

def decrypt(cipher_text, key):

	plain_text = ''
	
	for index, char in enumerate(cipher_text):
		key_index = key[index]
		char_index = ALPHABET.find(char)
		plain_text += ALPHABET[(char_index-key_index)%len(ALPHABET)]	
		
	return plain_text	

def random_sequence(plain_text):
	#we store the random values in a list
	random_sequence = []
	#size of the key = size of the plain_text
	for rand in range(len(plain_text)):
		random_sequence.append(randint(0,len(ALPHABET)))
		
	return random_sequence
	
if __name__ == "__main__":
	
	plain_text = "Shannon defined the quantity of information produced by a source for example the quantity in a message by a formula similar to the equation that defines thermodynamic entropy in physics. In its most basic terms Shannons informational entropy is the number of binary digits required to encode a message. Today that sounds like a simple even obvious way to define how much information is in a message. In 1948, at the very dawn of the information age, this digitizing of information of any sort was a revolutionary step. His paper may have been the first to use the word bit, short for binary digit. As well as defining information, Shannon analyzed the ability to send information through a communications channel. He found that a channel had a certain maximum transmission rate that could not be exceeded. Today we call that the bandwidth of the channel. Shannon demonstrated mathematically that even in a noisy channel with a low bandwidth, essentially perfect, error-free communication could be achieved by keeping the transmission rate within the channel's bandwidth and by using error-correcting schemes: the transmission of additional bits that would enable the data to be extracted from the noise-ridden signal. Today everything from modems to music CDs rely on error-correction to function. A major accomplishment of quantum-information scientists has been the development of techniques to correct errors introduced in quantum information and to determine just how much can be done with a noisy quantum communications channel or with entangled quantum bits (qubits) whose entanglement has been partially degraded by noise."
	key = random_sequence(plain_text)
	cipher_text = encrypt(plain_text, key)
	print("Encrypted message: \n%s" % cipher_text)
	decrypted_text = decrypt(cipher_text, key)
	print("Decrypted message: \n%s" % decrypted_text)
	
	