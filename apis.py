import json
import requests

from utils import get_path



class API(object):
    def __init__(self, username, token="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") -> None:
        self.url = "https://api.github.com/user"
        self.username = username
        self.token = token
        
        self.data = {}

        # self.get_user_detaisl()

    def get_user_detaisl(self):
        authentication = (self.username, self.token)
        response = requests.request('GET', url=self.url, auth=authentication)
        self.data = response.json()

        self.save_user_details()

    def save_user_details(self):
        FILE_DIR = get_path()
        with open(FILE_DIR, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_followers(self, url):
        response = requests.request('GET', url)

        return response.json()

    def get_followings(self, url):
        response = requests.request('GET', url.replace('{/other_user}', ''))

        return response.json()
