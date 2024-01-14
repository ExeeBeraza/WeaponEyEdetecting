# Detector de objetos en imagenes utilizando Yolov5.

## Procedimiento:

1. Crear dataset
    Consiste en almacenar un conjunto de imagenes de los objetos que se desean detectar etiquetando los objetos en dichas imagenes para que funcionen como ejemplos del objeto en cuestion.

2. Entrenamiento
    Se elige un marco de aprendizaje para entrenar la red neuronal. Para este caso se utilizara Yolo. 
      Yolo: 
        Es una familia de arquitecturas y modelos de deteccion de objetos entrenados previamente en el conjunto de datos COCO, y representa la investigacion sobre varios metodos de IA en vision futura, que incorpora practicas desarrolladas durante miles de horas de investigacion y desarrollo. 
  
3. Inferencia
    Se hace la inferencia en imagenes o videos de los distintos objetos que se buscan identificar. Se analizan a su vez
    los resultados obtenidos.

## Desarrollo de etapas

### Creacion de dataset

* En un directorio del proyecto dedicado para ser el dataset, se crean 2 carpetas __"images"__ y __"labels"__ una para las imagenes y otra para las etiquetas respectivamente.

* Dentro de cada una de las carpetas se crean a su vez dos carpetas. La primera de estas (train) dedicada para entrenamiento y la segunda (validation) para las validaciones correspondientes.

* Para construir el dataset, se recomiendan tener un numero elevado de imagenes (Aproximadamente 500 o 600 imagenes).

  i. Las imagenes descargadas se deben almacenar en la ruta __*/images/train*__.

    __Nota__: Se recomienda utilizar la extension de google chrome [Download all images](https://chromewebstore.google.com/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm?hl=es). Sin embargo, es necesario verificar las imagenes descargadas.


  ii. Luego seleccionar las ultimas 40 imagenes para moverlas a la ruta __*/images/validation*__

  __Nota__: Para el etiquetado de las imagenes, se recomienda utilizar la pagina [makesense.ai](https://www.makesense.ai/). Aqui mismo tambien se pueden crear los labels que se quieran. 
  Los archivos resultantes se pueden exportar en un archivo .zip para YOLO. Estos archivos extraidos se almacenaran en la ruta __/labels/train__. Esto debe repetirse para las imagenes de validacion (que sus archivos de etiquetado deben almacenarse en la carpeta de validation).

### Entrenamiento

  Para el entrenamiento es necesario desarrollar un par de conceptos:
    
    - Epocas: las epocas son la cantidad de iteraciones que va a tener el entrenamiento, de manera que mientras mayor epocas haya, mejor sera el entrenamiento. 

    - Batch size: esta relacionado con la forma en la que la red neuronal aprende. Son agrupaciones de datos en los que la red basa su entrenamiento.
  
  Para ver en detalle el proceso de entrenamiento con YOLO, se puede revisar la [documentacion oficial](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/).

* Para el entrenamiento es necesario utilizar un _google colab_, el cual se puede desplegar desde el acceso que da la documentacion oficial. Esto simplemente es un entorno en la nube que nos permitira entrenar la red neuronal. 
  Nota: Es necesario asegurarnos que en la configuracion del notebook, el acelerador de hardware este en GPU. El primer paso (clonacion de YOLO en el entorno colab) se encuentra explicado en el notebook.

* Luego, es necesario seleccionar el modelo de YOLO a utilizar. Para este caso se usara YOLOv5x (que es la red neuronal que tiene mayor rendimiento de las que ofrece YOLOv5). 

* Posteriormente, se debe subir un .zip con las imagenes del dataset a los archivos del proyecto en google colab.

* En el colab, hay que descomprimir la carpeta del dataset. Para esto, se puede utilizar el siguiente comando en la consola del notebook.

```shell
!unzip -q /content/<nombre de la carpeta del dataset>.zip -d /content
```

* Ahora se debe descargar el archivo _coco128.yaml_ para editarlo en nuestro equipo local. 
  En este archivo hay que: 
  - Eliminar todo lo que se encuentre por encima de la variable __path__ inclusive
  - Agregar los nombres de las clases de objetos a detectar y la cantidad de las mismas
  - Modificar las variables train y val, quedando de la siguiente manera:
  ```yaml
    train: /content/<nombre de la carpeta del dataset>/images/train
    val: /content/<nombre de la carpeta del dataset>/images/validation
  ```

  Con el archivo .yaml modificado, se recomienda cambiar el nombre al mismo a _"custom.yaml"_. Por ultimo, se debe subir el archivo a la misma localizacion de donde se descargo el archivo original.

* Con todo lo anterior, ahora se procede con el entrenamiento propiamente dicho. Para esto, hay que ejecutar el siguiente comando. 
  ```shell
  !python train.py --img <tamaño imagen> --batch 4 --epochs <numero de epocas> --data /content/yolov5/data/custom.yaml --weights yolov5x.pt --cache
  ```
  - img: tamaño de la imagen que se utilizara para la inferencia posteriormente.
  - epochs: se recomienda dejar en 50 o 60 para un buen entrenamiento.


* Mediante el tensorboard se puede apreciar la precision de la red entrenada. 

* Todo este proceso resulta en un archivo .pt que se utilizara para la inferencia. Se descarga este archivo mediante la linea de codigo:
  ```shell
  from google.colab import files
  files.download('./runs/train/exp/weights/best.pt')
  ```

### Proceso de Inferencia

### Pruebas

Proximamente...