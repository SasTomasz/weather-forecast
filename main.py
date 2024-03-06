import streamlit as st

st.title("Weather Forecast for the Next Days")
area = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if area:
    st.header(f"Temperature for the next {days} in {area}")
