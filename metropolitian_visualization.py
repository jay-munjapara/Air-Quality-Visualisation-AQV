#import libraries as per man pade!!
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import plotly
from sklearn.decomposition import PCA

import streamlit as st
import streamlit.components.v1 as components

import base64

########################################################################################################################

########## STREAMLIT START ##############################################################################################

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.title("**Air Quality Visualisation for Metropolitian Cities**")
# st.write("Air quality index (AQI) along with air pollution, Health Condition and Demographic data near {}".format(city))
# st.write("Air quality index (AQI) and PM2.5 air pollution near Colaba, Mumbai - MPCB, Uran")

# st.sidebar.selectbox(
#     "You Can do the following using this Website ",
#     ('Data Pre Processing using Pandas', 'Correcting','Completing','Creating','Modeling using Sklearn')
# )

########## CITY - DATA #################################################################################################

city = st.selectbox("City: ", ['MUMBAI', 'KOLKATA', 'CHENNAI', 'DELHI'])

px.set_mapbox_access_token(open("mapbox_token.txt").read())

########## READ CSV DATA ###############################################################################################

df = pd.read_csv("datasets/{}_DATA.csv".format(city))

########################################################################################################################

if st.checkbox('Show Data'):
    st.dataframe(df)
    coded_data = base64.b64encode(df.to_csv(index = False).encode()).decode()
    st.markdown(f'<a href="data:file/csv;base64,{df}" download = "data.csv">Download Data</a>', unsafe_allow_html = True)

st.write("Air quality index (AQI) along with air pollution, Health Condition and Demographic data near {}".format(city))

########## 2D GRAPH PLOT ###############################################################################################

fig_2d = px.scatter_mapbox(
    df, lat="Latitude", lon="Longitude", color="AQI", size="Population",
    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10, 
    hover_name = "Area", hover_data = ["Health"]
)

########## 3D GRAPH PLOT ###############################################################################################

X = df[['AQI', 'Population', 'Health', 'Latitude', 'Longitude']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig_3d = px.scatter_3d(
    df, x='AQI', y='Population', z='Health',
    color='AQI', hover_name='Area',
    hover_data=['AQI', 'Population', 'Health', 'Latitude', 'Longitude', 'Area'],
    title = f'Total Explained Variance: {total_var:.2f}%',
    #labels = {'0': 'Population', '1': 'Sex Ratio', '2': 'Literacy'} , symbol='Population'  , 'Ward','Station'
)

########################################################################################################################

########################################################################################################################

c1, c2 = st.beta_columns((1.1, 1))

with c1:
    st.subheader('3D Graph')
    st.plotly_chart(fig_3d)
    st.success("3D Graph Plotted!!! Yassss!!")
    # st.markdown("Looks like the average publication date is around **{}**, with your oldest book being **{}** and your youngest being **{}**.".format(1,2,3))
    # st.markdown("Note that the publication date on Goodreads is the **last** publication date, so the data is altered for any book that has been republished by a publisher.")

with c2:
    st.subheader('2D Graph')
    st.plotly_chart(fig_2d)
    st.success("2D Graph Plotted!!! Yassss!!")

########################################################################################################################

########################################################################################################################