import requests
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Acceder a la variable
proxie_key = os.getenv('proxie_key')

# Configuración del proxy
proxies = {
                "https": proxie_key
            }

# Función para realizar la búsqueda con requests
def search_artist_ticketmaster(query):
    # Búsqueda de los artistas con el input del usuario en el buscador
    url = f"https://www.ticketmaster.es/api/search/search-suggest?q={query}"
    
    # Configuración de headers para simular un navegador real
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Referer": "https://www.ticketmaster.es/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
    }
    
    # Hacemos la solicitud con el proxy
    response = requests.get(url, headers=headers, proxies=proxies)

    # Verificamos si la respuesta fue exitosa
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Request failed", "status_code": response.status_code}

# Función para realizar la búsqueda con requests
def get_artist_information(url):    
    # Configuración de headers para simular un navegador real
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Referer": "https://www.ticketmaster.es/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"
    }
    
    # Realizamos la solicitud GET a la URL
    response = requests.get(url, headers=headers, proxies=proxies)

    # Verificamos si la respuesta fue exitosa
    if response.status_code == 200:
        # Usamos BeautifulSoup para parsear el HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscamos el <script> que contiene el JSON
        script_tag = soup.find('script', type="application/ld+json")
        
        if script_tag:
            try:
                # Intentamos convertir el contenido del script en un objeto JSON
                json_data = json.loads(script_tag.string)
                print("aa")
                return json_data
            except json.JSONDecodeError:
                return {"error": "Error al parsear JSON desde el script"}
        else:
            return {"error": "No se encontró el script con el JSON"}
    
    else:
        print("error 2")
        return {"error": "Request failed", "status_code": response.status_code}