import cv2 as cv
from assets import assets
import sys


def display_image(window_name: str, image: str, time: int):
    cv.imshow(window_name, image)
    cv.moveWindow(window_name, 100, 100)
    cv.setWindowProperty(window_name, cv.WND_PROP_TOPMOST, 1)
    cv.waitKey(time)
    cv.destroyAllWindows()
