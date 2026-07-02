from pydantic import BaseModel

class CheckoutInfo(BaseModel):
    first_name: str
    last_name: str
    postcode: str