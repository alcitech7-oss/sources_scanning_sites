# utils/formatador.py
def formatar_moeda(valor):
    if valor is None:
        return "N/A"
    return f"R$ {valor:.4f}".replace(".", ",")


def formatar_ibovespa(valor):
    if valor is None:
        return "N/A"
    return f"{valor:,.2f}".replace(",", ".")
