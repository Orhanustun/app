
class WeatherData:
    def __init__(self, data):
        self.date = data.get("date")
        self.day = data.get("day")
        self.icon = data.get("icon")
        self.description = data.get("description")
        self.status = data.get("status")
        self.degree = float(data.get("degree", 0))
        self.min = float(data.get("min", 0))
        self.max = float(data.get("max", 0))
        self.night = float(data.get("night", 0))
        self.humidity = int(data.get("humidity", 0))

    def __str__(self):
        return f"{self.date} - {self.day}: {self.description} (Min: {self.min}, Max: {self.max}, Humidity: {self.humidity}%)"


health_list = ["asthma", "heart disease", "migraine", "allergy", "other"]
name = input("Please write your name: ")
age = float(input("Please Enter your age: "))

for i in range(len(health_list)):
    print("=>", health_list[i])

while True:
    health_issue = input("If you have any health issue from above, please write it here (or enter 'no' if none): ")

    # Check if the entered health_issue is in the health_list or is no
    if health_issue.lower() in [issue.lower() for issue in health_list] or health_issue.lower() == "no" or " ":
        if health_issue.lower() == "no":
            print("I understand")
        else:
            print("OK")
        break
    else:
        print("Wrong value. Please choose from the list or enter 'no'.")



class WeatherData:
    def __init__(self, data):
        self.date = data.get("date")
        self.day = data.get("day")
        self.icon = data.get("icon")
        self.description = data.get("description")
        self.status = data.get("status")
        self.degree = float(data.get("degree", 0))
        self.min = float(data.get("min", 0))
        self.max = float(data.get("max", 0))
        self.night = float(data.get("night", 0))
        self.humidity = int(data.get("humidity", 0))

    def __str__(self):
        return f"{self.date} - {self.day}: {self.description} (Min: {self.min}, Max: {self.max}, Humidity: {self.humidity}%)"

import http.client
import json

def get_weather(city):
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 7b7C2JirCFg2Qz3Ke7tfKs:03Y2P58IMXKN6VwJEj7Trk"
    }
    conn.request("GET", f"/weather/getWeather?data.lang=tr&data.city={city}", headers=headers)

    response = conn.getresponse()
    data = response.read()
    weather_info = json.loads(data.decode("utf-8"))

    weather_data_list = [WeatherData(item) for item in weather_info.get("result", [])]

    conn.close()

    return weather_data_list


weather_data = get_weather("izmir")
for weather in weather_data:
 print("Hello Mr " + name + " the weather of this day is like this => " + str(weather) )
 break