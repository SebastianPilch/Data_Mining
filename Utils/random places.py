# Importing necessary modules
import random

# Defining central coordinates for each city or region
cities = {
    "Warszawa": (52.2297, 21.0122),
    "Wrocław": (51.1079, 17.0385),
    "Kraków": (50.0614, 19.9366),
    "Poznań": (52.4064, 16.9252),
    "Gdańsk": (54.3520, 18.6466),
    "Łódź": (51.7592, 19.4550),
    "Katowice": (50.2599, 19.0216),  # Górny Śląsk
    "Lublin": (51.2465, 22.5684),
    "Bydgoszcz": (53.1235, 18.0084),
    "Szczecin": (53.4285, 14.5528),
    "Białystok": (53.1325, 23.1688),
    "Rzeszów": (50.0413, 21.9990),
}

# Setting distribution for locations
city_counts = {
    "Warszawa": 10,
    "Wrocław": 5,
    "Kraków": 5,
    "Poznań": 5,
    "Gdańsk": 5,
    "Łódź": 5,
    "Katowice": 10,  # Górny Śląsk
    "Lublin": 2,
    "Bydgoszcz": 2,
    "Szczecin": 2,
    "Białystok": 2,
    "Rzeszów": 2,
}

# Generate random coordinates around each city with small variations
locations_coords = {}
delta = 0.0135  # approximately 1.5 km

for city, count in city_counts.items():
    base_lat, base_lon = cities[city]
    for i in range(count):
        # Random shifts for latitude and longitude within ~1.5 km range
        lat = base_lat + (random.random() - 0.5) * 2 * delta
        lon = base_lon + (random.random() - 0.5) * 2 * delta
        # Adding unique key for each location
        location_key = f"{city}_{i+1}"
        locations_coords[location_key] = f"{lat}, {lon}"


print(locations_coords)

