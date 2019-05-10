from cloud import *


def breakcloud(cloud):
	"""
	receives 'cloud', an object of type Cloud.
	creates a file with the name 'plain.txt' that stores the current text that is encrypted in the cloud.
	you can use only the Read/Write interfaces of Cloud (do not use its internal variables.)
	"""
	original_output = ""
	original_cipher_text = ""
	zero_byte = b'\x00'
	i = 0
	current_byte = cloud.Write(i, zero_byte)

	while current_byte != None:
		original_cipher_text += current_byte
		original_output += cloud.Read(i)
		i += 1
		current_byte = cloud.Write(i, zero_byte)

	with open("plain.txt", mode="wb+") as file:
		file.write(xor(original_cipher_text, original_output))


def xor(x, y):
	"""
	xor function.
	:param x: first element in the xor.
	:param y: second element in the xor.
	:return: x ^ y
	"""
	return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))