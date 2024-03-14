import streamlit as st
from streamlit.components.v1 import html

from weather_data_operations import prepare_data_for_chart

if __name__ == '__main__':
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place")
    days = st.slider("Forecast Days", min_value=1, max_value=5)
    option = st.selectbox("Select data to view", ("Temperature", "Sky"))

    match option:
        case "Temperature":
            if place:
                if days > 1:
                    day_str = "days"
                else:
                    day_str = "day"
                st.header(f"Temperature for the next {days} {day_str} in {place}")
                data_for_chart = prepare_data_for_chart(days, place)
                st.line_chart(data_for_chart, x="datetime", y="temperature")

        case "Sky":
            if place:
                data_for_icons = prepare_data_for_chart(days, place)
                data_length = len(data_for_icons)

                # Grid
                rows = st.columns([3, 3, 3])
                index = 0

                for i in range(data_length):
                    for col in rows:
                        if index == data_length - 1:
                            break
                        date = data_for_icons.loc[index]["datetime"]
                        icon = data_for_icons.loc[index]["icon"]
                        tile = col.container(height=120)
                        tile.write(str(date))
                        tile.image(f"./icons/{icon}.png", width=55)
                        index += 1
                index = 0
