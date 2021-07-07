import cv2
import numpy as np
import os
import Guardar

def Pizarra(colorBajo, colorAlto):
    count = 0
    i = 0
    cap = cv2.VideoCapture(1)
    # colores para cambiar de lapiz

    # Colores para pintar
    colorRosa = (128, 0, 255)
    colorMorado = (135, 35, 100)
    colorAzul = (214, 41, 43)
    colorCeleste = (255, 113, 82)
    colorVerde = (0, 255, 36)
    colorAmarillo = (89, 222, 255)
    colorAnaranjado = (20, 112, 246)
    colorRojo = (0, 0, 255)
    colorCafe = (0, 44, 144)
    colorGris = (115, 115, 115)
    colorNegro = (0, 0, 0)
    colorBlanco = (249, 249, 249)
    colorGuardar = (130, 140, 50)
    colorLimpiarPantalla = (20, 112, 246)  # Solo se usará para el cuadro superior de 'Limpiar Pantalla'
    colorMarco = (0, 0, 0)  # enmarca los recuadros de los rectagulos
    # Grosor de línea recuadros superior izquierda (color a dibujar)
    grosorRosa = 7
    grosorMorado = 3
    grosorAzul = 3
    grosorCeleste = 3
    grosorVerde = 3
    grosorAmarillo = 3
    grosorAnaranjado = 3
    grosorRojo = 3
    grosorCafe = 3
    grosorGris = 3
    grosorNegro = 3
    grosorBlanco = 3
    # Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
    grosorPeque = 7
    grosorMedio = 3
    grosorGrande = 3
    # --------------------- Variables para el marcador / lápiz virtual -------------------------
    color = colorRosa  # Color de entrada, y variable que asignará el color del marcador
    grosor = 3  # Grosor que tendrá el marcador
    # ------------------------------------------------------------------------------------------
    x1 = None
    y1 = None
    imAux = None

    while True:

        k = cv2.waitKey(1)

        ret, frame = cap.read()
        if ret == False: break

        frame = cv2.flip(frame, 1)
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if imAux is None: imAux = np.zeros(frame.shape, dtype=np.uint8)

        # -----------------------Seccion superior --------------------------------
        # Cuadros en la parte superior izquierda ( reprentan el color a dibujar

        cv2.rectangle(frame, (50, 90), (0, 120), colorRosa, -1)  # relleno de rectangulo
        cv2.rectangle(frame, (50, 90), (0, 120), colorMarco, grosorRosa)  # recuadro del rectangulo
        cv2.rectangle(frame, (50, 120), (0, 150), colorMorado, -1)
        cv2.rectangle(frame, (50, 120), (0, 150), colorMarco, grosorMorado)
        cv2.rectangle(frame, (50, 150), (0, 180), colorAzul, -1)
        cv2.rectangle(frame, (50, 150), (0, 180), colorMarco, grosorAzul)
        cv2.rectangle(frame, (50, 180), (0, 210), colorCeleste, -1)
        cv2.rectangle(frame, (50, 180), (0, 210), colorMarco, grosorCeleste)
        cv2.rectangle(frame, (50, 210), (0, 240), colorVerde, -1)
        cv2.rectangle(frame, (50, 210), (0, 240), colorMarco, grosorVerde)
        cv2.rectangle(frame, (50, 240), (0, 270), colorAmarillo, -1)
        cv2.rectangle(frame, (50, 240), (0, 270), colorMarco, grosorAmarillo)
        cv2.rectangle(frame, (50, 270), (0, 300), colorAnaranjado, -1)
        cv2.rectangle(frame, (50, 270), (0, 300), colorMarco, grosorAnaranjado)
        cv2.rectangle(frame, (50, 300), (0, 330), colorRojo, -1)
        cv2.rectangle(frame, (50, 300), (0, 330), colorMarco, grosorRojo)
        cv2.rectangle(frame, (50, 330), (0, 360), colorCafe, -1)
        cv2.rectangle(frame, (50, 330), (0, 360), colorMarco, grosorCafe)
        cv2.rectangle(frame, (50, 360), (0, 390), colorGris, -1)
        cv2.rectangle(frame, (50, 360), (0, 390), colorMarco, grosorGris)
        cv2.rectangle(frame, (50, 390), (0, 420), colorNegro, -1)
        cv2.rectangle(frame, (50, 390), (0, 420), colorMarco, grosorNegro)
        cv2.rectangle(frame, (50, 420), (0, 450), colorBlanco, -1)
        cv2.rectangle(frame, (50, 420), (0, 450), colorMarco, grosorBlanco)
        # TITULO
        cv2.rectangle(frame, (190, 0), (480, 50), colorMarco, 6)
        cv2.rectangle(frame, (190, 0), (480, 50), colorRosa, -1)
        cv2.putText(frame, 'VIRTUAL PAINT', (210, 40), 3, 1, colorMarco, 4, cv2.LINE_AA)

        # limpiar pantalla
        cv2.rectangle(frame, (70, 0), (180, 50), colorMarco, 6)
        cv2.rectangle(frame, (70, 0), (180, 50), colorLimpiarPantalla, -1)
        cv2.putText(frame, 'Limpiar', (80, 20), 6, 0.8, colorMarco, 1, cv2.LINE_AA)
        cv2.putText(frame, 'pantalla', (80, 40), 6, 0.8, colorMarco, 1, cv2.LINE_AA)

        # Cuadrado dibujos en la parte superior derecha ( grosor del marcador para dibujar)
        cv2.rectangle(frame, (490, 0), (540, 50), (170, 180, 50), -1)
        cv2.rectangle(frame, (490, 0), (540, 50), (0, 0, 0), grosorPeque)
        cv2.circle(frame, (515, 25), 3, (0, 0, 0), -1)
        cv2.rectangle(frame, (540, 0), (590, 50), (170, 180, 50), -1)
        cv2.rectangle(frame, (540, 0), (590, 50), (0, 0, 0), grosorMedio)
        cv2.circle(frame, (565, 25), 7, (0, 0, 0), -1)
        cv2.rectangle(frame, (590, 0), (640, 50), (170, 180, 50), -1)
        cv2.rectangle(frame, (590, 0), (640, 50), (0, 0, 0), grosorGrande)
        cv2.circle(frame, (615, 25), 11, (0, 0, 0), -1)

        # variables Auxiliares para los colores
        # procedimiento
        maskCeleste = cv2.inRange(frameHSV, colorBajo, colorAlto)
        maskCeleste = cv2.erode(maskCeleste, None, iterations=1)
        maskCeleste = cv2.dilate(maskCeleste, None, iterations=2)
        maskCeleste = cv2.medianBlur(maskCeleste, 13)

        cnts, _ = cv2.findContours(maskCeleste, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

        for c in cnts:
            area = cv2.contourArea(c)
            if area > 1000:
                x, y2, w, h = cv2.boundingRect(c)
                x2 = x + w // 2

                if y1 is not None:
                    # para que los colores resalten cuando sean seleccionados
                    if 0 < x2 < 50 and 90 < y2 < 120:
                        color = colorRosa
                        grosorRosa = 6
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 120 < y2 < 150:
                        color = colorMorado
                        grosorRosa = 3
                        grosorMorado = 7
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 150 < y2 < 180:
                        color = colorAzul
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 7
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 180 < y2 < 210:
                        color = colorCeleste
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 7
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3

                    if 0 < x2 < 50 and 210 < y2 < 240:
                        color = colorVerde
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 7
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 240 < y2 < 270:
                        color = colorAmarillo
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 7
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 270 < y2 < 300:
                        color = colorAnaranjado
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 7
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 300 < y2 < 330:
                        color = colorRojo
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 7
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 330 < y2 < 360:
                        color = colorCafe
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 7
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 360 < y2 < 390:
                        color = colorGris
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 7
                        grosorNegro = 3
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 390 < y2 < 420:
                        color = colorNegro
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 7
                        grosorBlanco = 3
                    if 0 < x2 < 50 and 420 < y2 < 450:
                        color = colorBlanco
                        grosorRosa = 3
                        grosorMorado = 3
                        grosorAzul = 3
                        grosorCeleste = 3
                        grosorVerde = 3
                        grosorAmarillo = 3
                        grosorAnaranjado = 3
                        grosorRojo = 3
                        grosorCafe = 3
                        grosorGris = 3
                        grosorNegro = 3
                        grosorBlanco = 17

                    # para que resalte el tipo de grosor de linea
                    if 490 < x2 < 540 and 0 < y2 < 50:
                        grosor = 3
                        grosorPeque = 7
                        grosorMedio = 3
                        grosorGrande = 3
                    if 540 < x2 < 590 and 0 < y2 < 50:
                        grosor = 7
                        grosorPeque = 3
                        grosorMedio = 7
                        grosorGrande = 3
                    if 590 < x2 < 640 and 0 < y2 < 50:
                        grosor = 11
                        grosorPeque = 3
                        grosorMedio = 3
                        grosorGrande = 7
                    # limpiar pantalla
                    if 70 < x2 < 180 and 0 < y2 < 50:
                        cv2.rectangle(frame, (70, 0), (180, 50), colorMarco, 6)
                        cv2.rectangle(frame, (70, 0), (180, 50), colorLimpiarPantalla, -1)
                        cv2.putText(frame, 'Limpiar', (80, 20), 6, 0.8, colorMarco, 1, cv2.LINE_AA)
                        cv2.putText(frame, 'pantalla', (80, 40), 6, 0.8, colorMarco, 1, cv2.LINE_AA)
                        imAux = np.zeros(frame.shape, dtype=np.uint8)

                    # condicion para que no pinte la parte superior del menu
                    if -10 < x2 < 60 or -10 < x1 < 60 or -10 < y2 < 60 or -10 < y1 < 60:
                        imAux = imAux
                    # Dibujos y trazos
                    else:
                        # actualizando el color seleccionado
                        imAux = cv2.line(imAux, (x1, y1), (x2, y2), color, grosor)
                cv2.circle(frame, (x2, y2), grosor, color, 3)
                x1 = x2
                y1 = y2

            else:
                x1 = None
                y1 = None

        # cambiando los trazon a escala de grises para mostrar los colores en  la otra pantalla
        imAuxGray = cv2.cvtColor(imAux, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(imAuxGray, 10, 255, cv2.THRESH_BINARY)
        thInv = cv2.bitwise_not(th)
        frame = cv2.bitwise_and(frame, frame, mask=thInv)
        # sumamos los frame para que aparesca el color
        frame = cv2.add(frame, imAux)

        cv2.imshow('frame', frame)
        # cv2.imshow('imAux', imAux)
        # cv2.imshow('th', th)
        # cv2.imshow('thInv', thInv)
        # cv2.imshow('maskCeleste', maskCeleste)
        # funcion guardar

        # cv2.rectangle(frame, (0, 40), (50, 80), colorMarco, 6)
        # cv2.rectangle(frame, (0, 40), (50, 80), colorGuardar, -1)
        # cv2.putText(frame, 'Guardar', (1, 65), 1, 0.8, colorMarco, 1, cv2.LINE_AA)
        # creando carpeta para guardar las capturas
        Datos = 'Dibujos'
        if not os.path.exists(Datos):
            print('Carpeta creada: ', Datos)
            os.makedirs(Datos)

            # se guarda la con la letra s en la carpeta almacenada

        if k == 27:
            break
        if k == ord('s'):
            count += 1
            for i in range(1):
                Guardar.guardar(Datos, frame, colorMarco, count)
                break
    cap.release()
    cv2.destroyAllWindows()
