

# Ingenieria de Datos con Snowpark y visualización con Streamlit


## Contexto 
**INEGI** es un organismo público autónomo responsable de normar y coordinar el Sistema Nacional de Información Estadística y Geográfica, así como de captar y difundir información de México en cuanto al territorio, los recursos, la población y economía, que permita dar a conocer las características del país y ayudar a la toma de decisiones, publican el [Sistema de consulta](https://www.inegi.org.mx/siscon/) del cual se puden tomar set de datos públicos.

### Problema
- Datos en un almacenamiento server,los datos no estan con formato no correcto para ciencia o visualización de datos así como NULL (*) en algunas columnas.


### Qué construirás 
- Web App con Streamlit realizando data engineering y datos cargados, tranformación basa en tipos de datos( latitud/longitud) programadon End-2-End con Python.
![App](https://github.com/sfc-gh-csuarez/snowpark_inegi/blob/main/img/st1.png)

### Qué necesitas 
- Cuenta [GitHub](https://github.com/)  
- [VSCode](https://code.visualstudio.com/download) con Jupyter Notebook
- [SnowSQL](https://developers.snowflake.com/snowsql/)  
- [Python](https://www.python.org/) (Python 3.8)
- [Anaconda](https://www.anaconda.com/products/distribution)
- Snowpark Python 
- Streamlit 

### Arquitectura de Solución
![Arquitectura y modelo de servicio desde descarga de archivos en fuente Hosting de proveedor de datos, extracción y tranformación de datos con Snowpark Python, carga desde código hacia internal stage con Snoeflake, y a través de Streamlit y Python implementar la visualización de datos](https://github.com/sfc-gh-csuarez/snowpark_inegi/blob/main/img/modelo.png)


## Instalación

<h4>Código fuente</h4>
Decargar el repositorio que contiene el código necesario
[github repo](https://github.com/sfc-gh-csuarez/snowpark_inegi.git)

```shell
git clone https://github.com/sfc-gh-csuarez/snowpark_inegi.git 
```
Después de la descarga ingresar a la carpeta **snowpark_inegi-main** y abrir con Visual Studio Code o el editor de preferencia que soporte archivos Jupyter Notebook  

<h4>Creación de ambiente de desarrollo Python</h4> 
Crear un ambiente local de desarrollo para la instalación de algunas librerias así como de Snowpark con la versión Python 3.8.
Teniendo Anaconda instalado con la aplicaicón terminal, apuntar a la carpeta donde de descargo el clon de github, para crear un ambiente de desarrollo ejecutar:

```shell
conda create --name snowpark_env python=3.8 
conda activate snowpark_env
```

<h4>Instalación Snowpark Python</h4> 
Instalación de Snowpark 

```shell
pip install snowflake-snowpark-python pandas
pip install lat-lon-parser
pip install requests
conda install -c conda-forge streamlit 
conda install -c conda-forge pillow
```

<h4>Instalación Streamlit </h4> 

```shell
conda install -c conda-forge streamlit  
```

## Ejecución

Ejecutar en Jupyter Notebook para cada uno de los siguientes Notebooks, en Visual Studio Code (o terminal) ejecutar:

```shell
conda activate snowpark_env
```

<ul>
<li>01_INEGI_download.ipynb</li>
<li>02_INEGI_dataEngineering.ipynb</li>
<li>03_INEGI_dataModeling.ipynb</li>
<li>04_Streamlit.py
 para esta apartado ejecutar en Visual Studio Code (o en otra terminal):
 
 ```shell
streamlit run 04_Streamlit.py
```

</li>
</ul>