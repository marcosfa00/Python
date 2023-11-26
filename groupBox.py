# Procedemos con el QGroupBox con dos columnas de checkboxes en su interior
        groupBox = QGroupBox("Opciones de reproducción")
        horizontalBox = QHBoxLayout()
        groupBox.setLayout(horizontalBox)

        # Definimos la primera columna de checkboxes
        checkPrimera = QWidget()
        checkPrim = QVBoxLayout()
        checkPrimera.setLayout(checkPrim)
        checkAsinc = QCheckBox("Asíncrono")
        checkNombre = QCheckBox("Nombre de fichero")
        checkPersistente = QCheckBox("XML Persistente")
        checkPrim.addWidget(checkAsinc)
        checkPrim.addWidget(checkNombre)
        checkPrim.addWidget(checkPersistente)

        horizontalBox.addWidget(checkPrimera)

        # Definimos la segunda columna de checkboxes
        checkSegunda = QWidget()
        checkSeg = QVBoxLayout()
        checkSegunda.setLayout(checkSeg)
        checkFiltrar = QCheckBox("Filtrar")
        checkXML = QCheckBox("Es XML")
        checkReproduccion = QCheckBox("Reproducción NPL")
        checkSeg.addWidget(checkFiltrar)
        checkSeg.addWidget(checkXML)
        checkSeg.addWidget(checkReproduccion)

        horizontalBox.addWidget(checkSegunda)

        # Y añadimos la groupbox a la parte de abajo

        layoutFilaAbajo.addWidget(groupBox)