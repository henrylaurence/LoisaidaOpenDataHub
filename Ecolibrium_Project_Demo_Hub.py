# Libaries
import os
from pathlib import Path
import streamlit as st

# Streamlit page configuration
st.set_page_config(
    page_title="Ecolibrium Project Open Data Hub Demos",
    page_icon="👋")

# Directory
current = Path.cwd()
new = current / 'data'
os.chdir(new)

# Streamlit code
st.write("# Welcome to the Ecolibrium Data Hub")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ### What is the Ecolibrium Data Hub?

    The Ecolibrium Open Data Hub is our platform to clearly visualize local emissions, sustainable housing conditions, and other ecological hazards in the Lower East Side and surrounding neighborhoods. 

    We hope to use our dashboards as launch pads to "brainstorm" future discussion and neighborhood plans. 

    See our Open Data Demos in ~the sidebar on the left in order to learn more.

    ### What is Ecolibrium?

    Ecolibrium is a multi-disciplinary Climate Science Literacy and Environmental Justice project by Loisaida, Inc. Center that studies, surveys, and analyzes environmental conditions at the hyper-local level with the goal of improving public health and quality of life for our neighborhood and continuous Lower Manhattan community.

    Loisaida has assembled a diverse, multigenerational team of local and national collaborators, college students, recent graduates, high school seniors, and professionals working in the fields of data science, architecture and engineering who all seek to improve public health and monitor environmental conditions in the Lower East Side (“Loisaida”) neighborhood. The project is funded through the New York State Department of Environmental Conservation’s Environmental Justice award. Ecolibrium’s first phase will culminate in a comprehensive hazard map of the Lower East Side and a multimedia campaign and interactive exhibition that utilizes independent media resources to enhance public awareness of environmental health hazards affecting us.
   
    ### Want to learn more about Ecolibrium?
    
    Check out the Loisaida, Inc. Center website and our social media pages.
"""
) 