from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    log: str

app = FastAPI()
log = open('app/log.txt', 'a')


def send_data():
    with open('app/log.txt', 'r') as l:
        #method to send data for my email
        pass

@app.get('/')
def index():
    return {'log' : 'see.k is active 👀'}

@app.post('/send_log')
def send_log(item: Item):
    log.write(item.log)
    if(len(log.readlines()) > 10):
        send_data()
        return {'log' : 'all data set 👾'}
    return item


