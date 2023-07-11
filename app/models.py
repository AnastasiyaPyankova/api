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
    description = Column(String, nullable=True)
    prizes = relationship('Prize', secondary='betweenpromoprizes')
    participants = relationship('Participant', secondary='betweenpromoparticipants')


class Prize(BaseMixin):
    __tablename__ = 'prizes'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


class Participant(BaseMixin):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Result(BaseMixin):
    __tablename__ = 'winners'

    id = Column(Integer, primary_key=True)
    winner_id = Column(Integer, ForeignKey('participants.id'), nullable=False)
    winner = relationship('Participant')
    prize_id = Column(Integer, ForeignKey('prizes.id'), nullable=False)
    prize = relationship('Prize')


class BetweenPromoPrize(BaseMixin):
    __tablename__ = 'betweenpromoprizes'

    promo_id = Column(Integer, ForeignKey('promos.id'), primary_key=True)
    prize_id = Column(Integer, ForeignKey('prizes.id'), primary_key=True)


class BetweenPromoParticipant(BaseMixin):
    __tablename__ = 'betweenpromoparticipants'

    promo_id = Column(Integer, ForeignKey('promos.id'), primary_key=True)
    participant_id = Column(Integer, ForeignKey('participants.id'), primary_key=True)
