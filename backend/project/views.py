from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Worker, User, Complains
import os, base64, json

# ML files

# testing
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# Training
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten, Activation
from scipy.misc import imread
from sklearn.cluster import KMeans
from keras.layers import Dense, Input
from keras.models import load_model
import tensorflow as tf
import keras.backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import random
import pandas as pd
import time

from django.core.files.base import ContentFile

# Create your views here.

# testing functions
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


# Training functions
class LeNet:
    @staticmethod
    def build(width, height, depth, classes):
        # initialize the model
        model = Sequential()
        inputShape = (height, width, depth)

        # if we are using "channels first", update the input shape
        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)

        # first set of CONV => RELU => POOL layers
        model.add(Conv2D(20, (5, 5), padding="same",
            input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # second set of CONV => RELU => POOL layers
        model.add(Conv2D(50, (5, 5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        # return the constructed network architecture
        return model

EPOCHS = 30
INIT_LR = 1e-3
BS = 32


def preprocessing_and_training(EPOCHS,INIT_LR,BS):

	# initialize the data and labels
	print("[INFO] loading images...")
	data = []
	labels = []

	# grab the image paths and randomly shuffle them

	path="testdata_resized/"
	df=pd.DataFrame.from_csv("dataset.csv")


	# test=test.drop('label',1)

	temp = []
	for img_name in df.filename:
		image_path = path+img_name
		img = imread(image_path, flatten=True)
		img = img.astype('float32')
		temp.append(img)


	train_x = np.stack(temp)

	train_x /= 255.0

	train_x = train_x.reshape(len(df), 128,128,1).astype('float32')
	train_y = to_categorical(df.label.values,num_classes=5)

	print("no_prob")
	train_x=np.array(train_x)
	train_y=np.array(train_y)

	x_train,x_test,y_train,y_test=train_test_split(train_x,train_y,test_size=0.2,random_state=4)
	# time.sleep(10)

	aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
		height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
		horizontal_flip=True, fill_mode="nearest")


	aug.fit(train_x)

	print("[INFO] compiling model...")
	model = LeNet.build(width=128, height=128, depth=1, classes=5)
	opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
	model.compile(loss="binary_crossentropy", optimizer=opt,
		metrics=["accuracy"])

	# train the network
	print("[INFO] training network...")
	H = model.fit_generator(aug.flow(x_train, y_train, batch_size=BS),validation_data=(x_test, y_test),steps_per_epoch=len(x_train) // BS,epochs=EPOCHS, verbose=1)

	# save the model to disk
	print("[INFO] serializing network...")
	# model.save('mymodel.h5')
	plot_graph(H,EPOCHS,INIT_LR,BS)


def plot_graph(H,EPOCHS,INIT_LR,BS):

	plt.style.use("ggplot")
	plt.figure()
	N = EPOCHS
	plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
	plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
	plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
	plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
	plt.title("Training Loss and Accuracy on our system")
	plt.xlabel("Epoch #")
	plt.ylabel("Loss/Accuracy")
	plt.legend(loc="lower left")
	# plt.savefig(args["plot"])
	plt.show()

preprocessing_and_training(EPOCHS,INIT_LR,BS)


# views
def get_all_complaints(request):
    if request.method == 'GET':
        query = Complains.objects.values()
    return render(request, 'index.html', {'data': list(query)})

def register_complain(request):
    if request.method == 'POST':
        data=json.loads(request.body.decode("utf-8"))
        print(data)

    return JsonResponse({"data":"ok"})
































def frzi():
    # format, imgstr = query[0]['image'].split(';base64,')
    # ext = format.split('/')[-1]
    # data = base64.b64decode(imgstr)
    # # print(os.getcwd())
    # os.chdir('project/static/images/')
    # file_name = "image." + ext
    # with open(file_name, 'wb') as f:
    #     f.write(data)
    return True
