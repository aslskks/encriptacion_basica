from flask import Flask, request

app = Flask(__name__)

@app.route('/guardar_clave', methods=['GET'])
def guardar_clave():
    clave = request.args.get('clave')

    # Guardar la clave en un archivo
    with open('log.txt', 'w') as archivo:
        archivo.write(clave)

    return 'Clave recibida y guardada con éxito en el servidor.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
