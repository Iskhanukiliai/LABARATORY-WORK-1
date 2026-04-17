from flask import Flask
from flasgger import Swagger
from datetime import datetime
import random

app = Flask(__name__)
swagger = Swagger(app)

# task 1
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory()
        self.inventory = Inventory
        self._hp = max(0, hp)

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    # task 17 (Деструктор)
    def __del__(self):
        print(f"Player {self._name} удалён")

    # task 16 (Инкапсуляция)
    @property
    def hp(self):
        return self._hp

    # task 2
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')
        return cls(int(parts[0]), parts[1].strip(), int(parts[2]))

@app.route('/task1')
def __str__(self):
    return f"Player(id = {self._id}, name = {self._name}, hp = {self._hp})"

def __del__(self):
    print(f"Player {self._name} удален")

@property
def hp(self):
    return self._hp

@classmethod
def from_string(cls, data: str):
    parts = data.split(",")
    return cls(parts[0], parts[1].strip(), int(parts[2]))

@app.route("/task1")
def route_task1():
    p = Player(1, " ukiliai    ", 100)
    return str(p)


@app.route("/task2")
def route_task2():
    p = Player.from_string("2, alice, 90")
    return str(p)
#task 3
class Item:
    def __init__(self, item_id: int, name: str, hp_bonus: int):
        self.id = item_id
        self.name = name.strip().title()
        self.hp_bonus = hp_bonus
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', hp_bonus={self.hp_bonus})"
    #task 5 (Сравнение)
    def __eq__(self, other):
        return self.id == other.id
@app.route('/task3')
def route_task3():
    i = Item(1, " Health Potion ", 50)
    return str(i)

@app.route('/task5')
def route_task5():
    i1 = Item(10, "Potion", 50)
    i2 = Item(10, "Super Potion", 100)
    return f"Одинаковые ID: {i1 == i2}"


#task 4
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)
    def get_items(self):
        return self.items

@app.route('/task4')
def route_task4():
    inv = Inventory()
    inv.add_item(Item(1, "Shield", 30))
    return f"Items: {len(inv.get_items())}"


#task 6
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now().strftime("%H:%M:%S")
    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, time='{self.timestamp}')"

@app.route('/task6')
def route_task6():
    e = Event("ATTACK", {"damage": 25})
    return str(e)


#task 7, 15
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = int(event.data.get("damage", 0) * 0.9)
            self._hp -= damage

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.hp_bonus = int(item.hp_bonus * 1.1)
                self.inventory.add_item(item)

@app.route('/task7')
def route_task7():
    w = Warrior(1, "Warrior Hero", 100)
    w.handle_event(Event("ATTACK", {"damage": 50}))
    return f"Warrior HP: {w._hp}"

#task 8, 9
class Logger:
    def log(self, event, player, filename="log.txt"):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)
    def read_logs(self, filename="log.txt"):
        logs = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(";")
                    if len(parts) == 4:
                        e = Event(parts[2], eval(parts[3]))
                        e.timestamp = parts[0]
                        logs.append(e)
        except: pass
        return logs

@app.route('/task9')
def route_task9():
    logger = Logger()
    logs = logger.read_logs()
    return "<br>".join(str(e) for e in logs) if logs else "No logs"


#task 10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events): raise StopIteration
        val = self.events[self.index]
        self.index += 1
        return val

@app.route('/task10')
def route_task10():
    it = EventIterator([Event("START", {}), Event("END", {})])
    return str(next(it))


#task 11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data.get("damage", 0)

@app.route('/task11')
def route_task11():
    evs = [Event("ATTACK", {"damage": 30}), Event("ATTACK", {"damage": 40})]
    return f"Damages: {list(damage_stream(evs))}"


#task 12, 13
@app.route('/task13')
def route_task13():
    events = [Event("ATTACK", {"damage": 10}), Event("ATTACK", {"damage": 20})]
    total = sum(damage_stream(events))
    return f"Total Damage: {total}"


#task 14
decide_action = lambda hp: "HEAL" if hp < 50 else "ATTACK"

@app.route('/task14')
def route_task14():
    return f"Decision (40hp): {decide_action(40)}"


#task 18
@app.route('/task18')
def route_task18():
    hps = [20, 60, 80]
    filtered = [h for h in hps if h > 50]
    return f"Filtered HP: {filtered}"


#task 19
@app.route('/task19')
def route_task19():
    names = {"Shield", "Potion", "Shield"}
    return f"Unique (set): {names}"

#task 20
@app.route('/task20')
def route_task20():
    w = Warrior(1, "Aiganym", 100)
    w.handle_event(Event("ATTACK", {"damage": 30}))
    return {"status": "Done", "hp": w._hp, "advice": decide_action(w._hp)}
    p = Player(1, "ukiliai  ", 100)
    return p

@app.route('/')
def home():
    return "<h1>Сервер жұмыс істеп тұр<h1>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)