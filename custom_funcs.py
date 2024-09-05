# Importing and basic data processing to be accessed in web app demos.

# Libraries 

import os # Disable
from sodapy import Socrata
from pathlib import Path
import pandas as pd
import geopandas as gpd
from shapely import Point
import leafmap.foliumap as leafmap

# Socrata domain
socrata_domain = "data.cityofnewyork.us"

## Vector identifiers
CD_2020_ident = 'jp9i-3b7y'
NTA_2020_ident = '9nt8-h7nd'
MODZC_2020_ident = 'pri4-ifjk'
PLUTO_ident = '64uk-42ks'

# Attribute Identifiers
Air_Quality_ident = 'c3uy-2p5r'
Fuel_Oil_ident = ''
LocalLaw_ident = ''
BuildViol_ident = 'https://soda.demo.socrata.com/resource/4tka-6guv.json?$limit=50&$offset=150'
Boba_ident = ''
Tree_Census_ident = '5rq2-4hqu'

# Local data
Albedo_something  = ''

# Socrata client

client = Socrata(socrata_domain,
                 app_token=None,
                 timeout=100)

# Get vector data
CD_query = """
SELECT
    *
    WHERE
        boro_cd BETWEEN '100' AND '199'
    LIMIT
        1000
"""
CD2020 = client.get(CD_2020_ident,
                    query=CD_query,
                    content_type='json')
#CD2020 = gpd.GeoDataFrame(CD2020)
m = leafmap.Map(center=[40.7248387,-73.9775537], zoom=9)
m.add_geojson
m.show_in_browser()
#Air_Quality = client.get(Air_Quality_ident, content_type = 'geojson')
#MODZC202 = client.get(MODZC2020_ident, content_type='geojson')


TreeCensus_query = """
SELECT
    *
    WHERE
        nta_name == 
"""
# Shapefile processing