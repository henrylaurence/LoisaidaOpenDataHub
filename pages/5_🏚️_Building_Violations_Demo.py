import os
import numpy as np
import pandas as pd
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import streamlit as st
import streamlit_folium as st_folium

# Page config

st.title('Lower East Side Buildings/BINs/Addresses With Open Violations')
st.write('Author: Henry Alonso, Ecolibrium, Loisaida Center')
st.write('Date: 2024')
st.write('Source: Federal Census Bureau and NYC Department of Buildings')

# Data
NTA20_MN = gpd.read_file("NTA20_MN.geojson")
NTA20_LES = gpd.read_file("NTA20_LES_EastVillage_Chinatown.geojson")
OpenViol_MN = gpd.read_file("OpenViol_MN.geojson")
OpenViol_LES = gpd.read_file("LES_Buildings_OpenViolations.geojson")

# NTA Styling
style_NTAMN = {
    "stroke": True,
    "color": 'gray',
    "weight": 1,
    "opacity": 0.8, 
    "fill": False
}

# Popup Styling
marker_popup = ['ADDRESS', 'BIN', 'HPD_VIOLATIONS', 'DOB_VIOLATIONS', 'TOTAL_VIOLATIONS', 'DWELLING_UNITS', 'VIO_UNITS_RATIO', 'latitude', 'longitude']

# Marker Styling
marker_style_MN = folium.Marker(icon=folium.Icon(icon='building', color='blue', prefix='fa'), opacity=0.3)
marker_style_LES = folium.Marker(icon=folium.Icon(icon='building', color='blue', prefix='fa'))


# Mapping           
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=12, tiles=" CartoDB.Positron")

Markers_OpenViolMN = folium.GeoJson(data=OpenViol_MN,
                                    name='Buildings with Open Violations in Manhattan',
                                    marker=marker_style_MN).add_to(m)
Markers_OpenViolLES = folium.GeoJson(data=OpenViol_LES,
                                     name='Buildings with Open Violations in the Lower East Side Area',
                                     marker=marker_style_LES,
                                     tooltip=folium.GeoJsonTooltip(fields=['ADDRESS'], sticky=True),
                                     popup=folium.GeoJsonPopup(fields=marker_popup),
                                     highlight_function=lambda x: {"fillOpacity": 0.5},
                                     zoom_on_click=True).add_to(m)                                     
m.add_gdf(gdf=NTA20_MN, style=style_NTAMN, info_mode=False)
m.add_gdf(gdf=NTA20_LES, info_mode=False, zoom_to_layer=True)
#m.add_gdf(gdf=OpenViol_LES, info_mode= 'on_hover')
m.to_streamlit(height=500)
