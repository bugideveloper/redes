import os
import time
import json
import platform
import random
import re
import requests
#método para listar archivos
regex = '''^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'''

#Function to return the public ip address
def get_public_ip():
    url = "https://ifconfig.me/ip"
    r = requests.get(url=url)
    data = r.text
    return data

def valid_ip(ip):
    if (re.search(regex,ip)):
        return True
    else:
        return False

def get_hostName():
    return platform.node()

def get_files(path):
        data=[]
        archivos = os.listdir(path)
        localNum = random.randint(0,10000)
        for archivo in archivos:
                a = {"id":localNum,"nombre":archivo, "tamano": str(os.path.getsize(archivo)), "fecha": time.ctime(os.path.getmtime(archivo)), "ubicacion": os.path.abspath(os.getcwd())}
                json_data = json.dumps(a)
                data.append(json_data)
                localNum+=1
        return data

def get_dirs(path):
        archivos = os.listdir(path)
        return archivos


def get_archivos(path):
    print("Obteniendo archivos del directorio local")
    path = path
    data = []
    archivos = os.listdir(path)
    for archivo in archivos:
        a = {'Archivo':archivo}
        data.append(a)
    retjson(data)

def get_tabla(path):
    print("Obteniendo archivos del directorio local")
    path = path
    data=[]
    archivos = os.listdir(path)
    for archivo in archivos:
        a = {"nombre":archivo, "tamano": str(os.path.getsize(archivo)), "fecha": time.ctime(os.path.getmtime(archivo)), "ubicacion": os.path.abspath(os.getcwd())}
        json_data = json.dumps(a)
        data.append(json_data)
    return data

#método para obtener el detalle de un archivo seleccionado
def get_detalle(path, archivo):
	data=[]
	a = {'Nombre': archivo, 'Ult_acceso': time.ctime(os.path.getatime(archivo)), 'Fecha_mod': time.ctime(os.path.getmtime(archivo)), 'Size': os.path.getsize(archivo)}
	data.append(a)
	retjson(data)

def retjson(cadena):
	python2json = json.dumps(cadena)
	print(python2json)

#llamadas a los métodos
#get_archivos(".")
#get_detalle(".","paisaje-1.jpg")
