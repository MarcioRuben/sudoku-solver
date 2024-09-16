import cv2 as cv
import numpy as np

#BGR
#create a black image
'''para criar imagem com o numpy, cria-se um tuplo com três elementos'''
image = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(image,(0,0),(511,511),(255,0,0),5)
cv.imshow('imagem', image)
cv.waitKey(0)

