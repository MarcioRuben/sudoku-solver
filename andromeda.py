import cv2
import numpy as np
from matplotlib import pyplot

'''métodos de template matching'''
methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
            'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']

image = cv2.imread('sudo.png', 0)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()