import requests
import streamlit as st

# This project get data from https://www.visualcrossing.com/


def get_data_from_api(key, area="Kraków"):
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{area}?unitGroup=metric&include=days%2Chours&key={key}&contentType=json"
    r = requests.get(base_url)
    return r


if __name__ == "__main__":
    api_key = st.secrets["API_KEY"]
    data = get_data_from_api(api_key).content
    print(data)
