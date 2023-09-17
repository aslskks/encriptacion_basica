print("no se puedo perdon\con clave si")
p1 = input("quieres usar clave s/n: ").lower()
if p1 == "si" or "s":
	pass
else:
	exit()
import getpass
import base64
from cryptography.fernet import Fernet

# Clave secreta que se utiliza para desencriptar
clave_secreta = getpass.getpass("Ingresa la clave secreta: ").encode()

# Datos encriptados que quieres desencriptar
datos_encriptados = input("Ingresa los datos encriptados: ").encode()

# Inicializa el objeto Fernet con la clave secreta
fernet = Fernet(base64.urlsafe_b64encode(clave_secreta))

# Desencripta los datos
datos_desencriptados = fernet.decrypt(datos_encriptados)

# Puedes guardar los datos desencriptados en un archivo si es necesario
nombre_archivo = input("Ingresa el nombre del archivo destino (sin extensión): ")
nombre_archivo_destino = nombre_archivo + ".decrypted"

with open(nombre_archivo_destino, 'wb') as archivo_destino:
    archivo_destino.write(datos_desencriptados)

print("Datos desencriptados y guardados en", nombre_archivo_destino)
