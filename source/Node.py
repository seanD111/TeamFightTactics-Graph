import uuid


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

    def __init__(self):
        self.id = uuid.uuid4()
        self.data = {
            'nominal': {},
            'ordinal': {},
            'interval': {},
            'ratio': {}
        }
        self.properties = {}

    def add_data(self, type, data_name, data):
        if data_name not in self.data[type]:
            self.data[type][data_name] = []

        if isinstance(data, list):
            self.data[type][data_name].extend(data)
        else:
            self.data[type][data_name].append(data)

