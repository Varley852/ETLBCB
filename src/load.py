import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Salva um DataFrame do Pandas em um arquivo CSV, personalizando o separador e o decimal."""
    df.to_csv(nome_arquivo, sep= separador, decimal= decimal)
    return