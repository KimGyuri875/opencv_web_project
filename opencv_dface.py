from django.conf import settings
import numpy as np
import cv2
import pyautogui
def opencv_dface(path):
    target = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    h, w = target.shape
    _img = np.array(pyautogui.screenshot())
    if(type(target) is np.ndarray):
        print(target.shape)

        _img = np.array(pyautogui.screenshot())
        img = cv2.cvtColor(_img, cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
        minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)
        leftTop = maxLoc

        # maxValue == 0.8
        # print(maxValue)
        filtered = _img
        rightBottom = maxLoc[0] + h, maxLoc[1] + w
        if maxValue >= 0.7:
            cv2.rectangle(_img, leftTop, rightBottom, (255, 255, 0), 3)
            print(leftTop, rightBottom)
            cropping = _img[leftTop[1]:rightBottom[1], leftTop[0]:rightBottom[0]]
            filtered = 0
            filtered = cropping
        cv2.imwrite(path, filtered)
    else:
        print('something error')
        print(path)