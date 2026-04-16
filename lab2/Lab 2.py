from flask import Flask
from flasgger import Swagger
from datetime import datetime
import random

app = Flask(__name__)
swagger = Swagger(app)

class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory
        self._hp = max(0, hp)

        def __str__(self):
            return f"Player(id = {self._id}, name = {self._name}, hp = {self._hp})"
        def __del__(self):
            print(f"Player {self._name} удален")

        @property
        def hp(self):
            return self._hp
        @classmethod
        def from_string(cls, data:, str):
            parts = data.split(",")
            return cls(parts[0], parts[1].strip(), int(parts[2]))
@app.route(/"task1")
def route_task1():
    p = Player(1, "ukiliai  ", 100)
    return p
@app.route("/task2")
def route_task2:
    p = Player.from_string('2, alice, 90')
    return p


