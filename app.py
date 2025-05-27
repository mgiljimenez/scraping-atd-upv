import os
import requests
from flask import Flask, render_template, request, jsonify
from config.ticketmaster import search_artist_ticketmaster, get_artist_information
from config.booking import search_booking
from config.weather import get_weather

# Configuración de la aplicación Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q')
    results = search_artist_ticketmaster(query)
    return jsonify(results)

@app.route('/api/artist')
def artist_info():
    query = request.args.get('url')
    results = get_artist_information(query)
    return jsonify(results)

@app.route('/api/weather')
def weather_info():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    date = request.args.get('date')

    if not latitude or not longitude or not date:
        return jsonify({"error": "Missing required parameters: latitude, longitude, date"}), 400

    try:
        response = get_weather(latitude, longitude, date)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/booking')
def get_booking():
    calle = request.args.get('calle')
    cp = request.args.get('cp')
    checkin = request.args.get('checkin')
    num_adultos = request.args.get('num_adultos')
    num_ninos = request.args.get('num_ninos')
    num_habitaciones = request.args.get('num_habitaciones')

    results = search_booking(calle, cp, checkin, num_adultos, num_ninos, num_habitaciones)
    return jsonify(results)


# Ejecutar la app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)