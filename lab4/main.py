from flask import Flask

app = Flask(__name__)


class Player:
    def __init__(self, player_id, name, hp):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

    @classmethod
    def from_string(cls, data: str):
        parts = [x.strip() for x in data.split(",")]
        if len(parts) != 3:
            raise ValueError("Invalid format")
        try:
            player_id = int(parts[0])
            name = parts[1]
            hp = int(parts[2])
        except:
            raise ValueError("Invalid data")
        return cls(player_id, name, hp)


@app.route("/player")
def task1():
    p = Player(1, " john ", 120)
    return str(p)


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


@app.route("/player-from-string")
def task2():
    p = Player.from_string("2, alice , 90")
    return str(p)


@app.route("/item")
def task3():
    i = Item(1, " Sword ", 50)
    return str(i)


class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        for x in self._items:
            if x.id == item.id:
                return
        self._items.append(item)

    def remove_item(self, item_id: int):
        self._items = [item for item in self._items if item.id != item_id]

    def get_items(self):
        return self._items

    def unique_items(self):
        return set(self._items)

    def to_dict(self):
        return {item.id: str(item) for item in self._items}


@app.route("/inventory")
def task4():
    inv = Inventory()
    inv.add_item(Item(1, " Sword ", 50))
    inv.add_item(Item(2, " Shield ", 20))
    inv.add_item(Item(1, " Sword ", 50))

    result = []
    result.append("Items:")
    for item in inv.get_items():
        result.append(str(item))

    result.append("")
    result.append("Unique items:")
    for item in inv.unique_items():
        result.append(str(item))

    result.append("")
    result.append("Dictionary:")
    result.append(str(inv.to_dict()))

    return "<br>".join(result)


@app.route("/")
def home():
    return


if __name__ == "__main__":
    app.run(debug=True)