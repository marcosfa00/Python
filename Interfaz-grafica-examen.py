import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen")

        verticalBox = QVBoxLayout()
        horizontalBox = QHBoxLayout()
        verticalBox.addLayout(horizontalBox)
        horizontalBox2 = QHBoxLayout()
        verticalBox.addLayout(horizontalBox2)
        horizontal1Vertical1 = QVBoxLayout()
        horizontalBox.addLayout(horizontal1Vertical1)

        lblIcon = QLabel()
        pixmap = QPixmap("cd-128.png")
        lblIcon.setPixmap(pixmap)

        horizontal1Vertical1.addWidget(lblIcon)
        chkAnimado = QCheckBox("Animado")
        horizontal1Vertical1.addWidget(chkAnimado)

        lswLista = QListWidget()
        horizontalBox.addWidget(lswLista)

        caja4 = QVBoxLayout()
        horizontalBox.addLayout(caja4)

        btnAdList = QPushButton("Añadir a la lista")
        caja4.addWidget(btnAdList)
        btnSubir = QPushButton("Subir")
        caja4.addWidget(btnSubir)
        btnBajar = QPushButton("Bajar")
        caja4.addWidget(btnBajar)
        btnSaltar = QPushButton("Saltar")
        caja4.addWidget(btnSaltar)
        comboSaltar = QComboBox()
        caja4.addWidget(comboSaltar)
        btnAbrir = QPushButton("Abrir")
        caja4.addWidget(btnAbrir)
        btnReproducir = QPushButton("Reproducir")
        caja4.addWidget(btnReproducir)
        btnGuardar = QPushButton("Guardar")
        caja4.addWidget(btnGuardar)
        btnEliminar = QPushButton("Eliminar")
        caja4.addWidget(btnEliminar)

        grid2 = QGridLayout()
        horizontalBox2.addLayout(grid2)
        caja5 = QHBoxLayout()

        frameReproduccion = QFrame(caja5)





        container = QWidget()
        container.setLayout(verticalBox)
        self.setCentralWidget(container)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
