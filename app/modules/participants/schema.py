from pydantic import BaseModel


class ParticipantRead(BaseModel):
    id: int
    name: str


class ParticipantCreate(BaseModel):
    name: str
