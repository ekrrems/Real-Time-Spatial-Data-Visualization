from geopy.geocoders import Nominatim

def address_to_coordinates(address):
    geolocator = Nominatim(user_agent='my_app')  # Initialize the geolocator object
    location = geolocator.geocode(address)  # Retrieve the location information for the address
    
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

# Example usage:
address = 'yesilkoy bakirkoy, istanbul'  # Replace with the address you want to convert
coordinates = address_to_coordinates(address)
if coordinates is not None:
    latitude, longitude = coordinates
    print(f"The coordinates of {address} are: Latitude = {latitude}, Longitude = {longitude}")
else:
    print(f"Unable to find the coordinates for {address}")