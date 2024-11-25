
import requests

class AminoScraper:
    def __init__(self, token):
        self.base_url = "https://service.narvii.com/api/v1/"
        self.token = token

    def get_community_info(self, community_id):
        url = f"{self.base_url}g/s-x{community_id}/info"
        headers = {
            "NDCAUTH": self.token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch community info:", response.text)
    