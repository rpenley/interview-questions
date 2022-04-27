#!/usr/bin/python3

import sys

try:
	with open(sys.argv[1], 'r') as doc:
		document = doc.read()
		formatted = document.split('. ')
		for sentence in formatted:
			if len(sentence) > 40:
				sentence = sentence.rpartition(' ')
				for part in sentence:
					print(part)
			else:
				print(sentence)
except IndexError:
	print("ERROR: empty argument list, no text file was provided")
