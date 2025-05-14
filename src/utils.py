# src/utils.py
import os
from dotenv import load_dotenv
# .env फ़ाइल से वैरिएबल्स लोड करो
load_dotenv()
INFURA_API_KEY = os.getenv("INFURA_API_KEY")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
APP_LANG = os.getenv("APP_LANG", "en")
KEYS_FILE = os.getenv("KEYS_FILE", "wallets.txt")
