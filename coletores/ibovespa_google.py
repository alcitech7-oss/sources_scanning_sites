# coletores/ibovespa_google.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re


class GoogleIbovespa:
    def __init__(self):
        self.nome = "Google Ibovespa"

    def pegar(self):
        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

            driver.get("https://www.google.com/finance/quote/IBOV:INDEXBVMF")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "KycIzb"))
            )

            texto_completo = driver.find_element(By.CLASS_NAME, "KycIzb").text
            driver.quit()

            padrao = r"(\d+\.\d+,\d+)"
            match = re.search(padrao, texto_completo)
            if match:
                return float(match.group(1).replace(".", "").replace(",", "."))

            return None

        except Exception as e:
            print(f"Erro no Google Ibovespa: {e}")
            return None
