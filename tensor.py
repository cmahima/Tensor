import requests
import time

class Tensor:
    def __init__(self,url):
        self.url = url

        # upload image to server

    def classify(self, img_path):
        if not self.__validate_img(img_path):
            return;
        try:
            file = open(img_path, 'rb')
            data = file.read()
            #sleep.time(5)
            start=time.time()
            response = requests.post(self.url + '/classify', data=data)
            end=time.time()
            file.close()
        except:
            return 'Unable to connect to Bitnobi server with url: ' + self.url
        if not response.ok and response.status_code == 400:
            return response.text
        elif not response.ok and response.status_code == 404:
            return 'path: ' + response.reason
        print(end-start)
        return response.text

    def __validate_img(self,img_path):
        jpeg = '.jpg'
        if not img_path.endswith(jpeg):
            print('Invalid image type: Please use jpeg format')
            return False
        return True
