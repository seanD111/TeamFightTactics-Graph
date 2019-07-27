from . import Node
from . import constants


class TFTChampion(Node.Node):

    @staticmethod
    def create_from_dictionary(data_dict):
        new_node = TFTChampion()

        new_node.set_property("id", data_dict["id"])
        new_node.set_property("key", data_dict["key"])
        new_node.set_property("name", data_dict["name"])
        # these may need to be linked to TFT class instances
        new_node.add_data("nominal", "trait", data_dict["origin"])
        new_node.add_data("nominal", "trait", data_dict["class"])

        for i in range(0, 3):
            new_node.add_data("ratio", "cost", data_dict["cost"]*constants.GOLD_COST_SCALING[i])
            new_node.add_data("ratio", "attackDamage",
                              data_dict["stats"]["offense"]["attackDamage"]*constants.DAMAGE_HEALTH_SCALING[i])

            new_node.add_data("ratio", "attackSpeed", data_dict["stats"]["offense"]["attackSpeed"])
            new_node.add_data("ratio", "range", data_dict["stats"]["offense"]["range"])
            new_node.add_data("ratio", "health",
                              data_dict["stats"]["defense"]["health"]*constants.DAMAGE_HEALTH_SCALING[i])
            new_node.add_data("ratio", "armor", data_dict["stats"]["defense"]["armor"])
            new_node.add_data("ratio", "magicResist", data_dict["stats"]["defense"]["magicResist"])
            new_node.add_data("ratio", "manaStart", data_dict["ability"]["manaStart"])
            new_node.add_data("ratio", "manaCost", data_dict["ability"]["manaCost"])
            new_node.add_data("ratio", "manaPerAttack", constants.MANA_PER_ATTACK[i])
            new_node.add_data("ratio", "critDamage", constants.CRIT_DAMAGE[i])
            new_node.add_data("ratio", "critChance", constants.CRIT_RATE[i])

        return new_node

       # "abilities"

