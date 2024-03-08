from typing import List

# This is a model of weather data I'd like to use
# [{
# 	"datetime": "2024-03-07",
# 	"hours": [{
# 		"datetime": "00:00:00",
# 		"temp": 7.0,
# 		"conditions": "Rain, Partially cloudy",
# 		"icon": "rain"
# 	}]
# }]


class Hour(object):
    def __init__(self, datetime: str, temp: float, conditions: str, icon: str):
        self.datetime = datetime
        self.temp = temp
        self.conditions = conditions
        self.icon = icon


class WeatherData(object):
    def __init__(self, datetime: str, hours: List[Hour]):
        self.datetime = datetime
        self.hours = hours
