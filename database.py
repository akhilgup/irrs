import os
import mysql.connector
from datetime import datetime
import pandas as pd


db = mysql.connector.connect(user='root', password='akhilgupta',
                              host='localhost',
                              database='hack')


mycursor=db.cursor(buffered=True)

y=os.listdir('images/')
print(y)


for i in y:

	if i == '.DS_Store':
		continue
	
	y=  os.path.realpath(i)
	y = '/'.join(y.split('/')[:-1] + ['images'] + y.split('/')[-1:])
	print(y)

	
		
	time_stamp=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
	try:
		sql="INSERT INTO image_input (image_name, image_path, time_stamp) VALUES(%s,%s,%s)"
		data=(i,y,time_stamp)
		print(sql%data)

		mycursor.execute(sql,data)

	except:
		print("Duplicate record identified")
		pass


db.commit()

