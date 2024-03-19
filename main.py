import streamlit as st
import plotly.express as px
import pandas as pd

from weather_data_operations import prepare_data_for_chart


def set_subheader(choose_option, number_of_days, choose_place):
    if number_of_days > 1:
        day_str = "days"
    else:
        day_str = "day"
    st.subheader(f"{choose_option} for the next {number_of_days} {day_str} in {choose_place}")


if __name__ == '__main__':
    NO_PLACE_STR = "Sorry, We couldn't find Your place, please type another one"
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place")
    days = st.slider("Forecast Days", min_value=1, max_value=15, help="Set how many days You want to show")
    option = st.selectbox("Select data to view", ("Temperature", "Sky"))

    match option:
        case "Temperature":
            if place:
                data_for_chart = prepare_data_for_chart(days, place)

                # Plotly
                if isinstance(data_for_chart, pd.DataFrame):
                    set_subheader(option, days, place)
                    figure = px.line(data_for_chart, x="datetime", y="temperature", labels={"datetime": "Date", "temperature": "Temperature [C]"})
                    st.plotly_chart(figure)
                else:
                    st.subheader(NO_PLACE_STR)

        case "Sky":
            if place:
                data_for_icons = prepare_data_for_chart(days, place)

                if isinstance(data_for_icons, pd.DataFrame):
                    set_subheader(option, days, place)

                    # Grid
                    weight = 1
                    rows = st.columns([weight for i in range(6)])
                    index = 0
                    data_length = len(data_for_icons)

                    for i in range(data_length):
                        for col in rows:
                            if index == data_length - 1:
                                break
                            data_for_icons["date_str"] = data_for_icons["datetime"].dt.strftime('%a %H:%M')
                            date = data_for_icons.loc[index]["date_str"]
                            icon = data_for_icons.loc[index]["icon"]
                            tile = col.container(height=120)
                            tile.image(f"./icons/{icon}.png", width=55)
                            tile.write(str(date))
                            index += 1
                    index = 0
                else:
                    st.subheader(NO_PLACE_STR)
