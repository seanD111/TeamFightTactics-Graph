from collections import OrderedDict
import uuid

class Graph:
    """Base implementation of a graph
    References nodes by an ordered dictionary,
    and has functionality for calculating metrics
    """
    def __init__(self):
        self.id = uuid.uuid4()
        self.nodes = OrderedDict()

    def add_node(self, node):
        """

        :param node: Node
        :return:
        """
        self.nodes[node.get_id()] = node

    def get_node_by_property(self, property_type, property_value):
        """
        Returns the first node with matching property value
        :param ptype: (string) the type of property
        :param pvalue: (object) the value of the property
        :return:
        """
        for key, node in self.nodes.items():
            props = node.get_properties()
            if property_type in props:
                if props[property_type] == property_value:
                    return node



