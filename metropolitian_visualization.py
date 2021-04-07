########## import libraries as per man pade!! ##########################################################################

import base64
import plotly
import numpy as np
import pandas as pd
import streamlit as st
from plotly import tools
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from sklearn.decomposition import PCA
import streamlit.components.v1 as components

########################################################################################################################

########## STREAMLIT START ##############################################################################################

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.title("**Air Quality Visualisation (AQV)**")
st.write("BY JAY | ISHA | JENIL | YASH")
st.image('img/air_quality.jpg')

########################################################################################################################

st.title("**Air Quality Visualisation for Metropolitian Cities**")
st.write("Air quality index (AQI) along with air pollution, Health Condition and Demographic data near")

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

########## 3D GRAPH PLOT ###############################################################################################

X = df[['AQI', 'Population', 'Health', 'Latitude', 'Longitude']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig_3d = px.scatter_3d(
    df, x='AQI', y='Population', z='Health',
    color='AQI',color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1.0, 'red']], hover_name='Area',
    hover_data=['AQI', 'Population', 'Health', 'Latitude', 'Longitude', 'Area'],
    title = f'Total Explained Variance: {total_var:.2f}%',
)

# fig_3d.update_layout(
#     margin=dict(l=25, r=25, t=25, b=25),
#     paper_bgcolor="LightSteelBlue",
# )

########## 2D GRAPH PLOT ###############################################################################################

fig_2d = px.scatter_mapbox(
    df, lat="Latitude", lon="Longitude", color="AQI", size="Population",
    color_continuous_scale=[[0, 'green'], [0.5, 'yellow'], [1.0, 'red']], 
    size_max=15, zoom=10, hover_name = "Area", hover_data = ["Health"]
)

# fig_2d.update_layout(
#     margin=dict(l=10, r=10, t=10, b=10),
#     paper_bgcolor="LightSteelBlue",
# )

########################################################################################################################

########################################################################################################################

c1, c2 = st.beta_columns((1.1,1))

with c1:
    st.subheader('3D Graph')
    st.plotly_chart(fig_3d)
    # st.success("3D Graph Plotted!!! Yassss!!")
    # st.markdown("Looks like the average publication date is around **{}**, with your oldest book being **{}** and your youngest being **{}**.".format(1,2,3))
    # st.markdown("Note that the publication date on Goodreads is the **last** publication date, so the data is altered for any book that has been republished by a publisher.")

with c2:
    st.subheader('2D Graph')
    st.plotly_chart(fig_2d)
    # st.success("2D Graph Plotted!!! Yassss!!")

########################################################################################################################

c1, c2, c3 = st.beta_columns((1,2,1))
with c2:
    st.image('img/aqi.png')
    
########################################################################################################################