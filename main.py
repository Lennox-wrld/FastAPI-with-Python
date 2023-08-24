from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


@app.get('/')
def home():
    return {"data": 11.2}


items = {}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description='The item id')):
    return items[item_id]


# querry parameters

@app.get('/get-by-name/{item_id}')
def get_item(*, name: Optional[str] = None, test: int):
    for item_id in items:
        if items[item_id].name == name:
            return items[item_id]
        return {'Data': 'Not found'}

@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {'Item alredy exists'}
    
    items[item_id] = item
    return items[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id, item: Item):
    if item_id not in items:
        return {'Item does not exist'}
    
    items[item_id].update(item)
    return items[item_id]