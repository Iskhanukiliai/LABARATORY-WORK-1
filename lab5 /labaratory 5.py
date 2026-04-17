import numpy as np
from fastapi import FastAPI, HTTPException
import datetime

#task 1, 2
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()
        email_clean = email.lower().strip()
        if '@' not in email_clean:
            raise ValueError("Invalid email: must contain '@'")
        self._email = email_clean
    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email}

    @classmethod
    def from_string(cls, data: str):
        parts = [p.strip() for p in data.split(',')]
        return cls(int(parts[0]), parts[1], parts[2])

@app.get("/test-user")
def test_user():
    u = User.from_string("10, ishan ali, ISHAN@gmail.com")
    return u.to_dict()

#task 3
class Product:
    def __init__(self, product_id, name, price, category):
        self.id = int(product_id)
        self.name = str(name)
        self.price = float(price)
        self.category = str(category)
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price, 'category': self.category}


#task 4
class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, product: Product):
        if product.id not in self.products:
            self.products[product.id] = product
    def get_all_products(self):
        return list(self.products.values())

    #task 5
    def filter_by_price_numpy(self, min_price: float):
        all_prods = self.get_all_products()
        if not all_prods:
            return []

        prices_array = np.array([p.price for p in all_prods])
        mask = prices_array >= min_price
        return [all_prods[i] for i, condition in enumerate(mask) if condition]

@app.get("/filter/{min_price}")
def get_filtered_products(min_price: float):
    results = inventory.filter_by_price_numpy(min_price)
    return [p.to_dict() for p in results]


app = FastAPI(title="Lab 5 API: NumPy & FastAPI")

inventory = Inventory()
inventory.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
inventory.add_product(Product(2, "Mouse", 25.0, "Electronics"))
inventory.add_product(Product(3, "Keyboard", 150.0, "Electronics"))


@app.get("/")
def read_root():
    a =
    return
