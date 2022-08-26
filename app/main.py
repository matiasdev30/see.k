from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    value: str

app = FastAPI()

@app.get('/')
def index():
    return {'msg' : 'app v1'}


@app.post('/send_log')
def send_log(item: Item):
    return {'log' : item.value}