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

@app.get("/home")
def home():
    return "Добро пожаловать в магазин!"