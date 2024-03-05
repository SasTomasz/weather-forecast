import streamlit as st

st.title("Weather Forecast for Next Days")
st.text_input("Place")
st.slider("Forecast Days", min_value=1, max_value=5)
st.selectbox("Select data to view", ("Temperature", "Sky"))
