
import requests

class AminoInteract:
    def __init__(self, token):
        self.base_url = "https://service.narvii.com/api/v1/"
        self.token = token

    def like_post(self, post_id, community_id):
        url = f"{self.base_url}x{community_id}/s/blog/{post_id}/vote"
        headers = {
            "NDCAUTH": self.token
        }
        payload = {
            "value": 4  # 4 means "like"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Post liked successfully.")
        else:
            print("Failed to like post:", response.text)
    