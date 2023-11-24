import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QStackedLayout, QVBoxLayout, QHBoxLayout)
#como vamos a usar también cajas de colores, vamos a importar esta clase
from CajaColor import CajaColor

#Tambien vamos a trabajar con un grid layout como vimos antes
class panelGrid(QGridLayout):
    def __init__(self):
        super().__init__()
        #objeto fila, columna, heith, columna
        #fila1
        self.addWidget(CajaColor("red"))
        self.addWidget(CajaColor("blue"),0,1,1,2)
        #fila2
        self.addWidget(CajaColor("green"),1,0,2,1)
        self.addWidget(CajaColor("pink"),1,1,1,2)
        #fila3
        self.addWidget(CajaColor("orange"),2,1,1,1)
        self.addWidget(CajaColor("yellow"),2,2,1,1)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        #creamos el layout box horizontal y vertical
        horizontalBox = QHBoxLayout()
        verticalBox = QVBoxLayout()

        #vamos a crear botones
        btnRed = QPushButton("ROJO")
        btnRed.pressed.connect(self.on_Red_Pressed)

        btnBlue = QPushButton("AZUL")
        btnBlue.pressed.connect(self.on_Blue_Pressed)

        gridbtn = QPushButton("GRID")
        gridbtn.pressed.connect(self.on_Grid_Pressed)

        btnGreen = QPushButton("VERDE")
        btnGreen.pressed.connect(self.on_Green_Pressed)#conectamos el boton con la funcion que crearemos más adelante

        #añadimos los botones a la caja horizontal
        horizontalBox.addWidget(btnRed)
        horizontalBox.addWidget(btnBlue)
        horizontalBox.addWidget(gridbtn)
        horizontalBox.addWidget(btnGreen)

        #a continuacion vamso a crear unas tarjetas QStackedLayout(Esto permite poner elementos unos encima de otros)
        self.tarjeta = QStackedLayout()
        #añadimos los elementos
        self.tarjeta.addWidget(CajaColor("red"))
        self.tarjeta.addWidget(CajaColor("blue"))
        #ahora los elementos anteriores los añadimos al gridLayout
        widgetGrid = QWidget()
        widgetGrid.setLayout(panelGrid())
        self.tarjeta.addWidget(widgetGrid)
        self.tarjeta.addWidget(CajaColor("green"))
        self.tarjeta.setCurrentIndex(0)#para que se muestre el primer elemento

        #ahor aañadimos las tarjetas a la caja vertical
        verticalBox.addLayout(self.tarjeta)
        verticalBox.addLayout(horizontalBox)

        #ahora creamos el contenedor
        conenedor = QWidget()
        conenedor.setLayout(verticalBox)
        #ahora añadimos el contenedor a la ventana
        self.setCentralWidget(conenedor)
        self.show()


        #a continuacion vamos a definir las funciones de pulsar el boton
    def on_Red_Pressed(self):
        self.tarjeta.setCurrentIndex(0)
    def on_Blue_Pressed(self):
        self.tarjeta.setCurrentIndex(1)
    def on_Grid_Pressed(self):
        self.tarjeta.setCurrentIndex(2)
    def on_Green_Pressed(self):
        self.tarjeta.setCurrentIndex(3)

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv)  # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()





