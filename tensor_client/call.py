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
from light import LED
#start=time.time()
if __name__ == '__main__':
    url = ''
    t = Tensor(url)
    imgs=[]
    i=0

    
while (1):
      time.sleep(5)
   
      imgs.append(os.path.join("/home/mahima/images/frame_" + str(i)+ ".jpg"))
       
#      sleep(1)

          
      image="/home/mahima/images"+'/'+imgs[i]
      #end=time.time()
      
      res = t.classify(imgs[i])
      #print(end-start)
    #  time.sleep(5)
      resp=json.dumps(res)
      respp=resp
      l= len(res)
     # print(res)
      maxnum=0
      j=0
      k=0
    
      n=resp.count(':')
      #print(n)
    #  while(1):
      for z in range(10):
        #print("hi")
        index1=res.find(':',j,l-1)
        
        #print(index1)
        index2=res.find(',',k,l)
        #print(index2)
        s1=res[index1:index2]
        #print(s1)
        j=index1+1
        k=index2+1
        if 'e' in s1:
         continue
        s=res[index1+1:index2-12]
       # print(s)   
        #num=float(s)
       
        if(s>=maxnum):
         maxnum=s 
         ind=index1
        #j=index1+len(s1)
        #k=index2+len(s1) 
         
      
      substr=res[0:ind-1]
      li=substr.rfind('"')
      l=len(substr)
      name=substr[li+1:l]  
      str3=name
      ans="Person is "+name 
      print(ans)
      if ' ' in name:
        index3=name.find(' ',0,l-1)
        str1=name[0:index3]
        str2=name[index3+1:l-1]
        str3=str1+str2 
      os.system("espeak 'person'")
      os.system("espeak 'is'")
      os.system("espeak "+ str3)
     
      fromaddr = ""
      toaddr = ""
      msg = MIMEMultipart()
      msg['From'] = "tensor"
      msg['To'] = "flow" 
      msg['Subject'] = "TENSORFLOW CLASSIFICATION RESULT"
      body="\n"+ res+"\n"+ans
      msg.attach(MIMEText(body, 'plain'))
     #Following lines of code send image as an attachment 
      #filename=imgs[i]
      #attachment=open(imgs[i],"rb")
      #part = MIMEBase('application', 'octet-stream')
      #part.set_payload((attachment).read())
      #encoders.encode_base64(part)
      #part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      #msg.attach(part)
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(fromaddr, "")
      text = msg.as_string()
      server.sendmail(fromaddr, toaddr, text)
      server.quit()
      print(res+ imgs[i])
      os.remove(imgs[i])
      i+=1
      l=LED()
      LED.lit(l,maxnum)
      
