#task 1
class User:
    def __init__(self, user_id, name, email):

        self._id = user_id
        self._name = name.strip().title()

        email = email.lower()
        if '@' not in email:
            raise ValueError("Invalid email: must contain '@'")[cite: 14]
        self._email = email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User {self._name} deleted")
#task 2
@classmethod
    def from_string(cls, data: str):
        user_id_str, name, email = data.split(',')
        return cls(int(user_id_str.strip()), name.strip(), email.strip())
u1 = User(1, "john doe", "John@Example.COM")
print(u1)
u2 = User.from_string("2, Alice Wonderland, alice@wonder.com")
print(u2)

#task3
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