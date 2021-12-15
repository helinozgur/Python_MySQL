import mysql.connector
import cv2
from datetime import datetime
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="yeni_veritabani"
)

mycursor = mydb.cursor()
###Oluşturulan tablolar
# Resim Tablosu Bir Kez Tablo Oluşturmak İçin Yorum Satırından Çıkartılıp Çalıştırılmalıdır.
# mycursor.execute("CREATE TABLE image_bilgi (id INT AUTO_INCREMENT PRIMARY KEY,"
#                  " tarih datetime NOT NULL,"
#                  " resim LONGBLOB)")
#

image=cv2.imread("cicek.jpg")
date_time = datetime.now()
img=cv2.imencode('.jpg',image)[1].tobytes()
mycursor.execute("INSERT INTO image_bilgi (tarih,resim) VALUES(%s,%s)",(date_time,img))
mydb.commit()

