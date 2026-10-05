from fastapi import FastAPI
from pydantic import BaseModel

from database import engine, session
from models import Base, Users

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


Base.metadata.create_all(bind=engine)


# @app.get("/")
def home():
    return "You are in homepage"


app.add_api_route("/", home, methods=["GET"])


def signin(request: LoginRequest):
    u = request.username
    p = request.password
    db = session()
    try:
        users = db.query(Users).filter(Users.username == u, Users.password == p).first()
        if users:
            return "login successfull"
        else:
            raise KeyError(f"login failed with username {u}")
    except KeyError as error:
        return str(error)
    finally:
        db.close()


app.add_api_route("/login", signin, methods=["POST"])
