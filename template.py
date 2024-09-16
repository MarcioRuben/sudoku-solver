#template matching
import cv2
import numpy as np 

'''Template matching with one template'''

imagem = cv2.imread('sudoku.png')
template = cv2.imread('template2.png')

width, height = template.shape[:2]

imagem_grey = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
template_grey = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(imagem_grey, template_grey, cv2.TM_CCOEFF_NORMED)
threshold = 0.9

loc = np.where(result >= threshold)

for i in zip(*loc[::-1]):
    cv2.rectangle(imagem, i, (i[0] + width, i[1] + height), (0, 0, 255), 1)

cv2.imwrite('resultado.png', imagem)
