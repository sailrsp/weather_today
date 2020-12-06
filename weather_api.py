# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json 
import pytemperature #A module that helps to convert temperature units.
 
# Get weather data for any location on the globe immediately  openweather API  
# Enter your API key here 
api_key = " "
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# give introductory message
print('Hello, I am weather bot. I will give the weather of any city in the world')
  
# Give city name 
city_name = input("Enter city name : ") 
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
 
 
 


# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

    coordinates=x['coord']
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
    # store city name
    current_city =x['name']

  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
  
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
  
    # print following values 


    print('\n The weather for ', current_city,'is given below:')
    print(' Latitude, Longitude:',coordinates['lat'],';',coordinates['lon'])
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n Temperature( in deg Celsius)=" + str("{0:.2f}".format(pytemperature.k2c(current_temperature))) +       
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 