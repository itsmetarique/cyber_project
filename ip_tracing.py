import requests
def geolocate_ip(ip_address):
    location = geocoder.ip(ip_address)
    return location

def main():
    target_ip = "193.56.**.*"  # Replace with the IP address you want to geolocate
    location = geolocate_ip(target_ip)

    print("IP Address:", location.ip)
    print("City:", location.city)
    print("Region:", location.state)
    print("Country:", location.country)
    print("Latitude:", location.latlng[0])
    print("Longitude:", location.latlng[1])

if __name__ == "__main__":
    main()

import geocoder

def reverse_geocode(latitude, longitude):
    location = geocoder.reverse_geocode(latitude, longitude)
    return location

def main():
    target_latitude = 37.7749  # Replace with the latitude
    target_longitude = -122.4194  # Replace with the longitude
    location = reverse_geocode(target_latitude, target_longitude)

    print("City:", location.city)
    print("Region:", location.state)
    print("Country:", location.country)
    print("Postal Code:", location.postal)
    print("Address:", location.address)

if __name__ == "__main__":
    main()
Keep in mind that geolocation accuracy can vary based on the data sources and services used. Some services might provide more accurate results in certain regions or for specific types of IP addresses. It's important to review the terms of use and limitations of the geolocation service you choose.






def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    target_ip = "8.8.8.8"  # Replace with the IP address you want to trace
    ip_info = get_ip_info(target_ip)

    print("IP Address:", ip_info["ip"])
    print("Hostname:", ip_info.get("hostname", "N/A"))
    print("City:", ip_info.get("city", "N/A"))
    print("Region:", ip_info.get("region", "N/A"))
    print("Country:", ip_info.get("country", "N/A"))
    print("ISP:", ip_info.get("org", "N/A"))
    print("Location:", ip_info.get("loc", "N/A"))

if __name__ == "__main__":
    main()
