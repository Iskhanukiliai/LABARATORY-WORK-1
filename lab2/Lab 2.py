from flask import Flask
from datetime import datetime
import random
import ast

app = Flask(__name__)

# task 1
class Player:
    def __init__(self, player_id, name, hp):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

@app.route("/player")
def task1():
    p = Player(1, " john ", 120)
    return str(p)

    # task 2
    @classmethod
    def from_string(cls, data: str):
        parts = [x.strip() for x in data.split(",")]
        if len(parts) != 3:
            raise ValueError("Invalid format")
        try:
            player_id = int(parts[0])
            name = parts[1]
            hp = int(parts[2])
        except ValueError:
            raise ValueError("Invalid data")
        return cls(player_id, name, hp)


@app.route("/player-from-string")
def task2():
    p = Player.from_string("2, alice , 90")
    return str(p)


# task 3
class Item:
    def __init__(self, item_id, name, power):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)

@app.route("/item")
def task3():
    i = Item(1, " Sword ", 50)
    return str(i)


# task 4
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        for i in self.items:
            if i.id == item.id:
                return
        self.items.append(item)
    def remove_item(self, item_id: int):
        self.items = [i for i in self.items if i.id != item_id]
    def get_items(self):
        return self.items
    def unique_items(self):
        return set(self.items)
    def to_dict(self):
        return {item.id: item for item in self.items}
@app.route('/inventory')
def inventory_test():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    inv.add_item(Item(2, "Shield", 30))
    result = ""
    for item in inv.get_items():
        result += str(item) + "\n"
    result += "Уникальных: " + str(len(inv.unique_items()))
    return result

#task 5
def get_strong_items(self, min_power: int):
    return [item for item in self._items if (lambda x: x >= min_power)(item.power)]

@app.route("/strong-items")
def task5():
    inv = Inventory()
    inv.add_item(Item(1, " Sword ", 50))
    inv.add_item(Item(2, " Shield ", 20))
    inv.add_item(Item(3, " Axe ", 70))
    items = inv.get_strong_items(40)
    return "<br>".join(str(item) for item in items)

# task 6
class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"

@app.route("/event")
def task6():
    e = Event("ATTACK", {"damage": 20})
    return str(e)

# task 7
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = int(event.data.get("damage", 0) * 0.9)
            self._hp -= damage
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                boosted = Item(item.id, item.name, int(item.power * 1.1))
                self.inventory.add_item(boosted)
        else:
            super().handle_event(event)

@app.route("/handle-event")
def task7():
    p = Warrior(1, "thor", 100)
    e = Event("ATTACK", {"damage": 20})
    p.handle_event(e)
    return str(p)

# task 8
class Logger:
    def log(self, event, player, filename):
        with open(filename, "a") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")

@app.route("/write-log")
def task8():
    logger = Logger()
    logger.log(Event("ATTACK", {"damage": 10}), Player(1, "john", 100), "log.txt")
    return "log written"

# task 9
def read_logs(self, filename):
    events = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.split(";")
            data = ast.literal_eval(parts[3]) # 9 tapsyrma
            events.append(Event(parts[2], data))
    return events

Logger.read_logs = read_logs


@app.route("/read-logs")
def task9():
    return str(Logger().read_logs("log.txt"))

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
        e = self.events[self.index]
        self.index += 1
        return e

@app.route("/iterator")
def task10():
    events = [Event("ATTACK", {"damage": 10}), Event("HEAL", {"heal": 5})]
    return "<br>".join(str(e) for e in EventIterator(events))

# task 11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data["damage"]

@app.route("/damage")
def task11():
    events = [Event("ATTACK", {"damage": 5}), Event("HEAL", {"heal": 3})]
    return str(list(damage_stream(events)))

# task 12
def generate_events(players, items, n):
    event_type = lambda: random.choice(["ATTACK", "HEAL", "LOOT"])

    events = []
    for p in players:
        for _ in range(n):
            t = event_type()
            if t == "ATTACK":
                events.append(Event(t, {"damage": random.randint(5, 20)}))
            elif t == "HEAL":
                events.append(Event(t, {"heal": random.randint(5, 15)}))
            else:
                events.append(Event(t, {"item": random.choice(items)}))
    return events

@app.route("/generate")
def task12():
    players = [Player(1, "john", 100)]
    items = [Item(1, "Sword", 50)]
    return str(generate_events(players, items, 2)) #12 tapsyrma

# task 13
def analyze_logs(events):
    total_damage = sum(e.data.get("damage", 0) for e in events)

    event_types = [e.type for e in events]
    most_common = max(set(event_types), key=event_types.count)

    return {
        "total_damage": total_damage,
        "most_common_event": most_common
    }

# task 14
decide_action = lambda p: "HEAL" if p._hp < 30 else "ATTACK"

@app.route("/ai")
def task14():
    p = Player(1, "john", 20)
    return decide_action(p)

@app.route("/analyze")
def task13():
    events = [Event("ATTACK", {"damage": 10}), Event("ATTACK", {"damage": 20})]
    return str(analyze_logs(events))

@app.route("/")
def home():
    return "Сервер жұмыс істеп тұр"

if __name__ == "__main__":
    app.run(debug=True)