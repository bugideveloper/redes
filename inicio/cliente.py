import requests 
import json 
# defining the api-endpoint  
API_URL = "http://127.0.0.1:8000/api/archivo/"
  
id = 2
nombre = "Image.JPG"
tamano = "7222"
fecha = "2020-04-24T03:56:07.840869"
ubicacion = "/home/users/Desktop/"

# Add files to a database
data = {'nombre':nombre, 
        'tamano':tamano, 
        'fecha':fecha, 
        'ubicacion':ubicacion} 

json_data = json.dumps(data)
print(json_data) 
# sending post request and saving response as response object 
r = requests.post(url = API_URL,headers={"content-type":"application/json"} ,data = json_data)
#r = requests.post(url = API_URL, data = data) 

print(r.status_code)
# extracting response text  
#pastebin_url = r.text 
print("The query is done") 
