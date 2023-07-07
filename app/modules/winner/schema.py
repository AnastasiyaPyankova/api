from pydantic import BaseModel

from app.modules.participants.schema import ParticipantRead
from app.modules.prize.schema import PrizeRead


class WinnerRead(BaseModel):
    winners: ParticipantRead = None
    prizes: PrizeRead = None


class WinnerCreate(BaseModel):
    winner: int
    prize: int
