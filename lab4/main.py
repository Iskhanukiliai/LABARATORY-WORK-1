from flask import Flask
from flasgger import Swagger
from datetime import datetime
import random

app = Flask(__name__)
swagger = Swagger(app)

# task 1
class Item:
    def __init__(self, item_id, name, power):
        self.id = item_id
        self.name = name.strip()
        self.power = power

    def __str__(self):
        return f"Item({self.name}, Power: {self.power})"

@app.route('/task1')
def route_task1():
    item = Item(1, "Sword", 50)
    return {"result": str(item)}

# task 3
class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

@app.route('/task3')
def route_task3():
    inv = Inventory()
    inv.add_item(Item(1, "Shield", 30))
    return {"inventory_size": len(inv.get_items())}

# task 2
class Player:
    def __init__(self, player_id, name, hp):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self.inventory = Inventory()

    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self._hp = max(0, self._hp - damage)

@app.route('/task2')
def route_task2():
    p = Player(1, "aiganym", 100)
    return {"name": p._name, "hp": p._hp}

# task 6
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"

@app.route('/task6')
def route_task6():
    e = Event("ATTACK", {"damage": 20})
    return str(e)

# task 7 & 15
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            damage = int(damage * 0.9)  # -10%
            self._hp -= damage
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)  # +10%
                self.inventory.add_item(item)
        else:
            super().handle_event(event)

@app.route('/task7')
def route_task7():
    w = Warrior(1, "Warrior_Hero", 100)
    attack = Event("ATTACK", {"damage": 50})
    w.handle_event(attack)
    return {"warrior_hp": w._hp}

# task 8 & 9
class Logger:
    def log(self, event, player, filename="log.txt"):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    def read_logs(self, filename="log.txt"):
        events_list = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(";")
                    if len(parts) == 4:
                        e = Event(parts[2], eval(parts[3]))
                        e.timestamp = parts[0]
                        events_list.append(e)
        except:
            return []
        return events_list

@app.route('/task8')
def route_task8():
    p = Player(1, "Aiganym", 100)
    e = Event("LOOT", {"gold": 100})
    Logger().log(e, p)
    return "Log saved"

@app.route('/task9')
def route_task9():
    logs = Logger().read_logs()
    return {"history": [str(e) for e in logs]}

# task 10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index += 1
        return event

@app.route('/task10')
def route_task10():
    events_list = [Event("ATTACK", {"d": 10}), Event("HEAL", {"h": 5})]
    iterator = EventIterator(events_list)
    return {"first_event": str(next(iterator))}

# task 11
def damage_stream(events):
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)

@app.route('/task11')
def route_task11():
    events_list = [Event("ATTACK", {"damage": 15}), Event("ATTACK", {"damage": 25})]
    damages = list(damage_stream(events_list))
    return {"damages_found": damages}

# task 14
ai_decision = lambda hp: "HEAL" if hp < 30 else "ATTACK"

@app.route('/task14')
def route_task14():
    return {"decision": ai_decision(25)}

# task 20
@app.route('/task20')
def route_task20():
    w = Warrior(1, "Final_Hero", 100)
    e = Event("ATTACK", {"damage": random.randint(20, 50)})
    w.handle_event(e)
    return {"status": "Complete", "hp": w._hp}

@app.route('/')
def home():
    return "<h1>Сервер жұмыс істеп тұр</h1>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)