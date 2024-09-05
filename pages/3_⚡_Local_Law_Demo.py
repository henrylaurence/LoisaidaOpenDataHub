# Libraries
import pandas as pd
import geopandas as gpd
import folium
import leafmap.foliumap as leafmap
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(
    page_title='Lower East Side Housing Emissions Compliance',
    page_icon='⚡',
    layout='wide',
    initial_sidebar_state='expanded'
)
# Title 
st.title("Local Law 37 and 87 Compliant Tax Lots in the Lower East Side")

# Data

LES_Boundary = gpd.read_file('LES_Boundary.geojson')
LES_LL33_Lots = gpd.read_file('LES_LL33_Lots.geojson')
LES_LL97_Lots = gpd.read_file('LES_LL97_Lots.geojson')
LES_LL33_and_LL97_Lots = gpd.read_file('LES_LL33_and_LL97_Lots.geojson')

# Layer Style
styleBoundary = {
    "stroke": True,
    "color": "black",
    "weight": 0.8,
    "opacity": 1,
    "fill": False
    }
style33 = {
    "stroke":True,
    "color": "black",
    "weight": 0.4,
    "opacity": 1,
    "fill": True,
    "fillColor": "#fee58c",
    "fillOpacity": 0.8
    }
style97 = {
    "stroke": True,
    "color": "#73b7d2",
    "weight": 0.4,
    "opacity": 1,
    "fill": True,
    "fillColor": "#73b7d2",
    "fillOpacity": 0.8
    }
styleBoth = {
    "stroke": True,
    "color": "#b2a4d4",
    "weight": 0.4,
    "opacity": 1,
    "fill": True,
    "fillColor": "#b2a4d4",
    "fillOpacity": 0.8
    }
# Click Style 
#def on_click(event):
 #   feature_id = event['feature']['id']

#    clicked_feature = gdf.iloc[]

# Legend: 
legendDict = {
    "Local Law 33 Tax Lots": "#fee58c",
    "Local Law 97 Tax Lots": "#73b7d2",
    "Lots Compliants with Both": "#b2a4d4"
}

# Tooltip styling

# Map
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=12)
m.add_legend(title="Local Law Compliance", legend_dict=legendDict)
#m.add_gdf(PlutoMN, style=style, info_mode=None)
m.add_gdf(LES_Boundary, style=styleBoundary, info_mode=False, zoom_to_layer=True)
m.add_gdf(LES_LL33_Lots, style=style33)
m.add_gdf(LES_LL97_Lots, style=style97)

#m.add_gdf(bothLots, style=styleBoth)

m.to_streamlit(head=500)
