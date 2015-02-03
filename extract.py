#!/usr/bin/env python

import sys, os
import Image

def decode_image(image):
	"""Check the red portion of an image (r,g,b) tuple for hidden characters
	
	"""
        img = Image.open(image)

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
		
        print str(msg)

if __name__ == "__main__":

    if sys.argv[1] == 'decode':
        decode_image(sys.argv[2])

