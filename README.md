markdown
# 💱 Currency Exchange Rate Tracker

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat-square&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=flat-square&logo=docker)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas)

A lightweight Data Engineering pipeline built in Python to extract real-time currency exchange rates (USD, EUR, BTC) from a public REST API, clean and transform the payload using Pandas, and persist time-series data into a PostgreSQL database running inside a Docker container.

---
```
## 🏗️ Architecture & Data Flow

```text
[ AwesomeAPI REST API ] 
         │ (HTTP GET)
         ▼
  [ Python Script ] ──► [ Pandas Data Transformation ] ──► [ PostgreSQL / Docker ]

```

---

## 🔍 Quick Queries

Commands to query the loaded records directly from the Docker container:

* **Get all historical records:**
```bash
docker exec -it cotacoes_db psql -U user_cotacao -d db_cotacoes -c "SELECT * FROM historico_cotacoes ORDER BY data_cotacao DESC;"

```


* **Get only the latest quote for each currency:**
```bash
docker exec -it cotacoes_db psql -U user_cotacao -d db_cotacoes -c "SELECT DISTINCT ON (moeda) * FROM historico_cotacoes ORDER BY moeda, data_cotacao DESC;"

```


* **Export table data to a CSV file:**
```bash
docker exec -it cotacoes_db psql -U user_cotacao -d db_cotacoes -c "\copy historico_cotacoes TO 'cotacoes.csv' WITH CSV HEADER;"

