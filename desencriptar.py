import getpass
import base64
from cryptography.fernet import Fernet
datos_desencriptados = fernet.decrypt(datos_encriptados)
archivo_original = archivo_encriptado.replace('.encrypted', '')
with open(archivo_original, 'wb') as archivo_destino:
    archivo_destino.write(datos_desencriptados)
print(f"El archivo {archivo_encriptado} se ha desencriptado correctamente como {archivo_original}.")
