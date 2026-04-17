# task 1
class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name.strip().title()
        email = email.lower()
        if '@' not in email:
            raise ValueError("Invalid email: must contain '@'")
        self._email = email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"
    def __del__(self):
        print(f"User {self._name} deleted")

    # task 2
    @classmethod
    def from_string(cls, data: str):
        user_id_str, name, email = data.split(',')
        return cls(int(user_id_str.strip()), name.strip(), email.strip())

# task 3
class Product:
    def __init__(self, product_id, name, price, category):
        self.id = int(product_id)
        self.name = str(name)
        self.price = float(price)
        self.category = str(category)

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category
        }

# task 4
class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, product: Product):
        if product.id not in self.products:
            self.products[product.id] = product
    def remove_product(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]
    def get_product(self, product_id: int):
        return self.products.get(product_id)
    def get_all_products(self):
        return list(self.products.values())
    def unique_products(self):
        return set(self.products.values())

    # task 5
    def filter_by_price(self, min_price: float):
        all_prods = self.get_all_products()
        check_price = lambda p: p.price >= min_price
        return [p for p in all_prods if check_price(p)]

#task 6
class Logger:
    @staticmethod
    def log_action(user: User, action: str, product: Product, filename: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}; {user._id}; {action}; {product.id}\n")

    @staticmethod
    def read_logs(filename: str):
        logs = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    t, uid, act, pid = line.strip().split("; ")
                    logs.append({'timestamp': t, 'user_id': uid, 'action': act, 'product_id': pid})
        except FileNotFoundError:
            pass
        return logs

if __name__ == "__main__":
    print("task5 тексеру")

    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "Mouse", 25.0, "Electronics")

    inv = Inventory()
    inv.add_product(p1)
    inv.add_product(p2)

    min_price = 100.0
    expensive_items = inv.filter_by_price(min_price)

    print(f"Қымбат тауарлар{min_price}:")
    for p in expensive_items:
        print(f"- {p.name}: {p.price}")