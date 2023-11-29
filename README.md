

<div align="center">
  <img src='./assets/terminal.gif'>
  <br> 
</div>


# 🌎 PF_DataScience_Migraciones 🌍 

Repositorio para Proyecto Final de Data Science en bootcamp Henry, se analizan los datos de migraciones a nivel mudial y nacional. Aplicando un stack tecnológico como Google Cloud Platform, con Machine learning, presentación de KPIs y visualizaciones en PowerBi

## Skillset

- 💻 &nbsp;
  ![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
  ![R (Statistics)](https://img.shields.io/badge/-R-333333?style=flat&logo=R&logoColor=276DC3)
  ![Markdown](https://img.shields.io/badge/-Markdown-333333?style=flat&logo=markdown)
- 📚 &nbsp;
  ![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
  ![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
  ![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
  ![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
  ![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
- 🛢 &nbsp;
  ![BigQuery](https://img.shields.io/badge/-BigQuery-333333?style=flat&logo=bigquery)
  [![Google Cloud Platform](https://img.shields.io/badge/GoogleCloudPlatform-Up-<COLOR>.svg)](https://shields.io/)
- 📊 &nbsp;
  ![Power BI](https://img.shields.io/badge/-Power%20BI-333333?style=flat&logo=powerbi)
- ⚙️ &nbsp;
  ![Git](https://img.shields.io/badge/-Git-333333?style=flat&logo=git)
  ![GitHub](https://img.shields.io/badge/-GitHub-333333?style=flat&logo=github)
  ![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
  ![colab](https://img.shields.io/badge/-colab-333333?style=flat&logo=colabbadge)
  ![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-333333?style=flat&logo=visual-studio-code&logoColor=007ACC)
  [![Jira](https://badgen.net/badge/icon/jira?icon=jira&label)](https://https://jira.com/)

## Enlaces
<div align="center">

[Jira](https://jimenafioni.atlassian.net/jira/software/projects/PF/boards/2) <br>
[Notion](https://www.notion.so/Proyecto-Final-Henry-ee9df2791c4f4a508387789dc02b842e)<br>
[Drive](https://drive.google.com/drive/folders/1WnKWhaJwMHU0AG0Dm_H0j3qp9_FhGpYF)<br>
[GoogleCloudStorage](https://console.cloud.google.com/storage/browser?project=pf-data-science&prefix=&forceOnBucketsSortingFiltering=true)<br>
[Modelo_ML](https://github.com/DATASCIENTISTSHENRY/MODELO-ML)<br>
[Diccionario_de_datos](https://docs.google.com/spreadsheets/d/1ZPpcAVBxUZQtUsaX5dnRoTXet916yMVO/edit?usp=drive_link&ouid=108785850922164963725&rtpof=true&sd=true)<br>
</div>

## Objetivo y Alcance 📚

El objetivo de este proyecto es obtener un entendimiento del proceso migratorio en Argentina.<br> 
Se analizará la relación entre indicadores económicos, ambientales, sociales y la migración. Se buscará determinar de qué manera se ve afectada la cantidad de migrantes de argentina al modificarse dichos indicadores.
Se realizará una caracterización del proceso migratorio en Argentina, el mismo incluirá el análisis de la cantidad, países de origen y destino de migrantes. Se investigará la distribución geográfica de la población inmigrante en Argentina, analizando las provincias en las cuales se  radican los inmigrantes.
Se determinarán y calcularán indicadores claves de desempeño que tengan como propósito alcanzar una distribución homogénea de inmigrantes en el país. 
El resultado de este análisis se presentará en un dashboard interactivo. También se presentará un modelo de aprendizaje automático que dará como resultado el porcentaje de variación de la cantidad de inmigrantes en Argentina al modificar los indicadores estudiados.
 
## [Fuentes de datos](./FUENTES_DATOS/FuentesdeDatos.md) -- Enlace a la descripción 📚

#### [UNITED NATIONS](https://www.un.org/development/desa/pd/content/international-migrant-stock )

#### [BANCO MUNDIAL](https://datos.bancomundial.org/indicador/SM.POP.NETM)

#### [DATOS DEL GOBIERNO ARGENTINO](https://datos.gob.ar/dataset/interior-ingresos-egresos-personas-al-pais-residencias-otorgadas)



#### [DATOS DEL GOBIERNO ARGENTINO](https://www.argentina.gob.ar/interior/renaper/estadistica-de-poblacion/informes-provinciales)



##	Relación entre migración e indicadores económicos sociales y ambientales. 

En esta sección se busca estudiar la relacion entre a migración y los indicadores que se muestran en el gráfico a continuación. 


<div align="center">
  <img src='./assets/Indicadores_migracion.png'>
  <br> 
</div>


El dashboard diseñado en este trabajo cuenta con dos páginas donde puede evaluarse interactivamente la relación entre indicadores y migración.

Para abordar el estudio de la relación entre indicadores y la migración neta se trabajó con dos enfoques. Se estudió la relación entre indicadores y migración neta teniendo en cuenta datos de todos los países en el periodo de tiempo estudiado. Se calcularon los coeficientes de regresión lineal entre migración y cada uno de los indicadores. <br>
Luego, teniendo en cuenta que para cada país la variación de un determinado indicador puede afectar de manera diferente, debido a características únicas de cada país, se realizó el mismo análisis pero sólo considerando los datos de **Argentina**, que es nuestro pais de interés. Para ello se determinó la correlación entre migración neta y los indicadores con su variación en el tiempo. Los valores de coeficientes de regresión para el análisis con datos del mundo fueron más bajos que los valores encontrados para Argentina. Sin embargo, ambos análisis arrojaron que los indicadores más correlacionados con la migración neta son:

- Nivel de Ingresos: A mayor nivel de ingresos, mayor migración neta.
- Tasa de Pobreza: A mayor tasa de pobreza, menor migración neta.
- Cantidad de Importaciones: A mayor cantidad de importación, mayor migración neta.

La correlación positiva entre importaciones y migración neta es un hallazgo interesante, que se dio con bastante intensidad para los dos enfoques. Podría estudiarse el tema en profundidad para comprender el sentido de dicha correlación. Estudiar qué representa para el país un aumento en las importaciones y por qué afecta a la migración neta del país.


##  Caracterización del proceso migratorio en Argentina
### Principales países de origen y destino de migrantes en Argentina y su evolución en el tiempo. <br>
El dashboard también contiene una sección con información de los principales países de origen de los inmigrantes de Argentina y los países de destino que elijen quienes emigran de Argentina. Esta información analizada en el periodo de tiempo desde 1990 a 2020. Puede observarse que en 1990 el origen principal de los inmigrantes era Italia, luego a partir de 1995 pasó a ser Paraguay. Los países destino que tienen mayor cantidad de inmigrantes Argentinos son España y Estados Unidos. Son los principales destinos de los argentinos en el periodo estudiado.

Analizando los indicadores de los países de origen y destino, se puede ver que los países de destino tales como España, Estados Unidos Israel tienen valores de importaciones más altas que los países de origen. Este análisis es concordante con la correlación encontrada entre los indicadores y la migración neta. Sin embargo con respecto a la pobreza, Argentina es la que tiene el indicador más alto y sin embargo recibe inmigrantes de países en mejor situación. Esto puede deberse a que son otros factores no analizados los que están impulsando la migración hacia Argentina. Con respecto al índice de mortalidad, los países de origen de inmigrantes en general tienen valores más altos. A nivel global no se observó correlación entre migración neta y la tasa de mortalidad, pero para los países involucrados en el proceso migratorio de Argentina parecería tener injerencia. Con respecto al desempleo, Argentina tiene un valor de indicador más elevado que el de los países de origen de sus inmigrantes.




* Estructura poblacional de inmigrantes en Argentina <br>
* Radicación de inmigrantes dentro de Argentina.<br>



##  Radicación de inmigrantes dentro de Argentina
* Distribución de Inmigrantes por Provincias:  
La provincia de Buenos Aires alberga casi la mitad de los inmigrantes en Argentina, con un impresionante 46.6% de la población inmigrante residiendo allí. Le sigue la Ciudad Autónoma de Buenos Aires, que acoge al 28.68%. Esto indica una marcada concentración en el área metropolitana más grande del país por lo que como parte del nuestra propuesta, decidimos trabajar en distribuir los flujos hacia el interior.

* Origen de los Inmigrantes:  
Los países vecinos, como Paraguay y Bolivia, representan conjuntamente más del 50% de la población inmigrante en Argentina. Con Paraguay liderando con un 29.84% y Bolivia con un 21.77%, estos datos subrayan la influencia significativa de las naciones limítrofes en el flujo migratorio hacia Argentina.

* Distribución por Género y Edad:  
La mayoría de los inmigrantes son mujeres, representando un 51.64% de la población inmigrante total. En cuanto a la edad, los grupos de 30 a 54 años abarcan casi el 40% de la población inmigrante, destacando una migración predominantemente en edad laboral.

* Implicaciones Socioeconómicas:  
La preeminencia de provincias como Buenos Aires y la alta concentración de inmigrantes de países vecinos pueden tener repercusiones en la dinámica económica y social del país. Esto puede incluir una diversidad cultural enriquecedora, pero también desafíos en términos de integración, empleo y servicios sociales que se no se deben descuidar.

* Retos y Oportunidades:  
La concentración geográfica y la diversidad de orígenes sugieren la necesidad de programas de integración cultural y laboral adaptados a las necesidades específicas de estos grupos. Además, la distribución por género y edad destaca la importancia de políticas que aborden tanto las necesidades laborales como las de integración familiar y social.  

Estos datos revelan patrones significativos en la radicación de inmigrantes en Argentina, ofreciendo una visión detallada de las áreas clave que podrían requerir enfoque por parte de políticas públicas y programas de integración.



---
## Indicadores de desempeño KPI- Distribución Homogénea en el país (Argentina)

Existe en Argentina una concentración de población tanto nativa como inmigrante en la provincia de Buenos Aires y CABA. A través de los siguientes indicadores claves de desempeño se busca monitorear y definir objetivos para favorecer una mejor dispersión de inmigrantes dentro del territorio Argentino. 
Algunos de los beneficios de tener una distribución más homogénea son: 
•	Fomentar la diversidad cultural y social. Esto puede enriquecer la vida comunitaria y promover la tolerancia y la comprensión entre personas de diferentes orígenes culturales y étnicos.
•	Estimular el crecimiento económico en áreas más pequeñas y menos desarrolladas.
•	Contrarrestar la tendencia de despoblación en áreas rurales o menos desarrolladas

Para establecer los KPI se definen las siguientes zonas:

Zona de alta radicación de inmigrantes: Ciudad Autónoma de Bs As y Provincia de Buenos Aires<br>
Zona de radicación intermedia de inmigrantes: Córdoba, Santa Fe, Mendoza y Neuquén<br>
Zona de baja radicación de inmigrantes: La Pampa, Santa Cruz, La Rioja, Tucumán y Formosa<br>

---
### 🎯 KPI Reducción de residencias otorgadas en zona de alta radicación de inmigrantes. 
***
**Objetivo**  
Disminuir la proporción de inmigrantes que se radican en CIUDAD AUTÓNOMA DE BUENOS AIRES (CABA) y BUENOS AIRES, fomentando la redistribución de residencias hacia otras provincias argentinas.

**Fórmula**<br>
 KPI1= [(Residencias zona de alta radicación/Residencias Totales) trimestre anterior − (Residencias zona de alta radicación /Residencias Totales) trimestre actual]*100/Residencias zona de alta radicación/Residencias Totales) trimestre anterior 

**Justificación**
Este indicador busca medir la variación trimestral en la proporción de residencias otorgadas en CIUDAD AUTÓNOMA DE BUENOS AIRES (CABA) y BUENOS AIRES en relación con el total de residencias otorgadas en el país. Una disminución en este valor indica una tendencia positiva hacia la redistribución de inmigrantes hacia otras provincias argentinas, promoviendo una distribución más equitativa y balanceada de la migración en el país.  

---
### 🎯 KPI Aumento de residencias otorgadas en zona de radicación intermedia de inmigrantes. 
***
**Objetivo**  
Aumentar la proporción de inmigrantes que se radican en la zona de radicación intermedia, incentivando la migración hacia estas regiones y diversificando la distribución de residencias.

**Fórmula**<br>
KPI2=  [(Residencias zona radicación intermedia / Residencias Totales) trimestre actual− (Residencias zona radicación intermedia / Residencias Totales) trimestre anterior]*100/Residencias zona radicación intermedia / Residencias Totales) trimestre anterior


**Justificación**
Este indicador busca medir la variación trimestral en la proporción de residencias otorgadas en las cinco provincias con mayor cantidad de inmigrantes después de BUENOS AIRES, en relación con el total de residencias entregadas en el país. Un incremento en este valor refleja un aumento en la migración hacia estas provincias, lo cual implica una diversificación y desconcentración de la inmigración hacia regiones más allá de las principales urbes, promoviendo un desarrollo más equilibrado en el interior del país. 

---
### 🎯 KPI Aumento de residencias otorgadas en zona de baja radicación de inmigrantes. 
***
**Objetivo**  
Aumentar la proporción de inmigrantes que se radican en las zonas de baja radicación, fomentando la migración hacia estas regiones y contribuyendo a un mayor equilibrio en la distribución demográfica.

**Fórmula**<br>
KPI3=[(Residencias en zona de radicación baja / Residencias Totales) trimestre actual − (Residencias en zona de radicación baja/ Residencias Totales) trimestre anterior]*100/Residencias en zona de radicación baja/ Residencias Totales) trimestre anterior

**Justificación**
Este indicador mide la variación trimestral en la proporción de residencias otorgadas en las cinco provincias con menos radicaciones en relación con el total de residencias entregadas en el país. Un incremento en este valor refleja un aumento en la migración hacia estas provincias menos pobladas, lo que contribuye a descentralizar la concentración demográfica, estimular el desarrollo en áreas menos densamente pobladas y promover un equilibrio territorial más sostenible en Argentina.

---
## Stack Tecnológico
![Enlace](./assets/Workflow_Google_Cloud.png)

Para este proyecto es importante contar con una infraestructura sólida, escalable y segura. Es por eso que hemos elegido como stack tecnológico `Google Cloud Platform (GCP)`.

GCP nos ofrece una integración perfecta entre sus servicios, lo que permite un flujo de datos desde el almacenamiento hasta el análisis y la visualización. Esto es esencial para mantener la consistencia y precisión de los datos en todas las etapas del proyecto.
La escalabilidad de los servicios de GCP asegura que el proyecto pueda manejar grandes volúmenes de datos a medida que crece sin perder rendimiento. Esto es un punto muy fuerte ya que es común que en los proyectos relacionados con los datos, este aspecto se pase por alto.
También, ofrece una estructura de precios flexible que se adapta a las necesidades del proyecto. Esto significa que, al utilizar servicios específicos, se puede optimizar el costo, asegurando que el proyecto sea rentable sin sacrificar la calidad del análisis, ya que solo se paga por los recursos que se consumen y utilizan.


Video explicativo de la automatización [Enlace](https://drive.google.com/file/d/19sRh8OGCS8TRUH1Kb6oef4B0fGLy8gEs/view?usp=drive_link)

Para este proyecto vamos a utilizar 3 servicios de GCP.<br>
El primer servicio es `Cloud Storage`, que lo utilizaremos como Data Lake, el cual van a estar los datasets que obtengamos de las investigaciones. Cloud Storage permite almacenar grandes volúmenes de datos de manera segura y proporciona acceso rápido para análisis posteriores.
El segundo servicio es `Cloud Functions`, que lo utilizaremos para los pipelines de automatización. Acá vamos a crear 2 Pipelines. Uno para la Limpieza de los datasets que ingresan al Cloud Storage, y el otro para la transformación de esos datos y poder insertarlos en nuestro Data Warehouse.
Y el tercer servicio, utilizaremos `BigQuery` como Data Warehouse. En Bigquery podemos manejar un gran volumen de datos y poder realizar consultas de manera eficiente.

La automatización de tareas se ha logrado mediante el uso de Cloud Functions. Se han desarrollado dos funciones programadas en Python:

- ***Function 01 - ETL***: Esta función se encarga de ejecutar el proceso de Extracción,
Transformación y Carga (ETL) de los dataset que se guarden o actualicen en el primer bucket del `Cloud Storage`. Además, valida la estructura de los datos para que no haya errores al cargar los datasets equivocados, asegurando su adecuada preparación para su posterior análisis.

- ***Function 02 - Upload to BigQuery***: Esta función se ocupa de importar los datos procesados desde el bucket
que alberga los datasets limpios hacia el Datawarehouse. Pero antes realiza la validacion de los registros de la tabla en la cual se cargan los datasets, para que no hayan filas duplicadas, una vez validados, carga solo los nuevos registros de manera correta.

Es importante destacar que estas funciones realizan todo el trabajo de manera automatizada, dando eficiencia a la carga incremental en el DataWarehouse. Una vez realizado esto, se podra realizar querys en SQL para poder realizar analisis de los datos y poder visualizarlos posteriormente.

Finalmente, se utiliza `Power Bi` para la creación y diseño del dashboard y paneles
de control que permitirán una visualización efectiva de los datos. Además, se
implementan procesos de Machine Learning para la creación de un sistema de
recomendación basado en técnicas de aprendizaje automático

---
## Modelo de Machine Learning 
[Enlace](https://github.com/DATASCIENTISTSHENRY/MODELO-ML)

El propósito principal del modelo consiste en estimar el impacto de las variaciones en diversos indicadores, tales como Ingresos per cápita, Acceso a electricidad, Crecimiento PBI per cápita, Importaciones de Mercadería, Personas desempleadas de educación avanzada, Pobreza y Mortalidad, en la cantidad de inmigrantes que recibe argentina. Se puede ingresar a probar el modelo en el siguiente [link](https://migracion.streamlit.app/)
<div align="center">

![ModeloML](./assets/ModeloML.JPG)

</div><br>

























