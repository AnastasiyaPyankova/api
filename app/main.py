import uvicorn
from fastapi import FastAPI

from app.modules.participants.views import router as participants_router
from app.modules.prize.views import router as prize_router
from app.modules.promo.views import router as promo_router
from app.modules.winner.views import router as winner_router

app = FastAPI()

app.include_router(participants_router)
app.include_router(prize_router)
app.include_router(promo_router)
app.include_router(winner_router)


@app.get('/')
def root():
    return {
        'name': 'Api',
        'SWAGger': '/docs'
    }


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, host='0.0.0.0', reload=True)
