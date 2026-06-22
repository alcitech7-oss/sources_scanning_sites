from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


class YahooDolarSelenium:
    def __init__(self):
        self.nome = "Yahoo Dólar (Selenium)"

    def pegar(self):
        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

            driver.get("https://finance.yahoo.com/quote/USDBRL=X")
            time.sleep(5)

            texto = driver.find_element(By.TAG_NAME, "body").text
            driver.quit()

            padrao = r"USD/BRL.*?(\d+\.\d+)"
            match = re.search(padrao, texto, re.DOTALL)

            if match:
                return float(match.group(1))

            return None

        except Exception as e:
            print(f"Erro no Yahoo Dólar Selenium: {e}")
            return None
