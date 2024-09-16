import cv2
import numpy as np

templates = []
templates_shapes = []
templates_grey = []

#guarda todos os templates numa lista
for i in range(0, 9):
    templates.append(cv2.imread(f'template{i + 1}.png'))
    templates_shapes.append(templates[i].shape[:2])
    templates_grey.append(cv2.cvtColor(templates[i], cv2.COLOR_BGR2GRAY))
    

#adds the whitespace template
templates.append(cv2.imread('whitespace1.png'))
templates_shapes.append(templates[9].shape[:2])
templates_grey.append(cv2.cvtColor(templates[9], cv2.COLOR_BGR2GRAY))

#get the video stream input
video = cv2.VideoCapture('http://192.168.1.246:8080/video')

if not video.isOpened():
    print('Video is not working')
else:

    width = int(video.get(3))
    height = int(video.get(4))

    while (video.isOpened()):
        ret, frame = video.read()
        if ret:
            imagem = frame.copy()
            imagem_grey = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            threshold  = 0.75
            number_templates = len(templates)

            for comparisons in range(number_templates):
                resultado = cv2.matchTemplate(imagem_grey, templates_grey[comparisons], cv2.TM_CCOEFF_NORMED)
                location = np.where(resultado >= threshold)
                altura, largura = templates_shapes[comparisons] #gives us the height and width of the given template to do
                for i in zip(*location[::-1]):
                    cv2.rectangle(imagem, i, (i[0] + altura, i[1] + largura), (0, 0, 255), 2)
                    cv2.imshow('result', frame)
                    


        else:
            break
video.release()
cv2.destroyAllWindows()



