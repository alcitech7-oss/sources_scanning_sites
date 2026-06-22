# 📊 Source Scanning Sites

Financial robot that collects quotes for the **Dollar**, **Euro**, and **IBovespa** from multiple sources in real time.

---

## 🚀 Features

- Automatic quote collection
- Multiple sources: Google, Yahoo, UOL, and API Awesome
- Spreadsheet generation with historical data
- Trading session status (open/closed)
- Modular structure (easy to expand)

---

## 📁 Project Structure

---

## 🛠️ How to Run

```bash

# 1. Clone the repository
git clone https://github.com/alcitech7-oss/sources_scanning_sites.git

# 2. Enter the folder
cd sources_scanning_sites

# 3. Create and activate the virtual environment
python -m venv venv
venv\Scripts\activate

# 4. Install the dependencies
pip install -r requirements.txt

# 5. Execute
python main.py
...................................................................

📊 Example output
Currency Source Value Status
Dollar Google R$ 5.1522 Open Trading
Dollar Yahoo R$ 5.1515 Open Trading
Dollar Awesome R$ 5.1507 Open Trading
Euro Yahoo R$ 5.9121 Open Trading
Euro Awesome R$ 5.9067 Open Trading
Ibovespa Google 168,467.80 Open Trading

🧩 Technologies used
Python 3.10+

Selenium

BeautifulSoup

Pandas

OpenPyXL

Requests

📌 Notes
The trading status considers Brasília time (10 AM to 5 PM).

Fonts requiring Selenium run in headless mode (without opening a browser).

👨‍💻 Developed by

https://github.com/alcitech7-oss

📄 License
MIT — use, modify, and share freely.

---