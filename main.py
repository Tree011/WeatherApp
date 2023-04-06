import requests
import json
import pyttsx3

city = input('Enter the name of the city : ')

url =f'https://api.weatherapi.com/v1/current.json?key=790d3130377f423081120924230604&q={city}'

get_city = requests.get(url)
#print(get_city.text)
weather_now= json.loads(get_city.text)
temp_now = weather_now['current']['temp_c']
print(f'The weather now is {temp_now} degree celsius.')

engine = pyttsx3.init()
engine.say(f'The weather now is {temp_now} degree celsius.')
engine.runAndWait()
