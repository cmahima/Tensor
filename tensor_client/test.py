from tensor import Tensor
import os, os.path
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import json
from time import sleep
from email.MIMEBase import MIMEBase
from email import encoders
import time
import glob

#start=time.time()
if __name__ == '__main__':
    url = ''
    t = Tensor(url)
    imgs=[]
    i=0
    #folder="home/turtle/Desktop"
while (1):
     
      imgs.append(os.path.join("/home/turtle/images/image" + str(i)+ ".jpg"))
       
#      sleep(1)

          
      image="/home/turtle/images"+'/'+imgs[i]
      #end=time.time()
      
      res = t.classify(imgs[i])
      #print(end-start)
      
      resp=json.dumps(res)
     #rep=repr(res)
     #print (rep)
      #f resp.endswith('}'):
      #os.remove(image)
     # print('hi')
      fromaddr = ""
      toaddr = ""
      msg = MIMEMultipart()
      msg['From'] = "tensor"
      msg['To'] = "flow" 
      msg['Subject'] = "TENSORFLOW CLASSIFICATION RESULT"
      body="\n"+ res
      msg.attach(MIMEText(body, 'plain'))
      filename=imgs[i]
     # i+1
      attachment=open(imgs[i],"rb")
      part = MIMEBase('application', 'octet-stream')
      part.set_payload((attachment).read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      msg.attach(part)
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(fromaddr, "")
      text = msg.as_string()
      server.sendmail(fromaddr, toaddr, text)
      server.quit()
      print(res)
      os.remove(imgs[i])
      i+=1
      
