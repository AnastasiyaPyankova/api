from typing import List

from sqlalchemy import inspect, Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class BaseMixin(Base):
    __abstract__ = True

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in
                inspect(self).mapper.column_attrs}


class Promo(BaseMixin):
    __tablename__ = 'promos'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    prizes = Column(Integer, ForeignKey('prizes.id'), nullable=False)
    prize = relationship('Prize')
    participants = Column(Integer, ForeignKey('participants.id'), nullable=False)
    participant = relationship('Participant')


class Prize(BaseMixin):
    __tablename__ = 'prizes'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


class Participant(BaseMixin):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Winner(BaseMixin):
    __tablename__ = 'winners'

    winner = Column(Integer, ForeignKey('participants.id'), nullable=False, primary_key=True)
    winners = relationship('Participant')
    prize = Column(Integer, ForeignKey('prizes.id'), nullable=False)
    prizes = relationship('Prize')
