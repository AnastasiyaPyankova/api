from pydantic import BaseModel

from app.modules.participants.schema import ParticipantRead
from app.modules.prize.schema import PrizeRead


class ResultRead(BaseModel):
    winners: ParticipantRead = None
    prizes: PrizeRead = None


class ResultCreate(BaseModel):
    winner: int
    prize: int
