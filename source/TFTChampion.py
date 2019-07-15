from . import Node


class TFTChampion(Node.Node):
    def create_from_object(self, champ):
        self.properties["id"] = champ["id"]
        self.properties["key"] = champ["key"]
        self.properties["name"] = champ["name"]
        #these need to be linked to TFT class instances
        self.add_data("nominal", "origin", champ["origin"])
        self.add_data("nominal", "class", champ["class"])

        self.add_data("ratio", "cost", champ["cost"])

        self.add_data("ratio", "damage", champ["stats"]["offense"]["damage"])
        self.add_data("ratio", "attackSpeed", champ["stats"]["offense"]["attackSpeed"])
        self.add_data("ratio", "range", champ["stats"]["offense"]["range"])

        self.add_data("ratio", "health", champ["stats"]["defense"]["health"])
        self.add_data("ratio", "armor", champ["stats"]["defense"]["armor"])
        self.add_data("ratio", "magicResist", champ["stats"]["defense"]["magicResist"])

       # "abilities"

