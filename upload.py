import requests
import json
import os

url_token = "https://sm.ms/api/v2/token"
url_upload = "https://sm.ms/api/v2/upload/"
url_profile = "https://sm.ms/api/v2/profile/"
url_history = "https://sm.ms/api/v2/upload_history"

from config import *

class smms():
    def __init__(self, username=username, password=password):
        self.username = username
        self.password = password
        self.token = None

    def login(self):
        params = {
            'username': self.username,
            'password': self.password
        }
        r = requests.post(url_token, data=params)
        self.token = json.loads(r.text)['data']['token']
        self.headers = {
            'Authorization': self.token
        }

    def upload(self, path):
        filename = os.path.basename(path)
        files = {
            'smfile': (filename, open(path, 'rb')),
            'format': 'json'
        }
        r = requests.post(url_upload, files=files, headers=self.headers)
        json_content = json.loads(r.text)
        if json_content['success'] == True:
            return json_content['data']['url']
        else:
            return "Error"

    def history(self):
        r = requests.get(url_history, headers=self.headers)
        print(r.text)
