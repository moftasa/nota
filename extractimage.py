import re

def find_image(text):

	match = re.search("(?P<url>https?://[^\s]+)", text)
	if match is None:
		return None
	else:
		match = match.group("url")
	if (match[-3:] == "jpg") or (match[-3:]=="JPG") or (match[-4:]=="jpeg") or (match[-3:]=="png") or (match[-3:]=="PNG"):
		return match

