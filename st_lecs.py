# Import libs
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
# Set up the geolocator
geolocator = Nominatim(user_agent="city_coordinates")

# Create a function to get the coordinates of a city
def get_city_coordinates(city):
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

# Create the Streamlit UI
st.sidebar.title("City Coordinate Finder and Map Display")
city = st.sidebar.text_input("Enter the name of a city:")

if st.sidebar.button("Show on Map"):
    coordinates = get_city_coordinates(city)
    st.header(city)
    st.success("Coordinates of {}: {}".format(city, coordinates))
    co_dict = {"lat":[coordinates[0]], "lon":[coordinates[1]]}
    df = pd.DataFrame(co_dict)
    st.map(df)