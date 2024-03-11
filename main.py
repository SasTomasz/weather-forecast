import streamlit as st

from weather_data_operations import prepare_data_for_chart

if __name__ == '__main__':
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place")
    days = st.slider("Forecast Days", min_value=1, max_value=5)
    option = st.selectbox("Select data to view", ("Temperature", "Sky"))

    if place:
        if days > 1:
            day_str = "days"
        else:
            day_str = "day"
        st.header(f"Temperature for the next {days} {day_str} in {place}")
        data_for_chart = prepare_data_for_chart(days, place)
        st.line_chart(data_for_chart, x="datetime", y="temperature")
