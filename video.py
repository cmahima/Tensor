
from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.resolution=(200,200)
#camera.start_preview()
for i in range(10):
    sleep(0.1)
    camera.capture('/home/turtle/images/image%s.jpg' % i, resize=(640,480))
#camera.stop_preview()
