import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog
from cryptography.fernet import Fernet

class EncriptadorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Encriptador de Archivos')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel('Arrastra y suelta un archivo para encriptar:')
        self.layout.addWidget(self.label)

        self.button_encriptar = QPushButton('Seleccionar Archivo para Encriptar')
        self.layout.addWidget(self.button_encriptar)

        self.button_encriptar.clicked.connect(self.seleccionar_archivo_encriptar)

        self.central_widget.setLayout(self.layout)

    def encriptar_archivo(self, archivo_entrada):
        try:
            clave = Fernet.generate_key()  # Generar una clave Fernet

            with open(archivo_entrada, 'rb') as f_in:
                archivo_original = f_in.read()

            # Obtener el nombre y la extensión del archivo original
            nombre_original, extension = os.path.splitext(os.path.basename(archivo_entrada))

            # Crear el nombre del archivo encriptado con la extensión original y extensión .enc
            archivo_salida = f"{nombre_original}{extension}.enc"

            fernet = Fernet(clave)
            archivo_encriptado = fernet.encrypt(archivo_original)

            with open(archivo_salida, 'wb') as f_out:
                f_out.write(archivo_encriptado)

            print("Archivo encriptado con éxito y guardado como:", archivo_salida)
            print("Clave de encriptación:", clave.decode())  # Mostrar la clave generada
            os.remove(archivo_entrada)
        except Exception as e:
            print("Error al encriptar el archivo:", str(e))

    def seleccionar_archivo_encriptar(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo para Encriptar", "", "Todos los archivos (*)", options=options)

        if file_path:
            self.encriptar_archivo(file_path)

def main():
    app = QApplication(sys.argv)
    encriptador = EncriptadorApp()
    encriptador.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
