from time import time
import cv2

from exceptions import FailOpenCamera
from config import Config as cf


class Camera:
    def __init__(self, camera_number=0):
        self.eye = cv2.VideoCapture(camera_number)
        if not self.eye.isOpened():
            raise FailOpenCamera('Проверте номер камеры')
        self.codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        self.width = int(self.eye.get(3))
        self.height = int(self.eye.get(4))

    def write_video(self, path, video_length=30):
        finish_time = start_time = time()
        out_file = cv2.VideoWriter(path,
                                   self.codec,
                                   cf.fps,
                                   (self.width,
                                    self.height))
        status = True
        while finish_time - start_time <= video_length:
            status, frame = self.eye.read()
            out_file.write(frame)
            finish_time = time()

        out_file.release()
        return status
