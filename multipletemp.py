import cv2
import numpy as np 

'''Template matching with multiple templates'''

templates = []
templates_shapes = []
templates_grey = []

#guarda todos os templates numa lista
for i in range(0, 9):
    templates.append(cv2.imread(f'images/template{i + 1}.png'))
    templates_shapes.append(templates[i].shape[:2])
    templates_grey.append(cv2.cvtColor(templates[i], cv2.COLOR_BGR2GRAY))
    

#adds the whitespace template
'''for c in range(0, 4):
    if c < 3:
        templates.append(cv2.imread(f'whitespace{c + 1}.png'))
    
    templates_shapes.append(templates[8 + c].shape[:2])
    templates_grey.append(cv2.cvtColor(templates[8 + c], cv2.COLOR_BGR2GRAY))'''

templates.append(cv2.imread('images/whitespace1.png'))
templates_shapes.append(templates[9].shape[:2])
templates_grey.append(cv2.cvtColor(templates[9], cv2.COLOR_BGR2GRAY))



image = cv2.imread('images/sudoku.png')
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 0.77
number_templates = len(templates)

for templ in range(number_templates):
    resultado = cv2.matchTemplate(image_grey, templates_grey[templ], cv2.TM_CCOEFF_NORMED)
    loc = np.where(resultado >= threshold) #looks for all coordenates of the matching template on the original image
    largura, altura = templates_shapes[templ] 
    for coordenate in zip(*loc[::-1]): #loops throgh all the correspondent coordenates of a template and puts a rectangle around every match
        cv2.rectangle(image, coordenate, (coordenate[0] + altura,  coordenate[1] + largura), (0, 0, 255), 1)
        

cv2.imwrite('try.png', image)

