from collections import OrderedDict


class Graph:
    """Base implementation of a graph
    References nodes by an ordered dictionary,
    and has functionality for calculating metrics
    """
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, node):
        """

        :param node: Node
        :return:
        """
        self.nodes[node.id] = node

