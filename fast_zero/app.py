from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routes import auth, users
from fast_zero.schemas import Message

app = FastAPI(title='Expedition Control', version='version_dev')
app.include_router(auth.router)
app.include_router(users.router)


@app.get(
    '/', status_code=HTTPStatus.OK, response_model=Message, tags=['message']
)
def read_root():
    return {'message': 'Welcome to my aplicattion!'}
