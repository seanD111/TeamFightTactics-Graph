from . import Node


class TFTTrait(Node.Node):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_from_dictionary(data_dict):
        new_node = TFTTrait()

        new_node.set_property("id", data_dict["id"])
        new_node.set_property("key", data_dict["key"])
        new_node.set_property("description", data_dict["description"])
        new_node.set_property("accentChampionImage", data_dict["accentChampionImage"])
        new_node.set_property("bonuses", data_dict["bonuses"])

        return new_node


