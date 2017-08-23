
#		notes:		Brick counter
#
#		modified:	04 04 17 08:56 Bhaumik mistry 
#

import cv2
import colorPicker


def displayColorInfo():
	""" This method is for the available colors
	and color selection  """
	# for coloe list use this
	print " List of available colors"
	colorList = colorPicker.getColorAndValue()
	#print colorList

def testxx(image,gray_image,pixValArray):
	"""	TO DO RENAME THE FILE	"""
	#displayColorInfo()
	(h,w,rgb) = image.shape[:3]
	for pix in pixValArray:
		text = pix