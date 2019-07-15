from . import constants
from . import TFTChampion
import urllib.request
import json

class TFTFetcher:
    def __init__(self):
        self.input = {}
        self.output = {}

    def fetch_all(self):
        for url in constants.URLS:
            with urllib.request.urlopen(constants.URLS[url]) as response:
                self.input[url] = response.read()

    def process_all(self):
        for type in self.input:
            self.output[type] = json.loads(self.input[type])

    def create_champion_nodes(self):
        for champ in self.output['CHAMPIONS']:
            new_champion = TFTChampion.TFTChampion()
            new_champion.create_from_object(self.output['CHAMPIONS'][champ])
            yield new_champion
