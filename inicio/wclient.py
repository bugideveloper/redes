import asyncio
import websockets.exceptions
import websockets
import pickle
import random
from file_methods import *

class SocketClient(object):
    def __init__(self):
        self.serversIP = list()
        self.defaultServer = "127.0.0.1"
    
    def set_defaultServer(self,serverip):
        self.defaultServer = serverip
    
    def get_defaultServer(self):
        return self.defaultServer
    
    def get_serversIP(self):
        return self.serversIP
    
    #This function sends the data to the server
    async def hello(self,server_ip,path):
        uri = "ws://"+server_ip+":5678"
        async with websockets.connect(uri) as websocket:
            while True:
                ip = get_public_ip()
                archivos = get_files(path)
                archivos.insert(0,ip)
                #Here we have the same of files
                lista = pickle.dumps(archivos)
                await websocket.send(lista)
                await asyncio.sleep(random.random() * 5)
                mensaje = await websocket.recv()
                if mensaje.__class__.__name__ == 'bytes':
                    print("The data type receive from the server is "+str(type(mensaje)))
                    listas_ips_nuevas = pickle.loads(mensaje)
                    print("Printing the list the server ip address")
                    
                    for ip in listas_ips_nuevas:
                        print("Current IP: -> "+str(ip))
                        if ip not in self.serversIP:
                            print("Adding a server ip address")
                            self.serversIP.append(ip)
                print("Current Available Server")
                print(self.serversIP)
                #print(mensaje.__class__.__name__)
                #print("Mensaje recibido del servidor "+str(mensaje))
                #self.websocket = websocket
    
    #Function to receive data from the server
    async def echo(self,websocket):
        print("Printing an echo request")
        async for message in websocket:            
            archivos = pickle.loads(message)
            print("Datos recibidos del servidor")
            print(archivos)
    
    #Function to handle everything here
    async def handler(self,server_ip):
        consumer_task = asyncio.ensure_future(
            self.hello(server_ip))
        producer_task = asyncio.ensure_future(
            self.echo())
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()


    def start_connection(self,default_server,position,path):
        try:
            #default_server = '192.168.0.6'
            #Here goes the handler function
            asyncio.get_event_loop().run_until_complete(self.hello(default_server,path))
            #asyncio.get_event_loop().run_until_complete(self.handler(default_server))
        except (websockets.ConnectionClosedError,ConnectionRefusedError,TimeoutError):
            try:
                print("No se pudo conectar con el servidor "+(default_server))
                position += 1
                print("Conectandose al siguiente server "+self.serversIP[position])
                self.start_connection(self.serversIP[position],position,path)
            except IndexError:
                print("Connection Closed there is no server to connect!")
        #next_server = ips[1]
        #print("Connecting to another server "+(next_server))
        #start_connection(next_server)



#default_server = '192.168.0.6'
server_position = 0
client =  SocketClient()
#path = "C:/Users/theme/Desktop/thesis"

#path = "./../"
path = "C:/Users/theme/Desktop/"

client.start_connection(client.get_defaultServer(),server_position,path)
#client.start_connection(lista_ips[server_position],server_position)
#print(lista_ips[0])

        #asyncio.get_event_loop().run_until_complete(hello(ips[1]))
