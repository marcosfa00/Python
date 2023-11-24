import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette

#vamos a crear una clase que sea un widget
class CajaColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)#para que se pueda pintar el fondo
        paleta = self.palette()#obtenemos la paleta de colores
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))#le damos el color
        self.setPalette(paleta)#le damos la paleta a la caja

#ahora vamos a crear la clase de la ventana

class VentanaEjercicio(QMainWindow):
    #definimos el constructor
    def __init__(self):
        super().__init__()

        #caja que contenga la caja de colores
        box = QHBoxLayout()
        #En esta caja tendremos varios cuadrados de diferentes colores
        square =QHBoxLayout()#creamos la caja que contendrá los cuadrados en horizontal
        #añadimos los colores
        square.addWidget(CajaColor("red"))
        square.addWidget(CajaColor("yellow"))
        square.addWidget(CajaColor("purple"))

        #ahora crearemos otra caja que contenga otra etiqueta
        square2 = QVBoxLayout() #creamos la caja que contendrá los cuadrados en vertical
        square2.addWidget(CajaColor("blue"))

        #vamos a crear otra caja que contenga otra etiqueta
        square3= QVBoxLayout() #creamos la caja que contendrá los cuadrados en vertical
        square3.addWidget(CajaColor("red"))
        square3.addWidget(CajaColor("purple"))

        #ahora añadimos las cajas a la caja principal
        box.addLayout(square)
        box.addLayout(square2)
        box.addLayout(square3)

        #Ahora vamso a crear un contenedor
        container = QWidget()
        container.setLayout(box)
        self.setCentralWidget(container)
        #mostramos la ventana
        self.show()

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv) # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaEjercicio()
    # ejecutamos la union?
    aplicacion.exec()