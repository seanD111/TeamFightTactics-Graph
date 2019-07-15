from . import Node


class TFTClass(Node.Node):
    def __init__(self):
        super().__init__()

    def create_from_object(self, clas_obj):
        self.properties["key"] = clas_obj["key"]
        self.properties["name"] = clas_obj["name"]
        self.properties["description"] = clas_obj["description"]
        self.properties["accentChampionImage"] = clas_obj["accentChampionImage"]
        self.properties["bonuses"] = clas_obj["bonuses"]


       # "abilities"

