import logging
import pandas as pd
from pathlib import Path
from typing import TypedDict

logger = logging.getLogger(__name__)


class LimpezaStats(TypedDict, total=True):
    antes: int
    depois: int


def ler_csv(caminho: str | Path, encoding: str = "utf-8", sep: str = ",") -> pd.DataFrame:
    try:
        return pd.read_csv(caminho, encoding=encoding, sep=sep)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}") from e
    except UnicodeDecodeError as e:
        raise ValueError(
            f"Erro de encoding em '{caminho}'. Tente encoding='cp1252'."
        ) from e


def limpar_nulos(
    df: pd.DataFrame,
    subset: list[str] | None = None,
) -> tuple[pd.DataFrame, LimpezaStats]:
    if subset is not None:
        faltando = [c for c in subset if c not in df.columns]
        if faltando:
            raise ValueError(f"Colunas não encontradas no DataFrame: {faltando}")

    df_limpo = df.dropna(subset=subset).copy()
    stats: LimpezaStats = {"antes": len(df), "depois": len(df_limpo)}
    logger.info("Limpeza: %d → %d linhas", stats["antes"], stats["depois"])
    return df_limpo, stats


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python limpeza.py <arquivo.csv> [arquivo_saida.csv]")
        sys.exit(1)

    logging.basicConfig(level=logging.INFO)

    try:
        df_raw = ler_csv(sys.argv[1])
        df_limpo, stats = limpar_nulos(df_raw)
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

    removidas = stats["antes"] - stats["depois"]
    print(f"Linhas antes: {stats['antes']} | depois: {stats['depois']} | removidas: {removidas}")

    if len(sys.argv) > 2:
        saida = Path(sys.argv[2])
        if saida.exists():
            print(f"Aviso: '{saida}' já existe e será sobrescrito.")
        df_limpo.to_csv(saida, index=False)
        print(f"Arquivo salvo em: {saida}")
