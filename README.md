# Currency Exchange Rate Tracker (ETL Pipeline)

A lightweight Data Engineering pipeline built in Python to extract real-time currency exchange rates (USD, EUR, BTC) from a public REST API, clean and transform the payload using Pandas, and persist time-series data into a PostgreSQL database running inside a Docker container.

---

## Architecture & Data Flow

```text
[ AwesomeAPI REST API ] 
         │ (HTTP GET)
         ▼
  [ Python Script ] ──► [ Pandas Data Transformation ] ──► [ PostgreSQL / Docker ]
