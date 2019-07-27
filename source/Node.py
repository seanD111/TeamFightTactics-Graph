import uuid
import copy
from . import Link

class Node:
    """Base Node implementation

    Attributes:
        id (UUID): id used to uniquely identify each node
        data (dict): specifically holds data, as the following types
            'nominal' (dict)
            'ordinal' (dict)
            'interval' (dict)
            'ratio' (dict)
        properties (dict): holds arbitrary node properties, that are not data
    """

    def __init__(self, other=None):
        self._id = uuid.uuid4()
        self._links = []

        # TODO: check if other is a type of node
        if other is not None:
            self._data = other.get_base_data()
            self._properties = other.get_properties()
        else:
            self._data = {
                'nominal': {},
                'ordinal': {},
                'interval': {},
                'ratio': {}
            }
            self._properties = {}

    def set_property(self, prop_name, prop):
        """
        Overwrites the data of the given name of this node
        :param prop_name:
        :param prop:
        :return:
        """
        self._properties[prop_name] = prop

    def add_data(self, data_type, data_name, data):
        """
        Appends data to existing data of the same name on this node
        :param data_type:
        :param data_name:
        :param data:
        :return:
        """
        if data_name not in self._data[data_type]:
            self._data[data_type][data_name] = []

        if isinstance(data, list):
            self._data[data_type][data_name].extend(data)
        else:
            self._data[data_type][data_name].append(data)

    def set_data(self, data_type, data_name, data):
        """
        Overwrites the data of the given name of this node
        :param data_type:
        :param data_name:
        :param data:
        :return:
        """
        self._data[data_type][data_name] = []

        if isinstance(data, list):
            self._data[data_type][data_name].extend(data)
        else:
            self._data[data_type][data_name].append(data)

    def get_data(self):
        data_modified = copy.deepcopy(self._data)
        for link in self._links:
            data_modified = link.get_other(self).data_effect(data_modified)
        return data_modified

    def get_base_data(self):
        return copy.deepcopy(self._data)

    def get_properties(self):
        return copy.deepcopy(self._properties)

    def get_id(self):
        return copy.deepcopy(self._id)

    def disconnect(self, other_node):
        for i in range(len(self._links)-1, -1, -1):
            if self._links[i].get_other() is other_node:
                self._links.pop(i)
                other_node.disconnect(self)

    def connect_from(self, other_node):
        new_link = Link.Link(source=other_node, target=self)
        other_node.connect_effect(self)
        self._links.append(new_link)

    def connect_to(self, other_node):
        new_link = Link.Link(source=self, target=other_node)
        other_node.connect_effect(self)
        self._links.append(new_link)

    def connect_effect(self, other_node):
        """
        The effect applied when connected to another node
        :param other_node:
        :return:
        """
        pass

    def data_effect(self, other_data):
        """
        The passive data effect this node has on connected nodes
        :param other_data:
        :return:
        """
        return other_data
