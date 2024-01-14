# Sistema de detección de Armas

Sistema para la detección y clasificación de armas en tiempo real utilizando técnicas de visión computacional,
en conjunto con funciones de Opencv.

Implementado por Roberto Axel Valenzuela Padilla http://roberto-valenzuela.blogspot.com
Mayo 2013


## Instalación de librerias y requerimientos

Leer el archivo [install](docs/install.md) para ver en detalle las instrucciones de instalación.


## Compatibilidad

El sistema debe ser compatible para el siguiente equipo

- Linux Ubuntu 12.04 64 bits , en una computadora DELL Inspiron 4050

## Desarrollo de los procedimientos utilizados

Para ver los detalles de los procedimientos que se siguieron para utilizar la herramienta YOLO y los procesos
de entrenamiento, consultar el archivo [desarrollo con yolo]().

## Arquitectura del proyecto
Detalle de la [arquitectura](docs/arquitectura.md). utilizada para este proyecto.

## Ejecución

Para ejectuar este programa 
1. Se abre una terminal 
2. Se localiza en la dirección donde se encuentra el archivo 
3. Ingresamos el siguiente comando python Final.py
4. Se activara la cámara de la computadora.
5. El proceso comienza y se analiza cada frame
6. Si en la captura de video se detecta algún arma, se enmarca la posición del objeto.


## Licencia

El proyecto puede ser modificado, y utilizado para propios proyectos, mencionando
las referencias a este proyecto.


## Más Información

### Material de apoyo.
   * Proyecto final de la materia de Visión Computacional de la carrera Ingeniería 
    en Tecnologías de Software, FIME,UANL. Impartida por la Dra. Satu Elisa Schaeffer en el periodo enero-junio 2013
