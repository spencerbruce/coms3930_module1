"""
Uses web api from sunrise-sunset.org : https://sunrise-sunset.org/api
"""
import time
import json
import requests
from datetime import datetime
import board
import neopixel

pixels = neopixel.NeoPixel(board.D21, 8, brightness=0.1, auto_write=True, pixel_order=neopixel.GRB)

day = (5,5,30)
moon = (10,10,10)
sun = (200,169,110)
night = (0,0,0)

colors = [night, night, day, day, sun, day, day, night, night, moon]

# modify latitude and longitude for your current location
# lat and long for Columbia University:
lat = "40.712784"
lon = "-74.005943"

# api_response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400").json()
api_response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&date=today").json()
sunrise = api_response["results"]["sunrise"].split(":")
sunset = api_response["results"]["sunset"].split(":")
length = api_response["results"]["day_length"].split(":")
now = datetime.now().strftime("%H:%M:%S").split(":")
for i in range(3):
    sunrise[i] = int(sunrise[i][:2])
    sunset[i] = int(sunset[i][:2])
    length[i] = int(length[i])
    now[i] = int(now[i])
sunrise[0] -= 5
sunset[0] += 7

rest = 60

now = datetime.now()
risetime = datetime(now.year, now.month, now.day, sunrise[0], sunrise[1], sunrise[2])
settime = datetime(now.year, now.month, now.day, sunset[0], sunset[1], sunset[2])
nowseconds = now.hour*3600 + now.minute*60 + now.second
riseseconds = risetime.hour*3600 + risetime.minute*60 + risetime.second
setseconds = settime.hour*3600 + settime.minute*60 + settime.second
lengthseconds = length[0]*3600 + length[1]*60 + length[2]
boundary = lengthseconds//5
li = list(range(0,lengthseconds,lengthseconds//5))
curr = 0
if now >= risetime and now <= settime:
    for elem in li:
        if nowseconds - riseseconds >= elem:
            curr += 0
            colors = colors[1:] + [colors[0]]
    colors[:] = [colors[-1]] + colors[:-1]
    pixels[:] = [night]*2 + colors[:5] + [night]
    for i in range(lengthseconds//rest):
        time.sleep(rest)
        if i >= li[curr]:
            curr += 1
            pixels[:] = [night]*2 + colors[:5] + [night]
            colors = colors[1:] + [colors[0]]

colors = [day, day, night, night, moon, night, night, day, day, sun]
li = list(range(0,86400-lengthseconds,(86400-lengthseconds)//5))
curr = 0
if now >= settime:
    for elem in li:
        if nowseconds - setseconds >= elem:
            curr += 0
            colors = colors[1:] + [colors[0]]
    colors = [colors[-1]] + colors[:-1]
    pixels[:] = [night]*2 + colors[:5] + [night]
    for i in range((86400-lengthseconds)//rest):
        time.sleep(rest)
        if i >= li[curr]:
            curr += 1
            pixels[:] = [night]*2 + colors[:5] + [night]
            colors = colors[1:] + [colors[0]]
