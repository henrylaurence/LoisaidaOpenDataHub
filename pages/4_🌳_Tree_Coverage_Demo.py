# Libraries
import os
import pandas as pd
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import streamlit as st
from streamlit_folium import st_folium

# Streamlit page config
st.title('Lower East Side Tree Coverage')
st.write('Author: Henry Alonso, Ecolibrium, Loisaida Center')
st.write('Date: 2024')
st.write('Source: Federal Census Bureau and NYC Department of Buildings')

# Data

LES_Boundary = gpd.read_file('LES_Boundary.geojson')
#Tree15_MN = gpd.read_file('Tree15_MN.geojson')
Tree15_LES = gpd.read_file('Tree15_LES_Short.geojson')

# Popup Styling

# Marker Styling
Tree15_LES_Markers = folium.Marker(icon=folium.Icon(icon='tree', color='green', prefix='fa'))

# Map

m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=12, tiles=" CartoDB.Positron")

Tree15_LES_Markers_Plot = folium.GeoJson(data=Tree15_LES,
                                         name='2015 Tree Census Tree in the Lower East Side',
                                         marker=Tree15_LES_Markers).add_to(m)
m.to_streamlit(height=500)