# 🌍 Análisis de Ciudades Turísticas Mundiales

Análisis exploratorio de datos (EDA) completo de un dataset de ciudades turísticas con ratings de actividades y datos climáticos.

## 📊 Descripción del Proyecto

Este proyecto realiza un análisis exhaustivo de ciudades turísticas mundiales, evaluando diferentes aspectos como cultura, aventura, naturaleza, playas, vida nocturna, gastronomía, wellness, ambiente urbano y aislamiento. El objetivo es identificar patrones, correlaciones y generar insights estratégicos para el sector turístico.

## 🗂️ Estructura del Proyecto

proyecto-turismo/
├── data/
│   └── raw/
│       └── Worldwide Travel Cities Dataset (Ratings and Climate).csv
├── notebooks/
│   ├── 01_exploracion_inicial.ipynb
│   ├── 02_limpieza_preprocesamiento.ipynb
│   ├── 03_analisis_completo.ipynb
│   └── 04_dashboard_ejecutivo.ipynb
└── README.md

## 📋 Dataset

**Fuente:** Worldwide Travel Cities Dataset (Ratings and Climate): https://www.kaggle.com/datasets/furkanima/worldwide-travel-cities-ratings-and-climate

**Dimensiones:** 560 ciudades × 19 variables

**Variables principales:**
- **Identificación:** id, city, country, region
- **Geográficas:** latitude, longitude, avg_temp_monthly
- **Ratings de actividades:** culture, adventure, nature, beaches, nightlife, cuisine, wellness, urban, seclusion (escala 1-10)
- **Información turística:** ideal_durations, budget_level, short_description

## 🔧 Instalación y Configuración

### Dependencias

pandas>=1.3.0
numpy>=1.20.0
matplotlib>=3.5.0
seaborn>=0.11.0
scipy>=1.7.0

### Configuración

import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

## 📈 Fases del Análisis
### Fase 1: Exploración Inicial

- Carga y verificación de datos
- Análisis de calidad de datos
- Estadísticas descriptivas básicas
- Visualizaciones iniciales
- Detección preliminar de problemas

### Fase 2: Limpieza y Preprocesamiento

- #### Limpieza de datos:

- Tratamiento de valores nulos
- Eliminación de duplicados
- Validación de rangos
- Conversión de tipos de datos


- #### Detección de outliers:

- Método IQR
- Z-Score
- Análisis de ciudades extremas


- #### Creación de variables derivadas:

- avg_activity_rating: Promedio de todos los ratings
- rating_category: Categorías de calidad (Bajo/Medio/Alto/Excelente)
- temp_category: Categorías climáticas
- Índices combinados (aventura+naturaleza, cultura+gastronomía, etc.)



### Fase 3: Análisis Exploratorio Completo

- **Análisis Univariado:** Distribuciones, histogramas, estadísticas por variable
- **Análisis Bivariado:** Matriz de correlaciones, scatter plots de relaciones significativas
- **Análisis Multivariado:** Análisis por región, patrones complejos
- **Extracción de Insights:** Identificación de patrones clave y recomendaciones

### Fase 4: Dashboard Ejecutivo

- Panel de KPIs principales
- Ranking de mejores destinos
- Análisis radar de actividades
- Análisis geográfico
- Segmentación por tipo de experiencia
- Recomendaciones estratégicas

## 🎯 Funcionalidades Principales
### Análisis de Calidad de Datos

def clean_cities_data(df)
def detect_outliers_tourism(df)
def create_derived_variables_tourism(df)

### Análisis Exploratorio

def univariate_analysis_tourism(df)
def bivariate_analysis_tourism(df)
def multivariate_analysis_tourism(df)
def extract_insights_tourism(df, matriz_corr, strong_correlations)

### Dashboard Ejecutivo

def create_main_dashboard(df)
def segmentation_analysis(df)
def generate_recomandations(df)
def final_executive_dashboard(df, recomandations)

## 📊 Principales Métricas y KPIs


- **Rating Promedio Global:** Media de todas las actividades
- **Top Destinos:** Ciudades mejor valoradas
- **Distribución Geográfica:** Análisis por regiones
- **Temperatura Promedio:** Condiciones climáticas
- **Duración Ideal:** Tiempo recomendado de estancia
- **Segmentación:** Por tipo de experiencia dominante

## 🔍 Insights Clave Identificados

1. **Correlaciones Significativas:** Entre diferentes tipos de actividades
2. **Patrones Geográficos:** Performance por región
3. **Segmentación:** Clasificación por experiencia dominante
4. **Oportunidades:** Ciudades con alto potencial de crecimiento
5. **Benchmarking:** Comparativa entre destinos similares

## ⚠️ Problemas Identificados y Solucionados
### Errores Corregidos:

1. **División por cero** en cálculos de porcentajes
2. **Problemas de visualización** en gráficos
3. **Manejo de datos faltantes** en temperatura
4. **Conversión de tipos** para columnas numéricas


### Mejoras Implementadas:

- Validación robusta de datos antes de operaciones
- Manejo de errores con try-except
- Conversión inteligente de datos categóricos a numéricos
- Visualizaciones adaptativas según datos disponibles

## 🚀 Uso del Proyecto
### Ejecución Secuencial:
*Fase 1: Exploración* 
df, statistics, quality_info = main_phase1_cities()

*Fase 2: Limpieza*
df_clean, outliers_info = main_phase2_cities(df)

*Fase 3: Análisis Completo*
results = main_phase3_tourism(df_clean)

*Fase 4: Dashboard*
dashboard_results = main_dashboard_completed(df_clean)

## 📈 Resultados Esperados

- **Dataset Limpio:** Datos procesados y validados
- **Variables Derivadas:** Métricas adicionales para análisis
- **Correlaciones:** Identificación de relaciones significativas
- **Visualizaciones:** Gráficos informativos y profesionales
- **Recomendaciones:** Insights accionables para el sector turístico
- **Dashboard:** Panel ejecutivo para toma de decisiones

## 🛠️ Personalización
El código está diseñado para ser adaptable:

- **Fácil modificación** de umbrales y parámetros
- **Visualizaciones configurables** según necesidades
- **Métricas personalizables** para diferentes contextos
- **Extensible** para nuevas variables y análisis

## 📝 Notas Técnicas

- **Compatibilidad:** Python 3.7+
- **Rendimiento:** Optimizado para datasets de hasta 1000+ ciudades
- **Memoria:** Uso eficiente con validaciones preventivas
- **Robustez:** Manejo de errores en todas las fases críticas

## 🤝 Contribuciones
El proyecto está estructurado de manera modular para facilitar:

- Adición de nuevas métricas
- Mejoras en visualizaciones
- Extensión a otros datasets turísticos
- Implementación de nuevos algoritmos de análisis







