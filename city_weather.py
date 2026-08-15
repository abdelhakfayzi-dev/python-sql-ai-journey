import requests
def read_cities(filename):
    with open(filename, 'r') as f:
        cities = [line.strip() for line in f if line.strip()]
    return cities
def get_coordinates(city):
    coords = {
        "Casablanca": (33.5731, -7.5898),
        "Rabat": (34.0209, -6.8416),
        "Marrakech": (31.6295, -7.9811),
        "Oujda": (34.6851, -1.9082),
        "Agadir": (30.4278, -9.5981)
    }
    return coords.get(city,(0, 0))
def fetch_weather(lat,lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['current_weather']['temperature']
        wind = data['current_weather']['windspeed']
        return temp, wind
    else:
        return None, None
def print_report(city, temp, wind):
    if temp is not None:
        print(f"{city}: {temp}°C, Wind: {wind} km/h")
    else:
        print(f"{city}: Data unavailable")
def main():
    cities = read_cities('cities.txt')
    print("=== WEATHER REPORT ===")
    for city in cities:
        lat, lon = get_coordinates(city)
        temp, wind = fetch_weather(lat, lon)
        print_report(city, temp, wind)
if __name__ == "__main__":
        main()