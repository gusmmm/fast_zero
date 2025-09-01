from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import MessageResponse

app = FastAPI()


@app.get("/",
         status_code=HTTPStatus.OK,
         response_model=MessageResponse)
def read_root():
    return {'message': 'Ola Mundo!'}
