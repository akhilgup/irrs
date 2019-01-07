import mysql.connector

db = mysql.connector.connect(user='akhilgupta', password='8171834923',
                              host='devta.c6obkwbtq8na.us-east-2.rds.amazonaws.com',
                              database='irrs')


mycursor=db.cursor(buffered=True)

# sql = "DROP TABLE image_input"

#sql = "CREATE TABLE image_input(id INT AUTO_INCREMENT PRIMARY KEY, image_name VARCHAR(255) UNIQUE KEY, image_path TEXT, time_stamp VARCHAR(255))"
sql = "CREATE TABLE output_info(id INT AUTO_INCREMENT PRIMARY KEY, input_id INTEGER, image_name VARCHAR(255) UNIQUE KEY, image_path TEXT, vehicle VARCHAR(255), potholes VARCHAR(255), freeways VARCHAR(255), traffic VARCHAR(255), pedestrian_lanes VARCHAR(255), time_stamp timestamp, FOREIGN KEY(input_id) REFERENCES image_input(id))"

mycursor.execute(sql)
db.commit()