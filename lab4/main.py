from flask import Flask
from flasgger import Swagger
from datetime import datetime
import random
import ast

app = Flask(__name__)
swagger = Swagger(app)

#task 1
class Player:
    def __init__(self, player_id, name, hp):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = 0 if hp < 0 else hp
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"
    def __del__(self):
        print(f"Player {self._name} удалён")

@app.route('/player')
def player_info():
    return str(Player(1, " john ", 120))


#task 2
@classmethod
def from_string(cls, data):
    parts = data.split(',')
    return cls(int(parts[0].strip()), parts[1].strip(), int(parts[2].strip()))
Player.from_string = from_string

@app.route('/player-from-string')
def player_from_string():
    return str(Player.from_string("2, alice , 90"))


#task 3
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip().title()
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)

@app.route('/item')
def item_info():
    return str(Item(1, " Sword ", 50))


#task 4
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        if not any(i.id == item.id for i in self.items):
            self.items.append(item)
    def get_items(self):
        return self.items

@app.route('/inventory')
def inventory_info():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    return str(inv.get_items())


#task 5
def get_strong_items(self, min_power):
    return [i for i in self.items if i.power >= min_power]
Inventory.get_strong_items = get_strong_items

@app.route('/strong-items')
def strong_items():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    inv.add_item(Item(2, "Shield", 20))
    return str(inv.get_strong_items(30))

#task 6
class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"{self.type} {self.data}"

@app.route('/event')
def event_info():
    return str(Event("ATTACK", {"damage": 10}))

#task 7
def handle_event(player, event):
    if event.type == "ATTACK":
        player._hp -= event.data["damage"]

@app.route('/handle-event')
def handle_event_route():
    p = Player(1, "john", 100)
    handle_event(p, Event("ATTACK", {"damage": 10}))
    return str(p)

#task 8
class Logger:
    def log(self, event, player, filename):
        with open(filename, "a") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")

@app.route('/write-log')
def write_log():
    Logger().log(Event("ATTACK", {"damage": 10}), Player(1, "a", 100), "log.txt")
    return "ok"

#task 9
def read_logs(self, filename):
    events = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.split(";")
            events.append(Event(parts[2], {"data": parts[3]}))
    return events
Logger.read_logs = read_logs

@app.route('/read-logs')
def read_logs_route():
    return str(Logger().read_logs("log.txt"))

#task 10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        e = self.events[self.index]
        self.index += 1
        return e

@app.route('/iterator')
def iterator():
    return "ok"

#task 11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data["damage"]

@app.route('/damage')
def damage():
    return str(list(damage_stream([Event("ATTACK", {"damage": 5})])))


