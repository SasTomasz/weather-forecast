import pandas as pd
import streamlit as st

import weather_data_receiver


def prepare_data_for_chart(period, area):
    # TODO: Resolve problem with load DataFrame
    data = weather_data_receiver.get_demand_data(period, area)
    df = pd.read_json(data)
    print(df)
    pass


if __name__ == '__main__':
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place")
    days = st.slider("Forecast Days", min_value=1, max_value=5)
    option = st.selectbox("Select data to view", ("Temperature", "Sky"))

    prepare_data_for_chart(days, place)

    if place:
        st.header(f"Temperature for the next {days} in {place}")
