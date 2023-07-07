from pydantic import BaseModel

from app.modules.participants.schema import ParticipantRead
from app.modules.prize.schema import PrizeRead


class PromoRead(BaseModel):
    id: int
    description: str
    prizes: PrizeRead = None
    participants: ParticipantRead = None


class PromoCreate(BaseModel):
    name: str
    description: str
