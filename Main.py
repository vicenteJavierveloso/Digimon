import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QGridLayout, QWidget, QHBoxLayout, QLineEdit, QSpinBox, QComboBox
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digimon")
        tipos = ["Free", "Vaccine", "Virus", "Data"]
        stage = []
        atributo = []

        #Elementos
        #- Labels
        self.texto_id = QLabel("ID")
        self.texto_nombre = QLabel("Nombre")
        self.texto_stage = QLabel("Stage")
        self.texto_tipo = QLabel("Tipo")
        self.texto_atributo = QLabel("Atributo")
        self.texto_memoria = QLabel("Memoria")
        self.texto_HP = QLabel("HP")
        self.texto_SP = QLabel("SP")
        self.texto_Atk = QLabel("Atk")
        self.texto_Def = QLabel("Def")
        self.texto_Int = QLabel("Int")
        self.texto_Spd = QLabel("Spd")
        #- Entradas
        #Para usar el contenido de la lista al presionar un boton, usar
        #el metodo self.entrada_<nombre>.currentText() -> str
        self.entrada_id = QSpinBox()
        self.entrada_nombre = QLineEdit()
        self.entrada_stage = QComboBox()
        self.entrada_tipo = QComboBox()
        self.entrada_atributo = QComboBox()
        self.entrada_memoria = QSpinBox()
        self.entrada_HP = QSpinBox()
        self.entrada_SP = QSpinBox()
        self.entrada_Atk = QSpinBox()
        self.entrada_Def = QSpinBox()
        self.entrada_Int = QSpinBox()
        self.entrada_Spd = QSpinBox()

         # + Inserta la lista de stage al menu
        self.entrada_stage.insertItems(0,stage)
        # + Inserta la lista de tipos en el menu desplegable
        self.entrada_tipo.insertItems(0,tipos)
        # + Inserta la lista de atributos al menu desplegable
        self.entrada_atributo.insertItems(0,atributo)

        #Elemento de prueba
        self.texto_prueba = QLabel("Texto Prueba")

        #Contenedores
        #- VerticalGrid
        basicos = QGridLayout()
        stats = QGridLayout()

        #- Visualizador
        visual = QVBoxLayout()
        visual.addWidget(self.texto_prueba)

        #- Layout principal
        layout_principal = QHBoxLayout()
        layout_principal.addLayout(basicos)
        layout_principal.addLayout(stats)
        layout_principal.addLayout(visual)

        #- Contenedor principal
        contendor_principal = QWidget()
        contendor_principal.setLayout(layout_principal)

        #Fijar widgets en contenedores (basicos)
        basicos.addWidget(self.texto_id,0,0)
        basicos.addWidget(self.texto_nombre,1,0)
        basicos.addWidget(self.texto_stage,2,0)
        basicos.addWidget(self.texto_tipo,3,0)
        basicos.addWidget(self.texto_atributo,4,0)
        basicos.addWidget(self.texto_memoria,5,0)
        # + Entradas
        basicos.addWidget(self.entrada_id,0,1)
        basicos.addWidget(self.entrada_nombre,1,1)
        basicos.addWidget(self.entrada_stage,2,1)    
        basicos.addWidget(self.entrada_tipo,3,1)
        basicos.addWidget(self.entrada_atributo,4,1)        
        basicos.addWidget(self.entrada_memoria,5,1)
        #Fijar widgets en contendores (stats)
        stats.addWidget(self.texto_HP,0,0)
        stats.addWidget(self.texto_SP,1,0)
        stats.addWidget(self.texto_Atk,2,0)
        stats.addWidget(self.texto_Def,3,0)
        stats.addWidget(self.texto_Int,4,0)
        stats.addWidget(self.texto_Spd,5,0)
        # + Entradas
        stats.addWidget(self.entrada_HP,0,1)
        stats.addWidget(self.entrada_SP,1,1)
        stats.addWidget(self.entrada_Atk,2,1)
        stats.addWidget(self.entrada_Def,3,1)
        stats.addWidget(self.entrada_Int,4,1)
        stats.addWidget(self.entrada_Spd,5,1)

        self.setCentralWidget(contendor_principal)
        print(self.entrada_tipo.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()
