import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit
from cryptography.fernet import Fernet
import requests

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

        self.button_enviar_clave = QPushButton('Enviar Clave al Servidor')
        self.layout.addWidget(self.button_enviar_clave)

        self.input_clave = QLineEdit()
        self.input_clave.setPlaceholderText("Introduce la clave de encriptación")
        self.layout.addWidget(self.input_clave)

        self.button_encriptar.clicked.connect(self.seleccionar_archivo_encriptar)
        self.button_enviar_clave.clicked.connect(self.enviar_clave_al_servidor)

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
            os.remove(archivo_entrada)
            return clave.decode()
        except Exception as e:
            print("Error al encriptar el archivo:", str(e))
            return None

    def seleccionar_archivo_encriptar(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo para Encriptar", "", "Todos los archivos (*)", options=options)

        if file_path:
            clave = self.encriptar_archivo(file_path)
            if clave:
                self.input_clave.setText(clave)

    def enviar_clave_al_servidor(self):
        clave = self.input_clave.text()
        if clave:
            url = "http://127.0.0.1:5000"

            # Datos a enviar en el cuerpo de la solicitud (en este caso, un string vacío)
            data = clave

            # Enviar la solicitud POST
            try:
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    print("Solicitud enviada con éxito.")
                else:
                    print("Error al enviar la solicitud. Código de estado:", response.status_code)
            except Exception as e:
                print("Error al enviar la solicitud:", str(e))
            

def main():
    app = QApplication(sys.argv)
    encriptador = EncriptadorApp()
    encriptador.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
