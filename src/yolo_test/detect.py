import torch
import cv2 as cv
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'custom', path='Z:/DesarrolloExe/Proyecto_2_IA_2023/models/pistolas.pt')


cap = cv.imread('../../resources/pistolas/test.png')

while True:

    # Realizamos deteccion
    detect = model.detect(cap)

    # Muestra la imagen en una ventana
    cv.imshow('Detector de pistolas', np.squeeze(detect.render()))

    # Espera a que el usuario toque una tecla
    cv.waitKey(0)
    break


cv.destroyAllWindows()
