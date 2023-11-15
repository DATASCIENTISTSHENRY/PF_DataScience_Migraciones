

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


<div align="center">
  <img src='./assets/Indicadores_migracion.png'>
  <br> 
</div>

##  Caracterización del proceso migratorio en Argentina
* Principales países de origen y destino de migrantes en Argentina y su evolución en el tiempo. <br>
* Estructura poblacional de inmigrantes en Argentina <br>
* Radicación de inmigrantes dentro de Argentina.<br>





---
## Indicadores de desempeño KPI- Distribución Homogénea en el país (Argentina)

Existe en Argentina una concentración de población tanto nativa como inmigrante en la provincia de Buenos Aires y CABA. A través de los siguientes indicadores claves de desempeño se busca monitorear y definir objetivos para favorecer una mejor dispersión de inmigrantes dentro del territorio Argentino. 
Algunos de los beneficios de tener una distribución más homogénea son: 
•	Fomentar la diversidad cultural y social. Esto puede enriquecer la vida comunitaria y promover la tolerancia y la comprensión entre personas de diferentes orígenes culturales y étnicos.
•	Estimular el crecimiento económico en áreas más pequeñas y menos desarrolladas.
•	Contrarrestar la tendencia de despoblación en áreas rurales o menos desarrolladas

Para establecer los KPI se definen las siguientes zonas:

Zona de alta radicación de inmigrantes: Ciudad Autónoma de Bs As y Provincia de Buenos Aires
Zona de radicación intermedia de inmigrantes: 
Zona de baja radicación de inmigrantes:

---
### 🎯 KPI Reducción de residencias otorgadas en zona de alta radicación de inmigrantes. 
***
**Objetivo**  
Disminuir la proporción de inmigrantes que se radican en CIUDAD AUTÓNOMA DE BUENOS AIRES (CABA) y BUENOS AIRES, fomentando la redistribución de residencias hacia otras provincias argentinas.

**Fórmula**<br>
 KPI1= (Residencias zona de alta radicación/Residencias Totales) trimestre actual − (Residencias zona de alta radicación /Residencias Totales) trimestre anterior


**Justificación**
Este indicador busca medir la variación trimestral en la proporción de residencias otorgadas en CIUDAD AUTÓNOMA DE BUENOS AIRES (CABA) y BUENOS AIRES en relación con el total de residencias otorgadas en el país. Una disminución en este valor indica una tendencia positiva hacia la redistribución de inmigrantes hacia otras provincias argentinas, promoviendo una distribución más equitativa y balanceada de la migración en el país.  

---
### 🎯 KPI Aumento de residencias otorgadas en zona de radicación intermedia de inmigrantes. 
***
**Objetivo**  
Aumentar la proporción de inmigrantes que se radican en la zona de radicación intermedia, incentivando la migración hacia estas regiones y diversificando la distribución de residencias.

**Fórmula**<br>
KPI2=  (Residencias zona radicación intermedia / Residencias Totales) trimestre actual− (Residencias zona radicación intermedia / Residencias Totales) trimestre anterior.


**Justificación**
Este indicador busca medir la variación trimestral en la proporción de residencias otorgadas en las cinco provincias con mayor cantidad de inmigrantes después de BUENOS AIRES, en relación con el total de residencias entregadas en el país. Un incremento en este valor refleja un aumento en la migración hacia estas provincias, lo cual implica una diversificación y desconcentración de la inmigración hacia regiones más allá de las principales urbes, promoviendo un desarrollo más equilibrado en el interior del país. 

---
### 🎯 KPI Aumento de residencias otorgadas en zona de baja radicación de inmigrantes. 
***
**Objetivo**  
Aumentar la proporción de inmigrantes que se radican en las zonas de baja radicación, fomentando la migración hacia estas regiones y contribuyendo a un mayor equilibrio en la distribución demográfica.

**Fórmula**<br>
KPI3=(Residencias en zona de radicación baja / Residencias Totales) trimestre actual − (Residencias en zona de radicación baja/ Residencias Totales) trimestre anterior.

**Justificación**
Este indicador mide la variación trimestral en la proporción de residencias otorgadas en las cinco provincias con menos radicaciones en relación con el total de residencias entregadas en el país. Un incremento en este valor refleja un aumento en la migración hacia estas provincias menos pobladas, lo que contribuye a descentralizar la concentración demográfica, estimular el desarrollo en áreas menos densamente pobladas y promover un equilibrio territorial más sostenible en Argentina.
---
## Pipeline de la Automatización 
[Enlace]()

---
## Modelo de Machine Learning 
[Enlace](https://github.com/DATASCIENTISTSHENRY/MODELO-ML)

El propósito principal del modelo consiste en estimar el impacto de las variaciones en diversos indicadores, tales como Ingresos per cápita, Acceso a electricidad, Crecimiento PBI per cápita, Importaciones de Mercadería, Personas desempleadas de educación avanzada, Pobreza y Mortalidad, en la cantidad de inmigrantes que recibe argentina. Se puede ingresar a probar el modelo en el siguiente [link](https://migracion.streamlit.app/)
<div align="center">

![ModeloML](./assets/ModeloML.JPG)

</div><br>

























