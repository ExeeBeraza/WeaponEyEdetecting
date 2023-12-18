import math

import cv2 as cv
import numpy as np


def detect_painting(image):
    image = filtro(image)
    image, gx, gy, minimo, maximo, conv = mascara(image)
    imgnor = normalizar(image, minimo, maximo, conv)
    imbina = binarizar(image)


def pistola(imagen_a_procesar):
    # Objeto que carga la configuracion para detectar la pistola
    cascade_classifier = cv.CascadeClassifier(
        '../../detectores/detector_pistolas.xml')  # TODO: Agregar variable entorno

    pistolas_encontradas = cascade_classifier.detectMultiScale(imagen_a_procesar, 1.1, 9)

    if len(pistolas_encontradas) > 0:
        cant_pistolas_encontradas = 0
        for (x, y, ancho, alto) in pistolas_encontradas:
            # TODO: Cambiar color del rectangulo
            cv.rectangle(imagen_a_procesar, (x, y), (x + alto, y + ancho), cv.COLOR_BAYER_BGGR2RGB, 5)
            cv.putText(imagen_a_procesar, ("Pistola # " + str(cant_pistolas_encontradas)), (x, y), cv.FONT_ITALIC, 1.1,
                       (255, 255, 255), 2)
            cant_pistolas_encontradas += 1
    else:
        print("No encontre pistolas")

    return imagen_a_procesar


def mascara(image):
    sobelx = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])
    sobely = ([1, 2, 1], [0, 0, 0], [-1, -2, -1])
    img, gx, gy, minimo, maximo, conv = convolucion(sobelx, sobely, image)
    return img, gx, gy, minimo, maximo, conv


def convolucion(h1, h2, image):  # Para deteccion de bordes con convolucion
    pixels = image.load()
    ancho, alto = image.size
    a = len(h1[0])
    conv = np.empty((ancho, alto))
    gx = np.empty((ancho, alto))
    gy = np.empty((ancho, alto))
    minimo = 255
    maximo = 0
    for x in range(ancho):
        for y in range(alto):
            sumax = 0.0
            sumay = 0.0
            for i in range(a):
                for j in range(a):
                    try:
                        sumax += (pixels[x + i, y + j][0] * h1[i][j])
                        sumay += (pixels[x + i, y + j][0] * h2[i][j])

                    except:
                        pass
            gradiente = math.sqrt(pow(sumax, 2) + pow(sumay, 2))
            conv[x, y] = gradiente
            gx[x, y] = sumax
            gy[x, y] = sumay
            gradiente = int(gradiente)
            pixels[x, y] = (gradiente, gradiente, gradiente)
            p = gradiente
            if p < minimo:
                minimo = p
            if p > maximo:
                maximo = p
    image.save('convo.png')
    return image, gx, gy, minimo, maximo, conv


def normalizar(image, minimo, maximo, conv):  # normalizamos
    pixels = image.load()
    r = maximo - minimo
    prop = 255.0 / r
    ancho, alto = image.size
    for i in range(ancho):
        for j in range(alto):
            p = int(math.floor((conv[i, j] - minimo) * prop))
            pixels[i, j] = (p, p, p)

    return image


def binarizar(image):  # binarizamos la imagen
    pixels = image.load()
    ancho, alto = image.size
    minimo = int(argv[2])
    for i in range(ancho):
        for j in range(alto):
            if pixels[i, j][1] < minimo:
                p = 0
            else:
                p = 255
            pixels[i, j] = (p, p, p)
    image.save('binarizar.png')
    return img


def filtro(image):
    image, matriz = escala_grises(image)
    pixels = image.load()
    ancho, alto = image.size
    lista = [-1, 0, 1]
    for i in range(ancho):
        for j in range(alto):
            promedio = vecindad(i, j, lista, matriz)
            pixels[i, j] = (promedio, promedio, promedio)
    image.save('filtrado.png')
    return image


def escala_grises(image):  # escala de grises
    image = Image.open(image)
    pixels = image.load()
    ancho, alto = image.size
    matriz = np.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            (r, g, b) = image.getpixel((i, j))
            escala = (r + g + b) / 3
            pixels[i, j] = (escala, escala, escala)
            matriz[i, j] = int(escala)
    df = image.save('escaladegrises.png')
    return image, matriz


def vecindad(i, j, lista, matriz):  # filtrado
    promedio = 0
    indice = 0
    for x in lista:
        for y in lista:
            a = i + x
            b = j + y
            try:
                if matriz[a, b] and (x != a and y != b):
                    promedio += matriz[a, b]
                    indice += 1
            except IndexError:
                pass
            try:
                promedio = int(promedio / indice)
                return promedio
            except ZeroDivisionError:
                return 0


def main():
    imagen_pistola = cv.imread('<Agregar ruta imagen>')  # TODO: Agregar ruta de imagen
    # TODO: En caso de que no encuentre la imagen

    while True:
        imagen_en_blanco_y_negro = cv.cvtColor(imagen_pistola, cv.COLOR_BGR2GRAY)
        pistola_extraida = pistola(imagen_en_blanco_y_negro)

        # Muestra la imagen en una ventana
        cv.imshow('Pistola', pistola_extraida)

        # TODO: Agregar mas objetos para reconocer

        # Espera a que el usuario toque una tecla
        cv.waitKey(0)
        break


main()
