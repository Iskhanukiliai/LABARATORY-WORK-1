from flask import Flask
from flasgger import Swagger
from datetime import datetime
import random

app = Flask(__name__)
swagger = Swagger(app)

class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)
    def get_items(self):
        return self.items


class Item:
    def __init__(self, item_id: int, name: str, hp_bonus: int):
        self.id = item_id
        self.name = name.strip().title()
        self.hp_bonus = hp_bonus

    def __str__(self):
        return f'Item(id={self.id}, name="{self.name}", hp_bonus={self.hp_bonus})'
    def __eq__(self, other):
        return self.id == other.id


class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory()
        self._hp = max(0, hp)

    def __str__(self):
        return f'Player(id={self._id}, name="{self._name}", hp={self._hp})'
    def __del__(self):
        print(f'Player {self._name} удален')
    @classmethod
    def string_from(cls, data: str):
        parts = data.split(',')
        return cls(int(parts[0]), parts[1].strip(), int(parts[2]))
@app.route("/task1")
def task1():
    p = Player(1, "   ukiliai", 199)
    return str(p)


if __name__ == '__main__':

    p1 = Player(1, "  ukilai  ", 30)
    print(f"бірінші тапсырма: {p1}")

    p2 = Player.string_from("101, health potion, 300")
    print(f"тапсырма екі: {p2}")

    item_obj = Item(500, "Shield", 50)
    print(f"тапсырма үш: {item_obj}")

    ivt = Inventory()
    ivt.add_item(item_obj)
    ivt.add_item(Item(500, "Double", 100))
    print(f"тапсырма төрт: {len(ivt.get_items())}")

    app.run(port=5000, debug=True)