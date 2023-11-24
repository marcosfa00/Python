#Aquí vamos a usar el Layout caja de colores
#para ello debemos importarla
from CajaColor import CajaColor
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout)

class VentanaPrincipal(QMainWindow):
    #creamos el constructor
    def __init__(self):
        super().__init__()
        #le damos nombre
        self.setWindowTitle("Eemplo de Grid Layout_Marcosfa")
        #creamos una que contendrá los colores
        grid = QGridLayout()
        #objeto, fila, columna, heith, columna

        #fila1
        grid.addWidget(CajaColor("red"))#fila 0, columna 0 por defecto
        grid.addWidget(CajaColor("yellow"), 0, 1, 1, 2)#fila 0, columna 1, heith 1, columna 2
        #fila2
        grid.addWidget(CajaColor("green"), 1, 0, 2, 1)
        grid.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        #fila3
        grid.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        grid.addWidget(CajaColor("yellow"), 2, 2, 1, 1)

        #Ahora creamos el contenedor que contendrá el grid
        contenedor = QWidget()
        contenedor.setLayout(grid)
        self.setCentralWidget(contenedor)
        self.show()

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv) # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()
