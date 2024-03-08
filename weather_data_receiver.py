import requests
import streamlit as st
from http import HTTPStatus
from models import WeatherData, Hour
import json
# This project get data from https://www.visualcrossing.com/


def get_data_from_api(period, area="Kraków"):
    key = st.secrets["API_KEY"]
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{area}?unitGroup=metric&include=days%2Chours&key={key}&contentType=json"
    r = requests.get(base_url)
    return r


def transform_data(data):
    new_data = []
    hours = []
    for i in data:
        datetime = i["datetime"]
        for y in i["hours"]:
            hour = Hour(datetime=y["datetime"],
                        temp=y["temp"],
                        conditions=y["conditions"],
                        icon=y["icon"])
            hours.append(hour)
        weather_data = WeatherData(datetime=datetime, hours=hours)
        new_data = json.dumps(weather_data, default=lambda o: o.__dict__, indent=4)
    return new_data


def get_demand_data(period, area):
    # TODO: Fix problem with getting data - data from transform_data is only one day
    data = get_data_from_api(period, area)
    if data.status_code == HTTPStatus.OK:
        data = data.json()
        demand_data = data["days"][:period]
        demand_data = transform_data(demand_data)
    else:
        return "There is no data available"
    return demand_data


if __name__ == "__main__":
    user_demand_data = get_demand_data(2, "Kraków")
    print(user_demand_data)
