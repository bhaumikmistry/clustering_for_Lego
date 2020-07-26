#
#		notes:		select image, crop the image and 
#					resize, pixelate, posterize using
# 					K-means, count the lego bricks.
#
#		modified:	04 02 17 9:14 bm 
#						cropping works fine,
#						next step to mergee the k-means
#						and the lego brick counter
#		modified:	05 31 17 23:00 bm 
#						above works and tested
#						edit on histogram print.
#		modified:	06 02 17 18:50 bm
#						started working on vsc2
#						colorPicker will be helpful for 
#						color list and changing colors
#						

import cv2
import clusterPicture
import brickCounter
import colorPicker
import colorPaletteGenerator
#from matplotlib import pyplot as plt

# To store the corners for 
# cropping the image with mouse click
refPt =[]
cropping = False


def click_and_crop(event,x,y,flags,param):
	""" To call when cropping is needed 
		records the mouse click and crops
		the image and displays it.
		The click parameters are stored in 
		global variable refPt """
	global refPt, cropping 

	# Upper left of the crop square selection
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x,y)]
		print(refPt[0])
		cropping = True

	# Lower right of the crop square selection
	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x,y))
		print(refPt)
		cropping = False
		cv2.rectangle(image,refPt[0],refPt[1],(0,255,0),2)
		cv2.imshow("image",image)

def displayColorsImage(pixArray):
	""" Function to create and display an image """
	print("Displaying color map")
	lenList = len(pixArray)
	h = 300
	print(lenList)
	print(lenList*50)
	# creat a blank image
	imageColorMap = colorPaletteGenerator.createBlankImage(1,h,lenList*50)
	# paint the created image with colors from list
	imageColorMap = colorPaletteGenerator.populateTheList(image,pixArray)
	cv2.namedWindow('Color map')
	cv2.moveWindow('Color map',500,300)
	cv2.imshow('Color map', imageColorMap)

def displayRefColorImage():
	""" Display image for reffence lego color image """
	print("Displaying ref color image")
	imageReference = cv2.imread("Test/RefColorImage.png")
	cv2.namedWindow('Reference lego color image')
	cv2.moveWindow('Reference lego color image',630,300)
	cv2.imshow('Reference lego color image', imageReference)


# Read image
image = cv2.imread("test.jpg")
h,w = image.shape[:2];


# Resize image to fit in the screen
if h >= 600:
	image = cv2.resize(image,(int(w/3),int(h/3)),interpolation = cv2.INTER_AREA)

# back-up of original image
clone = image.copy();

# cropping procedure
cv2.namedWindow('image')
#call cropping method to get ROI
cv2.setMouseCallback('image',click_and_crop,image)
#cv2.namedWindow("image1", cv2.WINDOW_NORMAL)

#Debug
#print refPt

# Display image
while True:
	cv2.imshow("image",image)
	key = cv2.waitKey(1) & 0xFF

	# press q to close to
	if key == ord("q"):
		break

# draw
if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
	# Display image
	while True:
		cv2.namedWindow('ROI')
		cv2.moveWindow('ROI',0,int(50+h/3))
		cv2.imshow('ROI', roi)
		key = cv2.waitKey(1) & 0xFF

		# press q to close to
		if key == ord("q"):
			break


# To write image
if True:
	cv2.imwrite("Test/crop_image.png",roi);

h,w = roi.shape[:2];

ratio = w/float(h)
print("ratio = ", ratio)
print("h = ",h," w = ",w)
print("please choose a new height and width, will be set automatically")
newH = input("type h = ")
print("New h is: ",newH)
newW = float(newH)*ratio
print("New w is: ",newW)
roi = cv2.resize(roi,(int(newW),int(newH)),interpolation = cv2.INTER_AREA)


# Get clustered image
roi = clusterPicture.getClusterImage(roi, 5)

# Color to gray
# roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)


# To write image
if True:
	cv2.imwrite("Test/clust_image.png",roi);


hist = cv2.calcHist([gray_roi],[0],None,[256],[0,256])

#testing the histogram and graysvale image theory
if True:
	cv2.imwrite("Test/gray_clust_image.png",gray_roi);


# now only five pixel numbers will be calculated
# For loop will only print the non zero values from
# the histogram insted of all the values.
# pixVal is the pixel value 
# pix is the number of occurance.
pixVal = 0;	# to get color information from histogram
pixValArray =[]
for pix in hist:
	if pix > 0:
		pixValArray.append(pixVal)
		pixVal+=1
		print(pixVal,pix)
	else:
		pixVal+=1

h,w = roi.shape[:2];
# for display
roi1 = cv2.resize(gray_roi, (w*5,h*5),interpolation = cv2.INTER_NEAREST)

while True:
	cv2.namedWindow("clustered")
	cv2.moveWindow("clustered",500,100)
	cv2.imshow("clustered",roi1)
	key = cv2.waitKey(1) & 0xFF
 
	# press q to close to
	if key == ord("q"):
		break

displayColorsImage(pixValArray)
#displayRefColorImage()

# q to kill all
while True:
	# press q to close to
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		cv2.destroyAllWindows()
		break

xx = brickCounter.testxx(roi,gray_roi,pixValArray)

# display histogram 
#plt.hist(roi.ravel(),256,[0,256]); plt.show()


# Next step is to get the colors from user to 
# colors related from lego colors.





