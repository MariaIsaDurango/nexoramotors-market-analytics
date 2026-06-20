img_logo/LogoNexora_Motors.png

# 🚗 Nexora Motors — Market Analytics Dashboard

> Cuadro de mando interactivo y análisis estratégico del mercado de 
> coches de segunda mano en España para el comité directivo de Nexora Motors.

---

## 🏢 Contexto de negocio

**Nexora Motors** es una plataforma digital de compraventa de vehículos 
de segunda mano operando en el mercado español. La dirección ejecutiva 
necesita una herramienta que permita identificar qué variables determinan 
el precio de venta, qué comunidades concentran la oferta y qué tipo de 
vehículo genera mayor interés entre los compradores.

---

## 🎯 Problema detectado

Los mandos intermedios reciben informes tabulares estáticos que dificultan:
- Identificar patrones de pricing por marca, antigüedad y combustible
- Detectar qué mercados geográficos concentran la demanda
- Anticipar qué vehículos generan mayor engagement comprador

---

## 🛠️ Herramienta elegida — Power BI Desktop

### Justificación técnica y de negocio

| Criterio | Justificación |
|---|---|
| **Licencia** | Gratuita para escritorio — sin coste adicional para Nexora Motors |
| **Interactividad** | Filtros cruzados nativos que actualizan todos los gráficos simultáneamente sin código |
| **Audiencia** | Interfaz visual diseñada para usuarios no técnicos — ideal para el comité directivo |
| **Despliegue** | Publicación directa en Power BI Service con URL pública para acceso remoto |
| **Integración** | Importación nativa de CSV — compatible con el dataset limpio generado en Python |
| **Alternativas descartadas** | Streamlit requiere conocimientos de Python para el usuario final · Tableau limita funciones en versión gratuita |

### Componentes técnicos que se documentarán
- **Power Query:** transformaciones y columnas calculadas sobre el dataset limpio
- **DAX:** medidas para KPIs ejecutivos (precio medio, variación por segmento)
- **Visualizaciones:** mínimo 4 gráficos interactivos interconectados
- **Filtros:** segmentación por marca, combustible, ubicación y segmento de precio
---
## 🔀 Fusión de Datasets

### Datasets utilizados
| Dataset | Fuente | Registros | Plataforma |
|---|---|---|---|
| Milanuncios | https://zenodo.org/records/4674757 | 498 | Milanuncios.com |
| Flexicar | https://zenodo.org/records/6438480 | 791 | Flexicar.es |
| **Dataset fusionado** | `data/coches_fusionado.csv` | **1.289** | Ambas |

### Por qué se fusionaron
El dataset original de Milanuncios contaba con 498 registros, por debajo del 
mínimo de 1.000 recomendado para un análisis estadístico robusto. Se incorporó 
el dataset de Flexicar Barcelona para ampliar el volumen y enriquecer el análisis.

### Por qué se usó Python script en lugar de Jupyter Notebook
La fusión se ejecutó mediante el script `notebooks/02_fusion_datasets.py` en 
lugar de un notebook `.ipynb` debido a incompatibilidades del kernel Jupyter 
con Python 3.14 en el entorno Windows. El script es reproducible, documentado 
y produce resultados idénticos a un notebook.

### Proceso de limpieza del dataset Flexicar
| Acción | Columna | Criterio |
|---|---|---|
| Renombrado de columnas | Todas | Estandarización al esquema de Milanuncios |
| Conversión de precio | `precio` | De € completos a K€ (÷1000) |
| Cálculo de antigüedad | `antiguedad` | 2021 - año de fabricación |
| Estandarización de texto | `marca`, `combustible`, `transmision` | Capitalización uniforme |
| Imputación de columnas ausentes | `cv`, `precio_por_cv` | Flexicar no incluye potencia |
| Columna de fuente | `fuente` | Identifica origen del registro |

### Calidad del dataset fusionado
| Métrica | Valor |
|---|---|
| Total registros | 1.289 |
| Duplicados | 0 |
| Nulos críticos (precio, km) | 0 |
| Nulos en cv | 791 (61.4%) — solo registros Flexicar |
| Precio medio | 15,49 K€ |

## 📁 Estructura del repositorio

---

## 📊 Dataset

| Dimensión | Valor |
|---|---|
| Fuente | Milanuncios.com (scraping 9 abril 2021) |
| Repositorio | https://zenodo.org/records/4674757 |
| Licencia | CC BY-NC-SA 4.0 |
| Registros originales | 500 |
| Registros tras limpieza | 498 |
| Variables finales | 19 |

---

## ⚠️ Sesgos y gobernanza

> *Se documentará en Fase 7*

---

## 🔗 URL del Dashboard

> *Se añadirá tras el despliegue*

---

## 👤 Autor
**María Isabel Durango Pérez**  
Proyecto individual — Módulo II: Análisis y Visualización de Datos
