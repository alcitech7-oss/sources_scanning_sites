# processador/consolidador.py
from coletores.dolar_google import GoogleDolar
from coletores.dolar_yahoo import YahooDolarSelenium
from coletores.dolar_awesome import AwesomeDolar
from coletores.dolar_uol import UOL
from coletores.euro_yahoo import YahooEuroSelenium
from coletores.euro_awesome import AwesomeEuro
from coletores.ibovespa_google import GoogleIbovespa


def consolidar_dados():
    """
    Consolidates financial data from all available sources.

    Returns:
        dict: Structured data with keys:
            - "dolar": Sources and their USD/BRL values
            - "euro": Sources and their EUR/BRL values
            - "ibovespa": Sources and their index values
    """
    return {
        "dolar": {
            "Google": GoogleDolar().pegar(),
            "Yahoo": YahooDolarSelenium().pegar(),
            "Awesome": AwesomeDolar().pegar(),
            "UOL": UOL().pegar_dolar(),
        },
        "euro": {
            "Yahoo": YahooEuroSelenium().pegar(),
            "Awesome": AwesomeEuro().pegar(),
        },
        "ibovespa": {
            "Google": GoogleIbovespa().pegar(),
        },
    }
