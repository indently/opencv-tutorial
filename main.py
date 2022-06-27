import cv2 as cv
from assets import assets
import sys


def annotate_line():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    A, B = (200, 80), (450, 80)  # From: (X, Y) To: (X, Y)
    cv.line(image_copy, A, B, (0, 255, 255), thickness=3)

    cv.imshow('Line', image_copy)

    cv.waitKey()
    cv.destroyAllWindows()
    sys.exit("Finished!")


if __name__ == '__main__':
    annotate_line()