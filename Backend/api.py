import requests
import json

weather = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=49.74&lon=13.37&appid=16d2912b5d44cfbbc683f1d34837d843')
weather = json.loads(weather.text)
pops = []
for hour in weather['hourly']:
    pops.append(hour['pop'])

def average(pops):
    return sum(pops)/len(pops)
print(average(pops), '.............', len(pops))


