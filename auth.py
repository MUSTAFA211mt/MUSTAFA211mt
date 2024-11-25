
import requests

class AminoAuth:
    def __init__(self):
        self.base_url = "https://service.narvii.com/api/v1/"
        self.session = requests.Session()
        self.token = None

    def login(self, email, password):
        url = f"{self.base_url}g/s/auth/login"
        payload = {
            "email": email,
            "v": 2,
            "secret": f"0 {password}",
            "deviceID": "YOUR_DEVICE_ID"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.session.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            self.token = response.json().get("sid")
            print("Login successful!")
        else:
            print("Login failed:", response.text)

    def logout(self):
        if self.token:
            url = f"{self.base_url}g/s/auth/logout"
            headers = {
                "NDCAUTH": self.token
            }
            self.session.post(url, headers=headers)
            print("Logged out successfully.")
    