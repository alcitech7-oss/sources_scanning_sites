import requests


class AwesomeEuro:
    """
    Captures the EUR/BRL exchange rate using the Awesome API.
    No token or Selenium required — pure HTTP request.
    """

    def __init__(self):
        self.nome = "Awesome API Euro"

    def pegar(self):
        """
        Fetches the current EUR/BRL exchange rate.

        Returns:
            float: The exchange rate value, or None if an error occurs.
        """
        try:
            url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
            resposta = requests.get(url)
            dados = resposta.json()
            return float(dados["EURBRL"]["bid"])
        except Exception as e:
            print(f"Erro na Awesome Euro: {e}")
            return None
