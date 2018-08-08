
import requests
import time
import os
#import threading
#from wait import ThreadJob

class Tensor:
  def __init__(self,url):
        self.url = url


  def classify(self, img_path):
        if not self.__validate_img(img_path):
            return;
        try:
            file = open(img_path, 'rb')
            data = file.read()
            #time.sleep(5)
            #e=time.time()
            #print(e-s)
            #k = ThreadJob(classify,event,2)
            #k.start()
            start=time.time()
            response = requests.post(self.url + '/classify', data=data)
            stop=time.time()
            #sleep(5)
    
            file.close()
        except:
            return 'Unable to connect to Bitnobi server with url: ' + self.url
        if not response.ok and response.status_code == 400:
            return response.text
        elif not response.ok and response.status_code == 404:
            return 'path: ' + response.reason
        print(stop-start)
        t=stop-start
        #os.remove(img_path)
        ti=str(t)
        return  'result:'+ ti + response.text + img_path

  def __validate_img(self,img_path):
        jpeg = '.jpg'
        if not img_path.endswith(jpeg):
            print('Invalid image type: Please use jpeg format')
            return False
        return True
