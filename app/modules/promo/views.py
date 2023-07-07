from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import *
from app.modules.promo.schema import *

router = APIRouter(prefix='/promo')


@router.post('/', status_code=status.HTTP_200_OK)
def create_promo(
        data: PromoCreate,
        db: Session = Depends(get_session)
):
    promo = Promo(name=data.name, desription=data.description)

    try:
        db.add(promo)
        db.commit()
    except IntegrityError:
        db.rollback()

    return promo.to_dict()


@router.get('/', status_code=status.HTTP_200_OK)
def get_promos(
        db: Session = Depends(get_session)
):
    query = select(Promo)

    promos = db.scalars(query).all()
    return [promo.to_dict() for promo in promos]
