from utils.horario import status_pregao


def gerar_relatorio(dados):
    """
    Prints a formatted market summary to the terminal.

    Args:
        dados (dict): Consolidated data with structure:
            {
                "dolar": {"Google": 5.14, ...},
                "euro": {"Yahoo": 5.90, ...},
                "ibovespa": {"Google": 168306.02, ...}
            }

    Returns:
        None: Prints directly to the console.
    """
    print("\n📊 MARKET SUMMARY")
    print("=" * 40)
    print(f"Status: {status_pregao()}\n")

    for moeda, fontes in dados.items():
        print(f"{moeda.capitalize()}:")
        for fonte, valor in fontes.items():
            if valor:
                if moeda == "ibovespa":
                    print(f"  {fonte}: {valor:.2f} pontos")
                else:
                    print(f"  {fonte}: R$ {valor:.4f}")
            else:
                print(f"  {fonte}: ❌ not available")
        print()
