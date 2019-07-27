from .source import TFTFetcher
from .source import TFTGraph
from .source import TFTChampion
from .source import TFTItem
if __name__ == "__main__":
    fetcher = TFTFetcher.TFTFetcher()
    fetcher.fetch_all()
    fetcher.process_all()

    base_champions = TFTGraph.TFTGraph()

    base_items = TFTGraph.TFTGraph()

    for champ in fetcher.create_champion_nodes():
        base_champions.add_node(champ)

    for item in fetcher.create_item_nodes():
        base_items.add_node(item)

    aatrox = TFTChampion.TFTChampion(other=base_champions.get_node_by_property("key", "Aatrox"))

    bfsword = TFTItem.TFTItem(other=base_items.get_node_by_property("key", "bfsword"))

    aatrox.connect_to(bfsword)

    pass