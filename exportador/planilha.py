import pandas as pd
from datetime import datetime
from utils.horario import status_pregao
from utils.formatador import formatar_moeda, formatar_ibovespa


def gerar_planilha(dados):
    """
    Generates an Excel spreadsheet from the consolidated data.

    Args:
        dados (dict): Consolidated data with structure:
            {
                "dolar": {"Google": 5.14, ...},
                "euro": {"Yahoo": 5.90, ...},
                "ibovespa": {"Google": 168306.02, ...}
            }

    Returns:
        None: Saves the file to disk and prints a confirmation message.
    """
    linhas = []
    for moeda, fontes in dados.items():
        for fonte, valor in fontes.items():
            linhas.append(
                {
                    "Moeda": moeda.capitalize(),
                    "Fonte": fonte,
                    "Valor": (
                        formatar_ibovespa(valor)
                        if moeda == "ibovespa"
                        else formatar_moeda(valor)
                    ),
                    "Status": status_pregao(),
                }
            )

    df = pd.DataFrame(linhas)
    nome = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    df.to_excel(nome, index=False)
    print(f"✅ Planilha gerada: {nome}")
