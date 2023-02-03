

# Ingenieria de Datos con Snowpark y visualización con Streamlit


## Contexto 
**INEGI** es un organismo público autónomo responsable de normar y coordinar el Sistema Nacional de Información Estadística y Geográfica, así como de captar y difundir información de México en cuanto al territorio, los recursos, la población y economía, que permita dar a conocer las características del país y ayudar a la toma de decisiones, publican el [Sistema de consulta](https://www.inegi.org.mx/siscon/) del cual se puden tomar set de datos públicos.

### Problema
- El Instituto genera estadística básica, la cual obtiene de tres tipos de fuentes: censos, encuestas y registros administrativos, así como estadística derivada, mediante la cual produce indicadores demográficos, sociales y económicos, además de contabilidad nacional.Estos datos son una fuente muy utilizada para realizar analisis en todo tipo de industrias, sin embargo puede tener retos interesantes como el aceso  ya que se encuentran en un almacenamiento en formatos de  archivos,los datos pueden rrequerir procesamiento para ser utilizados por ejemplo  no estan con formato no correcto para ciencia o visualización de datos así como algunos temas de calidad de datos como  contener datos nulos (NULL)  (*) en algunas columnas.


### Qué construirás 
- En esta guía  aprenderás como construir una aplicación Web utilizando   Streamlit,  un marco de desarrollo de aplicación de código abierto en lenguaje Python,  realizará un proceso de ingeniería de datos carga, transformación  de  tipos de datos( latitud/longitud) en Pythonen Snowflake Data Cloud.
![App](https://github.com/sfc-gh-csuarez/snowpark_inegi/blob/main/img/st1.png)

### Qué necesitas 
- Acceso a [GitHub](https://github.com/)  
- [VSCode](https://code.visualstudio.com/download) con Jupyter Notebook
- [SnowSQL](https://developers.snowflake.com/snowsql/)  
- [Python](https://www.python.org/) (Python 3.8)
- [Anaconda](https://www.anaconda.com/products/distribution)
- Snowpark Python 
- Streamlit 

### Arquitectura de Solución
![Arquitectura y modelo de servicio desde descarga de archivos en fuente Hosting de proveedor de datos, extracción y transformación de datos con Snowpark Python, carga datos usando   código hacia un  internal stage con Snowflake, con una interfase en Streamlit usando  Python para implementar la visualización de datos](https://github.com/sfc-gh-csuarez/snowpark_inegi/blob/main/img/modelo.png)


## Instalación
<h4>Código fuente</h4>
Decargar el repositorio que contiene el código en [Github repo](https://github.com/sfc-gh-csuarez/snowpark_inegi.git):


```shell
git clone https://github.com/sfc-gh-csuarez/snowpark_inegi.git 
```
Después de descargar el proyecto debes  ingresar a la carpeta **snowpark_inegi-main** y abrir con Visual Studio Code o el editor de preferencia que soporte archivos Jupyter Notebook  

<h4>Creación de ambiente de desarrollo Python</h4> 
Crear un ambiente local de desarrollo para la instalación de algunas librerias así como de Snowpark con la versión Python 3.8.
Teniendo Anaconda instalado con la aplicación terminal o línea de comando, dentro de la carpeta donde de descargo el repositorio(clon) de github, para crear un ambiente de desarrollo ejecutar:

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


## Ejecución

Ejecutar en Jupyter Notebook para cada uno de los siguientes Notebooks, puede realizarlo en  en Visual Studio Code (o terminal) ejecutar:

```shell
pip install notebook
jupyter notebook
conda activate snowpark_env
```
Crear en snowflake una base de datos inegi y el  rol  inegi_role
```shell
create database inegi;
create role inegi_role;
grant role inegi_role to current_use();
```

<ul>
<li>01_INEGI_download.ipynb</li>
<li>02_INEGI_dataEngineering.ipynb</li>
<li>03_INEGI_dataModeling.ipynb</li>
<li>04_Streamlit.py <br>

Antes de ejecutar  el notebook 02_INEGI_dataEngineering.ipynb  asegurate de  crear  con el rol SYSADMIN una base de datos  con nombre inegi y actualizar los valores  de conexión a tu instancia de Snowflake  modificando en Visual Studio Code o  en tu editor preferido el archivo config.py por ejemplo:
```shell
"account": "AA99900.us-east-2.aws",
    "user": "admin_user",
    "password": "Contraseña_usuario",
    "warehouse": "compute_wh",
    "role": "SYSADMIN",
    "database": "inegi",
    "schema": "public"
```
 
 Para ejecutar la aplicación  web  puedes utilizar   Visual Studio Code (o en otra terminal):
 
 ```shell
streamlit run 04_Streamlit.py
```

</li>
</ul>