from tensor import Tensor
from PIL import Image
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 
import smtplib
import random

if __name__ == '__main__':
    url = ''
    t = Tensor(url)
    folder="/home/mahima/images"
    #while(true):
    for filename in os.listdir("/home/mahima/images"):
        numberoffiles=len(folder)
        img = random.choice(os.listdir("/home/mahima/images"))
        image=folder+'/'+img
        print(numberoffiles)
        res = t.classify(image)
        os.remove(image)
        #sending response as an email
        fromaddr = ""
        toaddr = ""
        msg = MIMEMultipart()
        msg['From'] = "Tensorflow"
        msg['To'] = "Mahima"
        msg['Subject'] = "CLASSIFICATION RESULT"
        body = '/n'+ res
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print(res)

       

