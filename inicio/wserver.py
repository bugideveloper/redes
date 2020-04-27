import asyncio
import datetime
import random
import websockets
import pickle
from file_methods import *
import json

class SocketServer(object):
    def __init__(self):
        self.mensaje = list()
        self.serversIP = list()
        self.websockets = list()
        
    async def time(self,websocket, path):
        while True:
            print("Buscando archivos")
            if self.mensaje is not None:
                for archivo in self.mensaje:
                    await websocket.send(json.dumps(archivo))
                await asyncio.sleep(random.random() * 5)
            #archivos = get_archivos("127.0.0.1",".")
            #for archivo in archivos:
                #await websocket.send(self.mensaje) 
            #    await websocket.send(archivo)    
            #await asyncio.sleep(random.random() * 3)
    
    async def echo(self,websocket, path):
        print("Printing an echo request")
        async for message in websocket:            
            archivos = pickle.loads(message)

            if archivos[0] not in self.serversIP and valid_ip(archivos[0]):
                self.websockets.append(websocket)
                print("The ip address is valid")
                print("IP address has been added "+str(archivos[0]))
                print(archivos)
                self.serversIP.append(archivos[0])
                self.mensaje.append(archivos)
            elif archivos[0] in self.serversIP and valid_ip(archivos[0]):
                print("Updateing data for "+archivos[0])
                self.mensaje.append(archivos)
                print("Enviando datos al cliente")
                lista = pickle.dumps(self.serversIP)
                
                await asyncio.wait([websocket.send(lista) for user in self.websockets])
                #await asyncio.wait([websocket.send(json.dumps(self.serversIP)) for user in self.websockets])
                #await asyncio.wait([websocket.send(self.serversIP) for user in self.websockets])

            #print("List of ip address added")
            #print(archivos[0])
            #self.mensaje = archivos
            #self.mensaje = "127.0.0.1"
    
    async def handler(self,websocket, path):
        consumer_task = asyncio.ensure_future(
            self.echo(websocket, path))
        producer_task = asyncio.ensure_future(
            self.time(websocket, path))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
    
    def start_all(self):
        start_server = websockets.serve(self.handler, "192.168.0.6", 5678)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


server = SocketServer()
server.start_all()


