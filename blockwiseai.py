from web3 import Web3
from datetime import datetime
import time

ETHERSCAN_API_KEY = "YourEtherscanAPIKey"

class TransactionFetcher:
    def __init__(self, address: str):
        self.address = Web3.to_checksum_address(address)

    def fetch_transactions(self, start_block=0, end_block=99999999):
        import requests
        url = f"https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "txlist",
            "address": self.address,
            "startblock": start_block,
            "endblock": end_block,
            "sort": "asc",
            "apikey": ETHERSCAN_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['result']
