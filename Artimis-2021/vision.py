from cscore import CameraServer

# Import OpenCV and NumPy
import cv2
import numpy as np

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()
    camera = cs.startAutomaticCapture()
    camera.setResolution(320, 240)
    cvSink = cs.getVideo()
    outputStream = cs.putVideo("Name", 320, 240)
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)

    while True:
        time, img = cvSink.grabFrame(img)
        if time == 0:
            outputStream.notifyError(cvSink.getError())
            continue
        outputStream.putFrame(img)
