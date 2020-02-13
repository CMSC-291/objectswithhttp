import requests


class Anthropod:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.html = requests.get(self.url).text
