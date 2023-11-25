import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

from PyQt6.QtGui import QPalette, QColor

class CajaColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color)) # Usar QPalette.ColorRole.Window en lugar de QPalette.Window
        self.setPalette(palette)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caja de Colores")

        hBox = QHBoxLayout()  # Layout principal horizontal

        # Contenedores verticales y cajas de color
        verticalBox1 = QVBoxLayout()
        verticalBox1.addWidget(CajaColor("blue"))

        verticalBox2 = QVBoxLayout()
        verticalBox2.addWidget(CajaColor("green"))

        verticalBox3 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(CajaColor("red"))
        hbox2 = QHBoxLayout()
        hbox2.addWidget(CajaColor("yellow"))
        verticalBox3.addLayout(hbox1)
        verticalBox3.addLayout(hbox2)

        verticalBox4 = QVBoxLayout()
        verticalBox4.addWidget(CajaColor("orange"))

        # Agregar contenedores verticales al layout horizontal principal
        hBox.addLayout(verticalBox1)
        hBox.addLayout(verticalBox2)
        hBox.addLayout(verticalBox3)
        hBox.addLayout(verticalBox4)

        container = QWidget()
        container.setLayout(hBox)
        self.setCentralWidget(container)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
