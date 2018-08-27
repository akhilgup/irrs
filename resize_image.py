from PIL import Image
import pandas as pd
import os
import cv2
from sklearn.utils import shuffle
import time



def resize_and_gray(path):

	

	files=os.listdir(path)
	c=603 #865
	df=pd.DataFrame.from_csv("pedestrian.csv")

	for i in files:

			# print(i)
		if i != '.DS_Store':
			img = cv2.imread(path+i,0) # image extension *.png,*.jpg
			print(i)

			image = cv2.resize(img,(128, 128))
			print(i)
			name="+"+str(c)+i
			c+=1
			# cv2.imwrite('testdata_resized/+'+str(c)+i,image)
		# image=img.resize(128, 128)
			df=df.append({'filename':name, 'label':4},ignore_index=True)
	print(df.tail())
	print(len(df))
	print(c)
	return df

# df.to_csv("traffic.csv")


def resize_and_gray_traffic(path):

	

	files=os.listdir(path)
	c=0 #865
	df=pd.DataFrame.from_csv("traffic.csv")

	for i in files:
		# print(i[0])
			# print(i)
		if i != '.DS_Store' and i[0]=='+':
			img = cv2.imread(path+i,0) # image extension *.png,*.jpg
			print(i[0])

			image = cv2.resize(img,(128, 128))
			print(i[0])
			name="+"+str(c)+i
			c+=1
			# cv2.imwrite('testdata_resized/_'+str(c)+i,image)
		# image=img.resize(128, 128)
			df=df.append({'filename':i, 'label':4},ignore_index=True)
	print(df.tail())
	print(len(df))
	print(c)
	return df

path='testdata_resized/'

value=resize_and_gray_traffic(path)

df=shuffle(value)
df.to_csv('pedestrian.csv')

