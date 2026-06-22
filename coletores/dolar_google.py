from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re


class GoogleDolar:
    """
    Captures the USD/BRL exchange rate from Google Finance.
    Uses Selenium in headless mode to handle JavaScript rendering.
    """

    def __init__(self):
        self.nome = "Google Dólar"

    def pegar(self):
        """
        Fetches the current USD/BRL exchange rate from Google Finance.

        Returns:
            float: The exchange rate value, or None if an error occurs.
        """
        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

            driver.get("https://www.google.com/finance/quote/USD-BRL")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "KycIzb"))
            )

            texto_completo = driver.find_element(By.CLASS_NAME, "KycIzb").text

            numeros = re.findall(r"\d+,\d+", texto_completo)
            if numeros:
                valor = float(numeros[0].replace(",", "."))
                driver.quit()
                return valor

            driver.quit()
            return None

        except Exception as e:
            print(f"Erro no Google Dólar: {e}")
            return None
