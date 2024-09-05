# Libraries
import pandas as pd
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import streamlit as st
from streamlit_folium import st_folium

# Config
st.set_page_config(
    page_title='New York City Air Quality Dashboard',
    page_icon='🧊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Header
st.title('New York City Air Quality Dashboard')
st.write('Author: Henry Alonso, Ecolibrium, Loisaida Center')
st.write('Date: 8/14/2024')
st.write('Source: New York City Department of Health and Mental Hygiene')

# Load data
Fine_22_MN = gpd.read_file('FineParticles2022_MN.geojson')
NO_22_MN = gpd.read_file('NitricOxide2022_MN.geojson')
NO2_22_MN = gpd.read_file('NitrogenDioxide2022_MN.geojson')
O3_22_MN = gpd.read_file('Ozone2022_MN.geosjon')

# Leafmap
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=9)

# Label options
label="Pollutant"
options = ['Fine Particles',
           'Nitric Oxide (NO)',
           'Nitrogen Dioxide (NO2)',
           'Ozone (O3)']

# Callback function for pollutant map
def update_map(pollutant):
    if pollutant == 'Fine Particles':
        st.session_state['selection'] = 0
        m.add_data(Fine_22_MN, 
                   column='Mean mcg/m3', 
                   scheme='quantiles',
                   cmap='Reds', 
                   legend_title='Fine Particles (mean mcg/m3)')
    elif pollutant == 'Nitric Oxide (NO)':
        st.session_state['selection'] = 1
        m.add_data(NO_22_MN, 
                   column='Mean ppb', 
                   scheme='quantiles', 
                   cmap='Reds', 
                   legend_title='Nitric Oxide (mean ppb)')
    elif pollutant == 'Nitrogen Dioxide (NO2)':
        st.session_state['selection'] = 2
        m.add_data(NO2_22_MN, 
                   column='Mean ppb', 
                   scheme='quantiles', 
                   cmap='Reds', 
                   legend_title='Nitrogen Dioxide (mean ppb)')
    elif pollutant == 'Ozone (O3)':
        st.session_state['selection'] = 3
        m.add_data(O3_22_MN, 
                   column='Mean ppb', 
                   scheme='quantiles', 
                   cmap='Reds', 
                   legend_title='Ozone (mean ppb)')
    m.to_streamlit(height=500)

# Initialize the session state
if 'pollutant' not in st.session_state:
    st.session_state['pollutant'] = 'Fine Particles'

# Select box
with st.sidebar:
    selected_pollutant = st.selectbox(label, options, index=options.index(st.session_state['pollutant']))

update_map(selected_pollutant)


### Add description and information to each selectbox item in future update