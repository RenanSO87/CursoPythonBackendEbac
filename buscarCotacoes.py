import os
from datetime import datetime
import pandas as pd
import requests


def buscar_cotacoes():
    """Consome a API pública da AwesomeAPI para buscar cotações atuais de moedas e criptomoedas."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()

        cotacoes = []
        for chave, item in dados.items():
            cotacoes.append(
                {
                    "Ativo": item["name"],
                    "Código": item["code"],
                    "Preço de Compra (R$)": round(float(item["bid"]), 2),
                    "Preço de Venda (R$)": round(float(item["ask"]), 2),
                    "Variação (%)": round(float(item["pctChange"]), 2),
                    "Última Atualização": datetime.fromtimestamp(
                        int(item["timestamp"])
                    ).strftime("%d/%m/%Y %H:%M:%S"),
                }
            )

        return pd.DataFrame(cotacoes)

    except requests.exceptions.RequestException as err:
        print(f"Erro ao conectar com a API: {err}")
        return None


def exportar_relatorios(df):
    """Exporta o DataFrame gerado para arquivos CSV e Excel com carimbo de data/hora."""
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    arquivo_excel = f"data/cotacoes_{timestamp}.xlsx"
    arquivo_csv = f"data/cotacoes_{timestamp}.csv"

    df.to_excel(arquivo_excel, index=False)
    df.to_csv(arquivo_csv, index=False, encoding="utf-8-sig")

    print(f"Relatório Excel salvo em: {arquivo_excel}")
    print(f"Relatório CSV salvo em: {arquivo_csv}")


def main():
    print("Iniciando coleta de dados financeiros...")
    df_cotacoes = buscar_cotacoes()

    if df_cotacoes is not None and not df_cotacoes.empty:
        print("\n--- COTAÇÕES ATUAIS ---")
        print(df_cotacoes.to_string(index=False))
        print("-----------------------\n")

        exportar_relatorios(df_cotacoes)
    else:
        print("Não foi possível gerar os relatórios devido a um erro na coleta.")


if __name__ == "__main__":
    main()