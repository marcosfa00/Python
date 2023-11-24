import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget
)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practica Examen Desarrollo Interfaces")

        # Layouts
        ventanaPrincipalBox = QVBoxLayout()
        mitadSuperiorBox = QHBoxLayout()
        ventanaPrincipalBox.addLayout(mitadSuperiorBox)

        # Componentes
        VerticalBoxCDyCheck = QVBoxLayout()
        lblIcon = QLabel()
        lblIcon.setPixmap(QPixmap("dvd.png"))
        VerticalBoxCDyCheck.addWidget(lblIcon)

        Horizontal_CheckboxyLabel = QHBoxLayout()
        checkBox = QCheckBox("Animado")
        Horizontal_CheckboxyLabel.addWidget(checkBox)
        VerticalBoxCDyCheck.addLayout(Horizontal_CheckboxyLabel)

        lista = QListWidget()
        self.lista = lista
        mitadSuperiorBox.addLayout(VerticalBoxCDyCheck)
        mitadSuperiorBox.addWidget(lista)

        # Botón "Añadir a la lista"
        btnAdList = QPushButton("Añadir a la lista")
        btnAdList.clicked.connect(self.on_AdList_Clicked)

        # Botones "Subir", "Bajar", y "Eliminar"
        btnSubir = QPushButton("Subir")
        btnBajar = QPushButton("Bajar")
        btnEliminar = QPushButton("Eliminar")

        # Layout para los botones
        verticalBoxBtn = QVBoxLayout()
        verticalBoxBtn.addWidget(btnAdList)
        verticalBoxBtn.addWidget(btnSubir)
        verticalBoxBtn.addWidget(btnBajar)
        verticalBoxBtn.addWidget(btnEliminar)
        mitadSuperiorBox.addLayout(verticalBoxBtn)

        container = QWidget()
        container.setLayout(ventanaPrincipalBox)
        self.setCentralWidget(container)
        self.show()

    def on_AdList_Clicked(self):
        texto = "Nuevo Elemento"
        self.lista.addItem(texto)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
