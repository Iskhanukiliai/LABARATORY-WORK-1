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

    #task 7
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self._hp = max(0, self._hp - damage)
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self._inventory.add_item(item)


#task 15
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            raw_damage = event.data.get("damage", 0)
            reduced_damage = int(raw_damage * 0.9)
            self._hp = max(0, self._hp - reduced_damage)
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
                self._inventory.add_item(item)
        else:
            super().handle_event(event)

#task 6
class Event:
    def _init_(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _str_(self):
        return f"[{self.timestamp}] {self.type}: {self.data}"

#task 8,9
class Logger:
    def log(self, event, player, filename="game_log.txt"):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    def read_logs(self, filename="game_log.txt"):
        logs = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    logs.append(line.strip())
        except FileNotFoundError:
            return ["Лог-файл еще не создан"]
        return logs

#task 10, 11
def damage_generator(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data.get("damage", 0)

#task 12, 14
ai_decision = lambda hp: "HEAL" if hp < 30 else "ATTACK"

#task 13, 19
def analyze_inventory(players_list):
    all_items = []
    for p in players_list:
        #task 18
        for item in p.inventory:
            all_items.append(item)

    #task 19
    unique_names = {item.name for item in all_items}

    return {
        "total_items_found": len(all_items),
        "unique_items_count": len(unique_names)
    }

#task 20
@app.route('/simulate')
def simulate():
    """
    Запуск полной цепочки задач (1-20)
    ---
    responses:
      200:
        description: Результат игры
    """
    warrior = Warrior(1, "Aiganym", 100)
    mage = Mage(2, "Akzhan", 100)

    sword = Item(101, "Fire Sword", 50)
    e1 = Event("ATTACK", {"damage": random.randint(30, 60)})
    e2 = Event("LOOT", {"item": sword})

    warrior.handle_event(e1)
    mage.handle_event(e2)

    logger = Logger()
    logger.log(e1, warrior)
    logger.log(e2, mage)

    stats = analyze_inventory([warrior, mage])

    return {
        "status": "Simulation Complete",
        "warrior_hp": warrior.hp,
        "mage_inventory_count": stats["total_items_found"],
        "unique_items_found": stats["unique_items_count"],
        "ai_suggests": ai_decision(warrior.hp)
    }

@app.route('/')
def home():
    return "Сервер жұмыс істеп тұр"
if __name__ == '__main__':
    app.run(port=5000, debug=True)