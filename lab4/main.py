from flask import Flask
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)

#task 1
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory()
        if hp < 0:

            self._hp = 0
        else:
            self._hp = hp

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

#task 2
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')

        if len(parts) != 3:
            raise ValueError("Неверный формат строки")

        try:
            player_id = int(parts[0].strip())
            name = parts[1].strip()
            hp = int(parts[2].strip())
        except:
            raise ValueError("Ошибка преобразования данных")

        return cls(player_id, name, hp)

@app.route('/')
def home():
    return "Сервер работает"
@app.route('/player')
def player_info():
    p = Player(1, " john ", 120)
    return str(p)
@app.route('/player-from-string')
def player_from_string():
    try:
        p = Player.from_string("2, alice , 90")
        return str(p)
    except ValueError as e:
        return f"Ошибка: {e}"

