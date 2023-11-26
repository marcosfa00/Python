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
        btnAdList.clicked.connect(lambda :self.on_add_clicked(lswLista))
        caja4.addWidget(btnAdList)
        btnSubir = QPushButton("Subir")
        btnSubir.clicked.connect(lambda: self.on_subir_clicked(lswLista))
        caja4.addWidget(btnSubir)
        btnBajar = QPushButton("Bajar")
        btnBajar.clicked.connect(lambda: self.on_bajar_clicked(lswLista))
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
        btnEliminar.clicked.connect(lambda: self.on_eliminar_clicked(lswLista))
        caja4.addWidget(btnEliminar)

        grid2 = QGridLayout()
        horizontalBox2.addLayout(grid2)

        container = QWidget()
        container.setLayout(verticalBox)
        self.setCentralWidget(container)
        self.show()






#las funciones se deben definir después del contructor
    def on_add_clicked(self, lista):
        song = input("Introduce la canción a añadir")
        if song:
            lista.addItem(song)
        else:
            print("No se ha introducido ninguna canción")


    def on_subir_clicked(self,lista):
        #obtenemos la posicion actual de la lista
        current_row = lista.currentRow()
        #debemos verificar que no es el primer elemento de la lista
        if  current_row > 0:
            lista.setCurrentRow(current_row -1)


    def on_bajar_clicked(self,lista):
        #obtenemos la posicion actual de la lista
        current_row = lista.currentRow()
        #comprobamos que no es el ultimo elemento de la lista
        if  current_row < lista.count() -1:
            lista.setCurrentRow(current_row +1)

    def on_eliminar_clicked(self,lista):
        #obytenemos la posicion actual en la lista
        currentRow = lista.currentRow()
        #verificamos si hay un elemento seleccionado
        if  currentRow >=0:
            lista.takeItem(currentRow)#se elimina el elemento de la lista
        else:
            print("Selecciona el elemento que quieres eliminar")





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
