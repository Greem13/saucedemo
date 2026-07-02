from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    locked_out: bool = False