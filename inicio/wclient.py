import asyncio
import websockets
import pickle
import random
from file_methods import *


async def hello():
    uri = "ws://127.0.0.1:5678"
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

asyncio.get_event_loop().run_until_complete(hello())