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