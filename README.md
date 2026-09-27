# 💱 Currency Exchange Rate Tracker

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat-square&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=flat-square&logo=docker)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas)

A lightweight Data Engineering pipeline built in Python to extract real-time currency exchange rates (USD, EUR, BTC) from a public REST API, clean and transform the payload using Pandas, and persist time-series data into a PostgreSQL database running inside a Docker container.

---

## 🏗️ Architecture & Data Flow

```text
[ AwesomeAPI REST API ] 
         │ (HTTP GET)
         ▼
  [ Python Script ] ──► [ Pandas Data Transformation ] ──► [ PostgreSQL / Docker ]