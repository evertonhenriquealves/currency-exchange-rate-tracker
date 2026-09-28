# 💱 Currency Exchange Rate Tracker

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat-square&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=flat-square&logo=docker)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas)

🇬🇧 A lightweight Data Engineering pipeline built in Python to extract real-time currency exchange rates (USD, EUR, BTC) from a public REST API, clean and transform the payload using Pandas, and persist time-series data into a PostgreSQL database running inside a Docker container.

🇧🇷 Um pipeline leve de Engenharia de Dados desenvolvido em Python para extrair cotações de moedas em tempo real (USD, EUR, BTC) de uma API REST pública, limpar e transformar os dados com Pandas e armazenar séries temporais em um banco de dados PostgreSQL rodando em container Docker.

---

## 🏗️ Architecture & Data Flow

```
[ AwesomeAPI REST API ] 
         │ (HTTP GET)
         ▼
  [ Python Script ] ──► [ Pandas Data Transformation ] ──► [ PostgreSQL / Docker ]

```

1. **Extraction:** Consumes current exchange rates from AwesomeAPI (`USD-BRL`, `EUR-BRL`, `BTC-BRL`).
2. **Transformation:** Parses raw JSON payloads, casts numeric data types (`float`), converts UNIX timestamps to standard `datetime`, and structures records into a Pandas DataFrame.
3. **Loading:** Appends structured records incrementally into the `historico_cotacoes` relational table.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Data Processing:** Pandas, SQLAlchemy, Psycopg2
* **Database:** PostgreSQL 15
* **Infrastructure:** Docker, Docker Compose
* **Version Control:** Git / GitHub

---

## 📁 Repository Structure

```
.
├── docker-compose.yml   # PostgreSQL container orchestration
├── main.py              # ETL pipeline logic (Extract, Transform, Load)
├── requirements.txt     # Python project dependencies
├── .gitignore           # Ignored files and directories
└── README.md            # Technical documentation

```

---

## ⚙️ Setup & Execution

### Prerequisites

* Docker & Docker Compose installed
* Python 3.10+ installed

### Step-by-Step

1. **Clone the repository:**
```bash
git clone [https://github.com/evertonhenriquealves/currency-exchange-rate-tracker.git](https://github.com/evertonhenriquealves/currency-exchange-rate-tracker.git)
cd currency-exchange-rate-tracker

```


2. **Install Python dependencies:**
```bash
pip install -r requirements.txt

```


3. **Start the PostgreSQL container:**
```bash
docker-compose up -d

```


4. **Run the ETL pipeline:**
```bash
python main.py

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
docker exec -it cotacoes_db psql -U user_cotacao -d db_cotacoes -c "\copy historico_cotacoes TO '/tmp/historico_cotacoes.csv' WITH CSV HEADER;"

```



---

## 📊 Target Table Schema (`historico_cotacoes`)

| Column Name | Data Type | Description |
| --- | --- | --- |
| `moeda` | `VARCHAR` | Base currency code (e.g., USD, EUR, BTC) |
| `moeda_destino` | `VARCHAR` | Target currency code (e.g., BRL) |
| `nome` | `VARCHAR` | Full currency pair name |
| `valor_compra` | `FLOAT` | Bid price |
| `valor_venda` | `FLOAT` | Ask price |
| `variacao` | `FLOAT` | Price variation |
| `data_cotacao` | `TIMESTAMP` | Timestamp of the rate quote |

