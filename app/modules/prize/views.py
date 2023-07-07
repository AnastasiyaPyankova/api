from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import *
from app.modules.prize.schema import *

router = APIRouter(prefix='/prize')


@router.post('/', status_code=status.HTTP_200_OK)
def create_prize(
        description: str,
        db: Session = Depends(get_session)
):
    prize = Prize(description=description)

    try:
        db.add(prize)
        db.commit()
    except IntegrityError:
        db.rollback()

    return prize.to_dict()
