#
#		notes:		Cluster Picture
#
#		modified:	04 04 17 08:56 Bhaumik mistry 
#
#		The function takes in an image and 
#		numbers of clusters needed
#
import cv2
from sklearn.cluster import MiniBatchKMeans


def getClusterImage(image, clusterVal):
	"""Clusterize the input image into clusterVal"""
	(h,w) = image.shape[:2]
	image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

	#reshape the image into a feature vector so that k-means can be applied
	image = image.reshape((image.shape[0] * image.shape[1],3))

	# apply k-means
	# apply k-means using the specified number of clusters and
	# then create the quantized image based on the predictions
	clt = MiniBatchKMeans(n_clusters = clusterVal)
	labels = clt.fit_predict(image)
	quant = clt.cluster_centers_.astype("uint8")[labels]

	# #reshape the feature to an iamge
	quant = quant.reshape((h,w,3))
	image = image.reshape((h,w,3))

	quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
	image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

	# return clustered image
	return quant


