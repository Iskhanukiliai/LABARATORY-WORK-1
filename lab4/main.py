from flask import Flask, jsonify
from flasgger import Swagger
from datetime import datetime
import random

app = Flask(__name__)
swagger = Swagger(app)

# task1
class Item:
    def __init__(self, item_id, name, power):
        self.id = item_id
        self.name = name.strip()
        self.power = power

    def __str__(self):

        return f"Item({self.name}, Power: {self.power})"

# task2
class Player:
    def __init__(self, player_id, name, hp):
        # task16
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self._inventory = Inventory()

    # task16
    @property
    def hp(self):
        return self._hp

    @property
    def inventory(self):
        return self._inventory

    # task17
    def __del__(self):
        print(f"Player {self._name} удалён")

    # task7
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self._hp = max(0, self._hp - damage)
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self._inventory.add_item(item)
#task 3
class Inventory:
    def _init_(self):
        #task 16
        self._items = []

    def add_item(self, item: Item):
        if item.id not in [i.id for i in self._items]:
            self._items.append(item)

    #task 18
    def _iter_(self):
        return iter(self._items)

    def get_strong_items(self, threshold):
        return [i for i in self._items if i.power > threshold]

    def get_items_list(self):
        return self._items

#task 2,4
class Player:
    def _init_(self, player_id: int, name: str, hp: int):
        #task 16
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self._inventory = Inventory()

    #task 16
    @property
    def hp(self):
        return self._hp
    @property
    def inventory(self):
        return self._inventory

    #task 17
    def _del_(self):
        print(f"Player {self._name} удалён из памяти")

    def _str_(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

# task20
@app.route('/')
def home():
    return "Сервер жұмыс істеп тұр"
if __name__ == '__main__':
    app.run(port=5000, debug=True)