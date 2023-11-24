import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,QPushButton, QLabel,
                             QVBoxLayout, QWidget, QLineEdit)
from PyQt6.QtCore import Qt

class FirstInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Interface")#titulo de la ventana
        self.setFixedSize(300,400)#ancho y alto de la ventana
        #ahora comenzamos con la interfaz en si
        #para hacer una etiqueta label si
        #queremos modificarla mas adelante se pone self si no es local
        self.Etiqueta = QLabel("etiqueta 1")
        self.Etiqueta2 = QLabel("etiqueta 2")
        #para centrar la etiqueta
        self.setCentralWidget(self.Etiqueta)
        #siempre vamos a necesitar un contenedor
        boxv = QVBoxLayout()#este es el layout más simple
        #para añadir las cosas
        boxv.addWidget(self.Etiqueta)
        boxv.addWidget(self.Etiqueta2)
        #ahora se crea otro conetedor (este siempre está fijo
        container = QWidget()
        container.setLayout(boxv)
        self.setCentralWidget(container)
        self.show()












if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv)  # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = FirstInterface()
    # ejecutamos la union?
    aplicacion.exec()
