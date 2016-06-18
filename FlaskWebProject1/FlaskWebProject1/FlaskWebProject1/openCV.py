import cv2

def resizeImage(placeId,filename):
	image = cv2.imread(str(filename))
	#calc the ratio
	r = 250.0 / image.shape[1]
	dim = (250, int(image.shape[0] * r))
	 
	# perform the actual resizing of the image
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	
	cv2.imwrite(str(placeId)+"_thumbnail.jpg", resized)