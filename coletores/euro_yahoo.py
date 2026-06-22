from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


class YahooEuroSelenium:
    """
    Captures the EUR/BRL exchange rate from Yahoo Finance.
    Uses Selenium in headless mode to handle JavaScript rendering.
    """

    def __init__(self):
        self.nome = "Yahoo Euro (Selenium)"

    def pegar(self):
        """
        Fetches the current EUR/BRL exchange rate from Yahoo Finance.

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

            driver.get("https://finance.yahoo.com/quote/EURBRL=X")
            time.sleep(5)

            texto = driver.find_element(By.TAG_NAME, "body").text
            driver.quit()

            padrao = r"EUR/BRL.*?(\d+\.\d+)"
            match = re.search(padrao, texto, re.DOTALL)

            if match:
                return float(match.group(1))

            return None

        except Exception as e:
            print(f"Erro no Yahoo Euro Selenium: {e}")
            return None
