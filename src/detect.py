from lib.loader import Loader

import torch
import cv2 as cv
import numpy as np
import pathlib

# Configuracion requerida para windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


def start_detection():

    loader = Loader()
    configs, err = loader.load_configs()
    if err is not None:
        raise err

    detector_models = configs['models']
    model = torch.hub.load(
        'ultralytics/yolov5',
        'custom',
        force_reload=True,
        path=detector_models['guns']
    )

    image = cv.imread('F:/Dev/AyudaExe/ProyectoFinalIA2023/resources/pistolas/glock.jpg')
    while True:
        # Realizamos deteccion
        detect = model(image)

        # Muestra la imagen en una ventana
        cv.imshow('Detector de pistolas', np.squeeze(detect.render()))

        # Espera a que el usuario toque una tecla
        cv.waitKey(0)
        break

    cv.destroyAllWindows()


def main():
    # Comienza deteccion
    start_detection()

main()
