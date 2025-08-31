# 🎵 ATD - Conciertos + Alojamiento + Tiempo

Aplicación desarrollada en el marco de la asignatura **Adquisición y Transmisión de Datos** del Doble Grado en Ciencia de Datos e Ingeniería de Organización Industrial (UPV).

Permite buscar conciertos (Ticketmaster), alojamientos cercanos (Booking.com) y consultar el tiempo (Open-Meteo) para la fecha del evento. Todo desde una única interfaz web en Flask.

## 🚀 Instalación rápida

Clona el repositorio y accede a la carpeta:

```bash
git clone https://github.com/mgiljimenez/scraping-atd-upv.git
cd scraping-atd-upv
```

Crea un entorno virtual e instálalo:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Crea un archivo `.env` con la variable proxie_key=""

## ▶️ Ejecución

Inicia la aplicación Flask:

```bash
python3 app.py
```

Accede desde tu navegador a:  
📍 `http://localhost:8000`

## 🌐 Producción

Desplegado en VPS (OVH Cloud) con Nginx, SSL (Let’s Encrypt) y systemd. 
Actualmente no se da soporte a este proyecto y se dio de baja dicho servidor
🔗 https://atd.rastrer.com 

---

© UPV · Proyecto académico con fines demostrativos
