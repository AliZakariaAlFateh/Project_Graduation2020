# import face_recognition
import cv2,os
import dlib
# import face_recognition
import numpy
import mysql.connector
# con=mysql.connector.connect(user='root',password='root',host='localhost',database='test')
# con=mysql.connector.connect(user='root',host='localhost',database='test')
con=mysql.connector.connect(user='root',host='localhost')
if(con):
    print("the connection is done")
_databases=con.cursor()
_databases.execute('show databases')
print(_databases.fetchall())
# face_rec=cv2.face.LBPHFaceRecognizer_create()