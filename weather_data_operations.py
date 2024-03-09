import csv
import json
from http import HTTPStatus

import pandas as pd
import requests
import streamlit as st

from models import WeatherData, Hour


# This project get data from https://www.visualcrossing.com/


def get_data_from_api(area="Kraków"):
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
        new_data.append(weather_data)
    return json.dumps(new_data, default=lambda o: o.__dict__, indent=4)


def get_demand_data(period, area):
    data = get_data_from_api(area)
    if data.status_code == HTTPStatus.OK:
        data = data.json()
        demand_data = data["days"][:period]
        # print(f"DEMAND DATA = \n{demand_data}")
        demand_data = transform_data(demand_data)
    else:
        return "There is no data available"
    return demand_data


def prepare_data_for_chart(period, area):
    # TODO: Resolve problem with load DataFrame
    data = get_demand_data(period, area)
    df = pd.read_json(data)
    print(df)


def convert_json_to_csv(json_data):
    json_data = json.loads(json_data)
    data_file = open("./data/weather_data.csv", "w")
    csv_writer = csv.writer(data_file)
    for i in json_data:
        print(i["datetime"])
        csv_writer.writerows(i)
    data_file.close()


if __name__ == "__main__":
    user_demand_data = get_demand_data(5, "Kraków")
    print(user_demand_data)
    # convert_json_to_csv(user_demand_data)
    # print(data_for_chart)
    # prepare_data_for_chart(5, "Kraków")
