import requests
from bs4 import BeautifulSoup
import json


class UOL:
    """
    Captures USD/BRL and EUR/BRL exchange rates from UOL Economia.
    Uses static HTML parsing with BeautifulSoup.
    """

    def __init__(self):
        self.nome = "UOL Economia"
        self.url = "https://economia.uol.com.br"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def pegar_dolar(self):
        """
        Fetches the USD/BRL exchange rate from the embedded JSON in the HTML.

        Returns:
            float: The exchange rate value, or None if an error occurs.
        """
        try:
            resposta = requests.get(self.url, headers=self.headers)
            pagina = BeautifulSoup(resposta.text, "html.parser")
            bloco = pagina.find("section", class_="currency-exchange")
            if bloco and bloco.get("data-dollar"):
                dados = json.loads(bloco.get("data-dollar"))
                return float(dados["sellPrice"].replace(",", "."))
        except:
            pass
        return None

    def pegar_euro(self):
        """
        Fetches the EUR/BRL exchange rate by searching for text patterns.
        Filters out values related to 'Turismo' and values below 2 (USD-based).

        Returns:
            float: The exchange rate value, or None if an error occurs.
        """
        try:
            resposta = requests.get(self.url, headers=self.headers)
            pagina = BeautifulSoup(resposta.text, "html.parser")

            for texto in pagina.stripped_strings:
                if "Euro" in texto and "R$" in texto and "Turismo" not in texto:
                    import re

                    numeros = re.findall(r"\d+,\d+", texto)
                    if numeros:
                        valor = float(numeros[0].replace(",", "."))
                        if valor > 2:
                            return valor
        except:
            pass
        return None
