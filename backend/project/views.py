from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Worker, User, Complains
import os, base64, json,io
from PIL import Image

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
def testing_image(st):

    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # print(dir_path)

    if st == '1':
        image = cv2.imread("im1.jpeg",0)
        orig = cv2.imread("im1.jpeg",1)
    elif st == '0':
        image = cv2.imread("image.jpeg",0)
        orig = cv2.imread("image.jpeg",1)

    # load the image
    # image = cv2.imread("test5.jpeg",0)
    # orig = image.copy()
    # orig = cv2.imread("test5.jpeg",1)

    # pre-process the image for classification
    image = cv2.resize(image, (128, 128))
    image = image.astype("float32") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    try:
        model=load_model('mymodel.h5')
    except:
        model=load_model('mymodel.h5')



    print("\n\n\n\n\n\n\n[INFO] loading network...\n\n\n\n\n")


    predictions=model.predict(image)
    # print(predictions[0])

    label = ['Vehicle','Potholes','Freeways','Traffic','Pedestrian Lanes']

    ak = []

    label_vehicle = "{}: {:.2f}%".format(label[0], predictions[0][0] * 100)
    label_potholes = "{}: {:.2f}%".format(label[1], predictions[0][1] * 100)
    label_freeways = "{}: {:.2f}%".format(label[2], predictions[0][2] * 100)
    label_traffic = "{}: {:.2f}%".format(label[3], predictions[0][3] * 100)
    label_pedestrain_lanes = "{}: {:.2f}%".format(label[4], predictions[0][4] * 100)

    ak = [label_vehicle, label_potholes, label_freeways, label_traffic, label_pedestrain_lanes]

    return ak

    # # draw the label on the image
    # output = imutils.resize(orig, width=400)
    # cv2.putText(output, label_vehicle, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
    #     0.6, (0, 255, 0), 2)

    # cv2.putText(output, label_potholes, (10, 50),  cv2.FONT_HERSHEY_SIMPLEX,
    #     0.6, (0, 255, 0), 2)

    # cv2.putText(output, label_freeways, (10, 100),  cv2.FONT_HERSHEY_SIMPLEX,
    #     0.6, (0, 255, 0), 2)

    # cv2.putText(output, label_traffic, (10, 125),  cv2.FONT_HERSHEY_SIMPLEX,
    #     0.6, (0, 255, 0), 2)

    # cv2.putText(output, label_pedestrain_lanes, (10, 150),  cv2.FONT_HERSHEY_SIMPLEX,
    #     0.6, (0, 255, 0), 2)

    # # show the output image
    # cv2.imshow("Output", output)
    # cv2.waitKey(0)

    # cv2.destroyAllWindows()
    # cv2.waitKey(1)


# views
def get_all_complaints(request):
    if request.method == 'GET':
        query = Complains.objects.values()

        base64_string = query[0]['image']

        base64_string = base64_string[18:].replace('\n','')

        base64_string = base64_string.encode()

        with open("im1.jpeg", "wb") as fh:
            fh.write(base64.decodebytes(base64_string))

        res = testing_image("0")
        print(res)

    return render(request, 'index.html', {'data': list(query), 'res': res})

def getSatAnal(request):
    return render(request, 'sat.html',{})

def register_complain(request):
    if request.method == 'POST':
        data=json.loads(request.body.decode("utf-8"))
        print(data)
        query = Complains.objects.create(title = data['title'], text = data['text'], image = 'data:/jpeg;base64,'+data['image'], location = data['location'], compl_by = data['email'], status = "Registered", results = data['results'])

    return JsonResponse({"data":"Your Complain has been registered and will be processed soon."})

def get_results(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        print(data)

        base64_string = data['image']

        base64_string = base64_string.encode()

        with open("im5.jpg", "wb") as fh:
            fh.write(base64.decodebytes(base64_string))

        dt = testing_image("1")

    return JsonResponse(testing_image("1"), safe=False)
