
import json
from datetime import timedelta

# Abrir el archivo JSON
with open("myfile.json", "r") as json_file:
    ourjson = json.load(json_file)

# Extraer los valores
token = ourjson.get("token", "Token no encontrado")
tiempo_restante = ourjson.get("expires_in", 0)

# Convertir tiempo a formato hh:mm:ss
tiempo_formateado = str(timedelta(seconds=tiempo_restante))

# Imprimir resultados
print(f"Token encontrado: {token}")
print(f"Tiempo restante antes de caducar: {tiempo_formateado}")

