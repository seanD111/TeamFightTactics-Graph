from .source import TFTFetcher
from .source import TFTGraph
if __name__ == "__main__":
    fetcher = TFTFetcher.TFTFetcher()
    fetcher.fetch_all()
    fetcher.process_all()

    graph = TFTGraph.TFTGraph()

    for champ in fetcher.create_champion_nodes():
        graph.add_node(champ)

    print(graph.nodes)