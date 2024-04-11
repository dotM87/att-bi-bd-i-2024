import os
import json
from pymongo import MongoClient

# Obtener la ruta del directorio actual
directorio_actual = os.path.dirname(__file__)

# Construir la ruta al archivo data.json
ruta_data_json = os.path.join(directorio_actual, 'driver', 'data.json')
# Cargar datos desde el archivo JSON
with open(ruta_data_json, 'r') as file:
    data = json.load(file)

# Conectar a MongoDB Atlas
client = MongoClient("mongodb+srv://m87:triaina@cluster0.ztxjdbr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["att-prueba"]
collection = db["tarifas-internet-fijo"]

# Insertar los datos en la base de datos
collection.insert_many(data)
print(data)
print("--------------------------------------------------------------")
print("Datos insertados en la base de datos")
