import os
import mysql.connector
from datetime import datetime
import pandas as pd


db = mysql.connector.connect(user='root', password='apporva',
                              host='localhost',
                              database='innotech')


mycursor=db.cursor(buffered=True)

y=os.listdir('images/')
print(type(y))


for i in y:
	
	y= os.path.realpath(i)

	
		
	time_stamp=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
	try:
		sql="INSERT INTO image_input (image_name, image_path, time_stamp) VALUES(%s,%s,%s)"
		data=(i,y,time_stamp)
		# print(sql%data)

		mycursor.execute(sql,data)

	except:
		print("Duplicate record identified")
		pass


db.commit()

