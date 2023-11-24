import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QStackedLayout, QVBoxLayout, QHBoxLayout)

#como vamos a usar también cajas de colores, vamos a importar esta clase
from CajaColor import CajaColor
#tambiénm usaremso panel grid por lo que lo vamso a importar del ejercicio anterior
from VentanaQstackLayout import panelGrid

class HBoxModificado(QHBoxLayout):
    def __init__(self):
        super().__init__()
        vBox1 = QVBoxLayout()
        vBox2 = QVBoxLayout()

        vBox1.addWidget(CajaColor("red"))
        vBox1.addWidget(CajaColor("blue"))
        vBox2.addWidget(CajaColor("green"))
        self.addLayout(vBox1)

        self.addWidget(CajaColor("yellow"))

        vBox2.addWidget(CajaColor("pink"))
        vBox2.addWidget(CajaColor("orange"))
        self.addLayout(vBox2)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de QStackedLayout con QT")

        self.setWindowTitle("Ejemplo de QStacke")

        #vamos a crear las cajas
        verticalBox = QVBoxLayout()
        horizontalBox = QHBoxLayout()

        #creamos los botones
        btnRed = QPushButton("ROJO")
        btnRed.pressed.connect(self.on_Red_Pressed)

        btnBlue = QPushButton("AZUL")
        btnBlue.pressed.connect(self.on_Blue_Pressed)

        btnGrid = QPushButton("GRID")
        btnGrid.pressed.connect(self.on_Grid_Pressed)

        boxModificado = QPushButton("BOX MODIFICADO")
        boxModificado.pressed.connect(self.on_Box_Modificado)

        #añadimos los botones a la caja horizontal
        horizontalBox.addWidget(btnRed)
        horizontalBox.addWidget(btnBlue)
        horizontalBox.addWidget(btnGrid)
        horizontalBox.addWidget(boxModificado)

        #creamos las tarjetas para que se superpongan
        self.tarjeta = QStackedLayout()
        #añadimos las tarjetas
        self.tarjeta.addWidget(CajaColor("red"))
        self.tarjeta.addWidget(CajaColor("blue"))
        #para añadir el grid layout
        widgetGrid = QWidget()
        widgetGrid.setLayout(panelGrid())#añadimos el panel grid que es la clase creada en el archivo anterior
        self.tarjeta.addWidget(widgetGrid)
        #para añadir el box modificado
        widgetBox = QWidget()
        widgetBox.setLayout(HBoxModificado())
        self.tarjeta.addWidget(widgetBox)
        self.tarjeta.setCurrentIndex(0)#para que se muestre el primer elemento

        #añadimos las tarjetas a la caja vertical
        verticalBox.addLayout(self.tarjeta)
        verticalBox.addLayout(horizontalBox)

        #mostramos la ventana
        control = QWidget()
        control.setLayout(verticalBox)
        # lo mostramos
        self.setCentralWidget(control)
        self.show()

    #a continuacion vamos a definir las funciones de pulsar el boton
    def on_Red_Pressed(self):
        self.tarjeta.setCurrentIndex(0)
    def on_Blue_Pressed(self):
        self.tarjeta.setCurrentIndex(1)
    def on_Grid_Pressed(self):
        self.tarjeta.setCurrentIndex(2)
    def on_Box_Modificado(self):
        self.tarjeta.setCurrentIndex(3)

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv) # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()