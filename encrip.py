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

        self.label = QLabel('Arrastra y suelta un archivo para encriptar perro:')
        self.layout.addWidget(self.label)

        self.button = QPushButton('Seleccionar Archivo')
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.seleccionar_archivo)

        self.central_widget.setLayout(self.layout)

    def encriptar_archivo(self, archivo_entrada, archivo_salida, clave):
        try:
            with open(archivo_entrada, 'rb') as f_in:
                data = f_in.read()

            fernet = Fernet(clave)
            archivo_encriptado = fernet.encrypt(data)

            with open(archivo_salida, 'wb') as f_out:
                f_out.write(archivo_encriptado)

            print("Archivo encriptado con éxito.")
            os.remove(archivo_entrada)
        except Exception as e:
            print("Error al encriptar el archivo:", str(e))

    def seleccionar_archivo(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "Todos los archivos (*)", options=options)

        if file_path:
            clave = Fernet.generate_key()  # Generar una clave Fernet
            archivo_salida, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo Encriptado", "", "Archivos Encriptados (*.enc)")

            if archivo_salida:
                self.encriptar_archivo(file_path, archivo_salida, clave)
                print("Clave de encriptación:", clave.decode())  # Mostrar la clave generada
            else:
                print("Debe seleccionar un nombre de archivo válido para guardar el archivo encriptado.")

def main():
    app = QApplication(sys.argv)
    encriptador = EncriptadorApp()
    encriptador.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
