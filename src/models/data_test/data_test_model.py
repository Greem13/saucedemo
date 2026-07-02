from pydantic import BaseModel
from typing import List
from src.models.data_test.user_model import User

class DataTest(BaseModel):
    users: List[User]
    error_message_locked_out_user: str
    error_message: str