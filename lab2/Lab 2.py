

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


# task3
class Inventory:
    def __init__(self):
        # task16
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    # task18
    def __iter__(self):
        return iter(self._items)

    def get_strong_items(self, threshold):
        return [i for i in self._items if i.power > threshold]


# task4
def create_player_from_string(data_str):
    pid, name, hp = data_str.split(',')
    return Player(int(pid), name, int(hp))


# task5
def compare_items(item1, item2):
    return item1.power > item2.power


# task6
class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()


# task8
class Logger:
    def log(self, event, player, filename="game_log.txt"):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    # task9
    def read_logs(self, filename="game_log.txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            return []


# task10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.events):
            res = self.events[self.index]
            self.index += 1
            return res
        raise StopIteration


# task11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data.get("damage", 0)


# task12
def get_random_event(items_list):
    etype = random.choice(["ATTACK", "LOOT"])
    if etype == "ATTACK":
        return Event("ATTACK", {"damage": random.randint(10, 50)})
    return Event("LOOT", {"item": random.choice(items_list)})


# task13
def analyze_logs(log_lines):
    return len(log_lines)


# task14
ai_decision = lambda hp: "HEAL" if hp < 30 else "ATTACK"


# task15
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            dmg = int(event.data.get("damage", 0) * 0.9)
            self._hp = max(0, self._hp - dmg)
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


# task19
def analyze_inventory(player):
    unique_names = {item.name for item in player.inventory}
    return len(unique_names)


# task20
@app.route('/')
def home():
    """
    Home page
    ---
    responses:
      200:
        description: Welcome message
    """
    return "<h1>AI Dungeon API</h1><p>Go to /apidocs for Swagger or /simulate</p>"


@app.route('/simulate')
def simulate():
    """
    Game simulation
    ---
    responses:
      200:
        description: Results
    """
    w = Warrior(1, "Aiganym", 100)
    items = [Item(1, "Sword", 50), Item(2, "Shield", 30)]
    ev = get_random_event(items)
    w.handle_event(ev)

    logger = Logger()
    logger.log(ev, w)

    return {
        "status": "Success",
        "player_hp": w.hp,
        "event": ev.type,
        "advice": ai_decision(w.hp)
    }


if __name__ == '__main__':
    app.run(port=5000, debug=True)