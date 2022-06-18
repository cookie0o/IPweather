# imports
from requests import get
import socket

def get_ip():
    """
    Get the IP4 address of the user.
    """
    try:
        hostname=socket.gethostname()   
        ip_address=socket.gethostbyname(hostname)
        # return the IP address
        return ip_address

    # if the IP address is not found, return the error message
    except Exception as error:
        # return the error message
        return error


def get_weather(ip_address):
    """
    Get the weather from the user's IP address.
    """
    # get the weather from the IP address
    try:
        lat_long = get("http://ip-api.com/json/?fields=lat,lon&ip={}".format(ip_address))
        lat = lat_long.json()['lat']
        lon = lat_long.json()['lon']
        weather_raw = get(f"https://weatherdbi.herokuapp.com/data/weather/{lat},{lon}")
      
        
        resp_dict = weather_raw.json()
        resp_dict = resp_dict.get("currentConditions")
        weather = resp_dict.get("comment")
        


        # return the weather
        return weather
        
    # if the weather is not found, return the error message
    except Exception as error:
        # return the error message
        return error
