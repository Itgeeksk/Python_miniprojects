import requests


city = input("Enter your city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a118e4b915fbfb737736634d31139853"
rest = requests.get(url)

data = rest.json() 

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind =  data['wind']['speed']
description =  data['weather'][0]['description']
temp= data['main']['temp']

print(f"""  
    Humidity : {humidity}
    Pressure : {pressure}
    Wind : {wind}
    Description: {description}
    Temperature :{round(temp - 273.15, 1)} C """)
