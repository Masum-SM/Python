"""  
Question: Use web search to find some API to get weather data. Use that to get your region’s weather data every 30 minute.
Write a function named weather_data() and write your code inside this function.
"""
import json
import requests
import schedule

def test():
    print("My name is masum")

def weather_data():
    api_url = "https://api.openweathermap.org/data/2.5/weather?lat=23.8103&lon=90.4125&appid=f0ad446cdcb731d2c7dc1087130f7336"
    res = requests.get(api_url)
    content_in_str = res.content.decode("UTF-8")
    contect_in_dict = json.loads(content_in_str)
    print(contect_in_dict["timezone"])
    data = contect_in_dict["weather"]
    sys =contect_in_dict["sys"]
    main = contect_in_dict["main"]
    wind = contect_in_dict["wind"]
    country = sys["country"]
    sunrise = sys["sunrise"]
    sunset = sys["sunset"]
    temp = main["temp"]
    sky = data[0]["main"]
    wind_spd = wind["speed"]
    
    print("Country Name : ",country)
    print("Sunrise : ",sunrise)
    print("Sunset : ",sunset)
    print("Tempeture : ",temp)
    print("sky : ",sky)
    print("Wind speed : ",wind_spd)


weather_data()


# schedule.every(3).minutes.do(weather_data)
# while True :
#     schedule.run_pending()