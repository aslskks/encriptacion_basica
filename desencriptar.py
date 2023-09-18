from cryptography.fernet import Fernet

def desencriptar_archivo(archivo_entrada, archivo_salida, clave):
    try:
        fernet = Fernet(clave)
        
        with open(archivo_entrada, 'rb') as f_in:
            archivo_encriptado = f_in.read()

        archivo_desencriptado = fernet.decrypt(archivo_encriptado)

        with open(archivo_salida, 'wb') as f_out:
            f_out.write(archivo_desencriptado)

        print("Archivo desencriptado con éxito. perro")
    except Exception as e:
        print("Error al desencriptar el archivo:", str(e))

# Reemplaza 'ruta_del_archivo_encriptado' con la ubicación de tu archivo encriptado
ruta_del_archivo_encriptado = f'{input("nombre del archivo encriptado en la misma carpeta: ")}.enc'
# Reemplaza 'ruta_del_archivo_desencriptado' con la ubicación donde deseas guardar el archivo desencriptado
ruta_del_archivo_desencriptado = "archivodesencriptado"
# Reemplaza 'tu_clave_en_base64' con la clave en base64 que se utilizó para encriptar el archivo
clave = input("clave: ")
tu_clave_en_base64 = clave

# Llama a la función de desencriptación
desencriptar_archivo(ruta_del_archivo_encriptado, ruta_del_archivo_desencriptado, tu_clave_en_base64)
