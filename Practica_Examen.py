#en este ejercicio vamos a practicas para el examen de Python, utilizando los diferentes layouts
#primero vamos a importar los modulos necesarios
import sys
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame)
#vamos a crear la clase de la ventana principal

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        #bien, ahora empieza lo bueno
        #creamos el titulo de la ventana
        self.setWindowTitle("Practica Examen Desarrollo Interfaces")
        #creamos el layout vertical
        ventanaPrincipalBox = QVBoxLayout()
        #creamos el layout horizontal
        mitadSuperiorBox = QHBoxLayout()
        #añadimos el layout horizontal al vertical
        ventanaPrincipalBox.addLayout(mitadSuperiorBox)
        #bien una vez hecha la ventana principal, vamos a empezar poco a pcoo
        VerticalBoxCDyCheck = QVBoxLayout()
        #creamos un label que contendrá una imagen
        lblIcon = QLabel()
        #creamos la imagen
        lblIcon.setPixmap(QPixmap("dvd.png"))
        #añadimos la imagen al layout vertical
        VerticalBoxCDyCheck.addWidget(lblIcon)
        #horizontal box de checkbox y label
        Horizontal_CheckboxyLabel = QHBoxLayout()
        checkBox = QCheckBox("Animado")
        Horizontal_CheckboxyLabel.addWidget(checkBox)

        VerticalBoxCDyCheck.addLayout(Horizontal_CheckboxyLabel)

        #ahora debemos crear una lista ya que es donde se van a ver las canciones
        lista = QListWidget()
        self.lista = lista
        #añadimos la lista al layout horizontal
        mitadSuperiorBox.addLayout(VerticalBoxCDyCheck)
        mitadSuperiorBox.addWidget(lista)



        #ahora vamos a crear un layout vertical que contendrá los botones
        verticalBoxBtn = QVBoxLayout()
        #creamos 8 botones y un combobox
        btnAdList = QPushButton("Añadir a la lista")
        btnAdList.clicked.connect(self.on_AdList_Pressed)

        verticalBoxBtn.addWidget(btnAdList)
        btnSubir = QPushButton("Subir")
        verticalBoxBtn.addWidget(btnSubir)
        btnBajar = QPushButton("Bajar")
        verticalBoxBtn.addWidget(btnBajar)
        horizontalBoxBtn = QHBoxLayout()
        verticalBoxBtn.addLayout(horizontalBoxBtn)
        btnSaltar = QPushButton("Saltar")
        comboSaltar = QComboBox()
        horizontalBoxBtn.addWidget(btnSaltar)
        horizontalBoxBtn.addWidget(comboSaltar)
        verticalBoxBtn.addLayout(horizontalBoxBtn)
        btnAbrir = QPushButton("Abrir")
        verticalBoxBtn.addWidget(btnAbrir)
        btnReproducir = QPushButton("Reproducir")
        verticalBoxBtn.addWidget(btnReproducir)
        btnGuardar = QPushButton("Guardar")
        verticalBoxBtn.addWidget(btnGuardar)
        btnEliminar = QPushButton("Eliminar")
        verticalBoxBtn.addWidget(btnEliminar)
        #ahora añadimos el verticalBoxBtn al horizontalBox2
        mitadSuperiorBox.addLayout(verticalBoxBtn)

        #vale ahora vamos a continuar con la ventana inferior
        #creamos el layout horizontal
        mitadInferiorHorizontalBox = QHBoxLayout()
        #añadimos el layout horizontal al vertical
        ventanaPrincipalBox.addLayout(mitadInferiorHorizontalBox)
        #creamos el layout Vertical
        verticalBoxCheckboxes = QVBoxLayout()
        lblTitulo = QLabel("Opcions de reproducción")
        verticalBoxCheckboxes.addWidget(lblTitulo)
        #creamos el layout horizontal
        horizontalBoxCheckboxes = QHBoxLayout()
        verticalBox3Primeros = QVBoxLayout()
        #creamos los checkbox
        checkbox1 = QCheckBox("Asíncorno")
        verticalBox3Primeros.addWidget(checkbox1)
        checkbox2 = QCheckBox("Nombre fichero")
        verticalBox3Primeros.addWidget(checkbox2)
        checkbox3 = QCheckBox("XML")
        verticalBox3Primeros.addWidget(checkbox3)
        #añadimos el layout vertical al horizontal
        horizontalBoxCheckboxes.addLayout(verticalBox3Primeros)
        verticalBox3Segundos = QVBoxLayout()
        # creamos los checkbox
        checkbox1 = QCheckBox("Asíncorno")
        verticalBox3Segundos.addWidget(checkbox1)
        checkbox2 = QCheckBox("Nombre fichero")
        verticalBox3Segundos.addWidget(checkbox2)
        checkbox3 = QCheckBox("XML")
        verticalBox3Segundos.addWidget(checkbox3)
        # añadimos el layout vertical al horizontal
        horizontalBoxCheckboxes.addLayout(verticalBox3Segundos)
        verticalBoxCheckboxes.addLayout(horizontalBoxCheckboxes)
        mitadInferiorHorizontalBox.addLayout(verticalBoxCheckboxes)



        #ahora vamos a definir las funciones de los botones






        #vamos a crear un contenedor para podeer ver a tiempo real los cambios
        container = QWidget()
        container.setLayout(ventanaPrincipalBox)
        self.setCentralWidget(container)
        #mostramos la ventana
        self.show()

    def on_AdList_Pressed(self):
         texto = "New Item"
         self.lista.addItem(texto)

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv) # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()
