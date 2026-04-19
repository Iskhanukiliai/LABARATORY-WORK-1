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



#2 esep
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



@app.get("/home")
def home():
    return "Дүкенге қош келдіңіз!"

