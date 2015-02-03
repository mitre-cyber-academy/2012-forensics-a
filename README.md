Challenge Description
=====================

The included .pngs of the MITRE logo contain the flag "MCA-1ACCEBAB".
The first, "mitre_enc.png" has the flag encoded n the red component of the first 
pixels of the image. The first pixel provides the length of the string, and
the next pixels provide the message.

If the challenge is better geared towards use of stanard stegenographic tools, 
OpenStego was used to encode the message using LSB-based stenography, so 
the tools used for detecting stegonography should catch this.

Solution
========

Using the Python Image Library (PIL) (I'm unsure of what tools they will be
using in Lesson 5)

def decode_image(img):
	"""Check the red portion of an image (r,g,b) tuple for hidden characters
	
	"""
	width, height = img.size
	msg = ""
	
	index = 0
	
	for row in range(height):
		for col in range(width):
			r,g,b,a = img.getpixel((col, row))
			
			if row == 0 and col == 0:
				length = r
			elif index <= length:
				msg += chr(r)
			
			index += 1
		
		return msg
