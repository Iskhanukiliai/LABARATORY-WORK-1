from fastapi import FastAPI, HTTPException
app = FastAPI()

#task1
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()
        clean_email = email.lower().strip()
        if "@" not in clean_email:
            raise ValueError("Email must contain @")
        self._email = clean_email

@app.get("/user/test")
def test_user():
    u = User(1, "  john doe  ", "John@Example.COM")
    return {"data": u.to_dict(), "str_repr": str(u)}



#task 2
    @classmethod
    def from_string(cls, data: str):
        try:
            parts = data.split(',')
            if len(parts) != 3:
                raise ValueError("Жолда үтір арқылы 3 элемент болуы керек: id, name, email")
            user_id = int(parts[0].strip())
            name = parts[1].strip()
            email = parts[2].strip()
            return cls(user_id, name, email)
        except (ValueError, IndexError):
            raise ValueError("Жолдағы деректердің дұрыс емес форматы")
    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"
    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email}

@app.get("/user/from-string")
def test_from_string():
    try:
        raw_data = "2, Alice Wonderland , alice@wonder.com"
        u = User.from_string(raw_data)
        return {
            "source_string": raw_data,
            "created_object": u.to_dict(),
            "str_repr": str(u) }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



#task 3
class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.id = product_id
        self.name = name.strip().title()
        self.price = float(price)
        self.category = category.strip().capitalize()
    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category}

@app.get("/product/test")
def test_product():
    p1 = Product(1, " Laptop ", 1200.0, "electronics")
    p2 = Product(1, "LAPTOP NEW", 1300.0, "electronics")
    products_set = {p1, p2}
    return {
        "p1_string": str(p1),
        "are_equal": p1 == p2,
        "unique_count": len(products_set),
        "as_dict": p1.to_dict()}

#task 4
class Inventory:
    def __init__(self):
        self._products = []
    def add_product(self, product: Product):
        if not any(p.id == product.id for p in self._products):
            self._products.append(product)
    def remove_product(self, product_id: int):
        self._products = [p for p in self._products if p.id != product_id]
    def get_product(self, product_id: int):
        for p in self._products:
            if p.id == product_id:
                return p
        return None
    def get_all_products(self):
        return self._products
    def unique_products(self):
        return set(self._products)
    def to_dict(self):
        return {p.id: p for p in self._products}
@app.get("/inventory/test")
def test_inventory():
    inv = Inventory()
    p1 = Product(101, "Mouse", 25.0, "Peripherals")
    p2 = Product(102, "Keyboard", 45.0, "Peripherals")
    p3 = Product(101, "Duplicate Mouse", 30.0, "Peripherals")

    inv.add_product(p1)
    inv.add_product(p2)
    inv.add_product(p3)

    return {
        "all_items": [str(p) for p in inv.get_all_products()],
        "count": len(inv.get_all_products()),
        "search_102": str(inv.get_product(102)),
        "inventory_dict": {p_id: str(p_obj) for p_id, p_obj in inv.to_dict().items()}}

#task 5
    def filter_by_price(self, min_price: float) -> list[Product]:
        check_price = lambda p: p.price >= min_price
        return [p for p in self._products if check_price(p)]

@app.get("/inventory/filter")
def test_filter():
    inv = Inventory()
    inv.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
    inv.add_product(Product(2, "Mouse", 25.0, "Electronics"))
    inv.add_product(Product(3, "Monitor", 300.0, "Electronics"))
    expensive_products = inv.filter_by_price(100.0)
    return {
        "expensive_count": len(expensive_products),
        "names": [p.name for p in expensive_products]}
#task 6
import datetime

class Logger:
    @staticmethod
    def log_action(user, action: str, product, filename: str = "actions.log"):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{now};{user._id};{action};{product.id}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    @staticmethod
    def read_logs(filename: str = "actions.log"):
        logs = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(";")
                    logs.append({
                        "timestamp": parts[0],
                        "user_id": int(parts[1]),
                        "action": parts[2],
                        "product_id": int(parts[3])})
        except FileNotFoundError:
            pass
        return logs

@app.get("/test-log")
def test_log():
    u = User(1, "Ukiliai", "test@mail.com")
    p = Product(101, "Laptop", 1200.0, "Tech")
    Logger.log_action(u, "ADD_TO_CART", p)
    return Logger.read_logs()

@app.get("/home")
def home():
    return "Дүкенге қош келдіңіз!"

