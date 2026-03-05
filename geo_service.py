# geo_service.py
import googlemaps
from datetime import datetime, timedelta


class GeoService:
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)
        # Diccionario para guardar consultas: {(origen, destino): (datos, timestamp)}
        self.cache = {}
        # Tiempo de vida del cache (ej. 24 horas)
        self.cache_ttl = timedelta(hours=24)

    def get_city_country(self, city_name):
        """
        Usa Google Geocoding API para obtener el país de una ciudad.
        Retorna el nombre del país ("Mexico", "United States", etc) o None si no se puede determinar.
        """
        try:
            geocode = self.gmaps.geocode(city_name)
            if geocode and 'address_components' in geocode[0]:
                for comp in geocode[0]['address_components']:
                    if 'country' in comp['types']:
                        return comp['long_name']
            return None
        except Exception as e:
            print(f"Error obteniendo país de ciudad: {e}")
            return None

    def validate_city(self, text):
        """
        Usa Google Places para asegurar que la ciudad existe y obtener su nombre oficial.
        """
        try:
            prediction = self.gmaps.places_autocomplete(
                input_text=text,
                types='(cities)'
            )
            if prediction:
                # Retorna el nombre formateado de la primera sugerencia
                return prediction[0]['description']
            return text
        except Exception as e:
            print(f"Error validando ciudad: {e}")
            return text

    def get_route_data(self, origin, destination):
        # 1. Crear una llave única para la ruta
        route_key = (origin.lower().strip(), destination.lower().strip())

        # 2. Verificar si está en cache y si aún es válido
        if route_key in self.cache:
            data, timestamp = self.cache[route_key]
            if datetime.now() - timestamp < self.cache_ttl:
                print(f"📦 [Cache Hit] Usando datos guardados para: {route_key}")
                return data
            else:
                print(f"⏰ [Cache Expired] Actualizando datos de Google...")

        # 3. Si no está en cache, llamar a la API de Google
        try:
            print(f"🌐 [API Call] Consultando Google Maps para: {route_key}")
            result = self.gmaps.distance_matrix(
                origins=origin,
                destinations=destination,
                mode="driving",
                units="metric",
                departure_time=datetime.now()
            )

            element = result['rows'][0]['elements'][0]

            if element['status'] == 'OK':
                route_data = {
                    "distance": round(element['distance']['value'] / 1000, 2),
                    "duration": round(element['duration_in_traffic']['value'] / 3600, 2) if 'duration_in_traffic' in element else round(element['duration']['value'] / 3600, 2),
                    "origin_full": result['origin_addresses'][0],
                    "dest_full": result['destination_addresses'][0]
                }

                # 4. Guardar en cache con el timestamp actual
                self.cache[route_key] = (route_data, datetime.now())
                return route_data

            return None
        except Exception as e:
            print(f"❌ Error en API: {e}")
            return None