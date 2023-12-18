import cv2 as cv


def extraer_pistola_de_imagen(imagen_a_procesar):
    # Objeto que carga la configuracion para detectar la pistola
    cascade_classifier = cv.CascadeClassifier('../../detectores/detector_pistolas.xml')

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


imagen_pistola = cv.imread('../../resources/pistolas/test.png')
while True:
    imagen_en_blanco_y_negro = cv.cvtColor(imagen_pistola, cv.COLOR_BGR2GRAY)

    pistola_extraida = extraer_pistola_de_imagen(imagen_en_blanco_y_negro)

    # Muestra la imagen en una ventana
    cv.imshow('Pistola', pistola_extraida)

    # Espera a que el usuario toque una tecla
    cv.waitKey(0)
    break
