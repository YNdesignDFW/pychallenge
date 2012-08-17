"""parseCode takes an argument which is a string of encoded text (each letter has been shifted 2 chars to the right), decodes, then prints decoded text."""
def parseCode(code):

	#print chr(ord('{')-2)
	
	i = 0
	decoded = '';
	"""while i < len(code):
		if code[i] != '.':
			if code[i] != ' ':
				decoded += chr(ord(code[i]) + 2)
		else:
			decoded += code[i]
		i += 1
		print decoded"""
	
	print code.maketrans("KOE","MQG")

parseCode("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
"""rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")  """