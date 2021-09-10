import requests
import json
import os

api_key = os.environ['covalent_api_key']

class ParseAPI:
    def __init__(self, id):
        self.openseaURL = f"https://api.opensea.io/api/v1/asset/0xae16529ed90fafc927d774ea7be1b95d826664e3/{id}/"
        self.covalentURL = f"https://api.covalenthq.com/v1/1/tokens/0xae16529ed90fafc927d774ea7be1b95d826664e3/token_holders/?limit=1&key={api_key}"
        self.totalSupply = 0
        self.data = []

    def fetchOpenseaData(self):
        values = requests.request("GET", self.openseaURL)
        return values.text

    def fetchContractData(self):
        totalSupply = requests.request("GET", self.covalentURL)
        return totalSupply.text
    
    def formatData(self):
        openseaData = json.loads(self.fetchOpenseaData())
        contractData = json.loads(self.fetchContractData())

        for i in openseaData['traits']:
            self.data.append(i['trait_count'])

        for i in contractData['data']['items']:
            self.totalSupply = i['total_supply']

        return self.data, self.totalSupply
        
if __name__ == "__main__":
    pass

