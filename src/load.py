import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Salva um DataFrame do Pandas em um arquivo CSV, personalizando o separador e o decimal.
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return


def salvarSQlite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    """A função serve para salvar o SQLite"""

    conn = sqlite3.connect(nome_banco)
    """Conn" = esta classe conecta com o método "nome_banco" """

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):

    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return


# "ORM" = é uma comunicação entre o banco de dados e a aplicação.
