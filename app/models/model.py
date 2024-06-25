from pydantic import BaseModel


class BaseRequest(BaseModel):
    user: str
    token: str
