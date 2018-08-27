from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2


def testing_image():

	# load the image
	image = cv2.imread("test5.jpeg",0)
	# orig = image.copy()
	orig = cv2.imread("test5.jpeg",1)
	 
	# pre-process the image for classification
	image = cv2.resize(image, (128, 128))
	image = image.astype("float32") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	print("[INFO] loading network...")

	model=load_model('mymodel.h5')

	predictions=model.predict(image)
	print(predictions[0])
	label = ['Vehicle','Potholes','Freeways','Traffic','Pedestrian Lanes']

	label_vehicle = "{}: {:.2f}%".format(label[0], predictions[0][0] * 100)
	label_potholes = "{}: {:.2f}%".format(label[1], predictions[0][1] * 100)
	label_freeways = "{}: {:.2f}%".format(label[2], predictions[0][2] * 100)
	label_traffic = "{}: {:.2f}%".format(label[3], predictions[0][3] * 100)
	label_pedestrain_lanes = "{}: {:.2f}%".format(label[4], predictions[0][4] * 100)
	 
	# draw the label on the image
	output = imutils.resize(orig, width=400)
	cv2.putText(output, label_vehicle, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_potholes, (10, 50),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_freeways, (10, 100),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_traffic, (10, 125),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_pedestrain_lanes, (10, 150),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)
	 
	# show the output image
	cv2.imshow("Output", output)
	cv2.waitKey(0)

	cv2.destroyAllWindows()
	cv2.waitKey(1)


testing_image()