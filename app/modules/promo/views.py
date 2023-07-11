from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import *
from app.modules.participants.schema import ParticipantCreate
from app.modules.prize.schema import PrizeCreate
from app.modules.promo.schema import *

router = APIRouter(prefix='/promo')


@router.post('/', status_code=status.HTTP_200_OK)
def post_promo(
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
    if not query:
        return status.HTTP_404_NOT_FOUND
    promos = db.scalars(query).all()
    return [promo.to_dict() for promo in promos]


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_promo(
        id: int,
        db: Session = Depends(get_session)
):
    promo = db.get(Promo, id)
    prizes_ids = select(BetweenPromoPrize)
    papticipants_ids = select(BetweenPromoParticipant)

    if id:
        prizes_ids = prizes_ids.where(BetweenPromoPrize.promo_id == id)
        papticipants_ids = papticipants_ids.where(BetweenPromoParticipant.promo_id == id)

    #не разобрался как из списка записей ids вытащить id записей из основных таблиц и вывести все записи в форме JSON
    return promo.to_dict()


@router.put('/{id}', status_code=status.HTTP_200_OK)
def put_promo(
        id: int,
        data: PromoCreate,
        db: Session = Depends(get_session)
):
    promo = db.get(Promo, id)
    new_values = data.dict()
    promo.update(**new_values)
    try:
        db.add(promo)
        db.commit()
    except IntegrityError:
        db.rollback()

    return promo.to_dict()


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_promo(
        id: int,
        db: Session = Depends(get_session)
):
    promo = db.get(Promo, id)
    try:
        db.delete(promo)
        db.commit()
    except IntegrityError:
        db.rollback()

    return "Success delete"


@router.post('/{id}/participant', status_code=status.HTTP_200_OK)
def post_participant_to_promo(
        id: int,
        data: ParticipantCreate,
        db: Session = Depends(get_session)
):
    participant = Participant(name=data.name)
    try:
        db.add(participant)
        db.commit()
    except IntegrityError:
        db.rollback()

    link = BetweenPromoParticipant(promo_id=id, participant_id=participant.id)
    try:
        db.add(link)
        db.commit()
    except IntegrityError:
        db.rollback()

    return participant.id.to_dict()


@router.delete('/{id}/participant/{participant_id}', status_code=status.HTTP_200_OK)
def delete_participant(
        id: int,
        participant_id: int,
        db: Session = Depends(get_session)
):
    participant = db.get(Participant, participant_id)
    link = select(BetweenPromoParticipant)
    link = link.where(BetweenPromoParticipant.promo_id == id, BetweenPromoParticipant.participant_id == participant_id)
    link = db.scalars(link)
    try:
        db.delete(participant)
        db.delete(link)
        db.commit()
    except IntegrityError:
        db.rollback()

    return "Success delete"


@router.post('/{id}/prize', status_code=status.HTTP_200_OK)
def post_prize_to_promo(
        id: int,
        data: PrizeCreate,
        db: Session = Depends(get_session)
):
    prize = Prize(name=data.description)
    try:
        db.add(prize)
        db.commit()
    except IntegrityError:
        db.rollback()

    link = BetweenPromoPrize(promo_id=id, prize=prize.id)
    try:
        db.add(link)
        db.commit()
    except IntegrityError:
        db.rollback()

    return prize.id.to_dict()


@router.delete('/{id}/participant/{prize_id}', status_code=status.HTTP_200_OK)
def delete_prize(
        id: int,
        prize_id: int,
        db: Session = Depends(get_session)
):
    prize = db.get(Prize, prize_id)
    link = select(BetweenPromoPrize)
    link = link.where(BetweenPromoPrize.promo_id == id, BetweenPromoPrize.prize_id == prize_id)
    link = db.scalars(link)
    try:
        db.delete(prize)
        db.delete(link)
        db.commit()
    except IntegrityError:
        db.rollback()

    return "Success delete"


@router.post('/{id}/raffle', status_code=status.HTTP_200_OK)
def raffle_winner(
        id: int,
        db: Session = Depends(get_session)
):

    return "Success delete"