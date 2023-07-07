from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import *
from app.modules.participants.schema import *

router = APIRouter(prefix='/participant')


@router.post('/', status_code=status.HTTP_200_OK)
def create_participant(
        data: ParticipantCreate,
        db: Session = Depends(get_session)
):
    participant = Participant(name=data.name)

    try:
        db.add(participant)
        db.commit()
    except IntegrityError:
        db.rollback()

    return participant.to_dict()
