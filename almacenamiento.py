# ALMACENAMIENTO EN DISCO DE LA INFORMACIÓN TRANSACCIONAL

# Se importa la librería de JSON que permite a Python manejar el formato
import json

# Es importante reconocer que el FILE_NAME no captura solo el nombre sino la,
# ruta en el sistema, en este caso, al tener solo un nombre se guardará al
# nivel del repositorio local.

FILE_NAME = "datos.json"

def save_data(history: list) -> bool:
    """
        La función save_data(...) es la encargada de guardar en el disco duro
        la información transaccional en memoria.
    """

    try:
        # Este es el Context Manager
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            # La sentencia with genera un entorno seguro para bautizar el archivo
            # temporalmente como file, ejecutar la identación y cerrar el archivo al terminar.
            # "w" es el modo escritura de naturaleza destructiva/creativa. 
            # "utf-8" es el estándar de escritura para hispanohablantes
            json.dump(history, file, indent=4)
            # Esta es la herramienta nativa de la librería JSON. Toma la lista de la memoria,
            # la traduce a JSON y la guarda en el archivo abierto "file". El parametro
            # "indent" indica los espacios de sangría al archivo para facilitar la visualización.
            
            # Si todo se ejecuta satisfactoriamente, se retornará un booleano satisfactorio.
        return True
    
    except Exception:
        return False


def load_data() -> list:
    """
        La función load_data() es la designada a recuperar del disco duro la
        información transaccional para manejarla en memoria.
    """

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            # "r" es el modo de lectura, por tanto, solo permite ver o extraer.
            return json.load(file)
            # La función load(archivo) toma el texto estructurado JSON y lo transforma
            # en la lista de diccionarios de Python lista para ser consumida por
            # la lista (transaction_history).
        
    except FileNotFoundError:
        # Manejo de error para cuando el archivo no existe.
        return []

    except json.JSONDecodeError:
        # Manejo de error para cuando el formato JSON se corrompe.
        return []