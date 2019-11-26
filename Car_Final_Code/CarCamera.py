from picamera import PiCamera
import time
import os

class CarCamera():

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = ('720p')
        self.camera.framerate = 24

    def GetPicturePath(self):
        directory = "/home/pi/Desktop/Car Images"
        path = directory + "/image.jpg"
        #Make the directory if it does not exist.
        if not(os.path.isdir(directory)):
            os.mkdir(directory)
        i = 0
        while(os.path.isfile(path)):
            path = directory + "/" + str(i) + "image.jpg"
            i += 1
        return path

    def TakePicture(self):
        print("Attempting to take picture.")
        picPath = self.GetPicturePath()
        print("Picture Path: " + picPath)
        self.camera.capture(picPath)
        return float(time.time())

    def start(self):
        os.chdir("/home/pi/Desktop/Car/videos")
        start_time = (time.time())
        self.camera.start_recording("{0:f}".format(start_time), format = 'h264')
        return float(time.time())


    def stop(self):
        if(self.camera.recording):
            self.camera.stop_recording()
            return float(time.time())
