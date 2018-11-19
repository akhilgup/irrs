#!/usr/bin/env python 

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import mysql.connector
from datetime import datetime
import pandas as pd
import numpy as np
import argparse
import imutils
import cv2
import sys
import os


db = mysql.connector.connect(user='root', password='akhilgupta',
                              host='127.0.0.1',
                              database='hack')


mycursor=db.cursor(buffered=True)


def testing_image(x):

	# load the image
	get_id="SELECT image_name,image_path,time_stamp FROM image_input WHERE id=(%s)"%str(x)
	mycursor.execute(get_id)
	tup=mycursor.fetchone()

	image = cv2.imread(tup[1],0)
	# orig = image.copy()
	orig = cv2.imread(tup[1],1)
	 
	# pre-process the image for classification
	image = cv2.resize(image, (128, 128))
	image = image.astype("float32") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	print("[INFO] loading network...")

	model=load_model('mymodel.h5')

	predictions=model.predict(image)
	# print(predictions[0])
	label = ['Vehicle','Potholes','Freeways','Traffic','Pedestrian Lanes']
	# return predictions[0]
	
	label_vehicle = "{}: {:.2f}%".format(label[0], predictions[0][0] * 100)
	label_potholes = "{}: {:.2f}%".format(label[1], predictions[0][1] * 100)
	label_freeways = "{}: {:.2f}%".format(label[2], predictions[0][2] * 100)
	label_traffic = "{}: {:.2f}%".format(label[3], predictions[0][3] * 100)
	label_pedestrain_lanes = "{}: {:.2f}%".format(label[4], predictions[0][4] * 100)
	timestamp=datetime.now().strftime('%d-%m-%Y %H:%M:%S')

	veh=label_vehicle[-6:]
	pot=label_potholes[-6:]
	free=label_freeways[-6:]
	traf=label_traffic[-6:]
	ped=label_pedestrain_lanes[-6:]


	# file=open("result.txt","w+")
	# file.write(label_vehicle+'\n')
	# file.write(label_potholes+'\n')
	# file.write(label_freeways+'\n')
	# file.write(label_traffic+'\n')
	# file.write(label_pedestrain_lanes+'\n')
	# # # draw the label on the image

	output = imutils.resize(orig, width=400)
	cv2.putText(output, label_vehicle, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_potholes, (10, 50),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_freeways, (10, 75),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_traffic, (10, 100),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, label_pedestrain_lanes, (10, 125),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 255, 0), 2)

	cv2.putText(output, timestamp, (150, 200),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (0, 0, 255), 2)

	out_img_name=tup[0][:-4]+'_res.jpg'
	out_path=os.path.realpath(out_img_name)
	# show the output image
	cv2.imwrite(out_img_name, output)
	try:
		sql="INSERT INTO output_info (input_id,image_name,image_path,vehicle,potholes,freeways,traffic,pedestrian_lanes,time_stamp) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s)"
		data=(int(x),out_img_name,out_path,veh,pot,free,traf,ped,timestamp)
		# print(output_file%data)
		# print("try")
		
		mycursor.execute(sql,data)
	except:
		# print("pass")
		pass
	
	
	# cv2.waitKey(0)

	# cv2.destroyAllWindows()
	# cv2.waitKey(1)

x=sys.argv[1]

testing_image(x)
db.commit()