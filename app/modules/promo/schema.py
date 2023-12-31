from pydantic import BaseModel

from app.modules.participants.schema import ParticipantRead
from app.modules.prize.schema import PrizeRead


class PromoRead(BaseModel):
    id: int
    name: str
    description: str
    # prizes: PrizeRead
    # participants: ParticipantRead


class PromoCreate(BaseModel):
    name: str
    description: str
