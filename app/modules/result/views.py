from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import *
from app.modules.result.schema import *

router = APIRouter(prefix='/result')


@router.post('/', status_code=status.HTTP_200_OK)
def create_winner(
        data: ResultCreate,
        db: Session = Depends(get_session)
):
    result = Result(winner=data.winner, prize=data.prize)

    try:
        db.add(result)
        db.commit()
    except IntegrityError:
        db.rollback()

    return result.to_dict()
