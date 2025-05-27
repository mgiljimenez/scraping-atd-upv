from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus
from datetime import datetime, timedelta
import time
import json

def search_booking(calle, cp, checkin, num_adultos, num_ninos, num_habitaciones):
    options = webdriver.ChromeOptions()

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
    options.add_argument("--lang=es-ES,es")
    options.add_argument("--start-maximized")
    options.add_argument("--enable-automation")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")

    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    direccion = f"{calle}, {cp}"
    direccion_codificada = quote_plus(direccion)

    checkin_datetime = datetime.fromisoformat(checkin)
    checkout_datetime = checkin_datetime + timedelta(days=1)

    checkin_str = checkin_datetime.strftime('%Y-%m-%d')
    checkout_str = checkout_datetime.strftime('%Y-%m-%d')


    try:
        url = (
        f"https://www.booking.com/searchresults.es.html"
        f"?ss={direccion_codificada}"
        f"&checkin={checkin_str}"
        f"&checkout={checkout_str}"
        f"&group_adults={num_adultos}"
        f"&group_children={num_ninos}"
        f"&no_rooms={num_habitaciones}"
        )
        print(url)
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        time.sleep(3)

        html = driver.page_source

        aceptar_boton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        aceptar_boton.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="property-card"]')))

        apartamentos = []
        resultados = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        n = 0

        for apartamento in resultados:
            if n >= 5:
                break
            try:
                mensaje = apartamento.find_element(By.CSS_SELECTOR, 'p.b99b6ef58f.c8075b5e6a')
                if "no tiene disponibilidad" in mensaje.text.lower():
                    continue
            except:
                pass

            try:
                nombre = apartamento.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text
                precio = apartamento.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').text
                valoracion = apartamento.find_element(By.CSS_SELECTOR, 'div.f63b14ab7a.dff2e52086').text
                url_imagen = apartamento.find_element(By.CSS_SELECTOR, 'img[data-testid="image"]').get_attribute('src')
                try:
                    enlace = apartamento.find_element(By.CSS_SELECTOR, 'a[data-testid="availability-cta-btn"]').get_attribute('href')
                except Exception as e:
                    print(e)
                    enlace = None
                apartamentos.append({"nombre":nombre, "precio":precio, "valoración":valoracion, "url imagen":url_imagen, "enlace":enlace})
                n += 1
            except Exception as e:
                print(e)
                continue

        return apartamentos

    except Exception as e:
        print("Ocurrió un error:", e)