import cv2
import numpy as np

from cscore import CameraServer


def main():
    body = cv2.CascadeClassifier("body.xml")
    face = cv2.CascadeClassifier("front_face.xml")
    upper_body = cv2.CascadeClassifier("upper_body.xml")
    cs = CameraServer.getInstance()
    cs.enableLogging()
    camera = cs.startAutomaticCapture()
    camera.setResolution(320, 240)
    cvSink = cs.getVideo()
    outputStream = cs.putVideo("Rectangle", 320, 240)

    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)

    while True:
        time, img = cvSink.grabFrame(img)
        if time == 0:
            outputStream.notifyError(cvSink.getError())
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bodies = body.detectMultiScale(gray, 1.3, 4)
        cv2.rectangle(img, (100, 100), (300, 300), (255, 255, 255), 5)
        outputStream.putFrame(img)
