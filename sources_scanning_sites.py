# sources_scanning_sites.py
from coletores.dolar_google import DolarGoogle
from coletores.dolar_yahoo import DolarYahoo
from coletores.dolar_awesome import DolarAwesome
from coletores.dolar_uol import DolarUol
from coletores.euro_yahoo import EuroYahoo
from coletores.euro_awesome import EuroAwesome
from coletores.ibovespa_google import IbovespaGoogle


def testar_fonte(nome, fonte, metodo):
    try:
        if hasattr(fonte, metodo):
            valor = getattr(fonte, metodo)()
            print(
                f"\n🔍 {nome}: {valor}" if valor else f"\n🔍 {nome}: ❌ não encontrado"
            )
        else:
            print(f"\n🔍 {nome}: ❌ método '{metodo}' não existe")
    except Exception as e:
        print(f"\n🔍 {nome}: ❌ Erro: {e}")


if __name__ == "__main__":
    print("🎣 Varrendo fontes de dados...\n")

    testar_fonte("Dólar Google", DolarGoogle(), "pegar")
    testar_fonte("Dólar Yahoo", DolarYahoo(), "pegar")
    testar_fonte("Dólar Awesome", DolarAwesome(), "pegar")
    testar_fonte("Dólar UOL", DolarUol(), "pegar")
    testar_fonte("Euro Yahoo", EuroYahoo(), "pegar")
    testar_fonte("Euro Awesome", EuroAwesome(), "pegar")
    testar_fonte("Ibovespa Google", IbovespaGoogle(), "pegar")
