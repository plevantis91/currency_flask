import requests
from datetime import datetime

class Currency:
    def __init__(self):
        self.api_key = open('api_key').readline().strip()
        self.url = f'http://api.exchangerate.host/live?access_key={self.api_key}'
        self.output = ''
        self.file_name = datetime.now().strftime('%d %b -%Y')

    def do_request(self):
        res = requests.get(self.url)
        if res.status_code == 200:
            self.output = res.json()
            print(self.output['rates']['USD'])

c = Currency()
c.do_request()