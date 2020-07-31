# import the necessary pacakges
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import pylab as plt
import argparse
import cv2

#constrct the argumetn parser and parse the argument 
#ap = argparse.ArgumentParser()
#ap.add_argument("-i","--image", required = True, help = "Path to the image")
#ap.add_argument("-c","--cluster",required = True, type = int, help = "# of clusters")
#args = vars(ap.parse_args())

#load image
#image = cv2.imread(args["image"])
image = cv2.imread("IMG_8009.PNG")
h,w = image.shape[:2];



print("h ", h)
print("w ", w)
black=0;
white=0;
lb=0;
db=0;
skin= 0;


## color codes
# 5 color
# 162 185 225 is skin color
# 26 20 24 is almost black color
# 99 121 154 is light brown color
# 48 52 65 is dark brown color
# 240 240 240 is white color

# 6 color
# 126 151 190	dark brown
# 81 100 129    light brown
# 23 18 22 		black 
# 243 242 238 	white
# 172 194 233 	skin
# 40 40 48		darkest brown

# 6
# for i in xrange(image.shape[0]):
#     for j in xrange(image.shape[1]):
#         pixel = image[i, j]
#         # print pixel
#         if pixel[0] == 172:
#         	image[i,j,0] = 0
#         	image[i,j,1] = 234
#         	image[i,j,2] = 255
#         	skin +=1
#         if pixel[0] == 23:        	
#         	image[i,j,0] = 0
#         	image[i,j,1] = 0
#         	image[i,j,2] = 0
#         	black +=1
#         if pixel[0] == 126:
#         	image[i,j,0] = 0
#         	image[i,j,1] = 196
#         	image[i,j,2] = 255
#         	lb +=1
#         if pixel[0] == 40:
#         	image[i,j,0] = 40
#         	image[i,j,1] = 40
#         	image[i,j,2] = 48
#         	db +=1
#         if pixel[0] == 81:
#         	image[i,j,0] = 46
#         	image[i,j,1] = 47
#         	image[i,j,2] = 104
#         	db +=1
#         if pixel[0] == 243:
#         	image[i,j,0] = 255
#         	image[i,j,1] = 255
#         	image[i,j,2] = 255
#         	white +=1

# print "white ",white
# print "Black ",black
# print "skin ",skin
# print "light b ",lb
# print "dark b ",db        

# # 5
# for i in xrange(image.shape[0]):
#     for j in xrange(image.shape[1]):
#         pixel = image[i, j]
#         print pixel
#         if pixel[0] == 162:
#         	image[i,j,0] = 0
#         	image[i,j,1] = 234
#         	image[i,j,2] = 255
#         	skin +=1
#         if pixel[0] == 26:        	
#         	image[i,j,0] = 0
#         	image[i,j,1] = 0
#         	image[i,j,2] = 0
#         	black +=1
#         if pixel[0] == 99:
#         	image[i,j,0] = 0
#         	image[i,j,1] = 196
#         	image[i,j,2] = 255
#         	lb +=1
#         if pixel[0] == 48:
#         	db +=1
#         if pixel[0] == 240:
#         	image[i,j,0] = 255
#         	image[i,j,1] = 255
#         	image[i,j,2] = 255
#         	white +=1

# print "white ",white
# print "Black ",black
# print "skin ",skin
# print "light b ",lb
# print "dark b ",db



image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

#reshape the image into a feature vector so that k-means can be applied
image = image.reshape((image.shape[0] * image.shape[1],3))

# #apply k-means
clt = MiniBatchKMeans(n_clusters = 5)
labels = clt.fit_predict(image)
quant = clt.cluster_centers_.astype("uint8")[labels]

# #reshape the feature to an iamge
quant = quant.reshape((h,w,3))
image = image.reshape((h,w,3))

quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

# resize to get to crop image
image = cv2.resize(image,(w/7,h/7),interpolation = cv2.INTER_AREA)

# roi and crop image
r = cv2.selectROI(image)
image = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

#chagne color format
#cv2.imwrite("pixel_image_temp5_newColor.png",image);
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image',400,800)


while(1):
    #cv2.imshow("image",np.hstack[(image,quant)])
    cv2.imshow('image',image)
    c = cv2.waitKey(0)
    if c == 27:
        cv2.destoyAllWindows()
        break

#plt.hist(image.ravel(),256,[0,256]); plt.show()


plt.imshow(image,'color')
plt.axis("off")
plt.show()


