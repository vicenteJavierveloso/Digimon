import sys
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QSpinBox, QLineEdit, QComboBox, QHBoxLayout, QGridLayout, QWidget, QListWidget, QMessageBox, QPushButton, QListWidgetItem

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digimon")
        self.setFixedSize(QSize(700,300))

        tipos = ["Free", "Vaccine", "Virus", "Data"]
        stage = ["Baby", "In-Training", "Rookie", "Champion", "Ultimate", "Mega"]
        atributo = ["Fire", "Water", "Plant", "Electric", "Wind", "Earth"]
        
        #Imagen
        self.imagen = QLabel()
        archivo = QPixmap("imagen.png")
        archivo = archivo.scaled(200,200)
        self.imagen.setPixmap(archivo)

        #Elementos Texto
        #Basicos
        self.texto_ID = QLabel("ID")
        self.texto_nombre = QLabel("Nombre")
        self.texto_stage = QLabel("Stage")
        self.texto_tipo = QLabel("Tipo")
        self.texto_atributo = QLabel("Atributo")
        self.texto_memoria = QLabel("Memoria")
        #Stats
        self.texto_HP = QLabel("HP")
        self.texto_Atk = QLabel("Atk")
        self.texto_Sp = QLabel("Sp")
        self.texto_Def = QLabel("Def")
        self.texto_Int = QLabel("Int")
        self.texto_Spd = QLabel("Spd")

        #Entradas
        #Basicos
        self.entrada_ID = QSpinBox()
        self.entrada_nombre = QLineEdit()
        self.entrada_stage = QComboBox()
        self.entrada_tipo = QComboBox()
        self.entrada_atributo = QComboBox()
        self.entrada_memoria = QSpinBox()
        #Stats
        self.entrada_HP = QSpinBox()
        self.entrada_Atk = QSpinBox()
        self.entrada_Sp = QSpinBox()
        self.entrada_Def = QSpinBox()
        self.entrada_Int = QSpinBox()
        self.entrada_Spd = QSpinBox()

        #Fijar maximos 
        self.entrada_HP.setMaximum(9999)
        self.entrada_Atk.setMaximum(9999)
        self.entrada_Sp.setMaximum(9999)
        self.entrada_Def.setMaximum(9999)
        self.entrada_Int.setMaximum(9999)
        self.entrada_Spd.setMaximum(9999)

        self.entrada_ID.setMaximum(249)

        #Fijar elementos de menus desplegables
        self.entrada_stage.insertItems(0,stage)
        self.entrada_tipo.insertItems(0,tipos)
        self.entrada_atributo.insertItems(0,atributo)

        #Lista de elementos
        self.lista = QListWidget()

        #Boton
        agregar = QPushButton("Añadir")
        agregar.clicked.connect(lambda: self.agregar(self.entrada_ID.value(), 
        self.entrada_nombre.text(), self.entrada_stage.currentText(), self.entrada_tipo.currentText(),
        self.entrada_atributo.currentText(), self.entrada_memoria.value(),
        self.entrada_HP.value(), self.entrada_Sp.value(), self.entrada_Atk.value(),
        self.entrada_Def.value(),self.entrada_Int.value(),self.entrada_Spd.value()))

        #Layouts
        contenedor_basicos = QGridLayout()
        contenedor_stats = QGridLayout()
        contenedor_grande = QHBoxLayout()
        
        #Añadir elementos
        #Basicos
        #Labels
        contenedor_basicos.addWidget(self.texto_ID,0,0)
        contenedor_basicos.addWidget(self.texto_nombre,1,0)
        contenedor_basicos.addWidget(self.texto_stage,2,0)
        contenedor_basicos.addWidget(self.texto_tipo,3,0)
        contenedor_basicos.addWidget(self.texto_atributo,4,0)
        contenedor_basicos.addWidget(self.texto_memoria,5,0)
        #Entradas
        contenedor_basicos.addWidget(self.entrada_ID,0,1)
        contenedor_basicos.addWidget(self.entrada_nombre,1,1)
        contenedor_basicos.addWidget(self.entrada_stage,2,1)
        contenedor_basicos.addWidget(self.entrada_tipo,3,1)
        contenedor_basicos.addWidget(self.entrada_atributo,4,1)
        contenedor_basicos.addWidget(self.entrada_memoria,5,1)
        
        #Stats
        #Labels
        contenedor_stats.addWidget(self.texto_HP,0,0)
        contenedor_stats.addWidget(self.texto_Atk,1,0)
        contenedor_stats.addWidget(self.texto_Sp,2,0)
        contenedor_stats.addWidget(self.texto_Def,3,0)
        contenedor_stats.addWidget(self.texto_Int,4,0)
        contenedor_stats.addWidget(self.texto_Spd,5,0)
        #Entradas
        contenedor_stats.addWidget(self.entrada_HP,0,1)
        contenedor_stats.addWidget(self.entrada_Atk,1,1)
        contenedor_stats.addWidget(self.entrada_Sp,2,1)
        contenedor_stats.addWidget(self.entrada_Def,3,1)
        contenedor_stats.addWidget(self.entrada_Int,4,1)
        contenedor_stats.addWidget(self.entrada_Spd,5,1)
        
        #Boton
        contenedor_stats.addWidget(agregar,6,1)

        contenedor_grande.addWidget(self.imagen)

        contenedor_grande.addLayout(contenedor_basicos)
        contenedor_grande.addLayout(contenedor_stats)
        
        contenedor_grande.addWidget(self.lista)
        
        ventana = QWidget()
        ventana.setLayout(contenedor_grande)
        self.setCentralWidget(ventana)

    def agregar(self, id, nombre, stage, tipo, atributo, memoria, hp, sp, atk, df, Int, spd):
        mono = str(str(id) + ' ' + nombre + ' ' + stage + ' ' + tipo + ' ' + atributo + ' ' + str(memoria) + ' ' + str(hp) + ' ' + str(sp) + ' ' + str(atk) + ' ' + str(df) + ' ' + str(Int) + ' ' + str(spd))
        self.lista.addItem(mono)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()