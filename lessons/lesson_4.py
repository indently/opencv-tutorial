import cv2 as cv
from assets import assets
import sys
import image_help


def annotate_line():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    A, B = (200, 80), (450, 80)  # From: (X, Y) To: (X, Y)
    cv.line(image_copy, A, B, (0, 255, 255), thickness=10)

    image_help.display_image('Line', image_copy, 2000)


def annotate_circle():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    circle_center = (300, 300)
    cv.circle(image_copy, circle_center, radius=200, color=(0, 255, 255), thickness=6)
    # -1 thickness fills the circle

    image_help.display_image('Circle', image_copy, 2000)


def annotate_square():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    left, top, right, bottom = 200, 200, 450, 450  # left top right bottom

    #  Line Type: https://www.oreilly.com/library/view/mastering-opencv-4/9781789344912/5c4150d2-b550-40be-8b18-f2e71e20d9be.xhtml
    cv.rectangle(image_copy, (left, top), (right, bottom), (0, 255, 0), thickness=6, lineType=cv.LINE_8)
    # -1 thickness fills the square

    image_help.display_image('Square', image_copy, 2000)


def annotate_text():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    text = 'This is cat'
    position = (450, 300)  # X, Y starts at bottom
    cv.putText(image_copy, text, position, fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=1.7, color=(0, 255, 0), thickness=2)

    image_help.display_image('Text', image_copy, 2000)


# T
def annotate_text_square():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()

    # Square
    left, top, right, bottom = 200, 200, 450, 450  # left top right bottom
    cv.rectangle(image_copy, (left, top), (right, bottom), (0, 255, 0), thickness=6,
                 lineType=cv.LINE_8)

    # Text
    text = 'This is cat'
    position = (left, bottom + 50)
    cv.putText(image_copy, text, position, fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=1.4, color=(0, 255, 0), thickness=2)

    image_help.display_image('Text Square', image_copy, 2000)


if __name__ == '__main__':
    annotate_line()
    annotate_text()
    annotate_circle()
    annotate_square()
    annotate_text_square()
    sys.exit("Finished!")
