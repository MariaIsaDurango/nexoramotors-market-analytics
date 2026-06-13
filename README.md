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