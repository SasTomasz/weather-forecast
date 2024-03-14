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
            # TODO: Read this article https://docs.kanaries.net/topics/Streamlit/streamlit-columns
            if place:
                data_for_icons = prepare_data_for_chart(days, place)
                data_length = len(data_for_icons)
                print(f"Data length: {data_length}")

                # Different layout idea

                # Grid
                rows = st.columns([3, 3, 3])
                row1 = st.columns(3)
                row2 = st.columns(3)
                number = 0
                index = 0

                for i in range(data_length):
                    for col in rows:
                        if index == data_length - 1:
                            break
                        date = data_for_icons.loc[index]["datetime"]
                        # icon =
                        tile = col.container(height=120)
                        tile.write(str(date))
                        tile.image("./icons/rain.png")
                        index += 1

                index = 0
                # Metric
                # col1, col2 = st.columns([2, 3])
                # with col1:
                #     st.metric(label="Metric 1", value=123)
                #     st.caption("This is some additional information about Metric 1.")
                #     st.metric(label="Metric 3", value=234)
                # with col2:
                #     st.metric(label="Metric 2", value=456)
                #     st.caption("This is some additional information about Metric 2.")
        case _:
            pass
