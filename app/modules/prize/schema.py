from pydantic import BaseModel


class PrizeRead(BaseModel):
    id: int
    description: str
