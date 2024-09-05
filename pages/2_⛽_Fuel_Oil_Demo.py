# Libraries
import pandas as pd
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import streamlit as st
from streamlit_folium import st_folium

# Config
st.set_page_config(
    page_title='New York City Fuel Oil Usage',
    page_icon='🧊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Title
st.title('New York City Fuel Oil Dashboard')
st.write('Author: Henry Alonso, Ecolibrium, Loisaida Center')
st.write('Date: 8/14/2024')
st.write('Source: ')

# Load data
FuelOil_MN_19 = gpd.read_file('FuelOil_MN_19.geojson')

# Map
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=12)

# Update Map

# Selectbox
label = 'Fuel choice'
options = ['Fuel Oil #2', 'Fuel Oil #4']

def update_map(fuel):
    if fuel == 'Fuel Oil #2':
        st.session_state['selection'] = 0
        m.add_data(FuelOil_MN_19,
                   column='Total Biodiesel Blended with #2 Fuel Oil',
                   scheme='Quantiles',
                   cmap='Blues',
                   legend_title="Total Biodiesel with #2 Fuel (gallons)")
    elif fuel == 'Fuel Oil #4':
        st.session_state['selection'] = 1
        m.add_data(FuelOil_MN_19,
                   column='Total Biodiesel Blended with #4 Fuel Oil',
                   scheme='Quantiles',
                   cmap='Blues',
                   legend_title="Total Biodiesel with #4 Fuel (gallons)")
    m.to_streamlit(height=500)
    
if 'fuel' not in st.session_state:
    st.session_state['fuel'] = 'Fuel Oil #2'

with st.sidebar:
    selected_fuel = st.selectbox(label,
                               options,
                               index = options.index(st.session_state['fuel']))
update_map(selected_fuel)