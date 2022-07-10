# imports
from requests import get
import socket

"""
Thanks to: communication.with.users@gmail.com for this great free weather API!
Github   : https://github.com/cookie0o
dev      : cookie0_o
"""

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
            print ("GET IP ERROR:")
            return error

class weather():

    def IP        (ip_address,  current_weather, location, tempC, humidity, windKMH, day_hour):
        """
        Get the weather from the user's IP address.
        """
        try:
            lat_long = get("http://ip-api.com/json/?fields=lat,lon&ip={}".format(ip_address))
            lat = lat_long.json()['lat']
            lon = lat_long.json()['lon']
            weather_raw = get(f"https://weatherdbi.herokuapp.com/data/weather/{lat},{lon}")
                
                
            # check if weather api is working
            if weather_raw.status_code == 200:
                # get the weather data
                weather_json = weather_raw.json()
            else:
                # return the error message
                print ("WEATHER API ERROR:")
                return weather_raw.status_code

            # check if ip get lat long api is working
            if lat_long.status_code == 200:
                # get the lat long data
                lat_long_json = lat_long.json()
            else:
                # return the error message
                print ("IP GET LAT,LONG API ERROR:")
                return lat_long.status_code
            

            # empty list to return the weather
            values = []

            # check if "current_weather" = True:
            if current_weather == True:
                weather = weather_json.get("currentConditions")
                weather = weather.get("comment")
                # add the weather to the list
                values.append(weather)

            # check if "location" = True:
            if location == True:
                location = weather_json.get("region")
                # add the location to the list
                values.append(location)

            # check if "tempC" = True:
            if tempC == True:
                tempC = weather_json.get("currentConditions")
                tempC = tempC.get("temp")
                tempC = tempC.get("c")
                tempC = str(tempC) + "°C"
                # add the temperature to the list
                values.append(tempC)

            # check if "humidity" = True:
            if humidity == True:
                humidity = weather_json.get("currentConditions")
                humidity = humidity.get("humidity")
                # add the humidity to the list
                values.append(humidity)

                
            # check if "windKMH" = True:
            if windKMH == True:
                windKMH = weather_json.get("currentConditions")
                windKMH = windKMH.get("wind")
                windKMH = windKMH.get("km")
                windKMH = str(windKMH) + "km/h"#
                # add the wind speed to the list
                values.append(windKMH)

            # check if "day_hour" = True:
            if day_hour == True:
                day_hour = weather_json.get("currentConditions")
                day_hour = day_hour.get("dayhour")
                # add the day and hour to the values list
                values.append(day_hour)


            # return the true values
            return values
            
            
        # if the weather is not found, return the error message
        except Exception as error:
            # return the error message
            print ("GET WEATHER ERROR:")
            return error

    def LOCATION  (location,    current_weather, tempC, humidity, windKMH, day_hour):
        """
        Get the weather from the input location
        """
        try:
            weather_raw = get(f"https://weatherdbi.herokuapp.com/data/weather/{location}")

            # check if weather api is working
            if weather_raw.status_code == 200:
                # get the weather data
                weather_json = weather_raw.json()
            else:
                # return the error message
                print ("WEATHER API ERROR:")
                return weather_raw.status_code


            # empty list to return the weather
            values = []

            # check if "current_weather" = True:
            if current_weather == True:
                weather = weather_json.get("currentConditions")
                weather = weather.get("comment")
                # add the weather to the list
                values.append(weather)

            # check if "tempC" = True:
            if tempC == True:
                tempC = weather_json.get("currentConditions")
                tempC = tempC.get("temp")
                tempC = tempC.get("c")
                tempC = str(tempC) + "°C"
                # add the temperature to the list
                values.append(tempC)

            # check if "humidity" = True:
            if humidity == True:
                humidity = weather_json.get("currentConditions")
                humidity = humidity.get("humidity")
                # add the humidity to the list
                values.append(humidity)

                
            # check if "windKMH" = True:
            if windKMH == True:
                windKMH = weather_json.get("currentConditions")
                windKMH = windKMH.get("wind")
                windKMH = windKMH.get("km")
                windKMH = str(windKMH) + "km/h"#
                # add the wind speed to the list
                values.append(windKMH)

            # check if "day_hour" = True:
            if day_hour == True:
                day_hour = weather_json.get("currentConditions")
                day_hour = day_hour.get("dayhour")
                # add the day and hour to the values list
                values.append(day_hour)


            # return the true values
            return values
            

        # if the weather is not found, return the error message
        except Exception as error:
            # return the error message
            print ("GET WEATHER ERROR:")
            return error

    def LAT_LONG  (LAT, LONG,   current_weather, location, tempC, humidity, windKMH, day_hour):
        """
        Get the weather from the input lat and long coordinates
        """
        try:
            weather_raw = get(f"https://weatherdbi.herokuapp.com/data/weather/{LAT},{LONG}")

            # check if weather api is working
            if weather_raw.status_code == 200:
                # get the weather data
                weather_json = weather_raw.json()
            else:
                # return the error message
                print ("WEATHER API ERROR:")
                return weather_raw.status_code


            # empty list to return the weather
            values = []

            # check if "current_weather" = True:
            if current_weather == True:
                weather = weather_json.get("currentConditions")
                weather = weather.get("comment")
                # add the weather to the list
                values.append(weather)

            # check if "location" = True:
            if location == True:
                location = weather_json.get("region")
                # add the location to the list
                values.append(location)

            # check if "tempC" = True:
            if tempC == True:
                tempC = weather_json.get("currentConditions")
                tempC = tempC.get("temp")
                tempC = tempC.get("c")
                tempC = str(tempC) + "°C"
                # add the temperature to the list
                values.append(tempC)

            # check if "humidity" = True:
            if humidity == True:
                humidity = weather_json.get("currentConditions")
                humidity = humidity.get("humidity")
                # add the humidity to the list
                values.append(humidity)

                
            # check if "windKMH" = True:
            if windKMH == True:
                windKMH = weather_json.get("currentConditions")
                windKMH = windKMH.get("wind")
                windKMH = windKMH.get("km")
                windKMH = str(windKMH) + "km/h"#
                # add the wind speed to the list
                values.append(windKMH)

            # check if "day_hour" = True:
            if day_hour == True:
                day_hour = weather_json.get("currentConditions")
                day_hour = day_hour.get("dayhour")
                # add the day and hour to the values list
                values.append(day_hour)


            # return the true values
            return values
            

        # if the weather is not found, return the error message
        except Exception as error:
            # return the error message
            print ("GET WEATHER ERROR:")
            return error
