from . import constants
from . import TFTChampion
from . import TFTItem
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
            new_champion = TFTChampion.TFTChampion.create_from_dictionary(self.output['CHAMPIONS'][champ])
            yield new_champion

    def create_item_nodes(self):
        for item in self.output['ITEMS']:
            new_item = TFTItem.TFTItem.create_from_dictionary(self.output['ITEMS'][item])
            yield new_item