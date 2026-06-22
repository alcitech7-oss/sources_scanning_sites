import requests


class AwesomeDolar:
    """
    Captures the USD/BRL exchange rate using the Awesome API.
    No token or Selenium required — pure HTTP request.
    """

    def __init__(self):
        self.nome = "Awesome API Dólar"

    def pegar(self):
        """
        Fetches the current USD/BRL exchange rate.

        Returns:
            float: The exchange rate value, or None if an error occurs.
        """
        try:
            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
            resposta = requests.get(url)
            dados = resposta.json()
            return float(dados["USDBRL"]["bid"])
        except Exception as e:
            print(f"Erro na Awesome API: {e}")
            return None
