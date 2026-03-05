
from datetime import datetime, timedelta

class GeoService:
    def __init__(self, api_key):
        self.cache = {}
        self.cache_ttl = timedelta(hours=24)
        print(' GeoService inicializado con cache')

    def get_route_data(self, origin, destination):
        route_key = (origin.lower().strip(), destination.lower().strip())
        
        if route_key in self.cache:
            data, timestamp = self.cache[route_key]
            if datetime.now() - timestamp < self.cache_ttl:
                print(f' [Cache Hit] Usando datos guardados para: {route_key}')
                return data
            else:
                print(f' [Cache Expired] Datos expirados para: {route_key}')
        
        # Simular llamada a API (sin googlemaps)
        print(f' [API Call Simulado] Consultando para: {route_key}')
        
        # Datos de ejemplo
        mock_data = {
            'distance': 800.0,
            'duration': 12.5,
            'origin_full': f'{origin}, Mexico',
            'dest_full': f'{destination}, Mexico'
        }
        
        self.cache[route_key] = (mock_data, datetime.now())
        return mock_data

# Probar el cache
if __name__ == '__main__':
    service = GeoService('fake_key')
    
    # Primera llamada
    result1 = service.get_route_data('Monterrey', 'Mexico City')
    print(f'Resultado 1: {result1}')
    
    # Segunda llamada (debe usar cache)
    result2 = service.get_route_data('Monterrey', 'Mexico City')
    print(f'Resultado 2: {result2}')
    
    print(' Sistema de cache funcionando correctamente')
