import altair as alt
import pandas as pd
from pandas import DataFrame
from snowflake.snowpark.session import Session
from config import connection_parameters
import streamlit as st
from PIL import Image
from style import divContainer,formatoNumero


@st.experimental_singleton
def snowsesion() -> Session:
    sesion = Session.builder.configs(connection_parameters).create()
    if sesion != None:
        print("Conectado")
        sesion.use_database('inegi')
        print(sesion.sql("select current_warehouse(), current_database(), current_role()").collect()) 
        return sesion
    else:
        print("Error de conexión")

def run_query(sesion,query):
    try:
        return sesion.sql(query)
    except :
        print("error: ")

#@st.experimental_memo() 
def inegiDataSet():
    st.set_page_config(
    page_title="INEGI App",
    page_icon="☻",
    layout="wide",
    initial_sidebar_state="expanded",)
    st.header("Censo y población México")
    

    with st.sidebar:
        image = Image.open('img/inegi.png')
        st.image(image, caption='INEGI',width=220)
        add_n_lines = st.slider("Elige volumen de problación (# habitantes):", 700000, 17000000,2125000 ,500000)
    query = "SELECT * FROM INEGI.PUBLIC.INEGI_MAPA where POBLACION_TOTAL > " + str(add_n_lines) + " order by POBLACION_TOTAL desc;"
    sesion = snowsesion()
    snowDF = run_query(sesion,query)
    snowPD = snowDF.to_pandas()
    
    
    col1,col2 = st.columns([3,1])
    with col1:
        with st.container():
            mapa = snowPD[['POBLACION_TOTAL','LATITUD', 'LONGITUD']]
            mapa = mapa.rename(columns={'LATITUD':'latitude', 'LONGITUD':'longitude'})
            st.map(mapa,zoom=4,use_container_width=True)
            

    with col2:
        with st.container():   
            totalpod = snowPD['POBLACION_TOTAL'].sum()
            formatoTotal = formatoNumero(totalpod)
            st.markdown(divContainer(), unsafe_allow_html=True)
            st.metric(label="Total" , value=formatoTotal, delta="2%",delta_color="inverse")
            #--  
            maxp = snowPD['POBLACION_TOTAL'].max()
            result_df = snowPD.loc[snowPD['POBLACION_TOTAL'] == maxp]
            st.markdown(divContainer(), unsafe_allow_html=True)
            formatMaxp = formatoNumero(maxp)
            label_max = str(result_df.loc[0].at['NOM_ENTIDAD'])
            st.metric(label="Mayor entidad: " + label_max, value=formatMaxp, delta="5%",delta_color="inverse")


    with st.container():
        st.subheader('Histograma por entidad')
        barDF = snowPD[['NOM_ENTIDAD','POBLACION_TOTAL']]
        chart = alt.Chart(barDF).mark_bar().encode(
        x='NOM_ENTIDAD',
        y='POBLACION_TOTAL',
        ).interactive()
        st.altair_chart(chart, use_container_width=True)        
       
    with st.container():
        st.table(snowPD)  

inegiDataSet()
