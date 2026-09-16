# 🛠️ Reto 3 — Diseño y Optimización de Flujos de Trabajo ETL Avanzados

> **Curso:** Business Intelligence y Big Data (Nivel 5) | Odisea Data  
> **Reto:** Diseñar y optimizar un flujo ETL avanzado para manejar grandes volúmenes de datos  
> **Herramienta principal:** Apache NiFi  
> **Autor:** Judit Giravent

---

## 🎯 Objetivo

Diseñar, implementar, automatizar y optimizar un flujo de trabajo ETL (Extract, Transform, Load) capaz de:

- Extraer datos de **múltiples fuentes heterogéneas** (CSV, APIs, SQL).
- Aplicar **transformaciones avanzadas** (limpieza, normalización, agregación, enriquecimiento).
- Cargar los datos procesados en un **destino estratégico** (SQLite + export final).
- **Automatizar** la ejecución programada.
- **Optimizar** el rendimiento (paralelización, caché, gestión de cuellos de botella).

---

## 🗺️ Fases del Proyecto

| # | Fase | Estado |
|---|------|--------|
| 0 | Creación de estructura | ✅ |
| 1 | Instalación y prueba de Apache NiFi | ⏳ |
| 2 | Preparación de fuentes de datos (CSV + API + SQL) | ⏳ |
| 3 | Diseño del flujo ETL en NiFi | ⏳ |
| 4 | Automatización y optimización | ⏳ |
| 5 | Ejecución, validación y capturas | ⏳ |
| 6 | Informes y publicación en GitHub | ⏳ |

---

## 📦 Estructura del Proyecto

```text
reto3-etl-avanzado/
├── data/                  # Datos (raw, processed, final)
├── etl/                   # Flujos NiFi, configuración, scripts
├── notebooks/             # Notebooks de exploración y validación
├── outputs/               # Capturas, gráficos y logs
├── docs/                  # Documentación detallada del proceso
├── reports/               # Informes finales
└── presentation/          # Presentación final
```

---

## 🛠️ Stack Tecnológico

- **ETL:** Apache NiFi
- **Fuentes:** CSV, API REST (JSON), SQLite
- **Destino:** SQLite + export CSV/Parquet
- **Lenguaje auxiliar:** Python 3.10+
- **Documentación:** Markdown → PDF

---

## 📦 Entregables

- [ ] **1. Proyecto ETL completo** → `etl/nifi_flows/flujo_principal.json`
- [ ] **2. Informe del proceso ETL** → `reports/informe_proceso_etl.md`
- [ ] **3. Dataset final** → `data/final/dataset_final.csv`
- [ ] **4. Documentación de validación** → `reports/validacion_control_calidad.md`

---

## 🚀 Cómo ejecutar

*(Se completará cuando el flujo esté implementado)*

---

## 👤 Autor

**Judit Giravent**  
Business Analytics Student | Odisea Data