# Practica Examen Lunes
# Creamos una clase llamada Ventana principal donde vamos a estructurar Todo
#Primero por supuesto hacemos los imports
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QSlider, QGroupBox)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PRACTICA EJERCICIO EXAMEN")
        #vamos a crear la ventana principal
        ventanaPrincipal= QVBoxLayout()
        parteSuperior = QHBoxLayout()
        parteInferior = QHBoxLayout()
        ventanaPrincipal.addLayout(parteSuperior)
        ventanaPrincipal.addLayout(parteInferior)


        #parteCD y checkbox
        #primero el winget donde ira todo esto y despues indicarle si la posicion es vertical o horizontal
        parteCD = QWidget()
        verticalBoxCD = QVBoxLayout()
        #Aquñi le indicamos al widget que va a usar una plantilla vertical
        parteCD.setLayout(verticalBoxCD)
        #creamos imagen y checkbox
        #para la imagen primero se debe crear un label
        labelIcon = QLabel()
        pixMap = QPixmap("cd-player.png")
        labelIcon.setPixmap(pixMap)
        checkBox = QCheckBox("Animado")

        verticalBoxCD.addWidget(labelIcon)
        verticalBoxCD.addWidget(checkBox)

        parteSuperior.addWidget(parteCD)

        #vale ahora que ya tenemos la parte del CD vamos a crear la lista de elementos
        lista =  QListWidget()
        #indicamos que esta lista empleara un layout vertical
        listaVertical = QVBoxLayout()
        lista.setLayout(listaVertical)

        #ahora añadiremos la lista a la parte superior
        parteSuperior.addWidget(lista)

        #ahora vamos a crear los botones, para ello se orientaran en vertical,
        # debemos tener en cuenta que cada boton es un widget asiq solo deberemos crear el
        # layout que seguitan estos botones
        LayoutBotones = QVBoxLayout()
        btnAddList = QPushButton("Add Button")
        btnUpList = QPushButton("Up")
        btnDownList = QPushButton("Down")
        LayoutBotones.addWidget(btnAddList)
        LayoutBotones.addWidget(btnUpList)
        LayoutBotones.addWidget(btnDownList)
        #ahora como vienen dos botones en horizontal, vamos a crear un layout horizontal
        btnSaltar = QPushButton("Saltar")
        comboBox = QComboBox()
        # Creamos el Layout Horizontal
        horizontalBotones = QHBoxLayout()
        horizontalBotones.addWidget(btnSaltar)
        horizontalBotones.addWidget(comboBox)
        LayoutBotones.addLayout(horizontalBotones)
        #Continuamos con los botones verticales
        btnOpen = QPushButton("Open")
        btnPlay = QPushButton("Play")
        btnSave = QPushButton("Save")
        btndelete =  QPushButton("Delete")
        LayoutBotones.addWidget(btnOpen)
        LayoutBotones.addWidget(btnPlay)
        LayoutBotones.addWidget(btnSave)
        LayoutBotones.addWidget(btndelete)

        parteSuperior.addLayout(LayoutBotones)

        #Bien ahora vamos a continuar con la parte inferior de la pantalla
        #Vamos a hacer los nombres en Vertical:
        names = QWidget()
        verticalNames = QVBoxLayout()
        names.setLayout(verticalNames)
        #la parte de los nombres son label
        lblSon = QLabel("Son: ")
        lblRitmo =QLabel("Ritmo: ")
        lblVolume =QLabel("Volumen")
        lblFormato = QLabel("Formato")
        lblSalidaAudio=QLabel("Salida audio")
        verticalNames.addWidget(lblSon)
        verticalNames.addWidget(lblRitmo)
        verticalNames.addWidget(lblVolume)
        verticalNames.addWidget(lblFormato)
        verticalNames.addWidget(lblSalidaAudio)
        #Añadimos todos los nombres a la parte Inferior
        parteInferior.addWidget(names)

        #Ahora procedemos a añadir los comboBox y los sliders de Volumen
        BtnAbajo = QWidget()
        Verticalbtn_abajo = QVBoxLayout()
        BtnAbajo.setLayout(Verticalbtn_abajo)
        #declaramos lo elementos
        comboSonido = QComboBox()
        # ahora los sliders
        # estos tienen que ser en horizontal
        sliderRitmo = QSlider()
        sliderRitmo.setOrientation(Qt.Orientation.Horizontal)
        sliderVolumen = QSlider()
        sliderVolumen.setOrientation(Qt.Orientation.Horizontal)
        comboFormato = QComboBox()
        comboSalidaAudio = QComboBox()
        #ahora añadimos todos los widgets al Layout
        Verticalbtn_abajo.addWidget(comboSonido)
        Verticalbtn_abajo.addWidget(sliderRitmo)
        Verticalbtn_abajo.addWidget(sliderVolumen)
        Verticalbtn_abajo.addWidget(comboFormato)
        Verticalbtn_abajo.addWidget(comboSalidaAudio)
        #añadimos el widget a la parte ifnerior
        parteInferior.addWidget(BtnAbajo)

        #Fantástico, ahora procederemos a crear unn grupo donde vamos a meter las opciones de leproducción
        #Para eso primero creamos un Widget
        # Crear el grupo de opciones de reproducción
        groupBox = QGroupBox("Opciones de Reproducción")
        horizontalOptions = QHBoxLayout()
        groupBox.setLayout(horizontalOptions)

        # Definir la primera columna de opciones
        options = QWidget()
        vertical = QVBoxLayout()
        options.setLayout(vertical)
        checkAsinc = QCheckBox("Asíncrono")
        checkNombre = QCheckBox("Nombre de fichero")
        checkPersistente = QCheckBox("XML Persistente")
        vertical.addWidget(checkAsinc)
        vertical.addWidget(checkNombre)
        vertical.addWidget(checkPersistente)

        # Agregar la primera columna al layout horizontal
        horizontalOptions.addWidget(options)

        # Definir la segunda columna de opciones
        checkSegunda = QWidget()
        checkSeg = QVBoxLayout()
        checkSegunda.setLayout(checkSeg)
        checkFiltrar = QCheckBox("Filtrar")
        checkXML = QCheckBox("Es XML")
        checkReproduccion = QCheckBox("Reproducción NPL")
        checkSeg.addWidget(checkFiltrar)
        checkSeg.addWidget(checkXML)
        checkSeg.addWidget(checkReproduccion)

        # Agregar la segunda columna al layout horizontal
        horizontalOptions.addWidget(checkSegunda)

        # Agregar el groupBox al layout parteInferior
        parteInferior.addWidget(groupBox)

        container = QWidget()
        container.setLayout(ventanaPrincipal)
        self.setCentralWidget(container)
        self.show()




if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())


