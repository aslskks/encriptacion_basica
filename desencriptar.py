import os
from cryptography.fernet import Fernet
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt

class DesencriptadorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.archivo_encriptado_label = QLabel('Arrastra y suelta el archivo encriptado aquí:')
        layout.addWidget(self.archivo_encriptado_label)

        self.archivo_encriptado_input = QLineEdit()
        self.archivo_encriptado_input.setReadOnly(True)
        layout.addWidget(self.archivo_encriptado_input)

        self.archivo_desencriptado_label = QLabel('Nombre del archivo desencriptado:')
        self.archivo_desencriptado_input = QLineEdit()
        layout.addWidget(self.archivo_desencriptado_label)
        layout.addWidget(self.archivo_desencriptado_input)

        self.clave_label = QLabel('Clave en base64:')
        self.clave_input = QLineEdit()
        layout.addWidget(self.clave_label)
        layout.addWidget(self.clave_input)

        self.cargar_archivo_button = QPushButton('Cargar Archivo')
        self.cargar_archivo_button.clicked.connect(self.cargar_archivo)
        layout.addWidget(self.cargar_archivo_button)

        self.desencriptar_button = QPushButton('Desencriptar Archivo')
        self.desencriptar_button.clicked.connect(self.desencriptar_archivo)
        layout.addWidget(self.desencriptar_button)

        self.setLayout(layout)
        self.setWindowTitle('Desencriptador')
        self.setGeometry(100, 100, 400, 200)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.archivo_encriptado_input.setText(file_path)
        # Configura el nombre del archivo desencriptado al eliminar la extensión ".enc" del archivo encriptado
        self.archivo_desencriptado_input.setText(os.path.splitext(os.path.basename(file_path))[0])

    def cargar_archivo(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo Encriptado", "", "Archivos Encriptados (*.enc);;Todos los archivos (*)", options=options)
        if file_path:
            self.archivo_encriptado_input.setText(file_path)
            # Configura el nombre del archivo desencriptado al eliminar la extensión ".enc" del archivo encriptado
            self.archivo_desencriptado_input.setText(os.path.splitext(os.path.basename(file_path))[0])

    def desencriptar_archivo(self):
        archivo_entrada = self.archivo_encriptado_input.text()
        archivo_salida = os.path.join(os.path.dirname(archivo_entrada), self.archivo_desencriptado_input.text())
        clave = self.clave_input.text()

        try:
            fernet = Fernet(clave)

            with open(archivo_entrada, 'rb') as f_in:
                archivo_encriptado = f_in.read()

            archivo_desencriptado = fernet.decrypt(archivo_encriptado)

            with open(archivo_salida, 'wb') as f_out:
                f_out.write(archivo_desencriptado)

            QMessageBox.information(self, 'Éxito', 'Archivo desencriptado con éxito.')
            os.remove(archivo_entrada)
        except Exception as e:
            QMessageBox.critical(self, 'Error', 'Error al desencriptar el archivo: ' + str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DesencriptadorApp()
    window.setAcceptDrops(True)
    window.show()
    sys.exit(app.exec_())
