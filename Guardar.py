import cv2


def guardar(Datos, frame, colorMarco, count):
    dibujo = cv2.rectangle(frame, (0, 600), (0, 400), colorMarco, 3)
    cv2.imwrite(Datos + '/Dibujo_{}.jpg'.format(count), dibujo)
    print('guardar')
    cv2.imshow('Dibujo', dibujo)
    count = count + 1
