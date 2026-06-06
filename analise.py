import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados"))

import pandas as pd
from limpeza import ler_csv, limpar_nulos

ARQUIVO = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dados",
    "lançamentos.csv",
)


def parse_valor(valor_str) -> float:
    if pd.isna(valor_str):
        return 0.0
    s = str(valor_str).strip().replace("R$", "").strip()
    if s in ("-", ""):
        return 0.0
    negativo = s.startswith("(") and s.endswith(")")
    s = s.strip("()").replace(".", "").replace(",", ".")
    return -float(s) if negativo else float(s)


def resumo_por_projeto(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip()
    df["Projeto"] = df["Projeto"].str.strip()
    df["valor_num"] = df["Valor(R$)"].apply(parse_valor)

    df_filtrado = df[df["Tipo(Natureza)"].isin(["Entrada", "Saída"])].copy()

    resumo = (
        df_filtrado.groupby(["Projeto", "Tipo(Natureza)"])["valor_num"]
        .sum()
        .unstack(fill_value=0)
    )

    resumo.columns = [
        "total_entradas" if "ntrada" in c else "total_saidas"
        for c in resumo.columns
    ]

    for col in ["total_entradas", "total_saidas"]:
        if col not in resumo.columns:
            resumo[col] = 0.0

    resumo["saldo"] = resumo["total_entradas"] - resumo["total_saidas"]
    return resumo.reset_index().rename(columns={"Projeto": "projeto"})


if __name__ == "__main__":
    df_raw = ler_csv(ARQUIVO)
    df, stats = limpar_nulos(df_raw, subset=[" Projeto ", "Tipo(Natureza)", " Valor(R$) "])
    removidas = stats["antes"] - stats["depois"]
    print(f"Linhas antes: {stats['antes']} | depois: {stats['depois']} | removidas: {removidas}")
    resumo = resumo_por_projeto(df)
    print("\nResumo por projeto:")
    print(resumo.to_string(index=False))
