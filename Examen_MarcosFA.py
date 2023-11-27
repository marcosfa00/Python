import sys


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QListWidget, QRadioButton)

# Creamos la clase VentanaPrincipal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen 7-12-2020 Marcos Fdez. Avendaño")

        # Indicamos que este widget va a ser vertical
        layoutPrincipal = QVBoxLayout()
        parteSuperior = QHBoxLayout()
        parteMedio = QHBoxLayout()
        parteInferior = QHBoxLayout()
        parteBotones1 = QHBoxLayout()
        parteBotones2 = QHBoxLayout()
        layoutPrincipal.addLayout(parteSuperior)
        layoutPrincipal.addLayout(parteMedio)
        layoutPrincipal.addLayout(parteInferior)
        layoutPrincipal.addLayout(parteBotones1)
        layoutPrincipal.addLayout(parteBotones2)

        # Vamos ahora a poner tres labels verticales
        labelNombres = QWidget()
        layoutNombres = QVBoxLayout()
        labelNombres.setLayout(layoutNombres)
        lblName = QLabel("Nombre")
        lblTratamiento = QLabel("Tratamiento")
        lblFormato = QLabel("Formato")
        layoutNombres.addWidget(lblName)
        layoutNombres.addWidget(lblTratamiento)
        layoutNombres.addWidget(lblFormato)

        # Ahora vamos a añadir el labelNombres al layout principal
        parteSuperior.addWidget(labelNombres)
        #ahora vamos a añadir los campos a otro layout Vertical
        text = QWidget()
        textsLayout = QVBoxLayout()
        text.setLayout(textsLayout)
        #Creamos los objetos
        txtName = QLineEdit()
        txtTratamiento = QLineEdit()
        cmbFormat = QComboBox()
        cmbFormat.addItems(["", "HTML", "XML", "SVG", "XLS"])

        textsLayout.addWidget(txtName)
        textsLayout.addWidget(txtTratamiento)
        textsLayout.addWidget(cmbFormat)

        parteSuperior.addWidget(text)

        #Segunda parte Arriba
        lbl2 = QWidget()
        layoutNombres2 = QVBoxLayout()
        lbl2.setLayout(layoutNombres2)
        #Creamos los elementos
        lblSurname = QLabel("Apellido")
        lblTelf = QLabel("Teléfono")

        layoutNombres2.addWidget(lblSurname)
        layoutNombres2.addWidget(lblTelf)

        parteSuperior.addWidget(lbl2)

        #ahora vamos con los txt de los campos anteriores
        text2 = QWidget()
        textsLayout2 = QVBoxLayout()
        text2.setLayout(textsLayout2)
        #Creamos los objetos
        txtSurname = QLineEdit()
        txtTelf = QLineEdit()

        textsLayout2.addWidget(txtSurname)
        textsLayout2.addWidget(txtTelf)

        parteSuperior.addWidget(text2)

        #ahora procedemos a programar la parte del medio
        listas = QWidget()
        layoutListas = QVBoxLayout()
        listas.setLayout(layoutListas)
        #Creamos los objetos
        list = QListWidget()
        layoutListas.addWidget(list)
        parteMedio.addWidget(listas)

        #Parte Radio Buttons
        radioButtons = QWidget()
        radioLayout = QVBoxLayout()
        radioButtons.setLayout(radioLayout)
        #Elementos
        lblFormatoCorreo = QLabel("Formato Correo:")
        radioHTML = QRadioButton("HTML")
        radioHTML.clicked.connect(lambda: self.onRadioBtn(radioHTML))
        radioTxtPlano = QRadioButton("Texto Plano")
        radioTxtPlano.clicked.connect(lambda: self.onRadioBtn(radioTxtPlano))
        radioPers = QRadioButton("Personalizado")
        radioPers.clicked.connect(lambda: self.onRadioBtn(radioPers))

        radioLayout.addWidget(lblFormatoCorreo)
        radioLayout.addWidget(radioHTML)
        radioLayout.addWidget(radioTxtPlano)
        radioLayout.addWidget(radioPers)

        parteMedio.addWidget(radioButtons)

        #Ahora pasamos a Crear la parte inferior de la interfaz
        dirCorreo = QWidget()
        dirCorreoLayout = QHBoxLayout()
        dirCorreo.setLayout(dirCorreoLayout)
        #elementos
        lblDirCorreo = QLabel("Dirección de Correo")
        txtDirCorreo = QLineEdit()
        dirCorreoLayout.addWidget(lblDirCorreo)
        dirCorreoLayout.addWidget(txtDirCorreo)

        parteInferior.addWidget(dirCorreo)

        #botones
        botones = QWidget()
        lyoutBotones = QHBoxLayout()
        botones.setLayout(lyoutBotones)
        #Creamos los botones
        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(lambda : self.onAddPressed(txtName,txtSurname,txtTratamiento,txtTelf,list))
        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(lambda : self.onEditPressed(txtName,txtSurname,txtTratamiento,txtTelf,list))
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(lambda : self.delete(list))
        btnPorDefecto = QPushButton("Por Defecto")
        lyoutBotones.addWidget(btnEngadir)
        lyoutBotones.addWidget(btnEditar)
        lyoutBotones.addWidget(btnBorrar)
        lyoutBotones.addWidget(btnPorDefecto)

        parteBotones1.addWidget(botones)

        #botones 2
        botones2 = QWidget()
        lyoutBotones2 = QHBoxLayout()
        botones2.setLayout(lyoutBotones2)
        #Creamos los botones
        lblspaciador = QLabel("                                            ")

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.onCancelarPressed)
        lyoutBotones2.addWidget(lblspaciador)
        lyoutBotones2.addWidget(btnAceptar)
        lyoutBotones2.addWidget(btnCancelar)


        parteBotones2.addWidget(botones2)


        # Creamos el contenedor para mostrar todo
        container = QWidget()
        container.setLayout(layoutPrincipal)
        self.setCentralWidget(container)
        self.show()


    #A continuación Definimos las Funciones
    def onCancelarPressed(self):
        self.close()

    def onRadioBtn(self,radio):
        print("Radio Button Seleccionado: "+radio.text())
    def onAddPressed(self,nombre,apellido,tratamiento,telf,lista):
        linea = nombre.text()+" "+apellido.text()+" "+tratamiento.text()+" "+telf.text()
        print(linea)
        lista.addItem(linea)
        nombre.setText("")
        apellido.setText("")
        tratamiento.setText("")
        telf.setText("")
    def onEditPressed(self,nombre,apellido,tratamiento,telf,lista):

        #obtenemos la cuenta total de la lista para recorrerla
        total = lista.count()

        for i in range(total):
            elemento = lista.item(i)
            textElemento = elemento.text()
            palabras = textElemento.split()

            nombre.setText(palabras[0])
            apellido.setText(palabras[1])
            tratamiento.setText(palabras[2])
            telf.setText(palabras[3])

        self.delete(lista)


    def delete(self,list):
        currentRow = list.currentRow()
        if currentRow>=0:
            list.takeItem(currentRow)
        else:
            print("Selecciona el elemento que quieres eliminar")

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
