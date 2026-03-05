import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyAsTP4yTb7j7XECoQcsBDMviooAv-v90P8")

try:
    result = gmaps.distance_matrix(
        origins="Tijuana, Mexico",
        destinations="Tlaquepaque, Mexico",
        mode="driving",
        units="metric",
        departure_time=datetime.now()
    )
    print("API call successful")
    print(result)
except Exception as e:
    print(f"Error: {e}")