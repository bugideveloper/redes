import requests 
import json
from file_methods import *
import time
import random
import os
# defining the api-endpoint  
API_URL = "http://127.0.0.1:8000/api/archivo/"

print("Host "+str(get_hostName()))

#Save the list of files allocated locally
def save_local(path):
        f = open("localFiles.txt","a")
        archivos = get_dirs(path)
        for archivo in archivos:
                print(archivo)
                f.write(archivo+"\n")
        f.close()
        return archivos

def save_local_json(path):
        f = open("localJsonFiles.txt","a")
        archivos = get_files(path)
        for archivo in archivos:
                print(archivo)
                f.write(archivo)
        f.close()
        return archivos

def read_file(fileName):
        files = open(fileName,"r")
        #print(file.read())
        lista= files.readlines()
        files.close()
        return lista


def start_client(path):
        if os.path.isfile('localJsonFiles.txt') and os.path.isfile('localFiles.txt'):
                print("Sending Date with local data")
                print("Reading previous files")
                lista = set(read_file("localFiles.txt"))
                nuevalista = set(get_dirs(path))
                print("Lista de archivos")
                print(lista)
                print("Nueva Lista")
                print(nuevalista)
        else:
                print("File does not exist generating one")
                save_local(path)
                archivos = save_local_json(path)
                print("Sending json data to the server")
                for archivo in archivos:
                        print(archivo)
                        r = requests.post(url = API_URL,headers={"content-type":"application/json"} ,data = archivo)
                        if (r.status_code == 201):
                                print("Se creo la informacion")
                        else:
                                print("La información no se envio")



#start_client(".")
"""
f = open("files.txt","a")
archivos = get_files(".")
simpledirs = get_dirs(".")

for archivo in archivos:
        print(archivo)
        f.write(archivo+"\n")
        
        #r = requests.post(url = API_URL,headers={"content-type":"application/json"} ,data = archivo)
        #if (r.status_code == 201):
        #        print("Se creo la informacion")
        #else:
        #        print("La información no se envio")
f.close()
"""