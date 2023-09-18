import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit
from cryptography.fernet import Fernet

class DesencriptadorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Desencriptador de Archivos')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel('Arrastra y suelta un archivo para desencriptar:')
        self.layout.addWidget(self.label)

        self.button_desencriptar = QPushButton('Seleccionar Archivo para Desencriptar')
        self.layout.addWidget(self.button_desencriptar)

        self.input_clave = QLineEdit()
        self.input_clave.setPlaceholderText("Introduce la clave de desencriptación")
        self.layout.addWidget(self.input_clave)

        self.button_desencriptar.clicked.connect(self.seleccionar_archivo_desencriptar)

        self.central_widget.setLayout(self.layout)

    def desencriptar_archivo(self, archivo_entrada, clave):
        try:
            fernet = Fernet(clave)

            with open(archivo_entrada, 'rb') as f_in:
                archivo_encriptado = f_in.read()

            # Obtener el nombre original eliminando la extensión .enc
            nombre_original, _ = os.path.splitext(os.path.basename(archivo_entrada))

            # Crear el nombre del archivo desencriptado con la extensión original
            archivo_salida = f"{nombre_original}"

            archivo_desencriptado = fernet.decrypt(archivo_encriptado)

            with open(archivo_salida, 'wb') as f_out:
                f_out.write(archivo_desencriptado)

            print("Archivo desencriptado con éxito y guardado como:", archivo_salida)
            os.remove(archivo_entrada)
        except Exception as e:
            print("Error al desencriptar el archivo:", str(e))

    def seleccionar_archivo_desencriptar(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo para Desencriptar", "", "Archivos Encriptados (*)", options=options)

        if file_path:
            clave = self.input_clave.text()  # Obtener la clave de desencriptación ingresada por el usuario
            if clave:
                self.desencriptar_archivo(file_path, clave)
            else:
                print("Debes ingresar la clave de desencriptación.")

def main():
    app = QApplication(sys.argv)
    desencriptador = DesencriptadorApp()
    desencriptador.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
