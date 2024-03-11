import csv
import json
from http import HTTPStatus

import pandas as pd
import requests
import streamlit as st

from models import WeatherData, Hour
import numpy as np


# This project get data from https://www.visualcrossing.com/


def get_data_from_api(area="Kraków"):
    key = st.secrets["API_KEY"]
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{area}?unitGroup=metric&include=days%2Chours&key={key}&contentType=json"
    r = requests.get(base_url)
    return r


def transform_data(data):
    new_data = []
    for i in data:
        hours = []
        datetime = i["datetime"]
        for y in i["hours"]:
            hour = Hour(datetime=y["datetime"],
                        temp=y["temp"],
                        conditions=y["conditions"],
                        icon=y["icon"])
            hours.append(hour)
        weather_data = WeatherData(datetime=datetime, hours=hours)
        new_data.append(weather_data)
    return json.dumps(new_data, default=lambda o: o.__dict__, indent=4)


def get_demand_data(period, area):
    data = get_data_from_api(area)
    if data.status_code == HTTPStatus.OK:
        data = data.json()
        demand_data = data["days"][:period]
        demand_data = transform_data(demand_data)
    else:
        return "There is no data available"
    return demand_data


def prepare_data_for_chart(period, area):
    data = get_demand_data(period, area)
    convert_json_to_csv(data)
    df = pd.read_csv("./data/weather_data.csv", parse_dates=["datetime"])
    return df


def convert_json_to_csv(json_data):
    json_data = json.loads(json_data)
    data_file = open("./data/weather_data.csv", 'w')
    csv_writer = csv.writer(data_file)

    # Write CSV Header
    csv_writer.writerow(["datetime", "temperature", "conditions", "icon"])

    for i in json_data:
        for j in i["hours"]:
            csv_writer.writerow([i["datetime"] + " " + j["datetime"],
                                 j["temp"],
                                 j["conditions"],
                                 j["icon"]])
    data_file.close()


if __name__ == "__main__":
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    print(chart_data)
