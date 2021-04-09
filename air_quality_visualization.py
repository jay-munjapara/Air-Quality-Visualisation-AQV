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

#########################################################################################################################

########## STREAMLIT START ##############################################################################################

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.title("**Air Quality Visualisation (AQV)**")
# st.balloons()
st.write("BY JAY MUNJAPARA | ISHA PATEL | JENIL KANANI | YASH BHAVSAR")
st.image('img/air_quality.jpg')

########################################################################################################################

st.title("**WHAT AIR QUALITY INDEX VALUE SAY**")
st.write("Find out what AQI values say about the possible health impacts given to you by air pollution.")

c1, c2, c3 = st.beta_columns((1,5,1))
with c2:
    st.image('img/aqi.png')

# col1, col2, col3 = st.beta_columns([1,10,1])

# with col1:
#     st.write("")

# with col2:
#     st.image('img/aqi.png')

# with col3:
#     st.write("")

########################################################################################################################

########### AQV for Metropolitian Cities ###############################################################################

st.title("**Air Quality Visualisation for Metropolitian Cities, India**")
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
    st.markdown(f'<a href="data:file/csv;base64,{df}" download = "{city}_DATA.csv">Download csv file</a>', unsafe_allow_html = True)

########## 3D GRAPH PLOT ###############################################################################################

X = df[['AQI', 'Population', 'Health', 'Latitude', 'Longitude']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig_3d = px.scatter_3d(
    df, x='AQI', y='Population', z='Health',
    color='AQI',color_continuous_scale=[[0, 'green'], [0.2, 'yellow'],[0.4, 'red'], [0.6, 'rgb(128,0,128)'], [1.0, 'rgb(191,30,46)']], 
    hover_name='Area', hover_data=['AQI', 'Population', 'Health', 'Latitude', 'Longitude', 'Area'],
    title = f'Total Explained Variance: {total_var:.2f}%',
)

# fig_3d.update(zmin=0.2, zmax=0.8)


# fig_3d.update_layout(
#     margin=dict(l=25, r=25, t=25, b=25),
#     paper_bgcolor="LightSteelBlue",
# )

########## 2D GRAPH PLOT ###############################################################################################

fig_2d = px.scatter_mapbox(
    df, lat="Latitude", lon="Longitude", color="AQI", size="Population",
    color_continuous_scale=[[0, 'green'], [0.2, 'yellow'],[0.4, 'red'], [0.6, 'rgb(128,0,128)'], [1.0, 'rgb(191,30,46)']], 
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

st.success("Graph Plotted, Successfully!!")

########### AQV for Most Air Polluted States ###########################################################################

st.title("**Air Quality Visualisation for Most Air Polluted States in India**")
st.write("Air quality index (AQI) along with air pollution, Health Condition and Demographic data near")

########## CITY - DATA #################################################################################################

states = st.selectbox("States: ", ['ANDHRA PRADESH', 'BIHAR', 'GUJARAT', 'KARNATAKA', 'MADHYA PRADESH', 'MAHARASHTRA', 'RAJASTHAN', 'TAMIL NADU', 'UTTAR PRADESH', 'WEST BENGAL'])

px.set_mapbox_access_token(open("mapbox_token.txt").read())

########## READ CSV DATA ###############################################################################################

df = pd.read_csv("datasets/{}_DATA.csv".format(states))

########################################################################################################################

if st.checkbox('Show Data:'):
    st.dataframe(df)
    coded_data = base64.b64encode(df.to_csv(index = False).encode()).decode()
    st.markdown(f'<a href="data:file/csv;base64,{df}" download = "{states}_DATA.csv">Download csv file</a>', unsafe_allow_html = True)

########## 3D GRAPH PLOT ###############################################################################################

X = df[['AQI', 'Population', 'Health', 'Latitude', 'Longitude']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig_3d = px.scatter_3d(
    df, x='AQI', y='Population', z='Health',
    color='AQI',color_continuous_scale=[[0, 'green'], [0.2, 'yellow'],[0.4, 'red'], [0.6, 'rgb(128,0,128)'], [1.0, 'rgb(191,30,46)']], 
    hover_name='Area', hover_data=['AQI', 'Population', 'Health', 'Latitude', 'Longitude', 'Area'],
    title = f'Total Explained Variance: {total_var:.2f}%',
)

# fig_3d.update_layout(
#     margin=dict(l=25, r=25, t=25, b=25),
#     paper_bgcolor="LightSteelBlue",
# )

########## 2D GRAPH PLOT ###############################################################################################

fig_2d = px.scatter_mapbox(
    df, lat="Latitude", lon="Longitude", color="AQI", size="Population",
    color_continuous_scale=[[0, 'green'], [0.2, 'yellow'],[0.4, 'red'], [0.6, 'rgb(128,0,128)'], [1.0, 'rgb(191,30,46)']], 
    size_max=15, zoom=5, hover_name = "Area", hover_data = ["Health"]
)

# fig_2d.update_layout(
#     margin=dict(l=10, r=10, t=10, b=10),
#     paper_bgcolor="LightSteelBlue",
# )

########################################################################################################################

########################################################################################################################

c1, c2, c3, c4 = st.beta_columns((0.5, 4, 5, 0.5))

with c2:
    st.subheader('3D Graph')
    st.plotly_chart(fig_3d)
    # st.markdown("Looks like the average publication date is around **{}**, with your oldest book being **{}** and your youngest being **{}**.".format(1,2,3))
    # st.markdown("Note that the publication date on Goodreads is the **last** publication date, so the data is altered for any book that has been republished by a publisher.")

with c3:
    st.subheader('2D Graph')
    st.plotly_chart(fig_2d)

st.success("Graph Plotted, Successfully!!")

########################################################################################################################

with st.beta_expander("See 'PM 2.5' and 'PM 10' values of cities in {}".format(states)):
    # st.write('Juicy deets')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df["Area"],
        x=df["PM2.5"],
        name='PM 2.5',
        marker_color=df["PM2.5"], #'rgb(26, 118, 255)',
        orientation='h',
        marker={'color': df["PM2.5"], 'colorscale': [[0, 'green'], [0.5, 'yellow'],[1.0, 'red']]}
    ))
    fig.add_trace(go.Bar(
        y=df["Area"],
        x=df["PM10"],
        name='PM 10',
        # marker_color= df["PM10"], #'rgb(55, 83, 109)', #[[0, 'green'], [0.2, 'yellow'],[0.4, 'red'], [0.6, 'rgb(128,0,128)'], [1.0, 'rgb(191,30,46)']],
        orientation='h',
        marker={'color': df["PM10"], 'colorscale': [[0, 'green'], [0.5, 'yellow'],[1.0, 'red']]}
        # color = df['PM10']
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(
        barmode='group', #xaxis_tickangle=-45,
        height=1000,
        width = 1300,
        bargap=0.25, # gap between bars of adjacent location coordinates.
        bargroupgap=0 # gap between bars of the same location coordinate.
    )
    # fig.show()

    st.plotly_chart(fig)

########################################################################################################################

st.write("")

c1, c2, c3 = st.beta_columns((1,5,1))
with c2:
    st.title("**About the Air Quality and Pollution Measurement**")
    # st.write("About the Air Quality Levels")
    st.write("")
    st.write("")
    st.write("")

c1, c2 = st.beta_columns((0.9,1.3))

with c1:
    st.image('img/aqi_chart.png')
with c2:
    st.image('img/aqi_guide.png')

st.write("")

col1, col2, col3 = st.beta_columns([1,10,1])

with col1:
    st.write("")

with col2:
    st.write("To know more about Air Quality and Pollution, check " + str('[Air Pollution [wikipedia]](https://en.wikipedia.org/wiki/Air_pollution)') + " or "  + str('[the guide to Air Quality and Your Health [airnow].](https://www.airnow.gov/aqi/aqi-basics/)'))
    st.write("For very useful health tips to Cope with Air Pollution and Stay Safe, check " + str('[www.aqi.in/blog/aqi-india-tips-cope-air-pollution-stay-safe/ [AQI India]](https://www.aqi.in/blog/aqi-india-tips-cope-air-pollution-stay-safe/)') + " blog.")

with col3:
    st.write("")

########################################################################################################################

# st.title("**WHAT AIR QUALITY INDEX VALUE SAY**")
# st.write("Find out what AQI values say about the possible health impacts given to you by air pollution.")

# col1, col2, col3 = st.beta_columns([1,10,1])

# with col1:
#     st.write("")

# with col2:
#     st.image('img/aqi.png')

# with col3:
#     st.write("")

########################################################################################################################