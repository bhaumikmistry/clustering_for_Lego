#
#		notes:		select image, crop the image and 
#					resize, pixelate, posterize using
# 					K-means, count the lego bricks.
#
#		modified:	04 02 17 9:14 Bhaumik mistry 
#					cropping works fine,
#					next step to mergee the k-means
#					and the lego brick counter


import cv2
import clusterPicture
#from matplotlib import pyplot as plt

# To store the corners for 
# cropping the image with mouse click
refPt =[]
cropping = False

# To call when cropping us needed,
# records the mouse click and crops
# the image and displays
def click_and_crop(event,x,y,flags,param):
	global refPt, cropping 

	# Upper left of the crop square selection
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x,y)]
		print refPt[0]
		cropping = True

	# Lower right of the crop square selection
	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x,y))
		print refPt
		cropping = False
		cv2.rectangle(image,refPt[0],refPt[1],(0,255,0),2)
		cv2.imshow("image",image)

# Read image
image = cv2.imread("IMG_8009.PNG")
h,w = image.shape[:2];


# Resize image to fit in the screen
if h >= 600:
	image = cv2.resize(image,(w/3,h/3),interpolation = cv2.INTER_AREA)

# back of original image
clone = image.copy();

# cropping prcoedure
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_and_crop,image)
#cv2.namedWindow("image1", cv2.WINDOW_NORMAL)

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
		cv2.moveWindow('ROI',0,50+h/3)
		cv2.imshow('ROI', roi)
		key = cv2.waitKey(1) & 0xFF

		# press q to close to
		if key == ord("q"):
			break


# To write image
if True:
	cv2.imwrite("Test/crop_image.jpg",roi);

h,w = roi.shape[:2];

ratio = w/float(h)
print "ratio = ", ratio
print "h = ",h," w = ",w
print "please choose a new h and w will be set automatically adjusted"
newH = raw_input("type h = ")
print "New h is: ",newH
newW = float(newH)*ratio
print "New w is: ",newW
roi = cv2.resize(roi,(int(newW),int(newH)),interpolation = cv2.INTER_AREA)


# Get clustered image
roi = clusterPicture.getClusterImage(roi, 5)

# Color to gray
# roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)


# To write image
if True:
	cv2.imwrite("Test/clust_image.jpg",roi);


hist = cv2.calcHist([roi],[0],None,[256],[0,256])
print hist




h,w = roi.shape[:2];
# for display
roi1 = cv2.resize(roi, (w*5,h*5),interpolation = cv2.INTER_NEAREST)

while True:
	cv2.namedWindow("clustered")
	cv2.moveWindow("clustered",500,100)
	cv2.imshow("clustered",roi1)
	key = cv2.waitKey(1) & 0xFF
 
	# press q to close to
	if key == ord("q"):
		break

cv2.destroyAllWindows()

# display hstogram 
#plt.hist(roi.ravel(),256,[0,256]); plt.show()


# Next step is to get the colors from user to 
# colors related from lego colors.





