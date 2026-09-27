import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# String de conexão explícita com driver psycopg2
DATABASE_URL = "postgresql+psycopg2://user_cotacao:pass_cotacao@localhost:5433/db_cotacoes"
engine = create_engine(DATABASE_URL)

def extrair_cotacoes():
    """Busca cotações em tempo real de Dólar, Euro e Bitcoin via API pública."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao acessar API: {response.status_code}")

def transformar_dados(dados_brutos):
    """Trata o JSON recebido e converte para um DataFrame Pandas padronizado."""
    lista_cotacoes = []
    
    for chave, item in dados_brutos.items():
        lista_cotacoes.append({
            "moeda": item["code"],
            "moeda_destino": item["codein"],
            "nome": item["name"],
            "valor_compra": float(item["bid"]),
            "valor_venda": float(item["ask"]),
            "variacao": float(item["varBid"]),
            "data_cotacao": datetime.fromtimestamp(int(item["timestamp"]))
        })
    
    df = pd.DataFrame(lista_cotacoes)
    return df

def carregar_no_banco(df):
    """Salva os dados tratados na tabela do PostgreSQL (modo append)."""
    with engine.begin() as connection:
        df.to_sql("historico_cotacoes", con=connection, if_exists="append", index=False)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cotações salvas no PostgreSQL com sucesso!")

def executar_pipeline():
    """Orquestra a execução das etapas de Extract, Transform e Load."""
    print("Iniciando pipeline de cotações...")
    dados_brutos = extrair_cotacoes()
    df_tratado = transformar_dados(dados_brutos)
    carregar_no_banco(df_tratado)

if __name__ == "__main__":
    executar_pipeline()