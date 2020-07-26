
#		notes:		colorPaletteGenerator.py
#                   
#
#		modified:	04 04 17 08:56 Bhaumik mistry 
#                       created
#       modified:   06 08 17 08:22 bm
#                       image write funtion.
#                       image name :- RefColorImage.png

## for generating the color palette layout ##
import cv2
import numpy as np
import colorPicker

def createBlankImage(rgb,h,w):
    """ Create blank image """
    imageHeight = h
    imageWeight = w
    image = np.zeros((imageHeight,imageWeight,rgb),np.uint8)
    return image

def colorTheImage(image,number,color):
    """ Fill color in the image """
    colorItHeight = 300
    colorItWidth = 50
    startWidth = colorItWidth*number
    endWidth=startWidth+50
    image[1:colorItHeight,startWidth:endWidth] = color
    return image

def displayImage(image,nameImage):
    """ Displays the image with nameImage as window image """
    while True:
        cv2.namedWindow("clustered")
        cv2.moveWindow("clustered",500,450)
        cv2.imshow("clustered",image)
        key = cv2.waitKey(1) & 0xFF
        # press q to close to
        if key == ord("q"):
            break    

def paintTheImage(image):
    """ paints the image with lego colors from colorPicker """
    color = colorPicker.getColorAndValue()
    count = 0
    for x in sorted(color):
        colorReversed = tuple(reversed(color[x]))
        image = colorTheImage(image,count,colorReversed)
        count +=1
    return image

def populateTheList(image,list):
    """ paint the image with colors from image """
    countT = 0 
    for pix in list:
        image = colorTheImage(image,countT,pix)
        countT += 1
    return image

def run():
    # Create an image
    image = createBlankImage(3,300,600)
    # paint the created image with colors from color picker
    image = paintTheImage(image)
    # display the image created
    displayImage(image,"newImage")
    # write image
    #cv2.imwrite("Test/RefColorImage.png",image);
    # Destroy all the windows
    cv2.destroyAllWindows()

run()