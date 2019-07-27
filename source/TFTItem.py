from . import Node


class TFTItem(Node.Node):

    def data_effect(self, other_data):
        for stat in self.get_data()["ratio"]:
            other_data["ratio"][stat] = [x + self.get_data()["ratio"][stat][0] for x in other_data["ratio"][stat]]

        return other_data

    @staticmethod
    def create_from_dictionary(data_dict):
        new_node = TFTItem()

        new_node.set_property("key", data_dict["key"])
        new_node.set_property("name", data_dict["name"])
        for stat in data_dict["stats"]:
            new_node.add_data("ratio", stat["name"], stat["amount"])

        if "buildsInto" in data_dict:
            for item in data_dict["buildsInto"]:
                new_node.add_data("nominal", "buildsInto", item)

        if "buildsFrom" in data_dict:
            for item in data_dict["buildsFrom"]:
                new_node.add_data("nominal", "buildsFrom", item)

        return new_node

       # "abilities"

