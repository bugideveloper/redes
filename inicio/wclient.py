import asyncio
import websockets.exceptions
import websockets
import pickle
import random
from file_methods import *


"""
async def hello(server_ip):
    try:
        uri = "ws://"+server_ip+":5678"
        async with websockets.connect(uri) as websocket:
            while True:
                ip = get_public_ip()
                archivos = get_files(".")
                archivos.insert(0,ip)
                #Here we have the same of files
                lista = pickle.dumps(archivos)
                print("List of files")
                print(archivos)
                await websocket.send(lista)
                await asyncio.sleep(random.random() * 5)
                await websocket.recv()
    except websockets.ConnectionClosedError:
        print("No se pudo conectar con el servidor "+(server_ip))
"""

async def hello(server_ip):
    uri = "ws://"+server_ip+":5678"
    async with websockets.connect(uri) as websocket:
        while True:
            ip = get_public_ip()
            archivos = get_files(".")
            archivos.insert(0,ip)
            #Here we have the same of files
            lista = pickle.dumps(archivos)
            print("List of files")
            print(archivos)
            await websocket.send(lista)
            await asyncio.sleep(random.random() * 5)
            await websocket.recv()



#asyncio.get_event_loop().run_until_complete(hello(default_server))

def start_connection(default_server,position):
    try:
        #default_server = '192.168.0.6'
        asyncio.get_event_loop().run_until_complete(hello(default_server))
    except (websockets.ConnectionClosedError,ConnectionRefusedError):
        try:
            print("No se pudo conectar con el servidor "+(default_server))
            position += 1
            print("Conectandose al siguiente server "+lista_ips[position])
            start_connection(lista_ips[position],position)
        except IndexError:
            print("Connection Closed there is no server to connect!")
        #next_server = ips[1]
        #print("Connecting to another server "+(next_server))
        #start_connection(next_server)


lista_ips = ['127.0.0.1','192.168.0.6','192.168.0.8'] #Lista regresada por el server master
#default_server = '192.168.0.6'
server_position = 0 #Servidor inicial - This help me check what is the current server
start_connection(lista_ips[server_position],server_position)
#print(lista_ips[0])

        #asyncio.get_event_loop().run_until_complete(hello(ips[1]))
