from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import *
from app.modules.winner.schema import *

router = APIRouter(prefix='/winner')


@router.post('/', status_code=status.HTTP_200_OK)
def create_winner(
        data: WinnerCreate,
        db: Session = Depends(get_session)
):
    winner = Winner(winner=data.winner, prize=data.prize)

    try:
        db.add(winner)
        db.commit()
    except IntegrityError:
        db.rollback()

    return winner.to_dict()
