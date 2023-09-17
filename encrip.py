import random
import getpass
import base64
from cryptography.fernet import Fernet
import os

def encriptar_archivo(archivo, clave):
    with open(archivo, 'rb') as archivo_original:
        datos = archivo_original.read()

    fernet = Fernet(clave)
    datos_encriptados = fernet.encrypt(datos)

    archivo_encriptado = archivo + '.encrypted'
    with open(archivo_encriptado, 'wb') as archivo_destino:
        archivo_destino.write(datos_encriptados)

    print(f"El archivo {archivo} se ha encriptado correctamente como {archivo_encriptado}.")

    return archivo_encriptado

def desencriptar_archivo(archivo_encriptado, clave):
    with open(archivo_encriptado, 'rb') as archivo_encriptado:
        datos_encriptados = archivo_encriptado.read()

    fernet = Fernet(clave)
    try:
        datos_desencriptados = fernet.decrypt(datos_encriptados)
        archivo_original = archivo_encriptado.replace('.encrypted', '')
        with open(archivo_original, 'wb') as archivo_destino:
            archivo_destino.write(datos_desencriptados)
        print(f"El archivo {archivo_encriptado} se ha desencriptado correctamente como {archivo_original}.")
    except:
        print("¡Clave de desencriptación incorrecta!")
        return False

    return True

# Ruta al archivo que deseas encriptar
archivo_a_encriptar = 'a.txt'

# Generar una clave aleatoria de 32 bytes
clave_correcta = Fernet.generate_key()
nombre_archivo = "clave_deencriptacion"
try:
    with open(nombre_archivo, 'w') as archivo:
        # Escribe datos en el archivo
        archivo.write(clave correcta)
except IOError as e:
    print("Ocurrió un error al escribir en el archivo:", str(e)

# Codificar la clave utilizando Base64
clave_correcta_codificada = base64.urlsafe_b64encode(clave_correcta)

# Encriptar el archivo utilizando la clave decodificada
archivo_encriptado = encriptar_archivo(archivo_a_encriptar, clave_correcta)

intentos_maximos = 3
intentos = 0
desencriptado_exitoso = False

while intentos < intentos_maximos:
    clave_ingresada = getpass.getpass('Ingrese la clave de desencriptación: ')

    # Codificar la clave ingresada utilizando Base64
    clave_ingresada_codificada = base64.urlsafe_b64encode(clave_ingresada.encode())

    # Decodificar la clave ingresada
    clave_ingresada_decodificada = base64.urlsafe_b64decode(clave_ingresada_codificada)

    if clave_ingresada_decodificada == clave_correcta:
        desencriptado_exitoso = desencriptar_archivo(archivo_encriptado, clave_ingresada_decodificada)
        break
    else:
        intentos += 1
        print("Clave incorrecta. Inténtelo nuevamente.")

if not desencriptado_exitoso:
    print("Ha excedido el número máximo de intentos. El archivo será eliminado.")
    os.remove(archivo_encriptado)
