import torch
import cv2 as cv
import numpy as np
import pathlib

# Configuracion requerida para windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='F:/Dev/AyudaExe/ProyectoFinalIA2023/models/modelo_detector_pistolas.pt')


cap = cv.imread('../../resources/pistolas/glock.jpg')

while True:
    # Realizamos deteccion
    detect = model(cap)

    # Muestra la imagen en una ventana
    cv.imshow('Detector de pistolas', np.squeeze(detect.render()))

    # Espera a que el usuario toque una tecla
    cv.waitKey(0)
    break

cv.destroyAllWindows()
