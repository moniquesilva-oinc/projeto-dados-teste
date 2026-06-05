import pandas as pd
import sys


def limpar_nulos(caminho_entrada: str, caminho_saida: str = None) -> pd.DataFrame:
    df = pd.read_csv(caminho_entrada)
    print(f"Linhas antes da limpeza: {len(df)}")

    df_limpo = df.dropna()
    print(f"Linhas após a limpeza: {len(df_limpo)}")
    print(f"Linhas removidas: {len(df) - len(df_limpo)}")

    if caminho_saida:
        df_limpo.to_csv(caminho_saida, index=False)
        print(f"Arquivo salvo em: {caminho_saida}")

    return df_limpo


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python limpeza.py <arquivo.csv> [arquivo_saida.csv]")
        sys.exit(1)

    entrada = sys.argv[1]
    saida = sys.argv[2] if len(sys.argv) > 2 else None
    limpar_nulos(entrada, saida)
